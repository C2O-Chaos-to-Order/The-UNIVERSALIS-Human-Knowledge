# Shared Human Knowledge MCP Interface Contracts

**Version:** v1  
**Status:** Six interface contracts implemented as JSON Schema definitions in schemas/mcp/human-knowledge-tools.v1.schema.json. A production MCP server and authorization middleware are not implemented.

## 1. Purpose and boundary

C2O and UNIVERSALIS share only versioned, interoperable MCP request/response schemas. The schemas define the shape of tool calls; they do not make storage, trust, privacy, or authorization policies identical.

The shared tool family is memory_search, memory_remember, memory_think, correct, verify, and audit. Each tool has separate request and response definitions. The remember/correct schemas reference the portable human-knowledge record contract.

## 2. Security invariant

Authentication and authorization are performed by the transport, gateway, or repository-specific boundary. Do not place bearer tokens, API keys, passwords, private credentials, C2O policy documents, approval tokens, or private identity data in these public request/response payloads.

Callers supply explicit data scopes and non-secret actor references where required. C2O maps authenticated principals to its private identity and policy system inside C2O. UNIVERSALIS handles identity and consent under its own open, inspectable implementation. A valid MCP payload is never an authorization grant.

The shared public schema exposes Evidence and Advisory labels only. C2O's private Controlled authority is not serialized through this shared interface.

## 3. Tool semantics

| Tool | Contract responsibility |
|---|---|
| memory_search | Scope-bound retrieval with record IDs, provenance references, verification status, confidence, and temporal filters |
| memory_remember | Validate and submit a record; accepted/queued is not the same as verified or authorized |
| memory_think | Produce an evidence-linked synthesis with contradiction and gap reporting; no hidden chain-of-thought output |
| correct | Append a superseding record, contradiction, retraction, or erasure request; never silently overwrite |
| verify | Request independent verification and return a receipt, verdict, timestamp, and limitations |
| audit | Retrieve scoped audit events and chain-integrity status; payload disclosure remains separately authorized |

## 4. Versioning and compatibility

- The v1 contract family is immutable after release; breaking changes require a new major version and new schema IDs.
- Additive optional fields may be introduced only when compatibility tests show older consumers can ignore them safely.
- Every response includes a request ID for correlation. Errors and validation failures must not silently coerce invalid inputs.
- The record schema and MCP schemas must be versioned together when a change affects meaning.
- No shared interface may widen access or authority when composed with another interface.

## 5. Validation and limitations

The repository baseline confirms JSON syntax. The human-knowledge validator additionally checks that the registry contains all six expected tool names, every tool maps to request and response definitions, and no secret-bearing property names are exposed. These checks do not replace full JSON Schema 2020-12 validation or a running MCP conformance harness.

## 6. Next steps

Add standards-compliant JSON Schema validation, request/response contract fixtures, transport authentication and scope tests, redaction tests, replayable verification receipts, and cross-profile conformance tests. Keep the C2O policy engine private and test that no private authority fields cross the boundary.
