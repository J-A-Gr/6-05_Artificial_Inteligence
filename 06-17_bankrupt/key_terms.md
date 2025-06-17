Confusion Matrix:
[[1216  238]
 [   4   43]]

**Classification Report:**

                precision recall f1-score support

           0       1.00      0.84      0.91      1454
           1       0.15      0.91      0.26        47

    accuracy                           0.84      1501

macro avg: 0.57 0.88 0.59 1501
weighted avg: 0.97 0.84 0.89 1501

**Classification Report Breakdown (for Logistic Regression on Bankruptcy Prediction) Class 0 (Not Bankrupt):**

Precision: 1.00
→ All predicted "not bankrupt" companies were truly healthy.

Recall: 0.84
→ Model missed ~16% of actually healthy companies.

F1-score: 0.91
→ Great balance; model very confident on this class.

Class 1 (Bankrupt):

    Precision: 0.15 → 85% of predicted bankruptcies were false alarms.

    Recall: 0.91 → Caught 91% of actual bankruptcies – very strong detection.

    F1-score: 0.26 → Weak balance due to low precision (many false positives).

Overall Accuracy: 0.84 (84%):

    Model gets 84% of all predictions right.

    Misleading in imbalanced data; class 0 dominates.

Macro Average (equal class weight):

    Precision: 0.57, Recall: 0.88, F1: 0.59

    Good recall, weak precision – reflects poor confidence in class 1.

Weighted Average (class size matters):

    Precision: 0.97, Recall: 0.84, F1: 0.89

    Heavily influenced by class 0 – appears very strong, but hides weakness in class 1.
