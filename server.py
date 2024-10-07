from flask import Flask, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze:
        return "No text provided for analysis.", 400

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    if isinstance(result, dict):  # Successful response
        response_text = f"For the given statement, the system response is " \
                        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, " \
                        f"'fear': {result['fear']}, 'joy': {result['joy']}, " \
                        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        return response_text
    else:
        return result, 500  # In case of an error message from the emotion detector

if __name__ == '__main__':
    app.run(debug=True, port=5000)
