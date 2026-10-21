# Project management and risks

## Working arrangements

The repository is https://github.com/f0nce/UyCare and must remain the same throughout the diploma. The team has not yet created a YouTrack project. management/youtrack-backlog.csv contains a prepared backlog, not live issues. UCPLAN identifiers are local planning references and must be mapped to the real YouTrack IDs before implementation branches claim tracker linkage.

The dates below are a proposed schedule beginning 21 October 2026. The 24 October milestone comes from the supplied rubric; its year and the final defense date need confirmation. Dates after the first pre-defense are planning targets and must be revised to the official academic calendar.

## Responsibility allocation

| Member | Primary responsibility | Concrete review contribution |
| --- | --- | --- |
| Akhmetov Kazbek | Web and Flutter clients, request/profile APIs, prototype | Review API contracts and independently reproduce ML evaluation |
| Uranov Daryn | Data model, offers/orders backend, classifier and data preparation | Review frontend/API integration and correctness tests |
| Tazhibayev Marsel | Coordination, requirements, moderation/audit integration, QA and releases | Review scope, acceptance evidence, risk changes and submission readiness |

This is a proposed detailed allocation based on the roles provided by the team. Team-lead work includes inspectable engineering deliverables, not only assigning others. No commits or reviews are attributed to members who did not perform them.

## Milestones

| Milestone | Target | Exit criterion |
| --- | --- | --- |
| M1 Analysis and design submission | 24 October 2026 assumed | Documents, diagrams, prototype, actual user/supervisor evidence, tracker and reviewed tag |
| M2 Request and assignment backend | 20 November 2026 proposed | Accounts, requests and concurrent offer acceptance tested |
| M3 Core workflow and ML experiment | 18 December 2026 proposed | Web journey, chat, reviews and initial domain evaluation |
| M4 Mobile and deployment | 8 January 2027 proposed | Android/iOS journey, TLS and backup restoration evidence |
| M5 Evaluation and final preparation | 22 January 2027 proposed | User baseline study, load results and requirement closure; official date pending |

## Risks and dependencies

| Risk | Likelihood / impact | Owner | Mitigation and trigger |
| --- | --- | --- | --- |
| No interview participants before pre-defense | High / High | Marsel | Recruit immediately; if fewer than three real discussions, mark evidence requirement unmet |
| Three clients and ML exceed team capacity | High / High | Kazbek | Share Flutter code and backend; prioritize essential journey and defer payments |
| Insufficient Kazakh domain labels | High / High | Daryn | Track coverage; narrow evaluated language claim and keep manual fallback |
| Concurrent acceptance creates two jobs | Medium / High | Daryn | Transactional lock plus unique constraint; real PostgreSQL concurrency test |
| Ratings or portfolio imply false verification | Medium / High | Marsel | Label self-declared content; only completed-job reviews; moderation with appeal |
| Exact locations or messages become public | Medium / High | Kazbek | Separate visibility, signed media access and negative permission tests |
| iOS build or signing access unavailable | Medium / Medium | Kazbek | Verify Mac/Xcode/simulator access early; device distribution is a separate dependency |
| GitHub write or tracker access missing | High / High | Marsel | Resolve member accounts/access before publishing or marking live tasks |
| Supervisor review arrives too late | Medium / High | Marsel | Send actual artifacts early and record decisions; do not invent sign-off |
| External product documentation changes | Medium / Low | Daryn | Record access date and recheck material claims before defense |

## Definition of done

A task is complete only when its acceptance criteria hold, relevant checks pass, its owner supplies evidence, another member reviews it, comments are resolved and the real YouTrack task links to the PR or commit. main is the reviewed baseline. Documentation changes follow the same review rule.

Use branches such as UYC-23-database-schema only after UYC-23 exists in YouTrack. Include the ID in the commit or PR description and link the change back from YouTrack. Every student uses their own identifiable account. Do not split or backdate one upload to simulate progressive contribution.

Tags pre-defense-1, pre-defense-2 and final-pre-defense identify exact reviewed submissions and must not be moved. Create pre-defense-1 only when the team selects the actual submitted commit. submission/checklist.md records unfinished obligations and submission metadata.
