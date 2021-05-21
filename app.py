from flask import Flask, jsonify,  request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        #username = request.form.get("USERNAME")
        from model import DPR
        model_load = DPR()
        abb= model_load.predict() 
        return render_template('index.html', prediction_text= abb)
    else :
        return render_template('index.html')


if __name__ == '__main__':
    print('*** App Started ***')
    app.run(debug=True)
