import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj ={ "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        return {
            'anger' : None,
            'sadness': None,
            'disgust': None,
            'joy': None,
            'fear': None,
            'dominant_emotion': None
        }
    elif response.status_coe == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        max_emotion = 0
        emotion_score = {}
        for e in emotions:
            emotion_score[e] = emotions[e]
            if emotions[e] > max_emotion:
                max_emotion = emotions[e]
                emotion_score['dominant_emotion'] = e

        return emotion_score