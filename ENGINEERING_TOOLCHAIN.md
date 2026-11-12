# Engineering Toolchain and Initial Build Plan

**Repository:** `C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge`  
**Repository responsibility:** Human Knowledge  
**Status:** Initial executable foundation proposed in this branch; specialized candidates remain proposed pending verification.  
**Boundary:** UNIVERSALIS public / independently operable. Do not add C2O-private credentials, policies, authority state, or private operational data.

## 1. Universal engineering foundation

This repository adopts the following baseline in proportion to its code and data:

- GitHub Actions CI with least-privilege workflow permissions.
- Automated tests and schema/configuration validation.
- CodeQL or equivalent static analysis, secret scanning, dependency review, and Dependabot after repository settings and alert ownership are confirmed.
- CycloneDX or SPDX SBOM generation, dependency vulnerability review, and action dependency inventory.
- Pinned toolchain versions, immutable action references, build provenance, and release signing as release workflows mature.
- Versioned specifications, changelogs, test fixtures, execution records, and explicit limitations.

**Candidate foundation tools from the owner-supplied proposal:** Secure SDLC Evidence Collector; repo-assurance; Chainguard Actions; cnspec SBOM Cataloger; actionlint; CodeQL; OSV-Scanner; Trivy/Grype; Gitleaks; CycloneDX/SPDX; SLSA provenance and in-toto attestations; cosign. These are candidates, not verified installations.

## 2. Repository-specific tools

PAISL sovereignty/privacy benchmark; Prufa accessibility and consent audits; AI Workflow Privacy Compliance Review Agent for editorial triage; source provenance, educational indexing, and correction records.

All candidate names and capability descriptions originate in the owner-supplied 2026-11-12 research submission. Before adoption, verify the canonical source, license, maintainer, release activity, security posture, compatibility, data flow, and test evidence. Do not infer implementation from a product description.

## 3. Initial implementation in this branch

- `.github/workflows/repository-quality.yml`: CI workflow running a dependency-free validator.
- `.github/scripts/repository_quality_baseline.py`: validator self-test and JSON validation for contract/schema/manifest directories plus `package.json` and `tsconfig.json`.
- This deliberately starts with a narrow, deterministic check. It does not claim to replace CodeQL, secret scanning, SBOM generation, formal ontology validation, accessibility audits, or domain-specific tests.

## 4. Next build increments

1. Inventory existing code, manifests, schemas, tests, and workflow permissions.
2. Add domain-native schema/contract fixtures and negative tests.
3. Add the relevant domain conformance harness and security scanner after source/license review.
4. Generate and archive SBOM, dependency, test, and provenance evidence.
5. Record failures, uncertainty, limitations, and verification status; never mark an unexecuted check as passed.

## 5. Evidence status

| Evidence item | Status |
|---|---|
| Toolchain candidates recorded | Documented |
| Initial validator and workflow authored | Implemented in this branch |
| CI execution | Passed — see HUMAN_KNOWLEDGE_VALIDATION.md |
| Domain-specific candidate review | Pending |
| Specialized integrations | Not yet implemented |
| Independent verification | Pending |


## Human Knowledge architecture increment

See `HUMAN_KNOWLEDGE_ARCHITECTURE.md` and `schemas/human-knowledge-record.schema.json`. This repository now defines the open, local-first profile with deterministic record checks, explicit contradictions, consent, independent verification receipts, and weakest-link confidence. The validator, negative tests, and synthetic fixture are in `.github/scripts/human_knowledge_contract.py` and `examples/human_knowledge/claim.json`. Candidate integrations remain proposed and unverified; they are not installed.
