# :hospital: Thoracic Surgery Survival Prediction: Project Overview
* Built a model using the [thoracic surgery dataset](https://archive.ics.uci.edu/ml/datasets/Thoracic+Surgery+Data) to predict the likelihood that a patient will survive for more than 1 year after thoracic surgeries have been performed
* Experimented with 4 different model families: information-based learning, similarity-based learning, error-based learning, and clustering
* Addressed imbalanced dataset with cost sensitive learning and oversampling techniques

## Code and Resources Used
* **Python Version**: 3.8.8
* **Packages**: pandas, numpy, matplotlib, seaborn, ipython.display
* **Thoracic Surgery Dataset**: https://archive.ics.uci.edu/ml/datasets/Thoracic+Surgery+Data
* **Relevant Paper**: https://www.sciencedirect.com/science/article/abs/pii/S1568494613002627

## Data Cleaning
Clamp transformation on FEV1 (the amount of air you can force from your lungs in one second) data outliers that were unlikely to be representative of human lung capacity. Upper clamp threshold calculated as the 3rd quartile plus 1.5 times the inter-quartile range.

## Model Building
* 4 classification models used
  * Decision Tree Classifier
  * K-Neighbors Classifier
  * Support Vector Classification (SVC)
  * K-Means Clustering
* Evaluation methods used
  * k-fold cross validation with k = 5
  * Plot confusion matrix
  * Average class accuracy based on harmonic means
  * Plot ROC curves for visual comparison
* In an attempt to correct the data imbalance, 4 methods were used
  * Cost sensitive learning where setting `class_weight = 'balanced'` was available
  * Random Oversampling
  * Synthetic Minority Oversampling (SMOTE)
  * Adaptive Synthetic (ADASYN)

## Model Performance
Decision Tree Classifier model with Random Over Sampler outperformed the other approaches in both average class accuracy (harmonic mean) and area under the ROC curve.

#### The highest scoring models according to average class accuracy (harmonic mean)

| Model  | Average Class Accuracy (Harmonic Mean) |
| ----------- | -----------: |
| DecisionTreeClassifier, Random  | 0.928 |
| KNeighborsClassifier, Random  | 0.859 |
| DecisionTreeClassifier, ADASYN  | 	0.839 |
| SVC, SMOTE  | 0.816 |
| KNeighborsClassifier, SMOTE  | 0.814 |

#### The highest scoring models according to areas under ROC curves
![ROC Curve Analysis](https://github.com/ayanoyamamoto0/assignments_2021-2022/blob/main/data_analytics/roc_curve.png)
