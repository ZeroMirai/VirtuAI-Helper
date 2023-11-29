import textwrap
import string


# Function to read config file and return it
def read_config(config_file_path):
    with open(config_file_path, "r") as config_file:
        for line in config_file:
            line = line.strip()
            if line.startswith("openAI_api_key:"):
                openai_key = line[15:]
            elif line.startswith("assembly_api_key:"):
                assembly_key = line[17:]
            elif line.startswith("assistant_name:"):
                assistant_name = line[15:]
            elif line.startswith("voice_vox_text_to_speech_model:"):
                voice_vox_text_to_speech_model = line[31:]

    return openai_key, assembly_key, assistant_name, voice_vox_text_to_speech_model


# Function to format a text from parameter
def format_text(unformatted_text):
    # Remove all punctuation in unformatted text
    removed_punctuation_text = "".join(
        ch for ch in unformatted_text if ch not in string.punctuation
    )
    # Convert the text to lowercase and removes spaces
    formatted_text = removed_punctuation_text.lower().replace(" ", "")
    return formatted_text


# Function to save a text from parameter and save it to .txt file
def save_text_to_file(unsaved_text, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(unsaved_text)


# Function to read a text from .txt file and return it
def read_text_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        output = file.read()
    return output


# Function to separate a Japanese answer and English answer from chat gpt to separate file
def separate_language(
    unseparate_file_path, first_separated_file_path, second_separated_file_path
):
    with open(unseparate_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("en:"):
                text = line[3:]  # Extract the text part after 'en:'
                with open(first_separated_file_path, "w", encoding="utf-8") as en_file:
                    en_file.write(text + "\n")
            elif line.startswith("jp:"):
                text = line[3:]  # Extract the text part after 'jp:'
                with open(second_separated_file_path, "w", encoding="utf-8") as jp_file:
                    jp_file.write(text + "\n")


# Function to clear the data inside the file
def clear_files(
    answer_file_path,
    answer_en_file_path,
    answer_jp_file_path,
    subtitle_file_path,
    chat_log_file_path,
    voice_recognition_file_path,
):
    # List of files to clear data inside
    uncleared_file_list = [
        answer_file_path,
        answer_en_file_path,
        answer_jp_file_path,
        subtitle_file_path,
        chat_log_file_path,
        voice_recognition_file_path,
    ]

    # Loop through uncleared_file_list and clear the data inside each file
    for file in uncleared_file_list:
        open(file, "w").close()

    save_text_to_file("*this is your chat log*", chat_log_file_path)


# Function to create a subtitle file(which can be use for OBS) and align text to center
def create_subtitle_file(answer_en_file_path, max_line_width, subtitle_file_path):
    # Read the answer_en_file_path and store it to text variable
    text = read_text_from_file(answer_en_file_path)

    # Generate the wrapped subtitle text
    wrapped_text = textwrap.wrap(text, width=max_line_width)

    # Center align each line of the wrapped text
    centered_text = [line.center(max_line_width) for line in wrapped_text]

    # Join the centered lines with line breaks
    formatted_text = "\n".join(centered_text)

    # Write the formatted text to the file
    save_text_to_file(formatted_text, subtitle_file_path)


# Function to refresh the chat log file by clearing its content if it's exceeds 3000 characters
def refresh_chat_log(chat_log_file_path):
    # Read chat log file and store it to file_contents variable
    file_contents = read_text_from_file(chat_log_file_path)
    # Count how many characters are there inside chat log file
    character_count = len(file_contents)

    # Check if the characters count exceeds 3000; if so, clear the file
    if character_count > 3000:
        save_text_to_file("*this is your chat log*", chat_log_file_path)
