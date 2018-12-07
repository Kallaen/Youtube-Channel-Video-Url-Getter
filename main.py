import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


from bs4 import BeautifulSoup
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS #CORS enabled for local use
app = Flask(__name__)
CORS(app) #CORS enabled for local use
YOUTUBE_CHANNEL_URL = "https://www.youtube.com/channel/UCfbmt_LlITBd9QF4nOEFjuA/videos"

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    arr = []
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            arr.append(domain + href)
    return arr

@app.route("/videos/<int:index>", methods=['GET'])
def getVideoByIndex(index):
    videos = getPlaylistLinks(YOUTUBE_CHANNEL_URL)
    return jsonify(videos[int(index)])

@app.route("/videos", methods=['GET'])
def getVideos():
    limit = request.args.get('limit') # Sets the limit of videos received
    videos = getPlaylistLinks(YOUTUBE_CHANNEL_URL)
    return jsonify(videos[:int(limit)])

if __name__ == "__main__":
    app.run(debug=True)