from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
    __name__:str

if __name__=='__main__':
    app.run()