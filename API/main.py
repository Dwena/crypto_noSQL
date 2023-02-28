from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def go_home():
    return 'Welcome to the CryptoData API!'

if __name__=="__main__":
    app.run()