# Here is your Final "Master Pipeline" Code. This single block combines every winning step we took—from loading and cleaning to the final high-performance model.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# 1. DATA LOADING
X = pd.read_csv('data/data.csv', index_col=0)
y = pd.read_csv('data/labels.csv', index_col=0)
df = pd.concat([X, y], axis=1)

# 2. FEATURE SELECTION (Variance Thresholding)
# Removing "boring" genes that don't change across patients
variances = X.var()
high_var_genes = variances[variances > 1.0].index
X_filtered = X[high_var_genes]

# 3. PREPROCESSING & SCALING
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_filtered)

# 4. UNSUPERVISED EXPLORATION (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 5. TRAIN-TEST SPLIT & BALANCING (SMOTE)
# Stratify ensures we keep the cancer-type ratios the same in both sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y['Class'], test_size=0.2, random_state=42, stratify=y['Class']
)

smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)

# 6. SUPERVISED LEARNING (The "Winner": Random Forest)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_bal, y_train_bal)

# 7. ANOMALY DETECTION (Isolation Forest)
iso = IsolationForest(contamination=0.05, random_state=42)
outliers = iso.fit_predict(X_scaled) # -1 = Outlier

# 8. FINAL EVALUATION
y_pred = rf_model.predict(X_test)
print("--- FINAL MODEL PERFORMANCE ---")
print(classification_report(y_test, y_pred))

# 9. FEATURE IMPORTANCE (The "Biological Insights")
importances = pd.Series(rf_model.feature_importances_, index=high_var_genes)
print("\nTop 5 Genetic Biomarkers:")
print(importances.sort_values(ascending=False).head(5))