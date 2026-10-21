# UyCare

Development of a Digital Platform for Coordinating Repair and Maintenance Services for Residential Complexes and Private Homes.

UyCare is a diploma project for a Kazakhstan residential repair marketplace. Customers publish requests, independent providers propose prices and availability, and customers choose a provider using the offer, portfolio and completed-job feedback. An optional ML component will suggest the work category from the request description.

## Problem and users

The project investigates fragmented repair coordination and difficulty comparing unfamiliar providers. This is a hypothesis awaiting direct user validation. Existing services already address parts of this problem. Target users are apartment residents, private homeowners, authorised OSI/KSK representatives, independent providers and platform moderators.

## Team and supervisor

| Member | Responsibility |
| --- | --- |
| Akhmetov Kazbek | Frontend, backend, web/Flutter journeys and integration |
| Uranov Daryn | ML, data preparation and backend business logic |
| Tazhibayev Marsel | Team lead, requirements, QA, moderation/audit integration and releases |

Supervisor: Elvira Aitmukhambetovna. Detailed allocation is proposed in [project management](docs/10-project-management.md).

## Scope and current status

Stage: first pre-defense analysis and design preparation, 21 October 2026. Prepared: documents, editable diagrams, a runnable browser interaction prototype and a task backlog. Not implemented: production API, database, Flutter app, trained model or payment processing. Interviews, supervisor review, a live YouTrack project and individual development/review history remain to be completed by the team.

The final MVP targets request publication, competing offers, provider selection, agreement history, chat, completion confirmation, reviews and moderation. Payment is direct between parties. Integrated payments and scheduled preventive maintenance are deferred.

## Selected proposed technologies

Flutter/Dart for iOS and Android; Next.js/TypeScript for web; Python/Django REST Framework for the shared API; PostgreSQL for durable records; Django Channels for chat; scikit-learn as the initial classification candidate. [Technology comparison](docs/05-technology-comparison.md) records alternatives and rationale.

## Run the prototype

Private hosted preview: https://uycare-repair-prototype.sunnychime6.chatgpt.site. The preview is owner-private; use the portable files when demonstrating to the committee unless sharing is explicitly configured.

Open [prototype/index.html](prototype/index.html) directly in a modern browser. It uses fictional data and local browser storage. To serve it locally with Python 3:

```sh
python3 -m http.server 8000 --directory prototype --bind 127.0.0.1
```

Then open http://127.0.0.1:8000. Use Reset demo to restore sample data. No account, secret or package installation is needed. Category suggestions are rule-based demonstrations, not a trained model. No real messages or payments are sent.

## Checks

Run `python3 tools/check_package.py` to check artifact presence, source counts and requirement/test linkage. If Node.js is available, run `node --test tests/prototype-domain.test.mjs` for the prototype's state rules. Follow [the prototype checklist](tests/prototype-checklist.md) for UI checks. These do not substitute for future production acceptance tests.

Preparation checks: the seven prototype domain tests and package consistency checks passed. The local server returned HTTP 200 and the private site deployment succeeded. Full browser interaction and mobile viewport inspection could not be completed in the preparation environment and remain manual checks. See [verification record](tests/preparation-verification.md).

## Ready-to-use deliverables

- [English Word report](deliverables/UyCare_PreDefense_Report.docx)
- [English presentation](deliverables/UyCare_PreDefense_Presentation.pptx)
- [Preparation Pull Request](https://github.com/f0nce/UyCare/pull/1) — substantive team review pending.

## Documentation

- [Proposal and scope](docs/01-project-proposal.md)
- [Relevance and discovery](docs/02-relevance-and-discovery.md)
- [Literature review](docs/03-literature-review.md) and [references](docs/12-references.md)
- [Existing-system comparison](docs/04-existing-system-comparison.md)
- [Technology comparison](docs/05-technology-comparison.md)
- [Requirements](docs/06-requirements.md) and [traceability](docs/traceability.md)
- [Architecture](docs/07-architecture.md) and [editable diagrams](diagrams/README.md)
- [UX and prototype](docs/08-ux-and-prototype.md)
- [Verification and evaluation](docs/09-verification-and-evaluation.md)
- [Management and risks](docs/10-project-management.md)
- [Supervisor feedback](docs/11-supervisor-feedback.md)
- [Submission checklist](submission/checklist.md)

## Project tracking

YouTrack project: not created yet. [Prepared backlog](management/backlog.md), [CSV import file](management/youtrack-backlog.csv) and [setup instructions](management/youtrack-setup.md) are available. UCPLAN references are planning IDs and must be replaced/mapped to actual issue IDs after import.

Repository: https://github.com/f0nce/UyCare. Use separate task branches, real issue references and peer-reviewed PRs. Keep main as the reviewed baseline and tag exact submissions. See [CONTRIBUTING](CONTRIBUTING.md). No formal pre-defense tag should be claimed until the actual submission commit is selected.
