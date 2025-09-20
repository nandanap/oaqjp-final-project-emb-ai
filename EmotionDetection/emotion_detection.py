import requests, json

def emotion_detector(text_to_analyze):
    # API CALL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Format Response
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    if response.status_code == 400:
        return {
            "anger" : None,
            "disgust" : None,
            "fear" : None,
            "joy" : None,
            "sadness" : None,
            "dominant_emotion" : None
        }
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extract Data
    emotion_data = {
        "anger" : emotions['anger'],
        "disgust" : emotions['disgust'],
        "fear" : emotions['fear'],
        "joy" : emotions['joy'],
        "sadness" : emotions['sadness'],
    }

    # Sort and Get Last Key
    emotion_data_sorted = dict(sorted(emotion_data.items(), key = lambda item : item[1], reverse =True))
    emotion_data['dominant_emotion'] = next(iter(emotion_data_sorted))

    # Return Final Data
    return emotion_data

