import requests
import json

#URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#Input json: { "raw_document": { "text": text_to_analyse } }
def emotion_detector(text_to_analyze):
    #IBM Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    # JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # If successful
        if response.status_code == 200:
            # Convert to dictionary
            response_dict = json.loads(response.text)
            # Access the emotion predictions
            emotion_data = response_dict.get('emotionPredictions', [])[0].get('emotion', {})
            # Extract individual emotion scores
            anger_score = emotion_data.get('anger', 0)
            disgust_score = emotion_data.get('disgust', 0)
            fear_score = emotion_data.get('fear', 0)
            joy_score = emotion_data.get('joy', 0)
            sadness_score = emotion_data.get('sadness', 0)
            # Calculate dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            # Output results in specified format
            result = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            return result
        else:
            return f"Error: Received response code {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"
