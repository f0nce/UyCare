# Technology comparison and decisions

## Decision method

Choices are assessed against the actual requirements: a shared mobile/web API, transactional provider selection, private chat, moderation, small-team delivery and Python-based ML. The assessments below are engineering judgements informed by official documentation. They are not performance measurements. Exact package versions and lockfiles will be fixed when implementation begins.

## Server platform

| Alternative | Fit | Cost or limitation | Decision |
| --- | --- | --- | --- |
| Django with DRF [S14] | Python integration; ORM and admin ecosystem support records and moderation | Domain permissions and async chat still need explicit implementation | Selected |
| FastAPI [S17] | Python types and API tooling suit a compact service | Need to assemble ORM, admin and account workflows | Viable alternative |
| NestJS [S18] | TypeScript modules align with web development | Python ML usually adds a boundary or separate runtime | Viable if team expertise changes |

ADR-001 selects Django with DRF because the project has many related records, an administrative workflow and a Python ML component. Django admin is for restricted staff use; it is not the customer interface. Revisit if a short implementation spike reveals a major team skill mismatch.

## Persistent storage

| Alternative | Fit | Cost or limitation | Decision |
| --- | --- | --- | --- |
| PostgreSQL [S15] | Foreign keys, unique constraints, transactions and row locks fit orders/offers/reviews | Schema changes require reviewed migrations | Selected |
| MySQL with InnoDB [S19] | Also supports transactional relational data | No measured reason it cannot satisfy this project | Viable alternative |
| MongoDB [S20] | Flexible documents and supported multidocument transactions | Linked permissions and assignment invariants require careful modelling | Not selected for the primary store |

ADR-002 selects PostgreSQL. Accepting an offer locks the request row and creates a unique assignment in one transaction. Database constraints complement application checks. PostgreSQL is a fit decision, not a claim that competing databases lack transactions.

## Component interaction

| Alternative | Fit | Cost or limitation | Decision |
| --- | --- | --- | --- |
| REST/JSON with WebSocket chat [S14, S16] | Straightforward resource API for Flutter and web; chat receives events | Two transports need consistent authorization and reconnect handling | Selected |
| GraphQL with subscriptions [S21] | Clients choose fields through a typed schema | Resolver permissions, query costs and subscription operations add decisions | Not selected initially |
| gRPC with browser adaptation [S22] | Generated typed contracts and efficient RPC | Browser adaptation and operational tooling add complexity | Reserved for a future internal service |

ADR-003 selects versioned REST resources under /api/v1 and authenticated WebSocket chat. Messages are stored before broadcast, and reconnecting clients retrieve history through REST. Redis is optional runtime infrastructure for a multi-process Channels deployment; it is not the authoritative message store. HTTP errors use documented 400/401/403/404/409 semantics.

## Category classification

| Alternative | Fit | Cost or limitation | Decision |
| --- | --- | --- | --- |
| Keyword rules | Deterministic, inspectable and cheap | Limited synonyms, negation and mixed-language handling | Required baseline |
| Word/character TF-IDF with logistic regression | Fast CPU inference; practical with a modest labelled corpus | Needs domain labels; weak semantic transfer | Initial ML candidate |
| Multilingual encoder with classifier, optionally SetFit [S07–S10] | Can exploit semantic and multilingual representations | Larger model, inference cost and possible overfitting | Experimental challenger |

ADR-004 selects the simplest candidate that meets the evaluation criteria. Train only after creating a documented dataset. A larger model is adopted only if held-out macro-F1 improves by at least 0.03 over TF-IDF while meeting latency and language-specific checks. This is a proposed decision threshold, not an achieved result. Any candidate that fails the quality gate remains experimental; manual selection stays available.

## Client and deployment boundaries

Flutter is fixed by the team. Next.js with TypeScript is the proposed web client. Both call the same backend, and business rules stay on the server. Object storage holds photos behind access-controlled URLs; provider portfolios and private request attachments have different visibility rules. Docker Compose is the planned local deployment method. A separate ML service, Kubernetes and a message broker are not initial requirements.

The pre-defense prototype is intentionally a portable HTML/CSS/JavaScript interaction model. It validates navigation and wording before the production clients are implemented; it is not claimed as a Flutter or Next.js build.
