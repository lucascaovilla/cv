from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask("Lucas Grisa Caovilla")

@app.route('/')
def home():
    return render_template('index.html')

app.run(host='0.0.0.0')
 