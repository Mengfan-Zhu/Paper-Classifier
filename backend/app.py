from flask import Flask, request

app = Flask(__name__)

# route config
@app.route('/backend/classifier')
def classifier():
    results = {'result': "Result"}
    return results