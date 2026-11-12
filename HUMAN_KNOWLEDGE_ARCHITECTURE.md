# UNIVERSALIS Human Knowledge Architecture

**Owner:** UNIVERSALIS / MotherThread  
**Repository boundary:** Public and independently operable. No C2O-private credentials, policies, authority state, private research records, or operational data may be added.  
**Status:** Initial portable record contract and deterministic validation profile implemented on the repository foundation branch. Tool integrations remain proposed pending verification.

## 1. Architectural invariant

UNIVERSALIS Human Knowledge is open, local-first, inspectable, and independently operable. Knowledge is represented as a typed graph with mandatory provenance, not as untraceable embedded prose. Users and operators must be able to inspect, export, correct, and independently run the knowledge substrate without a proprietary cloud service or LLM in the critical storage path.

The common substrate has three elements:

1. **Provenance-stamped graph substrate:** stable record IDs, explicit scope, source attribution, bi-temporal validity, derivation lineage, and explicit contradiction/supersession links.
2. **Ontology validation gate:** records are checked against versioned ontology and record contracts before promotion or use.
3. **Evidence-verification layer:** verification is distinct from assertion; verified status requires a time-stamped receipt and review by a different human or agent.

## 2. Candidate tool map (owner-supplied; not adopted)

| Layer | UNIVERSALIS candidates | Proposed use |
|---|---|---|
| Graph and memory substrate | chip-memory; THOUGHT; Exocortex | Local bi-temporal graph, explicit contradictions, deterministic memory operations, inspectable ontology |
| Ontology validation | fabio-rovai/open-ontologies; Quipu | RDF/OWL reasoning, SHACL validation, bitemporal predicates, non-widening authority composition |
| Provenance and audit | strata-agent-memory; Metis; memledger | Append-only claim receipts, independent replay, consent-gated tacit knowledge, weakest-link confidence |
| Citation integrity | retractionwatch-mcp; vivory-mcp-verification | Retraction/correction flags, DOI/source/document provenance, verification tools |
| Retrieval and query routing | THOUGHT graph/vector/fact/change/hybrid routing | Route to an appropriate structure and surface contradictions rather than silently selecting one answer |

These are architectural candidates, not verified dependencies. Before adoption, verify canonical source, license, maintainers, release activity, security posture, local-only behavior, LLM/network requirements, data export, compatibility, and tests.

## 3. Portable record contract

The normative first increment is the JSON Schema 2020-12 contract in schemas/human-knowledge-record.schema.json, version 1.0.0. The dependency-free validator is .github/scripts/human_knowledge_contract.py. It checks representative records and core invariants; it is not a full JSON Schema implementation or a production graph database.

Every record carries:

- Stable record ID, record type and status, subject, predicate, object, and scope.
- Valid-time and transaction-time intervals with timezone-aware timestamps.
- One or more provenance sources, locator, content hash, capture time, rights status, asserting actor, and derivation links.
- Consent state and purpose; human-sourced records require recorded granted consent.
- Verification status, method, independent verifier, timestamp, and proof-receipt reference before verified status.
- Confidence plus lineage scores; weakest-link scoring cannot exceed the least-trusted ancestor.
- Authority class, explicit contradiction links, supersession pointer, and erasure/tombstone state.

Bi-temporal facts are superseded, not silently overwritten. Contradictions are represented explicitly and are not erased by ranking or summarization. Consent and rights changes must stop serving affected content and trigger deletion/rebuild of derived content where required. A tombstone must not retain source text it claims to have erased.

## 4. UNIVERSALIS enforcement profile

- Local operation is a first-class mode; cloud services are optional adapters, never required for core graph access.
- Storage, provenance queries, and deterministic validation must not require an LLM.
- Ontology code and schemas are versioned, diffable, reviewable, and portable.
- Consent is explicit for human-contributed or tacit knowledge; serving is restricted to declared purpose and conditions.
- Evidence and Advisory are descriptive classes. C2O Controlled authority and private policy references are not accepted into the public profile.
- Verified claims require a verifier distinct from the asserting actor and an inspectable or replayable receipt.
- No central truth authority: source evidence, contradiction state, verifier identity, uncertainty, and method remain visible.

The validator's universalis profile rejects Controlled authority records.

## 5. Versioned MCP contract surface

The six shared v1 MCP request/response definitions are implemented in schemas/mcp/human-knowledge-tools.v1.schema.json; see MCP_INTERFACE_CONTRACTS.md. Each request and response exposes stable IDs, provenance references, scope, uncertainty, consent/rights state, and errors. The public schemas describe interoperability only; they do not inherit or expose C2O-private identity, policy, authorization, or source data.

## 6. Initial execution and limits

Run:

    python .github/scripts/human_knowledge_contract.py --self-test
    python .github/scripts/human_knowledge_contract.py --check --profile universalis
    python .github/scripts/repository_quality_baseline.py --self-test --check

The current increment is a portable JSON contract, deterministic Python checks, negative tests, and a synthetic fixture. It does not yet install chip-memory, THOUGHT, Exocortex, open-ontologies, Quipu, strata-agent-memory, Metis, memledger, retractionwatch-mcp, or vivory-mcp-verification. It does not yet provide a graph database, production MCP server, or external verification connectors.

## 7. Evidence status

| Item | Status |
|---|---|
| Candidate tools and architecture recorded | Documented |
| Portable record schema | Implemented in this branch |
| Six shared MCP v1 tool contracts | Implemented in this branch |
| Dependency-free semantic validator and negative tests | Implemented in this branch |
| Synthetic fixture, MCP registry checks, and CI execution | Passed — see HUMAN_KNOWLEDGE_VALIDATION.md |
| Full JSON Schema validation | Not implemented |
| Production graph storage, MCP server, and external verifiers | Not implemented |
| Candidate tool source/license/security review | Pending |
| Independent verification | Pending |
