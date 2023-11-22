import time
import pyautogui
from word2number import w2n
from functions.text_to_speech_utils import (
    create_voicevox_text_to_speech_file,
    play_text_to_speech_file,
    create_understood_sentence,
)
from functions.text_processing_utils import (
    format_text,
    create_subtitle_file,
    read_text_from_file,
    save_text_to_file,
)
from functions.record_voice import record_voice
from functions.voice_recognition import voice_recognition
from text_log.interaction_conditions import *

# URL for website
YOUTUBE_URL = "https://www.youtube.com/"
FACEBOOK_URL = "https://www.facebook.com/"
INSTAGRAM_URL = "https://www.instagram.com/"
REDDIT_URL = "https://www.reddit.com/"
GITHUB_URL = "https://github.com/"
X_URL = "https://twitter.com/"

# Constants for multimedia control and other key functions
PLAY_PAUSE_KEY = "playpause"
PRINTSCREEN_KEY = "prtscr"
VOLUME_UP_KEY = "volumeup"
VOLUME_DOWN_KEY = "volumedown"
WIN_KEY = "win"
ENTER_KEY = "enter"
SHIFT_KEY = "shift"
NEXT_KEY = "nexttrack"
PRV_KEY = "prevtrack"
DELAY_TIME = 0.5


# Function to create a text-to-speech file, play the generated text-to-speech and open website
def open_website_and_play_tts(
    jp_message,
    en_message,
    answer_jp_file_path,
    answer_en_file_path,
    subtitle_file_path,
    chat_log_file_path,
    voice_vox_text_to_speech_model,
    max_line_width,
    website_url,
):
    create_and_play_sentence(
        jp_message,
        en_message,
        answer_jp_file_path,
        answer_en_file_path,
        subtitle_file_path,
        chat_log_file_path,
        max_line_width,
        voice_vox_text_to_speech_model,
    )
    pyautogui.press(WIN_KEY)
    time.sleep(DELAY_TIME)
    pyautogui.write(website_url)
    pyautogui.press(ENTER_KEY)


# Function to display an error message if the input is invalid
def handle_invalid_input(
    error_message, answer_en_file_path, subtitle_file_path, max_line_width
):
    print(error_message)
    save_text_to_file(error_message, answer_en_file_path)
    create_subtitle_file(answer_en_file_path, max_line_width, subtitle_file_path)


# Function to convert user input from string to an integer
# and display an error message if the input is invalid
def handle_volume_input_from_voice(
    voice_recognition_file_path,
    subtitle_file_path,
    answer_en_file_path,
    key,
    max_line_width,
    assembly_key,
):
    while True:
        # Record user input
        record_voice()
        # Use a voice recognition function to convert speech into text
        voice_recognition(assembly_key)

        # Read voice recognized text and store it to unformatted_user_input_volume_level variable
        unformatted_user_input_volume_level = read_text_from_file(
            voice_recognition_file_path
        )

        print(unformatted_user_input_volume_level)

        cleaned_user_input_volume_level = format_text(
            unformatted_user_input_volume_level
        )

        try:
            # Format user input with word2number library which can turn a string to integer
            # for example "Two" to "2"
            formatted_user_input_volume_level = w2n.word_to_num(
                cleaned_user_input_volume_level
            )

            # A statement to check if user input is valid or not
            # (which it needed to be more than 0)
            if formatted_user_input_volume_level > 0:
                # Press volume key according to user input
                # (it needed to divided by two because 1 volume key press is equal to 2 volume up/down)
                pyautogui.press(key, presses=(formatted_user_input_volume_level // 2))
                break
            else:
                # If the user input is not greater than 0, the following error text will be displayed
                handle_invalid_input(
                    "ERROR: Please say a number greater than 0",
                    answer_en_file_path,
                    subtitle_file_path,
                    max_line_width,
                )
        except ValueError:
            # If the user input is not an integer or have any other word with the answer,
            # the following error text will be displayed
            handle_invalid_input(
                "ERROR: Please say only the number",
                answer_en_file_path,
                subtitle_file_path,
                max_line_width,
            )


# Function to generate an understood sentence file, create a text-to-speech file,
# and play the generated text-to-speech
def create_and_play_sentence(
    jp_message,
    en_message,
    answer_jp_path,
    answer_en_path,
    subtitle_path,
    chat_log_path,
    max_line_width,
    voice_vox_text_to_speech_model,
):
    # Generate an understood sentence file using the create_understood_sentence function
    create_understood_sentence(
        jp_message,
        en_message,
        answer_jp_path,
        answer_en_path,
        subtitle_path,
        chat_log_path,
        max_line_width,
    )
    # Create a text-to-speech file using the create_voicevox_text_to_speech_file function
    create_voicevox_text_to_speech_file(answer_jp_path, voice_vox_text_to_speech_model)
    # Play the generated text-to-speech
    play_text_to_speech_file()


# Function to execute a script if input is in condition list
def check_condition(
    user_input,
    chat_or_voice_input,
    answer_jp_file_path,
    answer_en_file_path,
    subtitle_file_path,
    chat_log_file_path,
    voice_recognition_file_path,
    voice_vox_text_to_speech_model,
    max_line_width,
    assembly_key,
):
    formatted_user_input = format_text(user_input)

    # Execute following script and press "play/pause media key"
    # if input matches play media condition
    if any(
        format_text(condition) in formatted_user_input
        for condition in play_media_condition
    ):
        create_and_play_sentence(
            "現在再生中のメディアです",
            "Now playing media",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        pyautogui.press(PLAY_PAUSE_KEY)

    # Execute following script and press "play/pause media key"
    # if input matches stop media condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in stop_media_condition
    ):
        create_and_play_sentence(
            "現在メディアを停止します",
            "Now stop media",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        pyautogui.press(PLAY_PAUSE_KEY)

    # Execute following script and press "next media key"
    # if input matches next track condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in next_track_condition
    ):
        create_and_play_sentence(
            "今、次のトラックにスキップします",
            "Now skip to next track",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        pyautogui.press(NEXT_KEY)

    # Execute following script and press "previous media key"
    # if input matches previous track condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in previous_track_condition
    ):
        create_and_play_sentence(
            "今、前のトラックに戻ります",
            "Now go back to previous track",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        pyautogui.press(PRV_KEY)

    # Execute following script and press "volume up key"
    # if input matches volume up condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in volume_up_condition
    ):
        create_and_play_sentence(
            "どれくらいの音量にしますか？",
            "How much volume do you want to turn up?",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        # If user choose to input with text it will excute code as followed
        if chat_or_voice_input == "1":
            try:
                # Ask how much volume user want to turn up
                volume_level = input("User(number): ")
                # convert user input into integer
                volume_level_int = int(volume_level)

                # A statement to check if user input is valid or not
                # (which it needed to be more than 0)
                if volume_level_int > 0:
                    pyautogui.press(VOLUME_UP_KEY, presses=(volume_level_int // 2))
                else:
                    # If the user input is not greater than 0,
                    # the following error text will be displayed
                    handle_invalid_input(
                        "ERROR: Please enter a number greater than 0",
                        answer_en_file_path,
                        subtitle_file_path,
                        max_line_width,
                    )
            except ValueError:
                # If the user input is not an integer or have any other word with the answer,
                # the following error text will be displayed
                handle_invalid_input(
                    "ERROR: User input is not an integer",
                    answer_en_file_path,
                    subtitle_file_path,
                    max_line_width,
                )

        # If user choose to input with voice it will excute code as followed
        elif chat_or_voice_input == "2":
            handle_volume_input_from_voice(
                voice_recognition_file_path,
                subtitle_file_path,
                answer_en_file_path,
                VOLUME_UP_KEY,
                max_line_width,
                assembly_key,
            )

    # Execute following script and press "volume down key"
    # if input matches volume down condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in volume_down_condition
    ):
        create_and_play_sentence(
            "どれくらい音量を下げますか？",
            "How much volume do you want to turn down?",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )

        # If user choose to input with text it will excute code as followed
        if chat_or_voice_input == "1":
            try:
                # Ask how much volume user want to turn down
                volume_level = input("User(number): ")
                # convert user input into integer
                volume_level_int = int(volume_level)

                # A statement to check if user input is valid or not
                # (which it needed to be more than 0)
                if volume_level_int > 0:
                    pyautogui.press(VOLUME_DOWN_KEY, presses=(volume_level_int // 2))
                else:
                    # If the user input is not greater than 0,
                    # the following error text will be displayed
                    handle_invalid_input(
                        "ERROR: Please enter a number greater than 0",
                        answer_en_file_path,
                        subtitle_file_path,
                        max_line_width,
                    )

            except ValueError:
                # If the user input is not an integer or have any other word with the answer,
                # the following error text will be displayed
                handle_invalid_input(
                    "ERROR: User input is not an integer",
                    answer_en_file_path,
                    subtitle_file_path,
                    max_line_width,
                )

        # If user choose to input with voice it will excute code as followed
        elif chat_or_voice_input == "2":
            print("How much volume do you want to turn down?")
            handle_volume_input_from_voice(
                voice_recognition_file_path,
                subtitle_file_path,
                answer_en_file_path,
                VOLUME_DOWN_KEY,
                max_line_width,
                assembly_key,
            )

    # Execute following script if input matches capture screen condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in capture_screen_condition
    ):
        create_and_play_sentence(
            "画面全体をキャプチャしますか、それとも特定のポイントだけですか？",
            "Do you want to capture the entire screen or just certain points?",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )

        # If user choose to input with text it will excute code as followed
        if chat_or_voice_input == "1":
            # Ask user if user want to capture entire screen or just certain points?
            user_choices = input("just entire screen[1] or just certain points?[2]: ")

            # If user choose to capture entire screen it will excute code as followed
            if user_choices == "1":
                create_and_play_sentence(
                    "現在画面全体をキャプチャ中",
                    "Now capturing the entire screen",
                    answer_jp_file_path,
                    answer_en_file_path,
                    subtitle_file_path,
                    chat_log_file_path,
                    max_line_width,
                    voice_vox_text_to_speech_model,
                )
                # Press Window keyboard shortcut for print screen
                pyautogui.hotkey(WIN_KEY, PRINTSCREEN_KEY)

            # If user choose to capture just certain points it will excute code as followed
            elif user_choices == "2":
                create_and_play_sentence(
                    "現在特定のポイントをキャプチャ中",
                    "Now capturing specific points",
                    answer_jp_file_path,
                    answer_en_file_path,
                    subtitle_file_path,
                    chat_log_file_path,
                    max_line_width,
                    voice_vox_text_to_speech_model,
                )
                # Press Window keyboard shortcut for snipping tool
                pyautogui.hotkey(WIN_KEY, SHIFT_KEY, "s")

        # If user choose to input with voice it will excute code as followed
        elif chat_or_voice_input == "2":
            # Record user input and utilize a voice recognition function to convert speech into text
            record_voice()
            voice_recognition(assembly_key)

            # Read user input and store it to user_choices variable
            user_choices = read_text_from_file(voice_recognition_file_path)
            print(user_choices)
            # If user choose to capture entire screen it will excute code as followed
            if any(
                format_text(condition) in format_text(user_choices)
                for condition in capture_entire_screen_condition
            ):
                create_and_play_sentence(
                    "現在画面全体をキャプチャ中",
                    "Now capturing the entire screen",
                    answer_jp_file_path,
                    answer_en_file_path,
                    subtitle_file_path,
                    chat_log_file_path,
                    max_line_width,
                    voice_vox_text_to_speech_model,
                )
                # Press Window keyboard shortcut for print screen
                pyautogui.hotkey(WIN_KEY, PRINTSCREEN_KEY)

            # If user choose to capture just certain points it will excute code as followed
            elif any(
                format_text(condition) in format_text(user_choices)
                for condition in capture_specific_screen_condition
            ):
                create_and_play_sentence(
                    "現在特定のポイントをキャプチャ中",
                    "Now capturing specific points",
                    answer_jp_file_path,
                    answer_en_file_path,
                    subtitle_file_path,
                    chat_log_file_path,
                    max_line_width,
                    voice_vox_text_to_speech_model,
                )
                # Press Window keyboard shortcut for snipping tool
                pyautogui.hotkey(WIN_KEY, SHIFT_KEY, "s")
            else:
                print("Invaid input")
    # Execute following script if input matches capture entire screen condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in capture_entire_screen_condition
    ):
        create_and_play_sentence(
            "現在画面全体をキャプチャ中",
            "Now capturing the entire screen",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        # Press Window keyboard shortcut for print screen
        pyautogui.hotkey(WIN_KEY, PRINTSCREEN_KEY)

    # If user choose to capture just certain points it will excute code as followed
    elif any(
        format_text(condition) in formatted_user_input
        for condition in capture_specific_screen_condition
    ):
        create_and_play_sentence(
            "現在特定のポイントをキャプチャ中",
            "Now capturing specific points",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            max_line_width,
            voice_vox_text_to_speech_model,
        )
        # Press Window keyboard shortcut for snipping tool
        pyautogui.hotkey(WIN_KEY, SHIFT_KEY, "s")

    # Execute following script and use the open_website function to "open Youtube"
    # if input matches open Youtube condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in open_youtube_condition
    ):
        open_website_and_play_tts(
            "今 ユーチューブ を開いています",
            "Now openning youtube",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            YOUTUBE_URL,
        )

    # Execute following script and use the open_website function to "open Facebook"
    # if input matches open Facebook condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in open_facebook_condition
    ):
        open_website_and_play_tts(
            "今 フェイスブック を開いています",
            "Now openning Facebook",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            FACEBOOK_URL,
        )

    # Execute following script and use the open_website function to "open Instagram"
    # if input matches open Instagram condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in open_ig_condition
    ):
        open_website_and_play_tts(
            "今 インスタグラム を開いています",
            "Now openning Instagram",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            INSTAGRAM_URL,
        )

    # Execute following script and use the open_website function to "open Reddit"
    # if input matches open Reddit condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in open_reddit_condition
    ):
        open_website_and_play_tts(
            "今 レディット を開いています",
            "Now openning Reddit",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            REDDIT_URL,
        )

    # Execute following script and use the open_website function to "open Github"
    # if input matches open Github condition
    elif any(
        format_text(condition) in formatted_user_input
        for condition in open_github_condition
    ):
        open_website_and_play_tts(
            "今 ギットハブ を開いています",
            "Now openning GitHub",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            GITHUB_URL,
        )

    # Execute following script and use the open_website function to "open X"
    # if input matches open X condition
    elif any(
        format_text(condition) in formatted_user_input for condition in open_x_condition
    ):
        open_website_and_play_tts(
            "今 エックス を開いています",
            "Now openning X",
            answer_jp_file_path,
            answer_en_file_path,
            subtitle_file_path,
            chat_log_file_path,
            voice_vox_text_to_speech_model,
            max_line_width,
            X_URL,
        )

    else:
        return True


# Function to check if the input matches any conditions and return True if it does
def check_if_in_condition(user_input):
    formatted_user_input = format_text(user_input)

    all_conditions_list = [
        play_media_condition,
        stop_media_condition,
        next_track_condition,
        previous_track_condition,
        volume_up_condition,
        volume_down_condition,
        capture_screen_condition,
        capture_entire_screen_condition,
        capture_specific_screen_condition,
        open_youtube_condition,
        open_facebook_condition,
        open_ig_condition,
        open_reddit_condition,
        open_github_condition,
        open_x_condition,
    ]

    # For loop to check if any codition is matched with input and return True if it does
    for condition_list in all_conditions_list:
        if any(
            format_text(condition) in formatted_user_input
            for condition in condition_list
        ):
            return True
