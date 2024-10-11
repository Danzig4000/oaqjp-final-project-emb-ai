import requests
import json

def emotion_detector(text_to_analyse):
    #IBM Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = payload, headers = headers)
    structured_response = json.loads(response.text)

    #For Success
    if response.status_code == 200:        
        anger_count = structured_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_count = structured_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_count = structured_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_count = structured_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_count = structured_response["emotionPredictions"][0]["emotion"]["sadness"]
        emotion_list = [anger_count, disgust_count, fear_count, joy_count, sadness_count]
        dominant_emotion_index = emotion_list.index(max(emotion_list))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion_key = emotion_keys[dominant_emotion_index]
    
    #For Error
    elif response.status_code == 400:
        anger_count = None
        disgust_count = None
        fear_count = None
        joy_count = None
        sadness_count = None
        dominant_emotion_key = None

    #Structured response
    result = {
        'anger': anger_count,
        'disgust': disgust_count,
        'fear': fear_count,
        'joy': joy_count,
        'sadness': sadness_count,
        'dominant_emotion': dominant_emotion_key
    }
    
    return result
