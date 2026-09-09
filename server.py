''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs Emotion detection over it using emotion_detector()
        function. The output returned shows the details for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detection function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the response
    an = response['anger']
    di = response['disgust']
    fe = response['fear']
    joy =  response['joy']
    sn = response['sadness']
    de = response['dominant_emotion']
    if de is None:
        return "Invalid text! Please try again!."

    #return f"'anger':{an},'disgust':{di},'fear':{fe},'joy':{joy},'sadness':{sn}.Result{de}"
    return "For the given statement, the system response is 'anger':{}, 'disgust':{}, 'fear':{}, 'joy':{} and 'sadness':{}. The dominant emotion is {}.".format(anger,disgust,fear,joy,sadness,dominant_emotion)
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
