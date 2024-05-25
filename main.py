from flask import Flask, render_template, request, redirect, url_for, jsonify
import matplotlib.pyplot as plt
import numpy as np
import logging
import os

app = Flask(__name__)




@app.route("/language", methods=['GET', 'POST'])
def language():
    return render_template("language.html")

@app.route("/behavior", methods=['GET', 'POST'])
def behavior():
    return render_template("behavior.html")

@app.route("/emotion", methods=['GET', 'POST'])
def emotion():
    return render_template("emo.html")

@app.route("/sense", methods=['GET', 'POST'])
def sense():
    return render_template("sense.html")

@app.route("/social", methods=['GET', 'POST'])
def social():
    return render_template("social.html")

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Server Error: {error}")
    return

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')  # Run the Flask development server
