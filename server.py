from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#Define decorator for application. Invoke GET method
@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route():
    #Get text to analyze from input
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    #Error handling
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    else:
        #Return structured output
        return (
            f"For the given statement, the system response is " \
            f"'anger': {anger}, 'disgust': {disgust}, " \
            f"'fear': {fear}, 'joy': {joy}, " \
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
   
