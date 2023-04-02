from flask import Flask, render_template, jsonify, request

from utils import MedicalInsurance
import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    if request.method == 'POST':
        data = request.form.get

        print("User Data is :",data)
        age = int(data('age'))
        gender = data('gender')
        bmi = eval(data('bmi'))
        children = int(data('children'))
        smoker = data('smoker')
        region = data('region')

        medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
        charges = medical_ins.predicted_price()

        return  render_template('index.html',prediction = charges)

    else:
        data = request.args.get

        print("User Data is ::::",data)
        age = int(data('age'))
        gender = data('gender')
        bmi = eval(data('bmi'))
        children = int(data('children'))
        smoker = data('smoker')
        region = data('region')

        medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
        charges = medical_ins.predicted_price()

        return  render_template('index.html',prediction = charges)
            
    # except:
    #     print(traceback.print_exc())
    #     return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080,debug=False)
