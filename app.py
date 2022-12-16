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
    age = int(request.form.get('age',type=int))
    x= print(f"age:{age}")
    sex = int(request.form.get('sex',type=int))
    cp = int(request.form.get('cp', type=int))
    trestbps = int(request.form.get('trestbps', 120,type=int))
    chol = int(request.form.get('chol', 50,type=int) )
    fbs = int(request.form.get('fbs', 10,type=int))
    restecg = int(request.form.get('restecg', 0,type=int))
    thalach = int(request.form.get('thalach', 2,type=int))
    exang = int(request.form.get('exang', 100,type=int) ) 
    oldpeak = request.form.get('oldpeak', 1.2,type=float) 
    slope = int(request.form.get('slope', 2,type=int))
    ca = int(request.form.get('ca', 0,type=int))
    thal = int(request.form.get('thal', 20,type=int))
    input_query =np.array([[age , sex ,cp ,trestbps,chol,fbs,restecg,thalach,exang,
                                oldpeak,slope,ca,thal]])
    result = model.predict(input_query)[0]
    # return x
    return jsonify({'placement':str(result)})

if __name__ == '__main__':
    app.run(debug=True)
