import requests


UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"


def voice_recognition(assembly_key):
    headers = {"authorization": assembly_key}
    filename = "recording.wav"

    def upload(filename):
        def read_file(filename, chunk_size=5242880):
            with open(filename, "rb") as _file:
                while True:
                    data = _file.read(chunk_size)
                    if not data:
                        break
                    yield data

        upload_response = requests.post(
            UPLOAD_ENDPOINT, headers=headers, data=read_file(filename)
        )

        audio_url = upload_response.json()["upload_url"]
        return audio_url

    def transcribe(audio_url):
        transcript_request = {"audio_url": audio_url}
        transcript_response = requests.post(
            TRANSCRIPT_ENDPOINT, json=transcript_request, headers=headers
        )
        job_id = transcript_response.json()["id"]
        return job_id

    def pull(transcript_id):
        pulling_endpoint = TRANSCRIPT_ENDPOINT + "/" + transcript_id
        pulling_response = requests.get(pulling_endpoint, headers=headers)
        return pulling_response.json()

    def get_transcription_result_url(audio_url):
        transcript_id = transcribe(audio_url)
        while True:
            data = pull(transcript_id)
            if data["status"] == "completed":
                return data, None
            elif data["status"] == "error":
                return data, data["error"]

    # save transcript
    def save_transcription(audio_url):
        data, error = get_transcription_result_url(audio_url)

        if data:
            text_filename = filename + ".txt"
            with open(text_filename, "w") as f:
                f.write(data["text"])
            print("transcription saved!\n-----------------------")
        elif error:
            print("error!", error)

    audio_url = upload(filename)
    save_transcription(audio_url)
