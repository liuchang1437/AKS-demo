from pyteaser import Summarize
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/summary", methods=['POST'])
def summary():
    title = request.get_json()['title']
    text = request.get_json()['text']
    summaries = Summarize(title, text)
    summary = " ".join(summaries)
    return jsonify(text=summary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
