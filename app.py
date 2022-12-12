from flask import Flask,request,jsonify
import pickle
import numpy as np

model = pickle.load(open('M.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return "hello noor"

@app.route('/predict',methods=['POST'])
def predict():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    cp = int(request.form.get('cp'))
    trestbps = int(request.form.get('trestbps'))
    chol = int(request.form.get('chol') )
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form.get('restecg'))
    thalac = int(request.form.get('thalac'))
    exang = int(request.form.get('exang') ) 
    oldpeak = request.form.get('oldpeak') 
    slop = int(request.form.get('slop'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))
    input_query =np.array([[age , sex ,cp ,trestbps,chol,fbs,restecg,thalac,exang,
                                oldpeak,slop,ca,thal]])
    result = model.predict(input_query)[0]
    return jsonify({'placement':str(result)})

if __name__ == '__main__':
    app.run(debug=True)