# Early Readmission Prediction (ERP) Model

> The ERP Model is a machine learning project that aims to predict the likelihood of a patient being readmitted to the hospital within 30 days of discharge. The model uses patient data, such as demographic information, medical history, medication history, and lab results, to make predictions.

## Problem Statement

Hospital readmissions can be costly and potentially harmful to the patient's health. Therefore, it is important to develop predictive models that can accurately identify patients at risk of readmission within 30 days of discharge. The ERP Model aims to address this problem by predicting the likelihood of readmission and enabling healthcare providers to intervene early with appropriate care and resources to prevent readmissions and improve patient outcomes.

## Data

The ERP Model uses a dataset of patient data collected from electronic health records (EHRs) or other healthcare databases. The dataset includes demographic information, medical history, medication history, and lab results for a large sample of patients who have been discharged from the hospital. The data has been preprocessed to make it suitable for modeling, including cleaning the data, removing missing values, encoding categorical variables, and normalizing numeric variables.

## Model

The ERP Model uses a machine learning algorithm to predict the likelihood of readmission within 30 days of discharge. The algorithm is trained on a training set of patient data and tuned to optimize its performance. The model is evaluated on a testing set of patient data using appropriate metrics, such as accuracy, precision, recall, and F1 score. The model is deployed in a production environment where it can be used to predict readmission risk for new patients.

## Installation

To install the ERP Model, clone the repository and install the required packages using pip:

```
git clone https://github.com/AnthonyByansi/erp-model.git

cd erp-model
pip install -r requirements.txt
```

## Usage

To use the ERP Model, import the `erp_model` module and call the `predict` function with a patient's data:

```
from erp_model import predict

patient_data = {
    'age': 60,
    'gender': 'M',
    'diagnosis': 'heart failure',
    'medications': ['furosemide', 'lisinopril'],
    'lab_results': {'sodium': 135, 'potassium': 4.0, 'creatinine': 1.2}
}

readmission_probability = predict(patient_data)

print(f"Readmission probability: {readmission_probability}")

```

The `predict` function returns a probability between 0 and 1, indicating the likelihood of readmission within 30 days of discharge

## Credits

The ERP Model was developed by Byansi Anthony as a project for Kaggle. Special thanks to my mentor for guidance and support.
