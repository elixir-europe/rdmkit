---
title: Federated learning
description: Practical guidance on training machine-learning models across distributed sites without centralising sensitive data.
contributors: [Jorge Miguel Silva]
page_id: federated_learning
related_pages:
  Tool_assembly: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=federated+learning#materials
---

## What is federated learning and when should you consider it?

### Description

Federated learning (FL) is a machine-learning paradigm for building models without centralising sensitive data. Rather than requiring participating organisations to copy their records to a single repository, FL sends the learning algorithm to each site. Each site trains the model locally and only aggregated model updates (such as gradient summaries) are exchanged with a central coordinator. This preserves data sovereignty and allows hospitals, biobanks and other organisations to collaborate on joint models while keeping raw data local.

The typical FL workflow follows an iterative cycle: (1) the coordinator distributes a global model to participating clients; (2) each client trains on its local data; (3) clients send model updates back to the coordinator; (4) the coordinator aggregates the updates into a new global model; and (5) the process repeats until convergence. FL was first deployed at Google for on-device keyboard prediction, where simulations involved approximately 1.5 million phones {% cite hard2018federated %}; in health-care case studies cohort sizes typically range from five to approximately three hundred sites, depending on governance constraints.

{% include image.html file="fl_workflow.svg" caption="Figure 1. The federated learning workflow. Only model updates are exchanged; raw data never leaves its origin." alt="Diagram showing the iterative federated learning cycle between a central coordinator and three client sites." %}

FL is not the only approach for privacy-preserving analysis of distributed data. Alternatives include secure multi-party computation (SMC), trusted research environments (TREs) and differential-privacy pipelines applied to pooled data. However, FL is especially suited to scenarios where data cannot leave its origin at all, where computational resources exist at each site, or where the volume of raw data makes centralisation impractical. Fully decentralised (peer-to-peer) FL topologies remove the need for a central coordinator but introduce additional complexity for consensus and are beyond the scope of this page. Open challenges such as communication cost, statistical heterogeneity and fairness remain active research topics {% cite li2022federated %}.

This page is aimed at researchers, data stewards and IT professionals who need to analyse sensitive data distributed across multiple institutions without centralising it, including those working with health data, genomic information or other privacy-sensitive datasets where regulatory constraints prevent data sharing.

### Considerations

* Is your data distributed across multiple institutions that cannot share raw records?
* Do privacy regulations (such as the EU General Data Protection Regulation, GDPR) or ethical constraints prevent data centralisation?
* Do all participating sites have sufficient computational resources to train models locally?
* Is there a trusted party that can act as the coordinating server, or do you need a fully decentralised topology?
* What is the expected number of participating sites and how stable is their connectivity?
* Have you considered whether a non-FL approach (such as a trusted research environment or secure multi-party computation) would be simpler for your use case?

### Solutions

* In traditional centralised training, data must leave its origin, which often conflicts with privacy legislation. FL overcomes this by bringing computation to the data and exchanging only model updates rather than raw records. You can pool statistical power across sites while complying with GDPR and ethical frameworks such as the [Five Safes](https://ukdataservice.ac.uk/help/secure-lab/what-is-the-five-safes-framework/).
* Before committing to a full deployment, you can use FL simulation tools such as the Flower simulation guides {% cite flower_sim_guide %} to test different configurations, client numbers and resource constraints on a single machine.
* If your federation involves only a small number of sites with modest data volumes, evaluate whether a trusted research environment or secure data linkage might be more cost-effective before investing in FL infrastructure.

## How should you partition and harmonise data for federated learning?

### Description

Data may be partitioned across organisations in different ways, and the partitioning strategy influences your choice of algorithm and security requirements. In a horizontal (sample-wise) partition, each site holds the same features but different cohorts, for example multiple hospitals collecting identical clinical measurements for different patients. In a vertical (feature-wise) partition, participating organisations share the same individuals but collect different variables, such as genetic data at one site and clinical data at another. A third variant, federated transfer learning, applies when sites share neither the same samples nor the same features and a domain-adaptation step bridges the gap.

In horizontal FL, model updates are typically combined by weighted averaging. The most widely used algorithm for this is Federated Averaging (FedAvg) {% cite li2022federated %}. In vertical FL, the model is split across sites so that each site computes on its own features and only intermediate representations are exchanged, using approaches such as split neural networks.

Differences in data collection protocols can cause site-to-site variability. Before launching a federated study, it is helpful to agree on a common data model or phenotype dictionary to align variable names and units. Quality control to detect outliers, missing values and batch effects, together with common pre-processing pipelines (such as normalisation or imaging correction), will improve the reliability of federated results.

### Considerations

* Is your federation horizontal (same features, different samples), vertical (same samples, different features), or a transfer-learning scenario (different samples and features)?
* Have you established a common data model or phenotype dictionary across all sites?
* Are there batch effects, missing values or outlier patterns that differ between sites?
* Do you need to support discovery queries so that external analysts can find which federated data partitions exist?
* Have you mapped your data management to FAIR principles (Findable, Accessible, Interoperable, Reusable)?

### Solutions

* For horizontal federations, FedAvg and its variants (FedProx, FedOpt) aggregate model updates by weighted averaging. For vertical federations, consider split neural networks {% cite splitnn18 %} or statistical alternatives such as federated singular-value decomposition (FedSVD) {% cite hartebrodt2024fedsvd %}, which has been applied to genome-wide association studies (GWAS) and other high-dimensional omics analyses. {% tool "pyvertical" %} {% cite pyvertical20 %} provides a Python implementation for vertical FL experiments.
* {% tool "omop-cdm" %} {% cite omop_jhu24 %} is widely adopted for observational health data and maps well onto federated structured-query-language (SQL) back-ends. A typical implementation follows an extract, transform and validate pipeline: extract source data into staging tables, transform using Observational Health Data Sciences and Informatics (OHDSI) tools to map local vocabularies to standard concepts, and validate completeness via a data-quality dashboard. See the [OHDSI collaborative protocol](https://www.ohdsi.org/data-standardization/) for implementation guidance {% cite ohdsi2024 %}.
* {% tool "omop-cdm" %} standardises longitudinal health records, while GA4GH Phenopackets formalise genetic and phenotypic findings for specific individuals. The two are complementary and can be used together in a federated study. Refer to the [GA4GH Phenopackets specification](https://www.ga4gh.org/product/phenopackets/) for schema definitions and validation rules.
* To let external analysts discover which federated data partitions exist, you can expose a read-only endpoint using {% tool "beacon-v2" %} (yes/no genomic-presence queries) {% cite beacon_v2 %} or the GA4GH Search/Data-Connect API for richer tabular filters {% cite ga4gh_search %}.
* Research Object Crate (RO-Crate) is a lightweight community standard for packaging research data together with its metadata. You can use {% tool "runcrate" %}, a command-line utility for manipulating Workflow Run RO-Crate packages, to bundle harmonised data descriptions and ensure provenance {% cite runcrate_cli %}.

| FAIR principle | Implementation in FL | Example |
|----------------|---------------------|---------|
| **Findable** | Assign persistent identifiers (PIDs) to models and datasets. | DataCite DOIs for FL model versions. |
| **Accessible** | Use standardised protocols for model access. | HTTPS APIs with OpenID Connect (OIDC) authentication. |
| **Interoperable** | Apply common data models and vocabularies. | OMOP CDM for clinical data; GA4GH Phenopackets for phenotypic data. |
| **Reusable** | Package with rich metadata and clear licences. | RO-Crate with Model Cards; CC-BY or Apache-2.0 licences. |

## How do you secure a federated learning system?

### Description

Even though raw data stays local in FL, model updates can still leak information about the training data. A layered security approach, analogous to the layers of the ISO/OSI networking model, helps you address risks at multiple levels. At the transport layer, encryption (Transport Layer Security, TLS) protects data in transit. At the network layer, Virtual Private Networks (VPNs) restrict connectivity to authorised endpoints. At the application layer, authentication, authorisation, secure aggregation and differential privacy (DP) work together to limit what any single party can learn. A defence-in-depth strategy combines all these layers, guided by a formal threat model.

Threat modelling is a structured process for systematically identifying and prioritising potential security and privacy risks. In a federated context, you should consider both external attackers (who might intercept communications) and honest-but-curious participants (who follow the protocol but attempt to infer information from the updates they see).

### Considerations

* Have you defined a threat model covering both external attackers and honest-but-curious participants?
* Is TLS or VPN encryption enforced for all communications between the coordinator and clients?
* Do you need secure aggregation (where the server never sees individual updates) or is differential privacy sufficient for your risk profile?
* How do you handle client authentication and authorisation? Is OpenID Connect (OIDC) available across all sites?
* What is your tolerance for bandwidth overhead from cryptographic protocols?
* Have you assessed both privacy threats (re-identification, linkability) and security threats (spoofing, tampering)?

### Solutions

* **Transport and network layers**: use TLS to encrypt all communications between the coordinator and clients. Where sites span different networks, consider a VPN to restrict connectivity to authorised endpoints.
* **Authentication and authorisation**: use OIDC and token-based access control. You can issue GA4GH Passport "Visa" tokens for mutual OIDC authorisation across sites {% cite ga4gh_passports %}.
* **Secure aggregation**: protocols such as SecAgg and SecAgg+ allow each client to encrypt its updates so that the coordinator only ever decrypts the aggregate sum. Differential privacy (DP) provides an additional layer by adding calibrated noise to updates, reducing the risk of re-identification. A threat model should guide how you combine these protections for your risk profile. LightSecAgg {% cite so2022lightsecagg %} reduces bandwidth overhead and copes with client drop-outs, enabling asynchronous FL; a reference implementation is available {% cite lightsecagg_repo %}, though it has not yet been merged into Flower core and still requires manual integration.

* **Threat modelling with LINDDUN and STRIDE**: you can combine the LINDDUN privacy-engineering framework with Microsoft's STRIDE model for comprehensive coverage. A practical four-step recipe:
  1. **Map data flows**: draw a data flow diagram (DFD) that captures FL clients, the coordinator and all artefacts exchanged (model updates, metrics, credentials).
  2. **Identify threats**: for each DFD element, inspect the seven LINDDUN privacy categories (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance) and the six STRIDE security categories (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).
  3. **Assess impact**: score every threat for both likelihood and impact (low, medium or high).
  4. **Select mitigations**: map each threat to technical or organisational controls and record the residual risk.

| Threat category | LINDDUN focus | STRIDE focus | Example mitigation in FL |
|-----------------|---------------|--------------|--------------------------|
| Linking | Re-identification via update correlation | — | Add Gaussian DP noise to model updates. |
| Identifying | Direct identifiers in logs | — | Remove user IDs before logging. |
| Non-repudiation | Verifiable update provenance | — | Retain only aggregate logs. |
| Detecting | Participation inference | — | Add dummy (zero) client updates. |
| Unawareness | Missing consent | — | Deploy a dynamic consent portal. |
| Non-compliance | GDPR Article 35 data protection impact assessment (DPIA) | — | Embed privacy-by-design checkpoints. |
| Spoofing | — | Identity fraud | Mutual TLS + OIDC. |
| Tampering | — | Model poisoning | Byzantine-robust aggregation. |
| Information disclosure | — | Data leakage | Secure aggregation (SecAgg+, LightSecAgg). |
| Denial of service | — | Resource exhaustion | Rate-limit slow or malicious clients. |
| Elevation of privilege | — | Unauthorised API use | Role-based access control and short-lived tokens. |

See the LINDDUN tutorial and companion worksheet pack for step-by-step templates {% cite wuyts2015linddun %}. Additional resources: [LINDDUN Tutorial PDF](https://downloads.linddun.org/tutorials/pro/v0/tutorial.pdf), [Online privacy-threat catalogue](https://linddun.org/threats/).

## How do you govern a federated learning study?

### Description

Governance in federated learning goes beyond technical security. The Five Safes framework {% cite ukdataservice2023 %}, originally developed by the UK Data Service for any context involving sensitive data, provides a structured approach to ethical and secure data use. Although the framework applies broadly and is not specific to FL, its five components map naturally onto federated workflows. Legal compliance with regulations such as GDPR also requires specific procedural steps before and during a federated study.

### Considerations

* Have you obtained ethical approvals and established data-sharing agreements for every participating site?
* Is there a governance body that approves which analyses can run on the federation?
* Have you conducted a data protection impact assessment (DPIA) for the federated processing?
* Are all participating researchers authorised, trained and bound by terms of acceptable use?
* How will you ensure that only aggregated outputs leave each site, and that those outputs cannot reconstruct individual contributions?

### Solutions

* **Safe data**: de-identify and harmonise data so that each site satisfies minimum quality and confidentiality standards. Use common phenotype dictionaries and perform quality control before including data in a federated study. Note that this requirement applies equally to pooled-data approaches; what is specific to FL is that the data never leaves its origin.
* **Safe projects**: approve analyses only if they offer public benefit and respect data sensitivity. Ethical approvals and data-sharing agreements should be in place for every federated run, with minimum clauses covering purpose limitation, data retention periods and breach notification protocols. The EDPS TechDispatch on FL {% cite edps2025 %} provides regulatory context and legal framework requirements.
* **Safe people**: ensure that participating researchers are authorised and trained. Users should authenticate via OIDC and sign terms that outline acceptable use.
* **Safe settings**: execute computations in secure environments. {% tool "eucaim" %}'s federated processing platform, for example, orchestrates tasks through middleware so that data remain within secure nodes.
* **Safe outputs**: export only aggregated model parameters or summary statistics. Outputs should be screened to ensure that no individual contributions can be reconstructed.
* **Provenance logging**: each Beacon or Search query can be captured as a `DataDownload` entity inside the Five-Safes RO-Crate so that auditors can trace who accessed which variant count {% cite beacon_v2 %}. A full JSON profile and example crates are available {% cite rocrate_fivesafes2023 %}.
* **Data protection impact assessment (DPIA)**: run a DPIA before production. Free templates are provided by the [ICO DPIA template](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/data-protection-impact-assessments-dpias/) {% cite ico2024dpia %} and the [CNIL PIA kit](https://www.cnil.fr/en/privacy-impact-assessment-pia) {% cite cnil2024pia %}.

## How do you plan data management and ensure provenance?

### Description

A Data Management Plan (DMP) is a structured document that records how data will be collected, stored, shared and preserved throughout a project. A machine-actionable DMP (maDMP) goes further by encoding these decisions in a standard format (typically JSON) so that they can be read and acted upon by software. In a federated study, your DMP should cover not only local data handling at each site but also cross-border governance, federated infrastructure requirements and model versioning.

Beyond planning, capturing FAIR-aligned metadata and provenance throughout the federated life cycle is essential for auditability, regulatory compliance and scientific credibility. {% tool "research-object-crate" %}, a lightweight community standard for packaging research data with its metadata, provides a practical way to bundle a complete federated run into a single, self-describing artefact.

### Considerations

* Have you selected a DMP tool that supports machine-actionable output (JSON or PDF)?
* Does your plan cover cross-border data governance and federated infrastructure requirements?
* Have you documented model versioning and provenance tracking?
* Can you package a complete federated run as a single, self-describing artefact?
* Have you assigned SPDX licence identifiers to your models, datasets and code?

### Solutions

* Use the {% tool "data-stewardship-wizard" %}, the ELIXIR-CONVERGE-supported DMP wizard, to create a machine-actionable DMP for federated studies. DSW implements the maDMP standard, allowing you to export your plan in JSON or PDF. Select an ELIXIR/CONVERGE knowledge model, answer the guided questions and export the plan for inclusion in your project records and RO-Crate. You can also use your institution's {% tool "dmponline" %} service. See the RDMkit guidance on [data management planning](/data_management_plan) {% cite RDMKit_dmp %}.

* Capture dataset-level metadata with {% tool "research-object-crate" %} or the Five-Safes RO-Crate profile. The Workflow-Run RO-Crate (Process Run Crate) profile {% cite rocrate_workflow %} formalises provenance for computational workflows. Full implementations for secure TRE contexts are available in the Five Safes RO-Crate record (Zenodo) {% cite rocrate_fivesafes2023 %}.

  <details>
  <summary>Example: minimal ro-crate-metadata.json for a federated training run</summary>

  ```json
  {
    "@context": [
      "https://w3id.org/ro/crate/1.1/context",
      "https://w3id.org/ro/terms/workflow-run/context"
    ],
    "@graph": [
      {
        "@id": "ro-crate-metadata.json",
        "@type": "CreativeWork",
        "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
        "about": { "@id": "./" }
      },
      {
        "@id": "./",
        "@type": "Dataset",
        "name": "Federated training run",
        "conformsTo": { "@id": "https://w3id.org/ro/wfrun/process/0.5" },
        "hasPart": [
          { "@id": "model.pkl" },
          { "@id": "metrics.json" }
        ],
        "mentions": { "@id": "#Training_1" }
      },
      {
        "@id": "https://flower.ai/",
        "@type": "SoftwareApplication",
        "name": "Flower"
      },
      {
        "@id": "#Training_1",
        "@type": "CreateAction",
        "name": "Federated training",
        "instrument": { "@id": "https://flower.ai/" },
        "result": { "@id": "model.pkl" }
      },
      { "@id": "model.pkl", "@type": "File" },
      { "@id": "metrics.json", "@type": "File" }
    ]
  }
  ```

  </details>

* Document trained models with **Model Cards** to record intended use, limitations and demographic performance.

  <details>
  <summary>Example: Model Card for a federated classifier</summary>

  ```yaml
  model_details:
    name: "Federated MNIST Classifier"
    version: "1.0"
    training_algorithm: "FedAvg"
    rounds: 100
    participants: 5
  intended_use:
    primary_use: "Handwritten digit classification"
    out_of_scope: "Medical imaging, document analysis"
  performance:
    metric: "accuracy"
    global_model: 0.98
    fairness_assessment: "Evaluated across demographic groups"
  ```

  </details>

* **Licensing and citations**: use SPDX identifiers (such as `Apache-2.0` or `CC-BY-4.0`) in model metadata to clarify reuse terms. Assign DataCite DOIs to federated datasets and model versions for persistent reference. Licence FL workflows under permissive licences (MIT, Apache-2.0) to encourage adoption. Include a `LICENSE` file and SPDX metadata in every crate.

## How do you ensure reproducibility and handle data retention?

### Description

Reproducibility in FL is harder than in centralised machine learning because the training process spans multiple sites, each with its own data, software environment and execution context. Containerisation (packaging software and its dependencies into reproducible images) is recommended so that every site runs the same code. A container image digest is a cryptographic hash that uniquely identifies the exact software environment used for a given run.

In a federated setting, retention policies apply primarily to intermediate results such as model updates, aggregated checkpoints and training metrics, not to raw training data, which stays at each site and is governed by local data-management policies. Data subjects retain erasure rights even in federated settings under GDPR Article 17 (right to erasure), which may require you to remove the influence of specific training data from an already-trained model.

### Considerations

* Do you capture the full software environment (container image digests, lock files) for every site?
* Are you versioning data schemas, models and evaluation metrics independently across sites?
* Have you defined a retention policy for model checkpoints, and do you know how to handle GDPR Article 17 (right to erasure) requests?
* Is your training architecture amenable to shard-based unlearning?
* Have you defined retention windows for intermediate results (model updates, checkpoints)?
* Do you have a disaster recovery and failover plan that covers distributed checkpoint storage?

### Solutions

* Register container image digests and environment lock files (such as `conda-lock`) inside your RO-Crate for full environment capture.

* Follow the **DOME-ML** recommendations for reproducible machine-learning validation. DOME-ML (Data, Optimisation, Model, Evaluation) {% cite walsh2021dome %} structures reproducibility into four pillars: version-control data schemas and document splits; log hyperparameters and convergence criteria; store model checkpoints with DOIs and environment lock files; and document evaluation metrics and version test datasets separately. Track preprocessing pipelines with {% tool "dvc" %} {% cite dvc_guide %}.

* **Retention and deletion**: implement per-node retention windows (for example, ninety-day rolling deletion of checkpoints) with automated deletion scripts and audit trails. The EDPS commentary emphasises that coordinated deletion mechanisms are needed across all participating nodes {% cite edps2025 %}.

* **Machine unlearning**: machine unlearning is the process of removing the influence of specific training data from a trained model. Emerging techniques include Sharded, Isolated, Sliced, and Aggregated (SISA) training, which trains on isolated data shards so that only the affected shard needs retraining; differential privacy, which provides a degree of natural forgetting through noise addition; and certified removal, which offers mathematical guarantees that a data point's influence has been removed {% cite wired_unlearn %} {% cite bourtoule2021unlearning %}.

* **Disaster recovery**: document checkpoint management and backup strategies across distributed sites. Test failover scenarios regularly and ensure that recovery procedures are included in your DMP.

## How do you operate and monitor a federated learning system?

### Description

Machine Learning Operations (MLOps) practices are important for reliable federated systems. You should maintain audit logs at both the coordinator and client sides to record training events, authentication attempts and errors. Service-level indicators (SLIs) give early warning of problems before they affect model quality. Choosing an appropriate FL framework is part of operational planning: the right choice depends on your existing code base, security requirements and the maturity of the community rather than on feature checklists alone.

### Considerations

* Do you have logging infrastructure at both the coordinator and every client site?
* Can you visualise round-level metrics (loss, accuracy) without revealing per-site performance (aggregate only)?
* Have you defined service-level objectives (SLOs) for coordinator uptime, client participation rate and round latency?
* How will you detect data drift or concept drift across federated sites?
* Is your monitoring stack deployed and accessible to all operators?
* What programming language and ML library does your team already use, and does your chosen framework support secure aggregation natively?

### Solutions

* Use **drift detection** to monitor whether local distributions diverge from global assumptions. For production, consider tools such as {% tool "evidently" %}, an open-source ML monitoring framework for drift detection and model performance tracking. Scrape system and application metrics via Prometheus, an open-source monitoring toolkit, and visualise them with Grafana. When possible, present only aggregate round-level metrics (loss, accuracy) to avoid revealing per-site performance.

* Track three core SLIs (coordinator availability, client-participation rate and per-round latency) because each affects convergence and the overall reliability of your federation:

| SLI | What it measures | Why it matters | How to measure |
|-----|-----------------|----------------|---------------|
| Coordinator availability | Whether the coordinating server is responsive. | A coordinator outage halts every training round {% cite beyer2016site %}. | Expose periodic HTTP or gRPC health probes; alert on SLO burn rate. |
| Client-participation rate | The fraction of selected clients that report updates each round. | Model quality degrades when too few clients report; large-scale studies observe significant accuracy loss at low participation {% cite bonawitz2019towards %} {% cite fedscale2022 %}. | Export `fl_clients_participation_ratio` each round. Flower and NVFLARE expose this metric via Prometheus {% cite flower_monitoring2023 %} {% cite nvflare_monitoring %}. |
| Per-round latency (p95) | The 95th-percentile duration of a training round. | Latency spikes warn of network congestion or stragglers {% cite beyer2018site %}. | Track `fl_round_duration_seconds` as a histogram; alert when p95 breaches the SLO budget for three consecutive windows. |

* **Framework selection guidance**: rather than comparing frameworks feature by feature, consider the following decision criteria. {% tool "flower" %} {% cite flower2022 %} is a Python-based framework with built-in secure aggregation (SecAgg+ from version 1.8) and a large community; it is a good starting point for most horizontal FL experiments {% cite flower_docs %} {% cite flower_secagg_example %}. If your regulatory environment requires homomorphic encryption for model training (for example, logistic regression or tree-based models), {% tool "fate" %} provides this out of the box {% cite fate2024 %}. For GPU-heavy workloads, {% tool "nvidia-flare" %} offers FedAvg, FedOpt and FedProx strategies {% cite flare2025 %}. {% tool "substra" %} adds a web interface for non-technical stakeholders to monitor training progress {% cite substra2025 %}. Whichever framework you choose, consider validating workflows locally through simulation before deploying to production.

* **Publishing results**: package every federated run as an RO-Crate using {% tool "runcrate" %}. When publishing to a repository such as Zenodo, share aggregated evaluation metrics, model cards and code rather than raw model weights, which may encode sensitive information about the training data.

* **Community channels**: the [Flower Slack](https://flower.ai/join-slack/) {% cite flower_slack %}, [FATE mailing list](https://groups.io/g/FedAI) {% cite fate_mailing %} {% cite fate_community %} and [ELIXIR Federated Human Data Slack](https://elixir-europe.org/internal-projects/commissioned-services/federated-human-data) {% cite ELIXIR_slack %} provide support and roadmap discussions.

## How do you address bias, costs and environmental impact?

### Description

Federated learning can amplify or mask biases present in individual sites' data. Because each site may serve different demographic populations, the global model may perform unevenly unless fairness is explicitly monitored and addressed. Defining appropriate fairness metrics and auditing both global and per-site performance are essential steps before deploying a federated model.

FL also involves computational costs distributed across multiple sites, making budgeting and resource planning more complex than centralised training. Each training round requires local computation at every client plus communication overhead, so the aggregate energy consumption and carbon emissions can be substantial, particularly for large federations with GPU-heavy workloads. Reporting and reducing the environmental footprint of ML training is increasingly expected by funders and institutions.

### Considerations

* Have you defined which fairness metrics (such as demographic parity or equal opportunity) are relevant to your use case?
* Can you audit both global and per-site model performance without violating privacy constraints?
* Are mitigation strategies (re-weighting, constrained optimisation) compatible with your FL framework?
* Have you estimated computational costs (VM or GPU hours) across all federated sites?
* Are you tracking energy consumption and CO₂ emissions for each training run?
* Do you know the carbon intensity of the electricity grid at each participating site?
* Have you set a carbon budget for the project, and do you have early-stopping criteria tied to it?

### Solutions

* **Bias and fairness**: use group-fairness metrics (demographic parity, equal opportunity) to audit both global and per-site models. Mitigation strategies include re-weighting, constrained optimisation and fairness-aware FedAvg variants. Follow the DOME-ML fairness evaluation guidelines for systematic bias assessment across federated model performance {% cite walsh2021dome %}.

* **Cost estimation**: estimate computational costs across federated sites using cloud pricing calculators and monitor actual usage via resource monitoring dashboards. Because costs are distributed, each site should track its own resource consumption and report it centrally for project budgeting.

* **Carbon footprint monitoring**: several tools can help you measure the environmental impact of training:
  * {% tool "codecarbon" %} {% cite codecarbon %}: a Python package that tracks CO₂ emissions during training.

    ```python
    from codecarbon import EmissionsTracker
    tracker = EmissionsTracker()
    tracker.start()
    # Run FL training
    emissions = tracker.stop()
    ```

  * {% tool "ml-co2-impact" %}: an online calculator for ML carbon footprint.
  * {% tool "green-algorithms" %}: a computational footprint calculator.

* **Optimisation strategies**: schedule training during low-carbon energy periods at each site; use model compression techniques (pruning, quantisation) to reduce per-round computation; implement early stopping based on your carbon budget. Evaluate whether edge devices or cloud GPUs are more efficient for your specific workload and grid carbon intensity. Cloud GPUs may be more energy-efficient per computation than older on-premises hardware, so this decision should be evidence-based rather than assumed. Adaptive client-selection strategies such as EcoLearn can reduce CO₂ by up to an order of magnitude without significant accuracy loss {% cite ecolearn23 %}.

## Bibliography

{% bibliography --cited %}
