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
        ar1 = str(request.form.get("ar1"))
        ar3 = str(request.form.get("ar3"))
        ar4 = str(request.form.get("ar4"))
        
        ar1_list = ar1.split("\n")
        ar3_list = ar3.split("\n")
        ar4_list = ar4.split("\n")
        
        
        model_load = DPR(ar1_list, ar3_list, ar4_list)
        abb= model_load.predict() 
        return render_template('index.html', prediction_text= abb)
    else :
        return render_template('index.html')


if __name__ == '__main__':
    print('*** App Started ***')
    app.run(debug=True)
