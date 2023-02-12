import streamlit as st

import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import joblib

#load model yang sudah di train
#pickle_in = open("model_prediksi_rumah_new.pkl", "rb")
#random_forest_regression_model = pickle.load(pickle_in)

loaded_model = joblib.load('model_prediksi_rumah_joblib.pkl')


def Home():
    return ('Sabar gan')
#'bedrooms', 'bathrooms', 'sqft_living', 'floors',	'grade', 'sqft_above, 'sqft_living15', 'yr_built'
def predicting(bedrooms, bathrooms, sqft_living,  floors, grade, sqft_above, sqft_living15, yr_built):
    prediction = loaded_model.predict([[bedrooms, bathrooms, sqft_living,  floors, grade, sqft_above, sqft_living15, yr_built]])
    output = round(prediction[0], 2)
    return output
# 'bedrooms', 'bathrooms', 'sqft_living', 'floors',	'grade', 'sqft_above, 'sqft_living15, 'yr_built'
def main():
    html_temp = """
    <div style="background-color:navy;padding:10px">
    <h1 style="color:white;text-align:center;">Prediksi Harga Rumah ($) </h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.subheader("Jumlah Kamar") #bedrooms
    bedrooms = st.slider("", min_value=0, max_value=11, value=0, step=1)

    st.subheader("Jumlah Kamar Mandi") #bathrooms
    bathrooms = st.slider("", min_value=0, max_value=8, value=0, step=1)

    st.subheader("Luas") #sqft_living
    sqft_living = st.text_input("luas bangunan secara keseluruhan (sqft)", "")

    st.subheader("Jumlah Lantai") #floors
    floors = st.slider("", min_value=1, max_value=3, value=1, step=1)

    st.subheader("Kelas / Grade") #grade
    grade = st.slider("", min_value=1, max_value=13, value=1, step=1)

    st.subheader("Luas bangunan di atas tanah")#sqft_above
    sqft_above = st.text_input("(sqft)", "")

    st.subheader("Rata-rata luas sekitar") #sqft_living15
    sqft_living15 = st.text_input("rata-rata luas tanah 15 tetangga terdekat (sqft)", "")

    st.subheader("Tahun Dibangun") #yr_built
    yr_built = st.text_input("tahun rumah dibangun", "")
    
    result = ""
    if st.button("Perkiraan harga"):

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        result = predicting(bedrooms, bathrooms, sqft_living, floors, grade, sqft_above, sqft_living15, yr_built)

    st.success('Hasil Prediksi : {} Dollars'.format(result))


nav = st.sidebar.radio("Halaman", ["Home", "Data Sample", "About Me"])
if nav == "Home":
    if __name__ == "__main__":
        main()

if nav == "Data Sample":
    st.title("Data Sample")
    data = pd.read_csv("dataFrame_test_train_new.csv", usecols=['bedrooms', 'bathrooms', 'sqft_living', 'floors',	'grade', 'sqft_above', 'sqft_living15', 'yr_built'])
    st.table(data.sample(100))
    plt.show()

# 'bedrooms', 'bathrooms', 'sqft_living', 'floors',	'grade', 'sqft_above, 'sqft_living15, 'yr_built'
if nav == "About Me":
    st.title(" Prediksi Harga Rumah")
    st.subheader("Gilang Agung Saputra (672019229)")
    
