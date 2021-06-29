from flask import Flask, json, jsonify, request, make_response

app = Flask(__name__)


@app.route('/')
def Home():
  return 'Test'

if __name__ == '__main__':
  app.run(debug=True) 
