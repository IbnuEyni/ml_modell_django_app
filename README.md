# Post Quality Predictor

## Overview
The Post Quality Predictor is a Django-based web application that predicts the quality of a post based on user reputation and taker interaction metrics. It uses a trained XGBoost machine learning model for prediction and provides visualizations for model performance evaluation.

## Features
- **Machine Learning Model**: Predicts post quality using XGBoost.
- **Interactive Web Interface**: Accepts user input for prediction through a Django web form.
- **Model Evaluation**: Includes metrics like RMSE, MAE, and R².
- **Visualization**: Displays charts for actual vs predicted values, residuals, and feature importance.

## Prerequisites
Ensure the following are installed:

- Python (>= 3.9)
- Django (4.2.7)
- Required Python libraries from `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IbnuEyni/ml_modell_django_app.git
   cd prediction
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add the `post_quality_model.joblib` file to the project directory.

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. Input `User Reputation` and `Interaction Delta` values on the form.
2. Click the **Predict** button to get the quality prediction.
3. View the predicted post quality on the result page.

## Demo

Below is a video demonstrating the app in action:

![Demo Video]('/home/shuaib/Desktop/School/Django/icog_django/ml_model_django_app.mp4') 


## Key Components

### `mll_model.py`
This script contains the `PostQualityPredictor` class, which:
- Loads and preprocesses data
- Trains and evaluates the XGBoost model
- Saves and loads the trained model
- Makes predictions for new inputs

### `views.py`
Handles user requests and integrates the machine learning model with the Django application.

### `templates/post_quality.html`
Defines the user interface for inputting data and displaying predictions.

## Dependencies
Install the required packages using:
```bash
pip install -r requirements.txt
```

Dependencies include:
- Django==4.2.7
- scikit-learn==1.3.2
- joblib==1.3.2
- numpy==1.26.2
- pandas==2.1.3
- xgboost==2.1.3
- matplotlib==3.8.0
- seaborn==0.12.2

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Contact
For any questions or feedback, please contact:
- **Name**: Amir Ahmedin
- **Email**: shuaibahmedin@gmail.com

