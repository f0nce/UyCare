# Architecture and diagrams

## System boundary

UyCare is a modular backend with a web client and a Flutter client. Customer, provider and moderator interactions enter through authenticated interfaces. External object storage holds media. Optional delivery services may later deliver push/email notifications. Direct payment and telephone conversations happen outside the system. In-app payments are not an active component.

The required editable diagrams and readable exports are in diagrams: system-context.drawio and .svg, use-cases.drawio and .svg, and components.drawio and .svg. An additional lifecycle diagram records job states. The drawio files open in diagrams.net and preserve individual shapes and connectors. The SVG files are readable without a diagram editor.

## Component responsibilities

Accounts owns login, roles and session lifecycle. Organisations owns membership and organisation-scoped authorization. Requests owns the initial description, category and location visibility. Offers owns price/schedule proposals and revisions. Orders alone accepts an offer and changes the job lifecycle. Profiles owns provider descriptions and portfolios. Reviews owns review eligibility and published aggregates. Messaging owns participant-bound conversations and history. Moderation owns reports and decisions. Classification owns model inference behind a replaceable Python interface. Media authorizes uploads/downloads, and Audit records critical actions.

All durable business data lives in PostgreSQL. Private request attachments are distinct from public portfolio media. The backend stores media metadata, not raw file bytes. The classifier is a local backend module initially; training runs offline and produces a versioned model artifact. This avoids a mandatory network dependency during request creation.

## Logical data model

| Entity | Key fields | Integrity rule |
| --- | --- | --- |
| User | id, roles, account status | Staff permission is separate from customer/provider roles |
| Organisation / Membership | organisation_id, user_id, role, status | Only active authorised membership grants organisation actions |
| ProviderProfile / PortfolioItem | user_id, skills, service area, media_id | One profile per provider; self-declared work is labelled |
| ServiceRequest | owner_user_id or organisation_id, creator_id, category, location, status | Exactly one ownership mode; public and private location fields separated |
| Offer | request_id, provider_id, price_kzt, scope, availability, state, revision | One active offer per provider/request; positive price |
| Job | request_id, accepted_offer_id, agreed_snapshot, state, version | Unique request_id; accepted offer belongs to request |
| AgreementChange | job_id, proposed_by, proposal, state | Both-party consent before snapshot replacement; history retained |
| Conversation / Message | request_id, provider_id, sender_id, client_message_id | Participants match request customer/provider; duplicate-safe IDs |
| Review | job_id, customer_id, provider_id, rating, moderation_state | One commissioning-customer review per completed job; rating 1–5 |
| Report / AuditEvent | actor_id, target, reason, decision, timestamp | Restricted access; append-only application history |
| ClassificationRecord | request_id, predicted_category, final_category, model_version | Prediction never overwrites the confirmed category silently |

## Offer acceptance transaction

Authenticate the actor and authorize ownership. Begin a transaction and lock the request row. Check that the request is Open and the offer is active and belongs to it. Create the unique Job, copy the accepted offer into its agreement snapshot, set the request to Assigned, accept the chosen offer and close competing offers. Commit. Repeated idempotency keys return the prior result, and conflicting selections return 409. Persist notification work in an outbox in the transaction; a retryable worker delivers it after commit. A failed notification must not undo or duplicate the job.

## Lifecycle and cancellation

Request states are Draft, Open, Assigned and Cancelled. A Job exists only after assignment and moves through Assigned, In progress, Awaiting confirmation and Completed. The customer may request corrections, returning the job to In progress. Either party may request cancellation before completion. The other party confirms it, or a moderator records a decision if disputed. Pending cancellation does not silently count as completion. Completed-job reviews follow confirmation, never only a provider's completion claim.

## API contract outline

| Endpoint | Purpose | Important response |
| --- | --- | --- |
| POST /api/v1/requests | Publish a validated request | 201; 400 for invalid input |
| GET /api/v1/requests?city=&category= | Browse eligible public summaries | 200; paginated and privacy-filtered |
| POST /api/v1/requests/{id}/offers | Submit an offer | 201; 403 own-request; 409 closed request |
| POST /api/v1/offers/{id}/accept | Create one assignment | 201 or replayed result; 409 conflict |
| POST /api/v1/jobs/{id}/transitions | Apply an authorized lifecycle command | 200; 403 wrong actor; 409 stale state |
| GET/POST /api/v1/conversations/{id}/messages | Read/send persisted chat | 200/201; 403 nonparticipant |
| POST /api/v1/categories/suggest | Return a suggestion or abstention | 200; manual selection works on failure |
| POST /api/v1/jobs/{id}/reviews | Review completed work | 201; 409 ineligible/duplicate |

The full implementation will generate OpenAPI documentation. These are design contracts, not live endpoints. Page-level UI visibility is not a security control: every operation requires server-side permission checks.

## Deployment and failure handling

A pilot deployment consists of a web service, Django ASGI service, PostgreSQL, private/public media buckets, and optional Redis for Channels. TLS terminates at the deployment edge. Secrets come from environment or a secret manager. Database migrations run as a controlled release step. Backups and restore tests are required before real-user operation.

If inference fails, the user selects a category manually. If WebSocket delivery fails, saved messages remain retrievable and the client reconnects. If two clients act on stale data, the server returns a conflict and the UI refreshes the current state. Exact addresses become visible only to the selected provider; telephone contact requires explicit consent.
