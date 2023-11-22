import os
from functions.chatgpt_interaction import make_respond
from functions.record_voice import record_voice
from functions.text_processing_utils import read_text_from_file, read_config
from functions.voice_recognition import voice_recognition
from functions.condition import check_condition, check_if_in_condition
from functions.text_to_speech_utils import test_voice_vox

# Constance for retry mechanism
MAX_RETRIES = 3  # How many time you want to retry before error text displayed
WAIT_TIME = 1  # Delay time before next recall api

# You can change chatGPT model here,
# For more information go to "https://platform.openai.com/docs/models/overview"
OPENAI_MODEL = "gpt-3.5-turbo"

# Set the maximum width for each line of the subtitle
max_line_width = 40

# File path
directory_path = os.path.dirname(os.path.realpath(__file__))
config_file_path = directory_path + r"\config.txt"
answer_file_path = directory_path + r"\text_log\answer.txt"
answer_en_file_path = directory_path + r"\text_log\answer_en.txt"
answer_jp_file_path = directory_path + r"\text_log\answer_jp.txt"
subtitle_file_path = directory_path + r"\text_log\subtitle.txt"
chat_log_file_path = directory_path + r"\text_log\chat_log.txt"
prompt_file_path = directory_path + r"\prompt.txt"
voice_recognition_file_path = directory_path + r"\recording.wav.txt"

# Read every config and store it as constant
# For OpenAI API key, you can get it here: "https://www.assemblyai.com/app/account"
# For AssemblyAI API key, you can get it here: "https://platform.openai.com/api-keys"
# For more information go to 'speaker.json' and "https://voicevox.hiroshiba.jp/"
# Format of config.txt should be like this:
#   openAI_api_key:YOUR_OPENAI_KEY
#   assembly_api_key:YOUR_ASSEMBLYAI_KEY
#   assistant_name:YOUR_DESIRE_ASSISTANT_NAME
#   voice_vox_text_to_speech_model:YOUR_DESIRE_VOICE_VOX_TEXT_TO_SPEECH_MODEL
(
    OPENAI_KEY,
    ASSEMBLY_KEY,
    ASSISTANT_NAME,
    VOICE_VOX_TEXT_TO_SPEECH_MODEL,
) = read_config(config_file_path)

# Use test_voice_vox function to check if VoiceVox engine is open
# and clear all file for the first time use
test_voice_vox(
    answer_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    chat_log_file_path,
    voice_recognition_file_path,
    VOICE_VOX_TEXT_TO_SPEECH_MODEL,
    subtitle_file_path,
)

# Ask the user to choose between text chat or voice chat for input
chat_or_voice_input = input("Do you want to use text chat[1] or voice chat[2]: ")

# Use the make_respond function with the provided user_input to generate a greeting for the user
user_input = "User just open the program! greeting your user!"
make_respond(
    user_input,
    ASSISTANT_NAME,
    max_line_width,
    VOICE_VOX_TEXT_TO_SPEECH_MODEL,
    answer_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    subtitle_file_path,
    chat_log_file_path,
    prompt_file_path,
    MAX_RETRIES,
    WAIT_TIME,
    OPENAI_MODEL,
    OPENAI_KEY,
)

# If user choose to input with text it'll excute code as followed
if chat_or_voice_input == "1":
    while True:
        # Get input from user
        user_input = input("User: ")
        # Add user input to chat log
        with open(chat_log_file_path, "a", encoding="utf-8") as chat_log_file:
            chat_log_file.write(f"\nUser have said: {user_input}")

        # If check_if_in_condition function is return false
        # execute the script using check_condition function
        if check_if_in_condition(user_input):
            check_condition(
                user_input,
                chat_or_voice_input,
                answer_jp_file_path,
                answer_en_file_path,
                subtitle_file_path,
                chat_log_file_path,
                voice_recognition_file_path,
                VOICE_VOX_TEXT_TO_SPEECH_MODEL,
                max_line_width,
                ASSEMBLY_KEY,
            )
        # If check_if_in_condition function is return false,
        # generate a response using make_respond function
        elif not check_if_in_condition(user_input):
            make_respond(
                user_input,
                ASSISTANT_NAME,
                max_line_width,
                VOICE_VOX_TEXT_TO_SPEECH_MODEL,
                answer_file_path,
                answer_en_file_path,
                answer_jp_file_path,
                subtitle_file_path,
                chat_log_file_path,
                prompt_file_path,
                MAX_RETRIES,
                WAIT_TIME,
                OPENAI_MODEL,
                OPENAI_KEY,
            )

# If user choose to input with voice it'll excute code as followed
elif chat_or_voice_input == "2":
    while True:
        # Record user input
        record_voice()
        # Use a voice recognition function to convert speech into text
        voice_recognition(ASSEMBLY_KEY)
        # Read the English answer from the file ans store it to answer_en variable
        user_input = read_text_from_file(voice_recognition_file_path)

        print(f"User: {user_input}")

        # Add user input to chat log
        with open(chat_log_file_path, "a", encoding="utf-8") as chat_log_file:
            chat_log_file.write(f"\nUser have said: {user_input}")

        # If check_if_in_condition function is return false,
        # execute the script using check_condition function
        if check_if_in_condition(user_input):
            check_condition(
                user_input,
                chat_or_voice_input,
                answer_jp_file_path,
                answer_en_file_path,
                subtitle_file_path,
                chat_log_file_path,
                voice_recognition_file_path,
                VOICE_VOX_TEXT_TO_SPEECH_MODEL,
                max_line_width,
                ASSEMBLY_KEY,
            )
        # If check_if_in_condition function is return false
        # generate a response using make_respond function
        elif not check_if_in_condition(user_input):
            make_respond(
                user_input,
                ASSISTANT_NAME,
                max_line_width,
                VOICE_VOX_TEXT_TO_SPEECH_MODEL,
                answer_file_path,
                answer_en_file_path,
                answer_jp_file_path,
                subtitle_file_path,
                chat_log_file_path,
                prompt_file_path,
                MAX_RETRIES,
                WAIT_TIME,
                OPENAI_MODEL,
                OPENAI_KEY,
            )


else:
    print("ERROR invaid input")
