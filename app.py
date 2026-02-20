from flask import Flask, request 

app = Flask(__name__) 

# Ruta Principal
@app.route('/') 
def home():     
    return "<h1>¡Hola! Mi servidor de Arduino está en línea 🚀</h1>" 

# Ruta para recibir datos
@app.route('/sensor', methods=['POST', 'GET']) 
def sensor():     
    if request.method == 'POST':         
        datos = request.json         
        return f"Recibido: {datos}", 200     
    return "Aquí llegarán los datos del sensor", 200 

if __name__ == '__main__':     
    import os     
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)
