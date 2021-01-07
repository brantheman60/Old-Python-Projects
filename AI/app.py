import os
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()
key = os.getenv('KEY')
region = os.getenv('REGION')

stop = False
def recognized(args):
    global stop
    print(args.result.text)

    if args.result.text == 'Stop.":
        stop=True

speech_config = speechsdk.SpeechConfig(subscription=key,
                                    region=region,
                                    speech_recognition_level='en-GB')

recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

recognizer.recognized.connect(recognized)
recognizer.start_continuous_recognition()

print("Say something! Say stop when you are done")

while not stop:
    time.sleep(0.1)
