"""A code for run server"""
from flask import Flask, request , render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")


@app.route('/emotionDetector')
def emotion_detection():
    """A function to get text sentiment analysis"""
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    result =emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    return f"For the given statement, the' system response is 'anger': \
    {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': \
    {result['joy']}, and 'sadness': {result['sadness']} The dominant emotion is \
    {result['dominant_emotion']}."


@app.route('/')
def render_index_page():
    """Render Index Page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
