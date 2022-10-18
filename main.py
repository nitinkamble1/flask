from flask import Flask,jsonify,render_template,request

app = Flask(__name__)

@app.route('/')
def hellow_flask():
    return "hellow Flask"

@app.route('/test')
def test():
    return ("this is my Test API")


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= 5000, debug=True)