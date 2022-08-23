from flask import Flask
from pytube import YouTube

app = Flask(__name__)



@app.route("/", methods = ["GET", "POST"])
def home():
    pass

@app.route("/download", methods = ["GET", "POST"])
def download_video():
    pass