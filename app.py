from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def home():
    if(request.method == 'GET'):
        data = "hello harshal"
        return data #return jsonify({'data': data})
    
    if(request.method == 'POST'):
        return("ssfsds")
    
    if(request.method == 'PUT'):
        return("ssfsds")
    
    if(request.method == 'DELETE'):
        return("ssfsds")

# driver function
if __name__ == '__main__':

	app.run(debug = True)
