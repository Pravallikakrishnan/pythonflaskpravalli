from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Cloud Computing. Your Python Flask app is successfully running on Azure App Service!"

if __name__ == '__main__':
    app.run(debug=True)

