from flask import Flask,render_template
import requests
app = Flask(__name__)

# @app.route('/')
# def index():
#     # r = requests.get('https://n95grvwygg.execute-api.us-east-1.amazonaws.com/default/test2')
#     return render_template("yes/index.html")

@app.route('/hello')
def hello():

    r = requests.get('https://n95grvwygg.execute-api.us-east-1.amazonaws.com/default/test2')
    print(type(r.text))
    return r.text

@app.route('/',methods = ['POST', 'GET'])
def result():
    res = requests.get('https://n95grvwygg.execute-api.us-east-1.amazonaws.com/default/test2')
    # res = {'a': 50, 'b': 60}
    return render_template("result.html", result=res)

if __name__ == '__main__':
   app.run()

