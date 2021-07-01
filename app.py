from flask import Flask, json, jsonify, request, make_response
# from tensorflow.keras.models import load_model
# import numpy as np
#from PIL import Image
#import sys
#import io

app = Flask(__name__)

# longitud, altura = 224, 224
# modelo = 'Modelo\modelo.h5'
# pesos = 'Modelo\pesos.h5'
# cnn = load_model(modelo) 
# cnn.load_weights(pesos) 

@app.route('/')
def Home():  
  return 'API Para Detección de Autismo'

# @app.route('/predict', methods=['POST'] )
# def Predict():
#   try:
#     file = request.files['file'].read()
#     image = Image.open(io.BytesIO(file))    
#     resizedImage = image.resize((longitud, altura))
#     x = np.expand_dims(resizedImage, axis=0)   
#     arreglo = cnn.predict(x)  
#     resultado = arreglo[0] 
#     autistic = (100 * (1 - resultado))
#     no_autistic = 100 * resultado
#     res = jsonify(tea = float(autistic), sinTea = float(no_autistic), estado = True)
#     return make_response(res, 200)
#   except :
#     res = jsonify(estado = False, mensaje = str(sys.exc_info() ) )
#     return make_response(res, 500)


if __name__ == '__main__':
  app.run(debug=True) 
