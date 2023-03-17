from flask import Flask, render_template,url_for, request, redirect, jsonify
from models import test as t
import speech_recognition as sr
import io, os, sys
import numpy as np
import http.client
import hashlib
import urllib
import random

import time

sys.path.append('./')
from threading import Thread as thread
import json
from flask_cors import CORS

from flask_socketio import SocketIO, emit
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

clients = []

appid = '20230316001602460'
secretKey = 'SiuppNQx32iV7g6cnjGN'

httpClient = None
myurl = '/api/trans/vip/translate'

class SimpleChat(WebSocket):

    def handleMessage(self):
        # echo message back to client
        language = self.data
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            now =  time.localtime()
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
            print(now_time +":- Say something!")
            audio = r.listen(source)
            message = "no value"
            try:
                # text = r.recognize_google(audio, language="zh-CN")
                text = r.recognize_google(audio)
                if language != "zh-CN":
                    text = translateWoldToChinese(text)
                else :
                    text = r.recognize_google(audio, language="zh-CN")
                message = json.dumps({'transcription': text})
            except sr.UnknownValueError:
                self.sendMessage("no value")
                print("Unknown value")
                print("--------------------------------")
            except sr.RequestError as e:
                print("Could not request results from Google Web API; {0}".format(e))
            self.sendMessage(message)

    def handleConnected(self):
        print(self.address, 'connected')
        
    def handleClose(self):
        print(self.address, 'closed')
server = SimpleWebSocketServer('', 8002, SimpleChat)


def translateWoldToChinese(msg):

    fromLang = 'auto'  
    toLang = 'zh' 
    salt = random.randint(32768, 65536)
    q= msg
    
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurlBase = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurlBase)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        # [{'src': 'good morning', 'dst': '早上好'}]
        translate_result = list(result['trans_result'])[0]['dst']
        return translate_result
    except Exception as e:
        print (e)
        print("lost baidu connection")
    finally:
        if httpClient:
            httpClient.close()
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# @app.route("/api/v1/users")

# camera = cv2.VideoCapture(0)
# face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# # cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# def generate_frames():
#     while True:
#         ## read the camera frame
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#             color = (0, 255, 0)
#             normal = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             faceRects = face_classifier.detectMultiScale(
#                     normal, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
#             if len(faceRects):
#                 for faceRect in faceRects: 
#                     x, y, w, h = faceRect
#                     cv2.rectangle(frame, (x, y), (x + h, y + w), color, 2)
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 print('222')
#                 break
#             yield(b'--frame\r\n'
#                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# def __del__():
#         camera.release()
#         cv2.destroyAllWindows()

@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/video")
# def video():
#     return Response(generate_frames(),mimetype="multipart/x-mixed-replace;boundary=frame" )

# @app.route("/stop_video")
# def stop_video():
#     __del__()
#     # redirect(request.url)
#     redirect(url_for('index'))


def display_video():
	return redirect(url_for('static', filename='test-stream.wav'), code=301)

@app.route("/speech", methods=["GET", "POST"])
def speech_feed():
    transcript = ""
    '''
        print html.render
        <!--<img src="{{ url_for('video') }}"  width="50%"/>-->
    '''
    return render_template("speech_feed.html", transcript = transcript)
@app.route("/foward/", methods=["GET", "POST"])
def foward():
    h = "test"
    return render_template("index.html", message = h)
    # return redirect(url_for("index", message = h))

@app.route("/chatInput", methods=["GET", "POST", "OPTIONS"])
def chatInput():
    k = {}
    if (request.method == "POST"):
        re = request.data.decode("UTF-8")
        k = json.loads(re)
        print(k['name'])
    return k

@app.route("/getMediaStream", methods=["GET", "POST", "OPTIONS"])
def getMediaStream():
    if (request.method == "POST"):
        print("###")
    # res = ""
    # if (request.method == "POST"):
    #     res = t.text()
    #     # noSpaceVal = res.replace(" ", "")
    #     # if (len(noSpaceVal) > 0):
    #     #     getMediaStream()
    # return res
    return "@@@"

@socketio.on('connect')
def handle_connect():
    print('WebSocket connected')

def run_server():
    print("WebSocket server running...")
    server.serveforever()

if __name__ == "__main__":
    server_thread = thread(target=run_server)
    server_thread.start()
    socketio.run(app)

    # app.run(host="0.0.0.0", debug=True, port=5000, threaded=True)


 