## 🚀 Setup & Installation Guide
This project uses ``uv``, an extremely fast Python package manager, to ensure that the genomic analysis environment is 100% reproducible.

1. Prerequisites
Ensure you have Python 3.10+ and uv installed.

```Bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone and Initialize
```Bash
# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (Scientific Stack + Kaggle)
uv add pandas numpy matplotlib seaborn scikit-learn jupyter kagglehub imbalanced-learn joblib
```

3. Data Acquisition
The notebook automatically handles data downloading via kagglehub. However, you must ensure you have a Kaggle account to access the Gene Expression Cancer RNA-Seq dataset.

4. Running the Analysis
Launch the Jupyter interface:

```Bash
uv run jupyter notebook
```


Open ``cancer_analysis.ipynb`` and run all cells to:
1. Filter 20,531 genes down to the most significant biomarkers.

2. Visualize cancer clusters using PCA.

3. Train a Random Forest Classifier (99% Accuracy).

4. Perform Inference on new genomic samples.

### 🛠 Project Structure

```Plaintext
├── data/               # Downloaded RNA-Seq CSV files
├── .venv/              # Isolated environment (managed by uv)
├── pyproject.toml      # Project dependencies and versions
├── cancer_analysis.ipynb # Main Research Notebook
├── genomic_scaler.pkl  # Saved Preprocessing Scaler
└── cancer_classifier.pkl # Trained Random Forest Model
```
