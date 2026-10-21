# Acceptance test catalogue

These are planned production tests. None is marked as passed by the static prototype. Record actual results in tests/results-template.md.

## AT-01 Accounts and roles

Requirement: FR-01. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Given an unauthenticated user, protected writes return 401. Given a provider without staff permission, moderation returns 403. Switching a UI role never grants a server permission.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-02 Create and edit a request

Requirement: FR-02. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: A valid request publishes once with an ID. Missing title/description/category or a past desired date is rejected. Once offers exist, a material edit invalidates active offers and requests resubmission.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-03 Request photos

Requirement: FR-03. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Unsupported content and oversized files are rejected server-side. Another customer cannot retrieve a private attachment by guessing its URL.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-04 Browse eligible requests

Requirement: FR-04. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: A city/category query excludes nonmatching and assigned/cancelled requests. A provider cannot see their own request as a bidding opportunity.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-05 Submit and revise an offer

Requirement: FR-05. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: One active offer per provider/request is maintained. Negative price, own-request bidding and bidding on a closed request are rejected. Revised offers retain an audit event.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-06 Compare providers

Requirement: FR-06. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: All active offers on the owned request are shown. Price sort is numeric. A provider without reviews displays No reviews yet instead of a fabricated rating.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-07 Accept exactly one offer

Requirement: FR-07. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Two simultaneous acceptance attempts produce exactly one assignment. A losing attempt returns 409. Repeating a successful request with the same idempotency key returns the same result.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-08 Coordinate progress

Requirement: FR-08. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Only Assigned to In progress to Awaiting confirmation to Completed is accepted. An unrelated user or invalid transition is rejected and no history changes.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-09 Handle cancellation

Requirement: FR-09. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Cancellation records actor, reason and time. A disputed cancellation stays pending for moderator review. Cancelled work cannot receive a completed-job review.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-10 Private messaging

Requirement: FR-10. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: A third party cannot read or send messages. After reconnect, the same ordered persisted history appears. Duplicate client message IDs do not create duplicates.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-11 Contact sharing and notifications

Requirement: FR-11. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Phone contact is absent before opt-in and visible only to the intended participant after sharing. The inbox records offer, acceptance and completion events without exposing private content to others.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-12 Suggest a category

Requirement: FR-12. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Blank/unsupported text has no forced category. Service failure leaves request creation usable. The final category, suggested category and model version are stored separately.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-13 Completed-job reviews

Requirement: FR-13. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Uncompleted, cancelled, unrelated and duplicate reviews are rejected. The displayed mean and count match eligible published reviews. Moderation removals recalculate them.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-14 Manage a provider profile

Requirement: FR-14. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Providers edit only their own profile. Self-declared experience is labelled as such. Uploading a photo never grants a verified-identity badge.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-15 Reports and moderation

Requirement: FR-15. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Only staff can resolve a report or suspend an account. Resolution retains an audit record and allows an appeal record without deleting original evidence.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-16 Organisation-owned requests

Requirement: FR-16. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: A member from organisation B cannot edit organisation A requests. Revoked membership immediately blocks new actions. Staff approval records the membership basis without claiming legal certification.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-17 Agreement history

Requirement: FR-17. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: Changing a profile or other offer cannot change the accepted price/scope snapshot. A proposed job change takes effect only after the other party accepts it.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## AT-18 Direct payment declaration

Requirement: FR-18. Setup: isolated test users, two organisations and seeded requests/offers appropriate to the case.

Procedure and expected result: No card number or payment credential is requested. A user declaration is labelled unverified and cannot trigger a platform-paid or escrow status.

Evidence: API responses, resulting records and an access-safe test log. Status: Not run.

## NT-01 Authorization

Requirement: NFR-01.

Procedure and expected result: Pass the complete cross-role and cross-organisation access matrix, including direct IDs and WebSocket sessions.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-02 Data integrity

Requirement: NFR-02.

Procedure and expected result: Run concurrent acceptance and repeated-command tests against PostgreSQL; exactly one assignment and at most one customer review per job remain.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-03 Response time

Requirement: NFR-03.

Procedure and expected result: On a documented 2 vCPU/4 GB test server with 10,000 requests and 25 concurrent clients, warm API p95 is at most 800 ms and error rate below 1% over 10 minutes, excluding uploads and ML.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-04 Usability

Requirement: NFR-04.

Procedure and expected result: At 390 and 1440 px, no horizontal overflow; all key controls have visible focus and labels. At least 80% of 5–8 recruited users finish the core task without intervention.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-05 Privacy and secret handling

Requirement: NFR-05.

Procedure and expected result: No secrets or real personal research data are committed. Logs redact tokens and private message text. Public request responses omit exact addresses and phone numbers.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-06 Recoverability

Requirement: NFR-06.

Procedure and expected result: Restore an encrypted backup to a clean environment and verify representative records and attachment references. Proposed pilot RPO 24 h and RTO 4 h are demonstrated, not assumed.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-07 Transport and sessions

Requirement: NFR-07.

Procedure and expected result: HTTP redirects to HTTPS, expired/revoked sessions fail, repeated login attempts are limited, and state-changing cookie requests require CSRF protection.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-08 Compatibility

Requirement: NFR-08.

Procedure and expected result: Run the same acceptance scenario in a named desktop browser, Android emulator/device and iOS simulator/device; record OS/app versions. Mobile success remains untested until Flutter exists.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-09 ML quality and latency

Requirement: NFR-09.

Procedure and expected result: On a frozen domain test set, macro-F1 is at least 0.80, at least 0.05 above keyword rules, and each evaluated language macro-F1 is at least 0.70. CPU warm p95 prediction time is at most 1 s. Otherwise keep manual selection and report failure.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-10 ML reproducibility

Requirement: NFR-10.

Procedure and expected result: A second team member reproduces metrics within 0.01 macro-F1 using the same data hash, split IDs, seed and locked environment. Test data never tune thresholds or vocabulary.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-11 Maintainability and traceability

Requirement: NFR-11.

Procedure and expected result: Every Must requirement has an acceptance record; reviewed changes pass appropriate checks and link to a real YouTrack ID after project setup.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.

## NT-12 Observability

Requirement: NFR-12.

Procedure and expected result: A failed acceptance and failed notification can be traced by correlation ID; audit records contain actor, action, target and time, not secrets.

Evidence: environment, exact commit, measurements/logs and reviewer. Status: Not run.
