import streamlit as st
from joblib import load
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

class PredictiveModels:
    def __init__(self) -> None:
        self.linear_regression_model = load('models/linear_regression.joblib')
        self.neural_network_model = load_model('models/neural_network.h5')
        self.random_forest_regressor_model = load('models/random_forest_regressor.joblib')
        self.svr_model = load('models/svr.joblib')
        self.xgboost_model = load('models/xgboost.joblib')
        self.scaler = StandardScaler()

    def get_predictions(self, input_data):
        response = {
            'Random Forest Regressor Prediction': self.random_forest_regressor_model.predict(input_data)[0],
            'Linear Regression Prediction': self.linear_regression_model.predict(input_data)[0],
            'Support Vector Regressor (SVR) Prediction': self.svr_model.predict(input_data)[0],
            'XGBOOST Prediction': self.xgboost_model.predict(input_data)[0],
            'Neural Network Prediction': self.neural_network_model.predict(input_data)[0][0]%5,
        }
        return response
    
# Function to preprocess input data
def preprocess_input(matric_percentage, intermediate_percentage, sgpa_bs1, sgpa_bs2, sgpa_bs3, sgpa_bs4):
    data = {
        "Matric percentage": [matric_percentage],
        "Intermediate percentage": [intermediate_percentage],
        "SGPA in BS First semester": [sgpa_bs1],
        "SGPA in BS Second semester": [sgpa_bs2],
        "SGPA in BS Third semester": [sgpa_bs3],
        "SGPA in BS Fourth semester": [sgpa_bs4]
    }
    data_df = pd.DataFrame(data)
    return data_df

def gpa_remarker(gpa):
    if gpa >= 3.50 and gpa <= 4.00:
        return "Extraordinary Performance"
    elif gpa >= 3.00 and gpa < 3.50:
        return "Very Good Performance"
    elif gpa >= 2.50 and gpa < 3.00:
        return "Good Performance"
    elif gpa >= 2.00 and gpa < 2.50:
        return "Satisfactory Performance"
    elif gpa >= 1.00 and gpa < 2.00:
        return "Poor Performance"
    elif gpa >= 0.00 and gpa < 1.00:
        return "Very Poor Performance"
    else:
        return "Error in Prediction"

# Function to display the Streamlit UI
def main():
    st.title("Prediction of SGPA and CGPA of 5th Semester")

    # User input form
    matric_percentage = st.slider("Matric Percentage", 0.0, 100.0, 50.0)
    intermediate_percentage = st.slider("Intermediate Percentage", 0.0, 100.0, 50.0)
    sgpa_bs1 = st.slider("SGPA in BS First Semester", 0.0, 4.0, 2.0)
    sgpa_bs2 = st.slider("SGPA in BS Second Semester", 0.0, 4.0, 2.0)
    sgpa_bs3 = st.slider("SGPA in BS Third Semester", 0.0, 4.0, 2.0)
    sgpa_bs4 = st.slider("SGPA in BS Fourth Semester", 0.0, 4.0, 2.0)

    if st.button("Submit"):
        input_data = preprocess_input(matric_percentage, intermediate_percentage, sgpa_bs1, sgpa_bs2, sgpa_bs3, sgpa_bs4)
        models = PredictiveModels()
        predictions = models.get_predictions(input_data)

        # Display predictions in a table
        st.subheader("Predictions:")
        prediction_table = {'Model': list(predictions.keys()), 'SGPA in BS Fifth Semester Prediction': [format(value, ".2f") for value in predictions.values()], 'CGPA in BS Fifth Semester Prediction': [format((value + sgpa_bs1 + sgpa_bs2 + sgpa_bs3 + sgpa_bs4)/5, ".2f") for value in predictions.values()], 'SGPA Remarks': [gpa_remarker(float(format(value, ".2f"))) for value in predictions.values()], 'CGPA Remarks': [gpa_remarker(float(format(value, ".2f"))) for value in predictions.values()]}
        prediction_table_df = pd.DataFrame(prediction_table)
        prediction_table_df.index += 1
        st.table(prediction_table_df)

if __name__ == "__main__":
    # ui()
    # data = {
    #     "Matric percentage": [80],
    #     "Intermediate percentage": [70],
    #     "SGPA in BS First semester": [1],
    #     "SGPA in BS Second semester": [2],
    #     "SGPA in BS Third semester": [3],
    #     "SGPA in BS Fourth semester": [2.5]
    # }
    # agent = PredictiveModels()
    # ddf = agent.get_predictions(pd.DataFrame(data))
    # print(ddf)
    main()
