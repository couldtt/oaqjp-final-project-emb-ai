"""
The emotion detection server
"""
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def ed_handler():
    """
    The emotion detector
    """
    text = request.args.get('textToAnalyze', '')
    resp = emotion_detector(text)
    if resp['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return resp

if __name__ == '__main__':
    app.run()
