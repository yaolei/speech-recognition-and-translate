import speech_recognition as sr
from time import sleep
import json
# server.serveforever()

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     print("Say something!")
#     while True:
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             message = json.dumps({'transcription': text})
#             server.sendMessage(message)
#         except sr.UnknownValueError:
#             print("Google Web API could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results from Google Web API; {0}".format(e))





def text():
    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)
    try:
        print("A moment of silence, please...")
        with m as source: 
            r.adjust_for_ambient_noise(source)
            run = True     
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while run:
            # sleep(0.01)
            print("Say something!")
            with m as source: audio = r.listen(source)
            
            print("Got it! Now to recognize it...")

            with open("recording.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:
                value = r.recognize_google(audio)
                k = format(value)
                if ("stop" in k):
                    print("system would be stop ........")
                    run = False
                else:
                    run = False
                    print("You said {}".format(value))
                    return k
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass

# if __name__ == "__main__":
#     text()