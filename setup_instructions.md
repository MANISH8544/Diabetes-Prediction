# Diabetes Prediction Website

A modern web application that uses machine learning to predict diabetes risk based on health parameters.

## Project Structure
```
diabetes-prediction/
│
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── diabetes_model.joblib  # Your trained ML model (place here)
├── templates/
│   └── index.html        # Frontend template
└── README.md             # This file
```

## Setup Instructions

### 1. Create Project Directory
```bash
mkdir diabetes-prediction
cd diabetes-prediction
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Project Structure Setup
Create the following folder structure:
```bash
mkdir templates
```

Then place the files as follows:
- `app.py` in the root directory
- `index.html` in the `templates/` folder
- Your `diabetes_model.joblib` file in the root directory
- `requirements.txt` in the root directory

### 5. Model File
Make sure your trained model file is named `diabetes_model.joblib` and placed in the root directory. The model should be trained to predict diabetes using these features in order:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Features

- **Modern UI**: Clean, responsive design with gradient backgrounds
- **Form Validation**: Client-side validation for all input fields
- **Real-time Prediction**: AJAX-based predictions without page reload
- **Risk Assessment**: Shows probability percentage and risk level
- **Mobile Responsive**: Works on all device sizes
- **Loading States**: Visual feedback during prediction
- **Error Handling**: Graceful error handling and user feedback

## Model Requirements

Your joblib model should have:
- `predict()` method for binary classification (0 = No Diabetes, 1 = Diabetes)
- `predict_proba()` method for probability estimation
- Trained on features in the exact order listed above

## Input Parameters

1. **Pregnancies**: Number of times pregnant (0-20)
2. **Glucose**: Plasma glucose concentration mg/dL (0-300)
3. **Blood Pressure**: Diastolic blood pressure mmHg (0-200)
4. **Skin Thickness**: Triceps skin fold thickness mm (0-100)
5. **Insulin**: 2-Hour serum insulin μU/mL (0-1000)
6. **BMI**: Body mass index kg/m² (0-70)
7. **Diabetes Pedigree Function**: Genetic predisposition (0-3)
8. **Age**: Age in years (1-120)

## Risk Levels

- **Low Risk**: < 30% probability
- **Moderate Risk**: 30-60% probability
- **High Risk**: > 60% probability

## Disclaimer

This application is for educational and demonstration purposes only. The predictions should not be used as a substitute for professional medical advice, diagnosis, or treatment.