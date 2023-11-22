import openai
import time
from functions.text_processing_utils import (
    separate_language,
    save_text_to_file,
    read_text_from_file,
    create_subtitle_file,
    refresh_chat_log,
)
from functions.text_to_speech_utils import (
    create_voicevox_text_to_speech_file,
    play_text_to_speech_file,
)


# Function to generate a respond from chatGPT api and create a file
# such as text-to-speech file, subtitle file and then play the generated text-to-speech
def make_respond(
    user_input,
    assistant_name,
    max_line_width,
    voice_vox_text_to_speech_model,
    answer_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    subtitle_file_path,
    chat_log_file_path,
    prompt_file_path,
    max_retries,
    wait_time,
    openai_model,
    OPENAI_KEY,
):
    create_respond(
        OPENAI_KEY,
        openai_model,
        assistant_name,
        user_input,
        prompt_file_path,
        chat_log_file_path,
        answer_en_file_path,
        answer_jp_file_path,
        answer_file_path,
        max_retries,
        wait_time,
    )
    create_voicevox_text_to_speech_file(
        answer_jp_file_path, voice_vox_text_to_speech_model
    )
    create_subtitle_file(answer_en_file_path, max_line_width, subtitle_file_path)
    play_text_to_speech_file()
    refresh_chat_log(chat_log_file_path)


# Function to call openAI api and generate a respond with chatGPT api
def create_respond(
    OPENAI_KEY,
    openai_model,
    assistant_name,
    user_input,
    prompt_file_path,
    chat_log_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    answer_file_path,
    max_retries,
    wait_time,
):
    openai.api_key = OPENAI_KEY

    # Read and store a prompt and chat log from a file to following variable
    prompt_content = read_text_from_file(prompt_file_path)
    chat_log_content = read_text_from_file(chat_log_file_path)

    # Function to make the OpenAI API request
    def make_openai_request():
        messages = [
            {"role": "system", "content": prompt_content},
            {
                "role": "user",
                "content": f"this is chat log:{chat_log_content} this is what user said: {user_input}",
            },
        ]
        chat = openai.ChatCompletion.create(model=openai_model, messages=messages)
        return chat.choices[0].message.content

    # Function to retry call chatGPT api in case it's errror
    def retry_call_api(func, max_retries, wait_time):
        retries = 0

        while retries < max_retries:
            try:
                return func()
            except openai.error.RateLimitError:
                print(
                    "Rate limit exceeded. Retrying in {} seconds...".format(wait_time)
                )
                time.sleep(wait_time)
                wait_time *= 2  # Exponential wait time
                retries += 1

        raise Exception("Max retries exceeded. Unable to make a successful request.")

    # Use the retry mechanism to make the OpenAI API request
    try:
        reply = retry_call_api(make_openai_request, max_retries, wait_time)
    except Exception as e:
        print("Error: {}".format(str(e)))
        return

    # Save the assistant's reply to the answer file
    save_text_to_file(reply, answer_file_path)

    # Separate the reply into English and Japanese parts
    separate_language(answer_file_path, answer_en_file_path, answer_jp_file_path)

    # Read the answer_en_file_path and store it to answer_en variable
    answer_en = read_text_from_file(answer_en_file_path)

    # Append the English answer to the chat log file
    with open(chat_log_file_path, "a", encoding="utf-8") as chat_log_file:
        chat_log_file.write(f"\nyou have responded: {answer_en}")

    # Print the English answer in cmd
    print(f"{assistant_name}: {answer_en}")
