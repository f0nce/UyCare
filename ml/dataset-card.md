# Repair category dataset card

Status: dataset not collected. Owner: Uranov Daryn. No training or evaluation result exists yet.

Purpose: suggest one category for a residential repair description, with user confirmation and abstention for uncertainty.

Planned labels: plumbing; electrical; heating_ventilation; appliances; furniture_carpentry; finishing. Out-of-scope and ambiguous examples receive separate evaluation tags rather than a fabricated in-scope ground truth.

Required record fields: example_id, source_group_id, text, language, label, provenance, consent_or_license_reference, synthetic_flag, annotator_ids, adjudication_note, split. Keep identifying data outside the corpus.

Before training, document actual counts per class/language, collection dates, source permissions, exclusions, near-duplicate grouping, annotator disagreement and unresolved coverage gaps. Follow docs/09-verification-and-evaluation.md for splitting and reporting. Record data hash and immutable test IDs. Synthetic-only testing cannot establish target-user accuracy.
