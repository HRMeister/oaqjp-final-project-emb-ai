"""
Initiates the Emotion Detector Applcation running on Flask
On the port: 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def detector():
    """
    Sends the get request using the emotion_detection fuction to
    analyze the input given and returns the results
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']},"
            f"'fear': {response['fear']}, 'joy': {response['joy']} and ",
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}")


@app.route('/')
def render_index():
    """
    Runs the html template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
