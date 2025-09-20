"""Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """This code receives the text from the HTML interface and
    runs sentiment analysis over it using emotion_detector()
    function. The output returned shows the output in the format requested by the user
    """
    text_to_analyze = request.args["textToAnalyze"]
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"]:

        return "For the given statement, the system response" \
            + f"is 'anger': {response['anger']}, 'disgust': {response['disgust']}," \
            + f"'fear': {response['fear']}, 'joy': {response['joy']} " \
            + f"and 'sadness': {response['sadness']}." \
            + f" The dominant emotion is {response['dominant_emotion']}."
    return "Invalid text! Please try again!."


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
