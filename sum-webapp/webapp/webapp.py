from flask import Flask, request, jsonify, render_template
import requests, os

app = Flask(__name__)
logic_url = os.environ.get('SUM_LOGIC_API_URL')
lb_url = os.environ.get('SUM_WEBAPP_LB_URL')

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", webapp_lb_url=lb_url)

@app.route("/summary", methods=['GET','POST'])
def summary():
    r = requests.post("{}/summary".format(logic_url), json=request.get_json(), timeout=3)
    return jsonify(text=r.json()['text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
