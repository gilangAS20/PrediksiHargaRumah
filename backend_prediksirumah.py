#from pyexpat import model
from flask import Flask, request, jsonify
import pandas as pd
import time
import matplotlib.pyplot as plt
import joblib
import sklearn

#model = pickle.load(open('model_prediksi_rumah_new.pkl', 'rb'))

app = Flask(__name__)

#pickle_in = open("model_prediksi_rumah_joblib.pkl", "rb")
loaded_model = joblib.load('model_prediksi_rumah_joblib.pkl')



@app.route('/')
def home():
    return "Hello World"

'''
@app.route('/predict', methods=['POST'])
def predict():
    jumlah_kamar = request.form.get('jumlah_kamar')
    jumlah_kamar_mandi = request.form.get('jumlah_kamar_mandi')
    luas = request.form.get('luas')
    jumlah_lantai = request.form.get('jumlah_lantai')
    grade = request.form.get('grade')
    luas_atas_tanah = request.form.get('luas_atas_tanah')
    rata_rata_luas = request.form.get('rata_rata_luas')
    tahun_dibangun = request.form.get('tahun_dibangun')

    result = {'jumlah_kamar': jumlah_kamar, 'jumlah_kamar_mandi': jumlah_kamar_mandi, 'luas': luas, 'jumlah_lantai': jumlah_lantai, 'grade': grade, 'luas_atas_tanah': luas_atas_tanah, 'rata_rata_luas': rata_rata_luas, 'tahun_dibangun': tahun_dibangun}

    return jsonify(result)
'''


@app.route('/predict', methods=['POST'])
def predict():
    jumlah_kamar = request.form.get('jumlah_kamar')
    jumlah_kamar_mandi = request.form.get('jumlah_kamar_mandi')
    luas = request.form.get('luas')
    jumlah_lantai = request.form.get('jumlah_lantai')
    grade = request.form.get('grade')
    luas_atas_tanah = request.form.get('luas_atas_tanah')
    rata_rata_luas = request.form.get('rata_rata_luas')
    tahun_dibangun = request.form.get('tahun_dibangun')

    input_query = np.array([[jumlah_kamar, jumlah_kamar_mandi, luas, jumlah_lantai, grade, luas_atas_tanah, rata_rata_luas, tahun_dibangun]])
    
    result = model.predict(input_query)[0]

    return jsonify({'hasil': result})

if __name__ == '__main__':
    app.run(debug=True)
    