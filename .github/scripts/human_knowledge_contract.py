#!/usr/bin/env python3
"""Dependency-free semantic checks for the portable human-knowledge record contract."""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

REQUIRED = {
    "schema_version", "record_id", "record_kind", "record_status", "subject",
    "predicate", "object", "scope", "valid_time", "transaction_time",
    "provenance", "consent", "verification", "confidence", "authority_class",
    "contradiction_refs", "superseded_by", "erasure",
}

def parse_time(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise ValueError(f"{field} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return parsed

def validate_record(record: dict, profile: str = "universalis") -> None:
    missing = REQUIRED - set(record)
    if missing:
        raise ValueError("missing required fields: " + ", ".join(sorted(missing)))
    if record["schema_version"] != "1.0.0":
        raise ValueError("unsupported schema_version")
    if record["record_kind"] not in {"claim", "relationship"}:
        raise ValueError("record_kind must be claim or relationship")
    if record["record_status"] not in {"active", "superseded", "retracted", "erased"}:
        raise ValueError("invalid record_status")
    prov = record["provenance"]
    if not isinstance(prov.get("sources"), list) or not prov["sources"]:
        raise ValueError("every record requires at least one provenance source")
    if not prov.get("asserted_by", {}).get("id"):
        raise ValueError("provenance.asserted_by.id is required")
    for source in prov["sources"]:
        for key in ("source_id", "source_kind", "locator", "content_sha256", "captured_at", "rights_status"):
            if not source.get(key):
                raise ValueError(f"source is missing {key}")
        digest = source["content_sha256"]
        if len(digest) != 64 or any(ch not in "0123456789abcdefABCDEF" for ch in digest):
            raise ValueError("source content_sha256 must be 64 hexadecimal characters")
        parse_time(source["captured_at"], "source.captured_at")
    valid_from = parse_time(record["valid_time"]["from"], "valid_time.from")
    valid_to = record["valid_time"]["to"]
    if valid_to is not None and valid_from > parse_time(valid_to, "valid_time.to"):
        raise ValueError("valid_time.to precedes valid_time.from")
    recorded_at = parse_time(record["transaction_time"]["recorded_at"], "transaction_time.recorded_at")
    recorded_to = record["transaction_time"]["recorded_to"]
    if recorded_to is not None and recorded_at > parse_time(recorded_to, "transaction_time.recorded_to"):
        raise ValueError("transaction_time.recorded_to precedes recorded_at")
    consent = record["consent"]
    if consent.get("status") not in {"granted", "not_required", "withdrawn"}:
        raise ValueError("consent status is invalid")
    if any(s["source_kind"] == "human" for s in prov["sources"]) and consent["status"] != "granted":
        raise ValueError("human-sourced knowledge requires recorded, granted consent")
    if consent["status"] == "not_required" and not consent.get("rationale"):
        raise ValueError("not_required consent status requires a rationale")
    if consent["status"] == "withdrawn" and record["record_status"] == "active":
        raise ValueError("withdrawn consent cannot leave a record active")
    verification = record["verification"]
    if verification.get("status") not in {"unverified", "verified", "refuted", "contested", "unverifiable"}:
        raise ValueError("verification status is invalid")
    if verification.get("status") == "verified":
        verifier = verification.get("verifier_id")
        if not verifier or verifier == prov["asserted_by"]["id"]:
            raise ValueError("self-review cannot verify a claim")
        if not verification.get("verified_at") or not verification.get("receipt_ref"):
            raise ValueError("verified claims require a time-stamped proof receipt")
        parse_time(verification["verified_at"], "verification.verified_at")
    confidence = record["confidence"]
    lineage = confidence.get("lineage_scores")
    if not isinstance(lineage, list) or not lineage:
        raise ValueError("confidence requires a non-empty provenance lineage")
    if confidence.get("method") == "weakest_link" and confidence["score"] > min(lineage) + 1e-12:
        raise ValueError("weakest-link confidence exceeds a lineage ancestor")
    authority = record["authority_class"]
    if authority not in {"Evidence", "Advisory", "Controlled"}:
        raise ValueError("invalid authority_class")
    context = record.get("authority_context", {})
    if profile == "c2o" and authority == "Controlled":
        if not context.get("approver_id") or not context.get("approval_ref") or not context.get("policy_ref"):
            raise ValueError("C2O Controlled knowledge requires approver, approval, and policy references")
    if profile == "universalis" and authority == "Controlled":
        raise ValueError("UNIVERSALIS public records cannot import C2O Controlled authority")
    if record["record_status"] == "superseded" and not record.get("superseded_by"):
        raise ValueError("superseded records require superseded_by")
    erasure = record["erasure"]
    if record["record_status"] == "erased":
        if not erasure.get("content_removed") or not erasure.get("tombstone_only"):
            raise ValueError("erased records must retain tombstone metadata only, not source content")
        if record["object"] is not None:
            raise ValueError("erased records must not retain the original claim object")

def self_test() -> None:
    sample_path = Path(__file__).resolve().parents[2] / "examples" / "human_knowledge" / "claim.json"
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    validate_record(sample, "universalis")
    validate_record(sample, "c2o")
    cases = []
    bad = json.loads(json.dumps(sample)); bad["provenance"]["sources"] = []
    cases.append((bad, "missing provenance"))
    bad = json.loads(json.dumps(sample)); bad["verification"] = {"status":"verified","verifier_id":"fixture-author","verified_at":"2026-11-12T00:00:00Z","receipt_ref":"receipt:1","method":"independent"}
    cases.append((bad, "self-review"))
    bad = json.loads(json.dumps(sample)); bad["confidence"]["score"] = 0.9
    cases.append((bad, "weakest-link"))
    bad = json.loads(json.dumps(sample)); bad["provenance"]["sources"][0]["source_kind"] = "human"
    cases.append((bad, "consent"))
    bad = json.loads(json.dumps(sample)); bad["authority_class"] = "Controlled"
    cases.append((bad, "Controlled authority"))
    bad = json.loads(json.dumps(sample)); bad["record_status"] = "erased"; bad["erasure"] = {"content_removed":True,"tombstone_only":True,"request_ref":"erase:1"}
    cases.append((bad, "erasure retaining claim object"))
    bad = json.loads(json.dumps(sample)); bad["valid_time"]["to"] = "2026-11-01T00:00:00Z"
    cases.append((bad, "invalid bitemporal range"))
    for bad_record, expected in cases:
        try:
            validate_record(bad_record, "universalis")
        except ValueError:
            continue
        raise AssertionError("negative test unexpectedly passed: " + expected)
    controlled = json.loads(json.dumps(sample))
    controlled["authority_class"] = "Controlled"
    controlled["authority_context"] = {"approver_id":"reviewer-1","approval_ref":"approval:1","policy_ref":"policy:1"}
    validate_record(controlled, "c2o")
    print("Human-knowledge contract self-test: PASS (2 profile positives, 7 negative cases)")

def check(root: Path, profile: str) -> int:
    files = sorted((root / "examples" / "human_knowledge").glob("*.json"))
    failures = []
    for path in files:
        try:
            validate_record(json.loads(path.read_text(encoding="utf-8")), profile)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            failures.append(f"{path}: {exc}")
    if failures:
        print("Human-knowledge record validation: FAIL")
        for failure in failures:
            print(" - " + failure)
        return 1
    print(f"Human-knowledge record validation: PASS ({len(files)} example(s), profile={profile})")
    return 0

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=("c2o", "universalis"), default="universalis")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    if args.self_test:
        self_test()
    if args.check:
        return check(args.root.resolve(), args.profile)
    if not args.self_test:
        parser.error("choose --self-test and/or --check")
    return 0

if __name__ == "__main__":
    sys.exit(main())
