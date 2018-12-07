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

@app.route("/videoes/<int:index>", methods=['GET'])
def getVideoByIndex(index):
    videos = getPlaylistLinks(YOUTUBE_CHANNEL_URL)
    return jsonify(videos[int(index)])

@app.route("/videoes", methods=['GET'])
def getVideos():
    limit = request.args.get('limit') # Sets the limit of videoes received
    videos = getPlaylistLinks(YOUTUBE_CHANNEL_URL)
    return jsonify(videos[:int(limit)])

if __name__ == "__main__":
    app.run(debug=True)



# Get youtube id
#http://youtu.be/5Y6HSHwhVlY
#http://www.youtube.com/embed/5Y6HSHwhVlY?rel=0
#http://www.youtube.com/watch?v=ZFqlHhCNBOI

# regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

# match = regex.match(self.youtube_url)

# if not match:
#     print('no match')
# print(match.group('id'))

    # match = regex.match("http://www.youtube.com/watch?v=ZFqlHhCNBOI")
    # print(match.group('id'))
