# VirtuAI-Helper

VirtuAI Helper is a python-based program that can execute scripts based on user input or chat with the user. It uses OpenAI API to generate responses with the chatGPT model and VoiceVox engine to synthesize speech in Japanese. The scripts that VirtuAI Helper can execute are multimedia functions such as play/pause media, turn up/down the volume, capture the screen, etc. and web functions such as open Facebook, YouTube, Twitter, etc. The program can receive input in two ways text input or voice input. For text input it can recive input in any language but for voice input it can only recognize English language.

![Example Image](guide/example_1.gif)

## Simple flowchart

![simple_flowchart](guide/flowchart.png)

## Table of Contents

- [VirtuAI-Helper](#virtuai-helper)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [File Structure](#file-structure)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Contributing](#contributing)
    - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
    - [Pull Requests](#pull-requests)
  - [Note](#note)
  - [License](#license)
  - [Credits](#credits)

## Features

- **Script Execution** You can use text or voice commands to execute scripts that perform various tasks on your device or on the web. For example, you can say “play music” or “open YouTube” and the program will execute the corresponding script.
- **Chat Mode** You can use text or voice input to chat with the program. The program will use OpenAI API to generate responses with the chatGPT model and VoiceVox engine to synthesize speech in Japanese. For example, you can say “how are you” or “tell me a joke” and the program will reply accordingly.
- **Voice Input** You can use voice input to interact with the program by pressing and holding the microphone button. The program will use AssemblyAI API to convert your speech-to-text and process it accordingly. For example, you can say “capture the screen” or “what is the weather today” and the program will execute the script or generate the response.

## Prerequisites

- **Python** 3.11. Download it [here](https://www.python.org/downloads/).
- **Voicevox software** Version 0.14.7. Download it [here](https://voicevox.hiroshiba.jp/), installed and running.
- **API keys** from OpenAI and AssemblyAI, you can get it from here [OpenAI](https://platform.openai.com/api-keys), [AssemblyAI](https://www.assemblyai.com/app/account).
- Open Broadcaster Software (_if you want the program to show the subtitle file_). Download it [here](https://obsproject.com/).
- Vtuber Studio, VoiceMeeter banana and EarTrumpet (_if you want the program to show virtual live2d_) if you didn't have it download it from here [Vtuber Studio](https://denchisoft.com/), [VoiceMeeter banana](https://vb-audio.com/Voicemeeter/banana.htm), [EarTrumpet](https://eartrumpet.app/).

## Installation

Follow these steps to install and set up VirtuAI Helper.

1. Download the project zip file from GitHub or Clone this repository by typing these in terminal or command prompt (but if you choose to download the project as a zip file you'll also need to extract the zip file).
   ```
   git clone https://github.com/ZeroMirai/VirtuAI-Helper.git
   ```
    
2. Open a terminal or command prompt and change the directory to the project folder by typing `cd` followed by where this folder is located for example `cd C:\Git_hub\VirtuAI Helper`.
3. Install all necessary library by typing.
   ```
   pip install -r requirements.txt
   ```
4. Configure the necessary API keys and other config in config.txt.

## File Structure

- 📁`functions`: Contains modular components of the project.
  - 📝`chatgpt_interaction.py`: Handles interactions with the OpenAI GPT model.
  - 📝`condition.py`: Script execution if user input is match conditions.
  - 📝`record_voice.py`: voice recording function.
  - 📝`text_processing_utils.py`: Utilities for all script to processing text.
  - 📝`text_to_speech_utils.py`: Utilities for text-to-speech part.
  - 📝`voice_recognition.py`: Implements speech-to-text using the AssemblyAI API.
- 📝`text_log folder`: Stores various text logs and files.
- 📝`main.py`: Main script for executing the VirtuAI Helper program.
- 📝`config.txt`: File to store various configuration and API keys.
- 📝`prompt.txt`: File to store user prompts.
- 📝`recording.wav.txt`: Transript from speech-to-text.
- 📝`requirements.txt`: File to Install all necessary library.
- 📝`JP_Voice.wav`: A generated text-to-speech file.
- 📝`recording.wav`: Audio recording file.

## Configuration

Before running the program, Ensure you have changed all the configurations and **pasted them right after the : in the file**. The file must have the following format.
  ```
  openAI_api_key:sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  assembly_api_key:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  assistant_name:xxxx
  voice_vox_text_to_speech_model:xx
  ```

- Edit the config.txt file with your OpenAI and AssemblyAI API keys and other config.
  - For openAI_api_key copy and paste your openAI API key here but if you didn't have it, you can get it [here](https://platform.openai.com/api-keys).
  - For assembly_api_key copy and paste your AssemblyAI API key here but if you didn't have it, you can get it [here](https://www.assemblyai.com/app/account).
  - For assistant_name type your desired assistant name (it doesn't affect anything in the code //it's just a text that will show before the answer).
  - For voice_vox_text_to_speech_model you can compare speaker.json name with [VoiceVox](https://voicevox.hiroshiba.jp/) and type id number you desire.
- you can create your own AI personality by changing the prompt in the `prompt.txt` **but don't change the rule part** (if you are too lazy to write your own prompt you can also ask chatGPT to make your own one by asking).
  ```
  Generate me a prompt so I can use with my AI assistant "that's a ..(personality,gender,traits).., ..(other personality,gender,traits).."
  ```

## Usage

To use VirtuAI Helper with OBS and Vtuber studio, you can follow this guide in [How to use with OBS and Vtuber studio](how_to_use_with_obs_and_vtuber_studio.md). For normal usage in the terminal or command prompt, you can follow the guide below.

1. Open VoiceVox engine.
2. Open `run.bat`.
3. Follow on-screen prompts and interact with VirtuAI Helper.

---
## Contributing

VirtuAI Helper is a project created for fun, if you are interested to contribute in this project here is how you can make this project better for everyone.

### Bug Reports and Feature Requests

If you found a bug or have an idea for a new feature, feel free to requests and reports by [open an issue](https://github.com/ZeroMirai/VirtuAI-Helper/issues) on GitHub and post it if it's a bug please give as much detail as possible or suggest an idea please include a step or a clear description.

### Pull Requests

If you have suggestions or improvements.

1. Fork the repository and create your own branch from `main`.
2. Work on your changes.
3. Write clear, concise commit messages that describe the purpose of your changes.
4. Open a pull request and provide a detailed description of your changes.

I'm primarily looking for code improvements and bug fixes. Once your changes are approved, they will be merged into the main project.

### ⭐ Share and Give a Star ⭐

**If you find this project useful I would be really grateful if you could consider sharing this small project with others and giving it a star on GitHub.**

---

## Note

- Ensure that you have the required dependencies and configuration set up before running the code.
- Running the program and VoiceVox engine simultaneously is necessary for proper program functionality.
- If you use this program with OBS and Vtuber Studio, you need to redo steps 5-8 every time the program is opened.
- For text input it can recive input in any language but for voice input it can only recognize English language.
- If text in obs is not showing, make sure  you place the Subtitle source above the Live2D source.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- **OpenAI** - Used to generate responses with the chatGPT model. For more information, visit [OpenAI API](https://openai.com/)
- **Voicevox** by Hiroshiba - Used to synthesize speech in Japanese. For more information, visit [VoiceVox Engine](https://voicevox.hiroshiba.jp/)
- **AssemblyAI API** - Used to convert speech to text. For more information, visit [AssemblyAI API](https://www.assemblyai.com/)
- **PyAutoGUI** - Used to perform multimedia tasks such as playpause media, turn updown the volume, and capture the screen. For more information, visit [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- **Webbrowser**- Used to open websites such as Facebook, YouTube, and Twitter. For more information, visit [Webbrowser](https://docs.python.org/3/library/webbrowser.html)
