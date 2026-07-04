# Wine Quality Prediction - EDA Summary

## Dataset Overview

* Total Samples: 1143
* Features Used: 11
* Target Variable: Quality

## Key Findings

* Alcohol shows a positive relationship with wine quality.
* Volatile acidity has a negative relationship with wine quality.
* Several features contain outliers, especially chlorides, sulphates, residual sugar, and sulfur dioxide.
* Most wines belong to quality classes 5 and 6, indicating a slightly imbalanced dataset.
* No significant missing values were found.
* The Id column was removed because it does not contribute to prediction.

## Next Step

Perform data preprocessing:

* Handle duplicates
* Treat outliers
* Scale numerical features
* Split the dataset into training, validation, and testing sets
