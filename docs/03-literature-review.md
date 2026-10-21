# Literature review

## Review scope and selection

This focused review connects marketplace governance, multilingual text classification, dataset quality and evaluation to UyCare decisions. Searches used publisher pages, ACL Anthology and author preprints on 21 October 2026. Search concepts included online labour platform governance, platform scams, Kazakh NLP resources, few-shot classification, sentence embeddings and data leakage. This is a focused engineering review, not an exhaustive systematic review.

The core scientific set contains eight published journal/conference/workshop papers [S01–S08], supplemented by two explicitly identified research preprints/technical reports [S09–S10]. Eight of these ten sources date from 2021–2025. The 2019 Sentence-BERT and 2020 XLM-R papers are retained as foundations for the candidate representations. Official product and technical sources [S11–S23] are used for design/comparison, not counted as scientific publications.

Sources were included when their method or finding changed a requirement, comparison, data procedure or evaluation decision. Generic application-project descriptions without a clear evaluation method were excluded. Author/publisher abstracts and accessible text support the synthesis; no numeric result is transferred to UyCare, and this package does not claim to have reproduced the cited experiments.

## Critical synthesis

Platform governance is part of system design. Immonen distinguishes platform models with different degrees of control [S01], while Ticona shows that trust mechanisms can coexist with harmful interactions and disputed responsibility [S02]. UyCare therefore makes provider selection explicit, limits verification claims, and provides reporting with a recorded moderator decision. Their settings differ from Kazakhstan housing repairs, so local interviews must determine which concerns and policies are relevant.

Text classification needs an appropriate representation and an evaluation set. Sentence-BERT and XLM-R establish useful foundations [S07, S08], while SetFit and multilingual E5 supply later alternatives [S09, S10]. None removes the need for labelled repair requests. A small TF-IDF model is an intentional comparator because it is cheap to train, inspect and serve. A more complex encoder is justified only if measured gains outweigh latency and maintenance costs.

The Central Asian language survey highlights resource limitations [S05]. MTEB demonstrates why broad embedding rankings cannot identify a universal winner [S06]. For UyCare, evaluation must separate Russian, Kazakh and mixed-language requests where the data support such analysis. News, sentiment or general retrieval datasets may help investigate tools, but they cannot be relabelled as a repair-request test set without a valid annotation process.

Dataset documentation and leakage prevention are complementary. Gebru et al. motivate recording provenance, intended use and limitations [S03]. Kapoor and Narayanan motivate a separate test set and explicit leakage checks [S04]. UyCare will group duplicates and paraphrases before splitting, fit the text vectorizer only on training data, and keep synthetic examples identifiable. Performance on generated examples alone will not establish real-user performance.

The resulting research gap is practical and bounded: can a coherent request-and-offer workflow and an optional category suggestion improve defined user tasks for the recruited target users? The project does not claim a new marketplace algorithm or a new language model. Its evaluation will establish the extent and limits of the implementation's benefit.

## Structured scientific analysis

| Source | Approach | Finding relevant to UyCare | Limitation | Design consequence |
| --- | --- | --- | --- | --- |
| S01 Jere Immonen (2023) | Comparative platform analysis distinguishes intermediary models and degrees of managerial control. | Platform governance differs across business models; a marketplace must state who selects and directs work. | The study is not a Kazakhstan home-repair evaluation. | Customer selection and provider-defined offers; explicit moderator role. FR-05, FR-07, FR-15. |
| S02 Julia Ticona (2022) | Ethnography, platform observations and interviews with 42 careworkers. | Trust signals coexist with scams and conflicting expectations of platform responsibility. | Carework in US cities differs from residential repair in Kazakhstan. | Report/appeal workflow, clear verification labels and restricted contact access. FR-14, FR-15. |
| S03 Timnit Gebru et al. (2021) | A structured documentation framework for dataset provenance and use. | Dataset composition, collection, intended use and limitations should be documented. | Documentation alone cannot make a dataset representative or remove label errors. | Dataset card, consent/source fields and per-language coverage. NFR-10. |
| S04 Sayash Kapoor and Arvind Narayanan (2023) | Review of leakage problems and a reproducibility case study. | Leakage can make model comparisons overly optimistic. | Scientific prediction settings differ from production request classification. | Group near-duplicates before splitting; fit preprocessing on train only; freeze test data. NFR-10. |
| S05 Yana Veitsman and Mareike Hartmann (2025) | Survey of language resources and NLP methods for Central Asian Turkic languages. | Data scarcity and language-specific characteristics limit direct transfer of general NLP results. | The survey supplies no repair-request benchmark. | Evaluate Kazakh separately; document mixed-language and transliteration cases. FR-12, NFR-10. |
| S06 Niklas Muennighoff, Nouamane Tazi, Loic Magne and Nils Reimers (2023) | Benchmark spanning multiple embedding tasks and datasets. | No evaluated embedding method dominates every task. | General benchmarks do not establish UyCare domain quality. | Choose the model using local classification and latency evaluation. NFR-09. |
| S07 Alexis Conneau et al. (2020) | Large-scale multilingual masked-language pretraining and transfer evaluation. | Multilingual representations support cross-language transfer. | Pretraining scale does not guarantee reliable small-domain or mixed-language classification. | Transformer alternative, evaluated against a simpler baseline. ADR-004. |
| S08 Nils Reimers and Iryna Gurevych (2019) | Siamese/triplet training produces reusable sentence embeddings. | Sentence embeddings provide a practical representation for downstream similarity and classification. | The original work does not validate Kazakh repair categories. | Foundation for embedding-based alternatives; not evidence of local accuracy. ADR-004. |
| S09 Lewis Tunstall et al. (2022) | Contrastive sentence-transformer fine-tuning followed by a classifier. | SetFit offers a prompt-free approach when labelled examples are scarce. | Results depend on datasets and encoder; no UyCare performance claim follows. | Candidate low-data experiment after a reliable labelled set exists. ADR-004. |
| S10 Liang Wang et al. (2024) | Multilingual contrastive embedding training with several model sizes. | Model size offers a quality versus inference-cost choice. | An embedding model is not a ready-made repair-category classifier. | Candidate multilingual encoder with a trained classification head. ADR-004. |

## Supporting sources

| Sources | Purpose | How used |
| --- | --- | --- |
| S11–S13 | Official product descriptions | Comparison of posting, offers, selection, communication and payment. |
| S14–S22 | Official technical documentation | Backend, storage and interaction alternatives and their constraints. |
| S23 | Official YouTrack documentation | Feasible import route and explicit distinction between prepared and live tasks. |

Full bibliographic references and verified URLs are in docs/12-references.md.
