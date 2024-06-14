from os import getenv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    target = getenv('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

@app.route('/status', methods=['GET'])
def status():
	return jsonify(
    Message = "Hello {}!".format(getenv('TARGET', 'World')),
	), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8883)