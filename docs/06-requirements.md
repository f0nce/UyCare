# Requirements specification

## Baseline and priorities

This is the initial proposed requirements baseline for team and supervisor review. Must items define the final MVP release gate. Should items are planned but may be deferred with a recorded decision. Proposed numerical thresholds are targets, not observed results. The first pre-defense requires the specification and prototype, not implementation of every item.

The prototype demonstrates selected interactions. Server authorization, concurrency, backups, trained ML and Flutter compatibility require later implementation tests. A working prototype control is not evidence that the corresponding production requirement is satisfied.

## Functional requirements

### FR-01 Accounts and roles

Priority: Must. Component: Accounts.

Customer and provider roles are stored independently; staff permissions are separate.

Acceptance: Given an unauthenticated user, protected writes return 401. Given a provider without staff permission, moderation returns 403. Switching a UI role never grants a server permission.

### FR-02 Create and edit a request

Priority: Must. Component: Requests.

An owner supplies title, description, category, property type, city/district, desired date and optional KZT budget.

Acceptance: A valid request publishes once with an ID. Missing title/description/category or a past desired date is rejected. Once offers exist, a material edit invalidates active offers and requests resubmission.

### FR-03 Request photos

Priority: Must. Component: Media.

An owner can attach up to five JPEG/PNG images, each no larger than 5 MB.

Acceptance: Unsupported content and oversized files are rejected server-side. Another customer cannot retrieve a private attachment by guessing its URL.

### FR-04 Browse eligible requests

Priority: Must. Component: Requests.

Providers filter open requests by city and category; exact address and contact are withheld.

Acceptance: A city/category query excludes nonmatching and assigned/cancelled requests. A provider cannot see their own request as a bidding opportunity.

### FR-05 Submit and revise an offer

Priority: Must. Component: Offers.

A provider proposes a positive KZT price, availability, scope and materials/travel inclusions.

Acceptance: One active offer per provider/request is maintained. Negative price, own-request bidding and bidding on a closed request are rejected. Revised offers retain an audit event.

### FR-06 Compare providers

Priority: Must. Component: Profiles.

A customer compares price, schedule, portfolio and review count; sorting is explicit.

Acceptance: All active offers on the owned request are shown. Price sort is numeric. A provider without reviews displays No reviews yet instead of a fabricated rating.

### FR-07 Accept exactly one offer

Priority: Must. Component: Orders.

Only the request owner or authorised organisation member can select an active offer.

Acceptance: Two simultaneous acceptance attempts produce exactly one assignment. A losing attempt returns 409. Repeating a successful request with the same idempotency key returns the same result.

### FR-08 Coordinate progress

Priority: Must. Component: Orders.

The assigned provider starts work and marks it ready for confirmation; the customer confirms completion.

Acceptance: Only Assigned to In progress to Awaiting confirmation to Completed is accepted. An unrelated user or invalid transition is rejected and no history changes.

### FR-09 Handle cancellation

Priority: Must. Component: Orders.

Before assignment the owner can cancel; after assignment either party requests cancellation and the other confirms.

Acceptance: Cancellation records actor, reason and time. A disputed cancellation stays pending for moderator review. Cancelled work cannot receive a completed-job review.

### FR-10 Private messaging

Priority: Must. Component: Messaging.

A chat belongs to a request/offer pair and is accessible to the customer and that provider.

Acceptance: A third party cannot read or send messages. After reconnect, the same ordered persisted history appears. Duplicate client message IDs do not create duplicates.

### FR-11 Contact sharing and notifications

Priority: Should. Component: Messaging.

A user may explicitly share a phone contact; essential events appear in an in-app inbox.

Acceptance: Phone contact is absent before opt-in and visible only to the intended participant after sharing. The inbox records offer, acceptance and completion events without exposing private content to others.

### FR-12 Suggest a category

Priority: Must. Component: Classification.

The service suggests a category from text and allows confirmation, correction or manual selection.

Acceptance: Blank/unsupported text has no forced category. Service failure leaves request creation usable. The final category, suggested category and model version are stored separately.

### FR-13 Completed-job reviews

Priority: Must. Component: Reviews.

Only the commissioning customer can leave one 1–5 rating and comment for the completed job.

Acceptance: Uncompleted, cancelled, unrelated and duplicate reviews are rejected. The displayed mean and count match eligible published reviews. Moderation removals recalculate them.

### FR-14 Manage a provider profile

Priority: Must. Component: Profiles.

Providers describe skills, service areas and self-uploaded portfolio work.

Acceptance: Providers edit only their own profile. Self-declared experience is labelled as such. Uploading a photo never grants a verified-identity badge.

### FR-15 Reports and moderation

Priority: Must. Component: Moderation.

Users report requests, profiles, messages or reviews; staff record decisions and reasons.

Acceptance: Only staff can resolve a report or suspend an account. Resolution retains an audit record and allows an appeal record without deleting original evidence.

### FR-16 Organisation-owned requests

Priority: Must. Component: Organisations.

An approved member may act for an organisation; ownership survives a member leaving.

Acceptance: A member from organisation B cannot edit organisation A requests. Revoked membership immediately blocks new actions. Staff approval records the membership basis without claiming legal certification.

### FR-17 Agreement history

Priority: Must. Component: Orders.

The accepted offer snapshot and subsequent agreed changes remain available to both parties.

Acceptance: Changing a profile or other offer cannot change the accepted price/scope snapshot. A proposed job change takes effect only after the other party accepts it.

### FR-18 Direct payment declaration

Priority: Should. Component: Orders.

Parties may record that payment will occur directly outside the platform.

Acceptance: No card number or payment credential is requested. A user declaration is labelled unverified and cannot trigger a platform-paid or escrow status.

## Nonfunctional requirements

### NFR-01 Authorization

Priority: Must.

All record and media operations enforce ownership/membership on the server.

Acceptance: Pass the complete cross-role and cross-organisation access matrix, including direct IDs and WebSocket sessions.

### NFR-02 Data integrity

Priority: Must.

Acceptance, status changes and review creation preserve database invariants.

Acceptance: Run concurrent acceptance and repeated-command tests against PostgreSQL; exactly one assignment and at most one customer review per job remain.

### NFR-03 Response time

Priority: Must.

Under the defined pilot load, ordinary reads remain responsive.

Acceptance: On a documented 2 vCPU/4 GB test server with 10,000 requests and 25 concurrent clients, warm API p95 is at most 800 ms and error rate below 1% over 10 minutes, excluding uploads and ML.

### NFR-04 Usability

Priority: Must.

Core web journeys work at mobile and desktop widths with keyboard navigation.

Acceptance: At 390 and 1440 px, no horizontal overflow; all key controls have visible focus and labels. At least 80% of 5–8 recruited users finish the core task without intervention.

### NFR-05 Privacy and secret handling

Priority: Must.

Private contacts, exact addresses and credentials are not public data.

Acceptance: No secrets or real personal research data are committed. Logs redact tokens and private message text. Public request responses omit exact addresses and phone numbers.

### NFR-06 Recoverability

Priority: Must.

Backups can restore a consistent pilot dataset.

Acceptance: Restore an encrypted backup to a clean environment and verify representative records and attachment references. Proposed pilot RPO 24 h and RTO 4 h are demonstrated, not assumed.

### NFR-07 Transport and sessions

Priority: Must.

Deployed authenticated traffic uses TLS and bounded sessions.

Acceptance: HTTP redirects to HTTPS, expired/revoked sessions fail, repeated login attempts are limited, and state-changing cookie requests require CSRF protection.

### NFR-08 Compatibility

Priority: Must.

The core workflow operates across the planned clients.

Acceptance: Run the same acceptance scenario in a named desktop browser, Android emulator/device and iOS simulator/device; record OS/app versions. Mobile success remains untested until Flutter exists.

### NFR-09 ML quality and latency

Priority: Must.

Category suggestions are optional and must pass a defined release gate.

Acceptance: On a frozen domain test set, macro-F1 is at least 0.80, at least 0.05 above keyword rules, and each evaluated language macro-F1 is at least 0.70. CPU warm p95 prediction time is at most 1 s. Otherwise keep manual selection and report failure.

### NFR-10 ML reproducibility

Priority: Must.

Dataset provenance, grouped split, preprocessing and model version are reproducible.

Acceptance: A second team member reproduces metrics within 0.01 macro-F1 using the same data hash, split IDs, seed and locked environment. Test data never tune thresholds or vocabulary.

### NFR-11 Maintainability and traceability

Priority: Must.

Mandatory requirements map to components, tasks and tests.

Acceptance: Every Must requirement has an acceptance record; reviewed changes pass appropriate checks and link to a real YouTrack ID after project setup.

### NFR-12 Observability

Priority: Should.

Failures and critical lifecycle actions are diagnosable without private content.

Acceptance: A failed acceptance and failed notification can be traced by correlation ID; audit records contain actor, action, target and time, not secrets.

## Important business rules

The lowest price never automatically wins. The customer selects a provider. A displayed rating includes its review count and is not a guarantee of quality. A profile without completed jobs remains eligible to respond. A budget, offer, accepted price and payment declaration are separate fields.

An accepted offer creates one job and freezes the agreement. Changes require a separate proposal and consent. A job may return from Awaiting confirmation to In progress if the customer requests corrections with a reason. Reopening a cancelled job is not implicit; publish a new request with a reference if needed.

An organisation request belongs to the organisation, with a recorded acting member. This platform workflow does not certify the member's statutory authority. Membership approval and revocation are administrative actions with evidence retained privately.
