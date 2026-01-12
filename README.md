# Credit Score Prediction System

A machine learning-based system for predicting credit scores using French credit data. This project implements data preprocessing, model training, and a web application for real-time credit score predictions.

## Project Overview

This project uses machine learning algorithms to predict credit scores for individuals based on their financial behavior and demographic information. The system classifies credit scores into three categories:
- **Good Credit Score (0)**
- **Poor Credit Score (1)**
- **Standard Credit Score (2)**

## Dataset

The project uses French credit data (`credit_FR.csv`) containing various financial and demographic features including:
- Age, Annual Income, Monthly Income
- Banking information (number of accounts, credit cards)
- Loan details (interest rates, number of loans, payment history)
- Credit utilization and debt information
- Occupation, payment behavior patterns

## Technology Stack

- **Python 3.x**
- **Machine Learning**: scikit-learn, XGBoost
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Web Framework**: Streamlit
- **Model Persistence**: joblib

## Dependencies

Install the required packages using:
```bash
pip install -r requirements.txt
```

Key dependencies:
- pandas==2.0.3
- numpy==1.24.3
- scikit-learn==1.3.0
- xgboost==2.0.0
- streamlit==1.24.1
- matplotlib==3.7.2
- seaborn==0.12.2

## Usage

### Running the Web Application

1. Ensure all dependencies are installed
2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your browser and navigate to the provided local URL
4. Fill in the applicant's details in the form
5. Click "Predict Credit Score" to get the prediction

### Data Processing and Model Training

The project includes Jupyter notebooks for data cleaning and model development:
- `creditScore-Prediction/src/dataCleaning.ipynb` - Data preprocessing and cleaning
- `creditScore-Prediction/src/modeling.ipynb` - Model training and evaluation

## Project Structure

```
creditScore-Prediction/
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── creditScore-Prediction/
│   ├── data/                      # Dataset files
│   │   ├── credit_FR.csv         # Raw dataset
│   │   ├── cleaned_credit_FR.csv # Cleaned dataset
│   │   └── cleaned_credit_FR_age_18_60.csv # Age-filtered dataset
│   ├── models/                    # Trained models and encoders
│   │   ├── labelEncoders/        # Label encoders for categorical variables
│   │   └── ordinalEncoders/      # Ordinal encoders
│   ├── src/                       # Source code
│   │   ├── dataCleaning.ipynb    # Data preprocessing notebook
│   │   └── modeling.ipynb        # Model training notebook
│   ├── visuals/                   # Generated visualizations
│   │   ├── Boxplots for the different Numeric Features.png
│   │   ├── Correlation Matrix of Numeric Features.png
│   │   └── [Other visualization files]
│   ├── logging/                   # Logging utilities
│   ├── output/                    # Output files
│   └── pipeline/                  # ML pipeline components
├── template.py                    # Project structure setup script
└── Dockerfile                     # Docker configuration
```

## Features

### Input Features
The application accepts both numerical and categorical inputs:

**Numerical Features:**
- Age (18-60 years)
- Annual Income, Monthly Inhand Income
- Number of Bank Accounts, Credit Cards
- Interest Rate, Number of Loans
- Payment delays and credit inquiries
- Outstanding debt and credit utilization
- Monthly investments and balance

**Categorical Features:**
- Occupation (Scientist, Teacher, Engineer, etc.)
- Month (January, July, August, etc.)
- Credit Mix (Good, Standard, Bad)
- Payment behavior patterns
- Minimum payment status

### Model Performance
The system uses a Random Forest classifier as the primary prediction model, with label encoders for categorical variables to ensure proper preprocessing.


## Visualizations

The project includes comprehensive data visualizations:
- Boxplots for numeric features
- Correlation matrices
- Categorical feature distributions by credit score
- Age vs income and credit score scatter plots
- Credit mix analysis

## Data Preprocessing

The data cleaning process includes:
- Handling missing values
- Age filtering (18-60 years)
- Categorical variable encoding
- Feature engineering
- Data validation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Disclaimer

This is a machine learning demonstration project. The predictions should not be used as the sole basis for financial decisions. Always consult with financial professionals for credit assessments.
