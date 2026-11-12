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

The shared Human Knowledge MCP v1 request/response registry is in `schemas/mcp/human-knowledge-tools.v1.schema.json`; see `MCP_INTERFACE_CONTRACTS.md` and `HUMAN_KNOWLEDGE_VALIDATION.md` for the interface boundary, evidence, and outstanding validation limits.

## Powers energy architecture register — 2026-11-12

Powers treat energy efficiency as a measurable, enforceable, auditable capacity—not only a permission or evaluation. In the current UNIVERSALIS repository set, the canonical implementation is maintained in the Intelligence Powers repository.

- **Canonical open architecture:** [UNIVERSALIS Powers energy architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_ARCHITECTURE.md).
- **Shared v1 contract:** [Powers energy schema](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/schemas/powers/powers-energy-contracts.v1.schema.json).
- **Executed checks and limitations:** [Powers validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_VALIDATION.md).

The open implementation is local-first and independently operable. Measurement, forecasting, receipts, and synergy calculation do not require a central database or truth authority. It keeps actual workload telemetry and local policy in the operator's chosen environment. The shared contract excludes private credentials and policy values. PDU/RAPL/Kepler/GPU layers require overlap reconciliation; synergy comparisons require matched workload cohorts and SLO profiles. External tools and their advertised savings remain candidates until independently verified.

## Four-document source coverage — 2026-11-12

The complete owner-supplied tool inventory and status matrix for Human Knowledge, Powers, Human Capabilities, and Mapping/Matrix/Organization/Ecosystem Mapping is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md.

Treat every third-party name in that register as a proposed candidate/reference pattern until canonical source, license, maintenance, security, compatibility, and behavior are reviewed. The register distinguishes documented tools, basic contracts, passing CI, and actual integrations. This repository owns only the parts assigned to its domain. No C2O-private repository links or policy values are part of this public register.

## Master toolchain coverage register — 2026-11-12

The current public inventory for the original four toolchain documents plus the Intelligence Capabilities source is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md. It distinguishes documentation, basic contracts, passing CI, and actual integrations. This public register contains no links to C2O-private owner repositories or policy values.
