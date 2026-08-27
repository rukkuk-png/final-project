""" This is the emotional detection script"""
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
    return response.text
