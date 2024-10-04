import requests
import json

def emotion_detector(text_to_analyze):
    #IBM Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    #JSON
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            #For Success
            return response.json()
        else:
            #For Error
            return f"Error: Received response code {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"
