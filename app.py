from flask import Flask, redirect, url_for, request, render_template
#from symptom_diagnosis import diagnose
import sys
sys.path.append('./')
from prediction import predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/symptoms', methods=['POST', 'GET'])
def symptoms():
    if request.method == 'POST':
        symptoms = request.form["nm"]
        return redirect(url_for("diagnosis", symptoms_list = symptoms))
    else:
        return render_template("symptoms.html")
 
@app.route('/diagnosis/<symptoms_list>')
def diagnosis(symptoms_list):

    output_str = predict(symptoms_list.split(", "))
    # final_list = diagnose(symptoms_list.split(", "), {'chest pain': 'breathing execies', 'cough': 'cough medicine'})
    # output_str = ""
    # for i in range(len(final_list)):
    #     output_str += final_list[i]
    #     if i != len(final_list) -1:
    #         output_str += ", "
    return f"<p><h1>The diagnosis for your symptoms {symptoms_list} are as follows:</h1></p> \
        <p>{output_str}</p>"

if __name__ == '__main__':
    app.run(debug=True)
