# Verification and evaluation plan

## Evaluation questions

RQ1. Can target users complete request creation, offer comparison and provider selection with fewer coordination errors than a manual message-based baseline?

RQ2. Can a category classifier improve macro-F1 over keyword rules while keeping CPU latency and language-specific quality within the stated targets?

RQ3. Does the implementation preserve authorization and data integrity under invalid actions, duplicate submissions and concurrent acceptance?

## Functional verification

Each Must requirement has an acceptance test in tests/acceptance-cases.md and a row in docs/traceability.md. Unit tests cover validation and lifecycle rules. Integration tests use PostgreSQL for acceptance transactions, review uniqueness and permission checks. API tests include negative ownership and organisation cases. End-to-end tests execute the main customer/provider journey in web and Flutter clients. Security checks include direct object identifiers, private media, expired sessions, WebSocket participation and upload validation.

Mocking the database cannot establish transaction correctness. A concurrent test must issue two real acceptance operations and inspect persistent outcomes. Network reconnect tests verify saved message history rather than only a visible toast.

## User evaluation and baseline

Recruit 5–8 consenting participants from the target roles after the discovery discussions. Use two comparable fictional repair scenarios and the same three provider offers. In one condition participants coordinate using a prepared message thread and unstructured profile information; in the other they use UyCare. Alternate condition order across participants to reduce learning effects. This is a controlled manual-coordination baseline, not a claim to reproduce every person's WhatsApp behaviour.

Define the task before testing: create an adequate request, identify an offer meeting a specified availability and scope constraint, select it, and explain the recorded agreement. Measure independent completion, elapsed time, wrong or missing fields, wrong-provider selections and post-task confidence. Record interventions separately. Report individual outcomes and medians; with this sample size, avoid population-level or causal claims beyond the test conditions.

Proposed targets are at least 80% independent completion and at least 20% lower median task time than the manual condition without an increased error rate. These are evaluation targets, not promised results. If improvement is absent, report it and identify the design change or scope revision. No invented time savings appear in the proposal.

## ML data and experimental design

Start with the six-category taxonomy in the proposal. Aim to collect at least 600 labelled domain examples across Russian and Kazakh, with at least 30 held-out examples per category overall and transparent language counts. The number is a collection target; no dataset currently exists. If representative data cannot be obtained, narrow the experimental claim and retain manual classification in the product.

Collect consented descriptions or use lawfully reusable data with documented provenance. Remove names, telephone numbers and exact addresses. Two annotators independently label at least 20% of examples and resolve disagreements with a written guide. Track mixed and out-of-scope cases. Synthetic paraphrases may supplement training but must be flagged and grouped with their source; the main test set must contain independently sourced human descriptions.

Group duplicate descriptions, paraphrases and the same underlying job before making a 60/20/20 train/validation/test split, stratified as far as groups permit. Preserve group IDs and the data hash. Fit vocabulary and scaling on training data only. Choose confidence thresholds and hyperparameters on validation data only. Freeze the test set before the final comparison.

Compare keyword rules, word/character TF-IDF plus logistic regression, and a multilingual encoder with a classification head. Use the same splits and labels. Report macro-F1, per-class precision/recall/F1, confusion matrix, per-language results, abstention coverage, conditional error among shown suggestions, warm CPU p50/p95 latency and model size. Do not report high conditional accuracy without its coverage. Run training with three seeds where stochasticity applies and disclose variation.

The release gate is NFR-09. The experimental challenger replaces TF-IDF only if the predeclared quality/latency rule in ADR-004 is met. Blank, mixed-trade and unknown-category inputs test fallback behaviour separately. A failed model experiment is still a valid research finding; it must not be relabelled as a successful deployment.

## Performance conditions

For the proposed API test, use 2 vCPU and 4 GB RAM, 10,000 requests, realistic offers/messages, 25 concurrent clients and a 10-minute steady-state measurement after warm-up. Record host, database version, dataset size, network placement and exact commit. Use a mix of list, detail and write operations and report its proportions. API p95 must be at most 800 ms with less than 1% errors, excluding uploads and classifier calls, which have separate measurements.

## Reporting and completion gate

Each result records requirement, environment, commit, input/fixture, expected outcome, actual outcome, tester, date and evidence link. Results use Not run, Passed, Failed or Blocked. A plan or prototype walkthrough cannot be marked as a production test pass. The final gate requires passing all Must acceptance criteria or a supervisor-reviewed scope change, no unresolved critical access/integrity defect, and reproducible ML results or an explicitly documented fallback.
