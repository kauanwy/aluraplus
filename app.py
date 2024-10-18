from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def Alura_plus():
    return render_template('alura_plus.html')

if __name__ == "__main__":
    app.run(debug=True)