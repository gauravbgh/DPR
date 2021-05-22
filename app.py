from flask import Flask, jsonify,  request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from model import DPR

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        #username = request.form.get("USERNAME")
        ar1 = request.form["ar1"]
        ar3 = request.form["ar3"]
        ar4 = request.form["ar4"]
        
        
        ar1_list = ar1.split("\n")
        #ar3_list = ar3.split("\n")
        #ar4_list = ar4.split("\n")
        
        
        #model_load = DPR(ar1_list, ar3_list, ar4_list)
        #abb= model_load.predict() 
        return render_template('index.html', prediction_text= ar1_list)
    else :
        return render_template('index.html')


if __name__ == '__main__':
    print('*** App Started ***')
    app.run(debug=True)
