import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
iris_model = pickle.load(open('iris_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Iris - Flower Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)









# Iris
if selected == 'Iris - Flower Prediction':

    # page title
    st.title('Flower Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        sepalLength = st.text_input('Sepal Length')

    with col2:
        sepalWidth = st.text_input('Sepal Width')

    with col3:
        petalLength = st.text_input('Petal Length')

    with col1:
        petalWidth = st.text_input('Petal Width')

    # code for Prediction
    iris_diag = ''

    # creating a button for Prediction

    if st.button(' Result'):

        user_input = [sepalLength, sepalWidth, petalLength, petalWidth]

        user_input = [float(x) for x in user_input]

        iris_prediction = iris_model.predict([user_input])

        if iris_prediction[0] == 0:
            iris_diag = 'Setosa'
        elif iris_prediction[0] == 1:
            iris_diag = 'Versicolor'
        else:
            iris_diag = 'Virginica'

    st.success(iris_diag)





# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Coming Soon...")



