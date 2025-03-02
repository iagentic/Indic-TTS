import requests
import base64
# import pyaudio

# Define the target URL"
url = "http://localhost:5050"

# Create the request payload
source = """
మన మహాన దేశం అభివృద్ధి మరియు ప్రగతిలో మీ అందరి సహకారం అమూల్యం. ఈ రోజు, మనం ఒక కీలక దశలో ఉన్నాం, ఇక్కడ మనం ఐక్యంగా సవాళ్లను ఎదుర్కొని, అవకాశాలను సద్వినియోగం చేసుకోవాలి. మన వైవిధ్యం మన బలం, మన ఐక్యత మన శక్తి. అందరూ కలిసి, సమృద్ధి, శక్తివంతమైన మరియు సమగ్ర భారత నిర్మాణానికి ప్రతిజ్ఞ చేద్దాం, ఇక్కడ ప్రతి పౌరుడికి సమాన అవకాశాలు లభిస్తాయి మరియు మన దేశం ప్రపంచంలో ఒక కొత్త శిఖరాన్ని అధిరోహిస్తుంది.
"""
payload = {
    "input": [
        {
            "source": source
        }
    ],
    "config": {
        "gender": "male",
        "language": {
            "sourceLanguage": "te"
        }
    },
    # "stream":"true"
}

# Send the POST request with JSON payload
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    print("Response JSON:")
    # print(response_json)
    
    # Optional: decode the base64 audio content and save it as a WAV file
    if "audio" in response_json and response_json["audio"]:
        audio_content = response_json["audio"][0]["audioContent"]
        audio_data = base64.b64decode(audio_content)
        with open("output.wav", "wb") as f:
            f.write(audio_data)
        print("Audio saved as output.wav")
    else:
        print("No audio content found in the response.")
else:
    print(f"Request failed with status code: {response.status_code}")
