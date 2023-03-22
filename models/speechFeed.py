from flask import Flask, render_template, redirect, request
import speech_recognition as sr

def contentPOST():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED Send Post Request")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
    elif request.method == "GET":
        print("Send GET Request")
    
    return transcript


