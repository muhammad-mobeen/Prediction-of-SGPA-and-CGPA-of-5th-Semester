# Predictive Models for SGPA and CGPA Prediction

## [Live Demo](https://emproject.streamlit.app/)

This repository contains code for predicting SGPA (Semester Grade Point Average) and CGPA (Cumulative Grade Point Average) for the fifth semester of a student based on various input features.

## Overview

The project consists of two main components:

1. **EM_Models.ipynb**: A Jupyter Notebook where predictive models are trained and evaluated using a dataset. The notebook covers Linear Regression, Support Vector Regression (SVR), Neural Network, XGBoost, and Random Forest Regressor models.

2. **main.py**: A Python script utilizing the trained models to create a Streamlit web application. Users can input their academic data, and the application displays predictions for SGPA and CGPA using different models.

## Usage

### 1. Training Predictive Models

#### Dependencies
- Ensure the required Python libraries are installed using `pip install -r requirements.txt`.

#### Steps
1. Open and run the `EM_Models.ipynb` notebook to:
   - Load the dataset (`Final Data Set - Altered.xlsx`).
   - Preprocess the data, handle missing values, and select relevant features.
   - Train various models: Linear Regression, SVR, Neural Network, XGBoost, and Random Forest Regressor.
   - Evaluate and save the trained models in the `models` directory.

### 2. Making Predictions

#### Dependencies
- Make sure to have the required Python libraries installed using `pip install -r requirements.txt`.

#### Steps
1. Run the Streamlit application using `streamlit run main.py`.
2. Access the web application in your browser.
3. Input your academic data in the provided sliders.
4. Click the "Submit" button to view predictions for SGPA and CGPA using different models.
5. The application will display results in a table with SGPA and CGPA predictions, as well as remarks for each.

## File Structure

- `EM_Models.ipynb`: Jupyter Notebook for training predictive models.
- `main.py`: Python script for the Streamlit web application.
- `models/`: Directory to store the trained models.
- `requirements.txt`: List of required Python libraries.
- `Final Data Set - Altered.xlsx`: Dataset used for model training.
- `README.md`: Detailed documentation about the project.

## Credits

This project was created by [Muhammad Mobeen](muhammadmobeen.com). Feel free to reach out for any questions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the contributors and libraries used in this project. See `EM_Models.ipynb` and `main.py` for specific dependencies and references.

---
