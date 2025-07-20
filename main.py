import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys
import time 

base_url = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
filename=sys.argv[1]
headers = {
    "authorization": API_KEY_ASSEMBLYAI
}

def upload(filename):
    def read_file(filename , chunk_size=5242880):
     with open(filename , 'rb') as _file:
        while True:
            data=_file.read(chunk_size)
            if not data :
                break
            yield data
    upload_response = requests.post(base_url,
                        headers=headers,
                        data=read_file(filename))

    audio_url = upload_response.json()["upload_url"]
    return audio_url

def transcrib(audio_url):
    transcrib_request={"audio_url" : audio_url}
    transcrib_response = requests.post(transcript_endpoint , json = transcrib_request , headers = headers)
    job_id=transcrib_response.json()['id']
    return job_id



def poll(transcrib_id):
    polling_endpoint = transcript_endpoint+'/'+transcrib_id
    polling_response=requests.get(polling_endpoint,  headers = headers)
    return polling_response.json()

def get_transcription_result_url(audio_url):
    transcrib_id= transcrib(audio_url)
    while True:
        data = poll(transcrib_id)
        if data['status']=='completed':
            return data , None
        elif(data['status']=='error'):
            return data , data['error']
        
        print("waiting 30 seconds...")
        time.sleep(30)


def save_transcript(audio_url):
    data , error = get_transcription_result_url(audio_url)
    if data:
        text_filename=filename+".txt"
        with open(text_filename, "w") as f:
            f.write(data['text'])
        print('trancription saved')
    elif error :
        print("Error!!" , error )
    
    
audio_url= upload(filename)
save_transcript(audio_url)

