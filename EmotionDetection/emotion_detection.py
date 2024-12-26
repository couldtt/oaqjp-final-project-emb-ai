import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {
        "raw_document": { "text": text_to_analyse } 
    }
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code == 400:
        default_emotion = {
            "anger": None,
            "disgust": None,
            "dominant_emotion": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
        return default_emotion
    data = resp.json()
    emotions = data['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

