import requests
import urllib.parse
import sounddevice as sd
import soundfile as sf
import romajitable
import random
from functions.text_processing_utils import (
    clear_files,
    create_subtitle_file,
    read_text_from_file,
    save_text_to_file,
)


# Function to test if VoiceVox is opend and clear a file for first time use
def test_voice_vox(
    answer_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    chat_log_file_path,
    voice_recognition_file_path,
    voice_vox_text_to_speech_model,
    subtitle_file_path,
):
    save_text_to_file("操作する準備ができています", answer_jp_file_path)
    create_voicevox_text_to_speech_file(
        answer_jp_file_path, voice_vox_text_to_speech_model
    )
    play_text_to_speech_file()
    clear_files(
        answer_file_path,
        answer_en_file_path,
        answer_jp_file_path,
        subtitle_file_path,
        chat_log_file_path,
        voice_recognition_file_path,
    )


# Function to random a understood word and create a sentence with given parameter
def create_understood_sentence(
    SecondWordJp,
    SecondWordEn,
    answer_jp_file_path,
    answer_en_file_path,
    subtitle_file_path,
    chat_log_file_path,
    max_line_width,
):
    understood_word_jp = [
        "はい",
        "了解しました",
        "分かりました",
        "承知しました",
        "オーケーです",
        "了解です",
        "理解しました",
        "わかった",
        "参りました",
        "かしこまりました",
    ]
    understood_word_en = [
        "Understood",
        "Okay",
        "Got it",
    ]
    # Random a understood word in Japanese and append it with the word in parameter
    random_understood_sentence_jp = (
        random.choice(understood_word_jp) + ", " + SecondWordJp
    )
    # Random a understood word in English and append it with the word in parameter
    random_understood_sentence_en = (
        random.choice(understood_word_en) + ", " + SecondWordEn
    )
    # Save Japanese complete Japanese sentence to answer Japanese file
    save_text_to_file(random_understood_sentence_jp, answer_jp_file_path)
    # Save Japanese complete English sentence to answer Japanese file and chat log file
    save_text_to_file(random_understood_sentence_en, answer_en_file_path)
    save_text_to_file(random_understood_sentence_en, chat_log_file_path)
    # Create a subtitle file with complete English sentence
    create_subtitle_file(answer_en_file_path, max_line_width, subtitle_file_path)
    print(random_understood_sentence_en)


# Function to create a text-to-speech file using voicevox engine
def create_voicevox_text_to_speech_file(answer_jp_path, voice_vox_text_to_speech_model):
    # Read the answer_jp_path and store it to answer_jp variable
    answer_jp = read_text_from_file(answer_jp_path)

    # Turn some of the answer that have a english text to katakana text for example
    # If answer_jp contain a word "apple" it'll turn it to "appuru"
    result = romajitable.to_kana(answer_jp)
    katakaned = result.katakana

    # Text-to-speech part (make sure you have open VOICEVOX.exe)
    voicevox_url = "http://localhost:50021"
    params_encoded = urllib.parse.urlencode(
        {"text": katakaned, "speaker": voice_vox_text_to_speech_model}
    )
    request = requests.post(f"{voicevox_url}/audio_query?{params_encoded}")
    params_encoded = urllib.parse.urlencode(
        {
            "speaker": voice_vox_text_to_speech_model,
            "enable_interrogative_upspeak": True,
        }
    )
    request = requests.post(
        f"{voicevox_url}/synthesis?{params_encoded}", json=request.json()
    )

    with open("JP_Voice.wav", "wb") as outfile:
        outfile.write(request.content)
        outfile.close()


# Function to play a generated text-to-speech file
def play_text_to_speech_file():
    data, fs = sf.read("JP_Voice.wav", dtype="float32")
    sd.play(data, fs)
    status = sd.wait()
