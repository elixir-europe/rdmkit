---
title: Machine learning
description: This page is about setting best practices for data towards enabling FAIR ML.
contributors: [Styliani-Christina Fragkouli, Uladzislau Vadadokhau, Adriano Fonzino, Fotis Psomopoulos, Mihaly Varadi,
Edward Parkinson, Federico Bianchini, Munazah Andrabi]
page_id: machine_learning
related_pages:
  Your_tasks: [data_quality, sensitive]
training:
  - name: Machine learning events and materials on TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=machine+learning#events

---
## What is machine learning (on this page)?
 
### Description
The definition of Machine Learning (ML) can become so vague that it can reach the point of becoming a philosophical question. There are two main approaches; the first one considers the model as the centre of the definition. In this perspective, ML is defined mainly by the characteristics and capabilities of the model employed. This approach focuses on the technical aspects of ML, by emphasising factors such as algorithms, data processing and model performance {% cite ravi2022 %}.
In contrast, the second approach places the entire ML process at the centre of the definition of ML. In this form, the entire process is seen as a single entity, which includes all internal aspects/steps  such as data collection, preprocessing, feature engineering, model training, evaluation and deployment. This approach acknowledges that all these stages are interconnected.

For the purposes of this page, we will be using the first definition, i.e. the model-centred approach. The reasons behind this choice mainly include the technical focus with a strong emphasis on the technical aspects of ML and the performance evaluation because it provides a clear framework for comparing against other models.

## What is FAIR in machine learning?

### Description
As global standards for good data stewardship, the FAIR principles have become instrumental in ML, impacting policies and practices across sectors {% cite psomopoulos2023Roadmap %}. Embraced by policymakers and research institutes, implementing FAIR in ML enhances technical performance and proves economically advantageous.

FAIR is an aspirational guideline, not a stringent standard, propelling better data utilisation in ML. Applying the FAIR principles in ML involves creating easily discoverable models with comprehensive metadata, openly accessible with clear licensing, compatible with other systems via standardised formats, and designed for reuse with meticulous documentation, licensing and versioning {% cite huerta2023FAIR %}.
Actualising these principles necessitates infrastructural adjustments and stakeholder education {% cite castro2021Working %}.

FAIR ML holds immense potential in life sciences, from accelerating drug discovery processes to driving innovative bioinformatics applications through data interoperability from various sources. The transformative power of FAIR extends to enhancing predictive modelling, genetic research, disease diagnosis, and much more, demonstrating the criticality of its adoption for the future of life sciences {% cite ravi2022FAIR %}.


### Considerations 

There are several key considerations in applying the FAIR principles in ML and the life sciences:
- Findability: How can an ML model be easily identified? What metadata is necessary to make a model easily searchable?
- Accessibility: What measures must be in place to ensure the ML model is easily accessible? How does licensing impact the accessibility and usage of the model? 
- Interoperability: How can an ML model effectively work with other systems or models? What role does data standardisation play in this regard? What documentation is needed to ensure seamless interoperability? What is the community-backed metadata schema used for annotating the model?
- Reusability: How can an ML model be designed for optimal reuse? What is the role of version control and comprehensive documentation in ensuring others can easily understand and build upon the model?
- Ethics and Privacy: What ethical considerations and privacy protections must be implemented when dealing with data, especially in sensitive areas like healthcare? How might these considerations impact the FAIRness of ML models?
- Quality Assurance: How can the data quality used for ML models be controlled? How does data quality impact the robustness and reliability of ML models?
- Sustainability: What are the strategies for maintaining models and their dependencies?
- Evaluation: How can FAIR models be transparently evaluated? What role does documentation of performance metrics, validation procedures, and evaluation results play in providing users with an understanding of a model’s capabilities and limitations?

### Solutions
Applying the FAIR principles in ML is the focal point of initiatives such as the ELIXIR {% tool "dome" %} {% cite walsh2021Author %} recommendations and the [ELIXIR ML Focus Group](https://elixir-europe.org/focus-groups/machine-learning). The following solutions apply to the above-mentioned considerations at a high level:
- Use community-backed and standardised metadata that includes details about the model's authors, creation date, model type, training data, intended tasks, and performance metrics (such as {% tool "bioimage" %}, {% tool "schema-org" %}, {% tool "dome" %}, and {% tool "onnx" %}).
- Assign a unique and persistent identifier to each model. This identifier should be linked to the model's metadata to improve searchability.
- Ensure that models are open-sourced and shared on public platforms (e.g. {% tool "github" %}  or {% tool "huggingface" %}) to improve accessibility.
- Specify the terms of use in the licensing information, or link to standard licenses. This must include what users are allowed to do with the model. The most commonly used license on {% tool "github" %} is the [MIT License](https://opensource.org/license/mit/), other options can be explored [here](https://choosealicense.com/).
- Implement Application Programming Interfaces (APIs) to allow easy interaction with the model.
- Use standardised formats for sharing models, making them compatible with different platforms and languages ({% tool "onnx" %} for neural networks, for example).
- Provide clear documentation about the model's requirements, design, usage, and output formats. This will ensure the model can interact with other systems more easily.
- Implement version control for the models. This allows for tracking changes, resolving conflicts, and supporting reusability.
- Provide comprehensive documentation about the model's training data, architecture, hyperparameters, and performance. This allows other researchers to reproduce the original work or build upon it.
- Design models modularly, separating data pre-processing, the model itself, and post-processing. This makes each component reusable in different contexts.
- Ensure that models and their dependencies (like libraries or data sources) are maintained regularly or provide versioned snapshots of your library and all its dependencies, e.g. by offering dockerised containers.
- Implement anonymisation techniques for sensitive data and always gain consent before using data, especially in sensitive areas like healthcare. Note that privacy considerations can affect the FAIRness of the data, but models can be trustworthy even when they compromise on specific FAIRness aspects. See also the [Data sensitivity page](data_sensitivity) for more information.

## Data readiness for the ML models
 
### Description
The success of an ML model depends on the input data. Finding an appropriate dataset can be a challenge. The data has to be cleaned, explored, and evaluated before ML model training. Data preparation is often the most time-consuming step in the AI lifecycle. The “Garbage in, Garbage out” principle (GIGO) has to be kept in mind at this stage: models trained on unreliable data will produce unreliable predictions {% cite sansone2023FAIR %}.

To prepare data for ML models, several steps need to be followed. Firstly, data should be collected from reliable and diverse resources, ensuring it represents the problem domain accurately. Then, data cleaning techniques such as removing duplicates, handling missing values, and addressing outliers should be applied to enhance data quality. A commonly used practice for this task is the implementation of {% tool "scikit-learn" %}. Regarding features, on one hand there is the selection or extraction that can be performed to identify the most relevant and informative attributes for the model {% cite comess2020Bringing %}. On the other hand, there is the problem of the number of features which exceeds that of observations due to the nature of data in life sciences {% cite berisha2021Digital %}. Furthermore, data normalisation and standardisation might be necessary to scale features appropriately. Also, over or under-sampling can be used to handle an imbalanced dataset {% cite williamson2023Data %}. 

### Considerations
- The type of the data (text, images, time series, and others).
- Is there a “curse” of the data (more features than observations)?
- Are all variables converted to numeric type (data encoding)?
- Does the data need preprocessing?
- Are there outliers in the data?
- How are missing values treated (drop vs impute, random and non-random missing values)?
- Are there duplicates in the data?
- Does every subset (train, validation, and test) of the data represent the overall population, if data has been split?
- Data provenance: The source of the data, and whether it is recognised by the community. (source of data, involved points and more)
- Dataset size: Ensure the data set captures the full complexity of the underlying distribution, for example, the biological heterogeneity in the sample population.
- Balanced dataset: a dataset where all classes are properly and equally represented (i.e. same number of cases in each class and more).
- Availability of data/License associated with data
- Are the data  processed and AI-ready? One of the possible ways to achieve this would be through a curation effort.

### Solutions
- Classical ML algorithms have to be applied with caution to the high-dimensional data. For example, in a high-dimensional space distances between points have little difference meaning that algorithms based on distance measurement would fail. Additionally, the term blind spots can be defined here as a particular combination(s) of variables not covered by a given set of observations. Therefore, “cursed” data often represents a distorted picture of a real-world concept. One of the most direct solutions is to reduce the dimensional space. For instance, the theory of the domain can be applied to get a subset of features that are proven to be related to the target variable. Principal components analysis (PCA) and likewise methods do not result in domain-specific features but increase the model's general ability by reducing its variance.
- ML models take only numeric values as input with some exceptions (e.g. {% tool "catboost" %}). Categorical data has to be encoded into numbers via various strategies. The simplest is one-hot encoding. Namely, a new feature per every level of a categorical variable is created and the relation of that level to a particular observation is encoded with 1 (observation has this level of a variable) or 0. The drawback of this method is that the feature number is increased if the categorical variable has many levels. Other methods include label/ordinal encoding, target encoding, frequency encoding, and vectorisation (for text data). It is always a good idea to encode a variable in a way where encoding has a meaning which can help a model to recognise patterns in the data. For example, a variable storing temperature values with levels cold, warm, and hot can be encoded with 1 (cold), 2 (warm), and 3 (hot). However, the context of the task has to be considered in this case.
- Before dropping anomalies from the data, it is required to determine their nature and whether it is possible to convert them to regular values with a high level of confidence.
- Augmentation allows artificially increasing the diversity of the data by realistic data points to improve performance (decreasing overfitting, resolving class imbalance, rare events prediction) of the ML model or reducing the cost of data collection. Images can be augmented by random rotations, re-scaling, cropping, zooming, and noise addition. Several neural networks for this purpose are used (GANs, adversarial ML, neural style transfer). For NLP purposes word(s) deletion/insertion/swap and synonym replacement are used. For the regular table data, synthetic observations can be generated by drawing values from a distribution, utilising agent-based and deep-learning models. However, this process has to be planned carefully and performed with the assistance of an expert in the domain and with the utilisation of suitable tools like {% tool "keras" %}, {% tool "tensorflow" %} and {% tool "cuda" %}.
- For some ML algorithms, variables have to be put on the same scale. It is a crucial rule for unsupervised algorithms based on distance evaluation between data points (e.g. K-Means) and algorithms for dimensionality reduction (e.g. PCA). On the other hand, linear regression, tree-based algorithms, and neural networks can handle non-normalised data. The most popular technique is mean scaling, where each data point is converted to a z-score with a mean equal to 0 and a standard deviation equal to 1. In addition, data can be rescaled to a range [0, 1] by the min-max scaling technique.
- Source Verification: Establish robust mechanisms to verify the source of data and ensure its authenticity. Use cryptographic techniques or digital signatures to validate data integrity and origin.
- Metadata and Documentation: Maintain comprehensive metadata and documentation for each dataset, including information about data collection methodologies, ethical considerations, and any potential biases. This helps establish transparency and assists in community recognition.
- Depending on the type of data, certain preprocessing and transformation techniques can be followed:
  - Text Data: Implement text preprocessing techniques such as tokenisation, stemming, and stop-word removal to prepare textual data for analysis. Apply techniques like term frequency-inverse document frequency (TF-IDF) or word embeddings to represent text data in a numerical format.
  - Image Data: Utilise image preprocessing techniques such as resizing, cropping, and normalisation to standardise image sizes and enhance model performance. Apply image augmentation techniques like rotation, flipping, and colour jittering to increase dataset diversity.
  - Time-Series Data: Perform time-series preprocessing techniques such as resampling, interpolation, and feature engineering to extract relevant temporal patterns. Apply sliding windows or lagged variables to capture temporal dependencies.
- License: It is of pivotal importance to work in agreement and compliance with the license of data especially if you are planning to share them or a part of those also if those have been preprocessed.
- Data Balance: The dataset must be balanced. For data in labelled classes, ensure each class is sufficiently represented in the dataset. For data with continuous labels, like in regression tasks, evaluate how well the range of outputs is covered.
- Curation: If you are sharing a dataset there is the need to provide information about the curation process performed or if the dataset has to be curated before its usage.

## Bibliography

{% bibliography --cited %}
