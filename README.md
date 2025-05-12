# IEEE TinyML Workshop Metadata Analysis

This repository contains structured metadata and scripts used to analyze the presence and trends of TinyML and Edge AI related research in local and international IEEE conferences. It supports the development of a workshop proposal titled:

"**TinyML in Action: From Theory to Deployment**"  
For MERCon 2025

## Repository Structure

```
MERCon_workshop_proposal/
│
├── all_conf/                        # Metadata from 5 local IEEE conferences
│   ├── ICAC/
│   ├── ICARC/
│   ├── ICIIS/
│   ├── Mercon/
│   └── SCSE/
│       └── *.csv (2020–2024)
│
├── all_conf_international/         # Metadata from 4 international IEEE conferences
│   ├── AICAS/
│   ├── EDGE/
│   ├── ISCAS/
│   └── PERCOM/
│       └── *.csv (2020–2024)
│
├── TinyML/                         # Keyword metadata
│   ├── ml_keywords.csv             # Machine Learning keywords
│   └── nn_keywords.csv             # Neural Network keywords
│
├── MERCOn.png                      # Bar plot showing TinyML-related paper distribution
├── tmp/                            # Temporary workspace
├── new_plot_all.py                 # Script to generate summary plots
├── tinyml_ml_all.py                # Extract all ML-related papers
├── tinyml_nn_all.py                # Extract all NN-related papers
├── tinyml_plus_ml.py               # Identify papers matching TinyML keywords
└── tinyml_only.py                  # Temporary/unused script
```

## Conference Metadata

- `all_conf/`: Contains metadata from five local IEEE conferences (ICAC, ICARC, ICIIS, MERCon, SCSE) from 2020 to 2024 in `.csv` format.
- `all_conf_international/`: Contains metadata from four international IEEE conferences (AICAS, EDGE, ISCAS, PERCOM), also from 2020 to 2024.

Each CSV file contains parsed metadata for that year's conference proceedings, including paper titles, abstracts, authors, and keywords.

## TinyML Definition Used

In this project, TinyML is considered as:

- Efficient Machine Learning, including:
  - Parameter-efficient, computationally efficient, and energy-efficient models
  - Architectures that can run on microcontrollers — or are likely to do so in the future
- Both neural networks and classical ML models are considered
- Emphasis is on edge deployment, resource-awareness, and real-world usability

## Usage Instructions

Run the following scripts to analyze and visualize trends:

```bash
python new_plot_all.py        # Generate bar plots for paper distributions
python tinyml_ml_all.py       # Get all ML-related papers
python tinyml_nn_all.py       # Get all neural network-related papers
python tinyml_plus_ml.py      # Extract TinyML-relevant papers
```

Note: `tinyml_only.py` is a temporary or deprecated script and is not used in the main pipeline.

## Workshop Relevance

This repository supports the upcoming MERCon 2025 workshop proposal:

"TinyML: A Compact Revolution in Engineering AI"

The goal is to identify local and global trends in TinyML research, especially:
- How efficiency-centered ML is evolving in IEEE conferences
- What types of engineering applications are emerging in TinyML
- Bridging theory with deployable models on microcontrollers and edge devices

## License

This work is provided for academic and research purposes. Please cite appropriately if reusing any content, data, or analysis scripts.
