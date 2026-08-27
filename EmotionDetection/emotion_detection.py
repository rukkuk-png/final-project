""" This is the emotional detection script"""
import json
import requests # Import the requests library to handle HTTP requests


# Define a function named emotion_detection that takes a input  string(text_to_analyze)

def emotion_detector(text_to_analyze):
    """ This is the function emotion_detector"""
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
	# Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	# Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header ,timeout = 60)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    list_emotion_predictions = formatted_response['emotionPredictions']
    dic_emotion = list_emotion_predictions [0]
    anger_score = dic_emotion['emotion']['anger']
    disgust_score = dic_emotion['emotion']['disgust']
    fear_score = dic_emotion['emotion']['fear']
    joy_score =  dic_emotion['emotion']['joy']
    sadness_score = dic_emotion['emotion']['sadness']
    final_list = dic_emotion['emotion']
    max_val = max(final_list ,key=final_list.get)
    return {'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion':max_val}
