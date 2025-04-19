# Insurance Premium Prediction

## Project Overview

This project focuses on predicting health insurance premiums based on individual demographic and health-related features. Using a structured dataset, the analysis explores key factors that influence insurance charges — such as age, BMI, smoking habits, and number of children—and applies machine learning model to estimate premiums accurately.

The project was implemented using **Python** in a **Jupyter Notebook** environment, utilizing popular data science libraries including **pandas**, **matplotlib**, **seaborn**, and **scikit-learn**. The dataset used in this notebook comes from [Kaggle](https://kaggle.com/datasets/teertha/ushealthinsurancedataset).

## Objective

* Understand how various demographic and health-related features affect insurance charges

* Perform exploratory data analysis (EDA) to uncover trends and correlations

* Train and evaluate regression model to predict insurance premiums

* Fine-tune the model using hyperparameter optimization to improve performance

* Visualize model results and key feature importances to derive insights

## Methodology

* Loaded and explored the insurance dataset, confirming data quality

* Performed univariate and multivariate analysis on variables such as `age`, `bmi`, `smoker`, `region`, and `charges`

* Encoded categorical features using **Label Encoding** and **One-Hot Encoding**

* Conducted correlation analysis to identify top predictors of insurance charges

* Trained a **Random Forest Regressor** to predict insurance premiums

* Evaluated model performance using **MAE** and **R² score**

* Applied **GridSearchCV** to tune model parameters such as `max_depth`, `min_samples_split`, and `min_samples_leaf`

* Compared model performance before and after tuning

## Key Visualizations

* **Countplot** showing distribution of smokers, gender, and regions

* **Correlation heatmap** displaying relationships between variables

* **Feature importance plot** highlighting key drivers of insurance charges

* **Model comparison plots** (before and after hyperparameter tuning) illustrating improvements in prediction accuracy

## Key Takeaways

* **Smoking status** is the most influential factor affecting insurance charges, followed by **BMI** and **age**

* **Region**, **sex** have minimal impact on premium costs, indicating near-uniform pricing across locations

* Model performance significantly improved after hyperparameter tuning, reducing prediction error

* The final model achieved a strong **R² score (~0.88)** and low **MAE (~$2,500)** on the test set

* Feature importance and correlation analysis align, validating the interpretability of the model

## Conclusion

This project demonstrates the end-to-end process of building a regression model for predicting insurance premiums — from data cleaning and visualization to model tuning and evaluation. By understanding which variables drive costs, insurers can price policies more effectively, and customers can gain insight into the factors affecting their premiums. This type of analysis not only enhances decision-making but also strengthens the business value of data science in the insurance domain.
