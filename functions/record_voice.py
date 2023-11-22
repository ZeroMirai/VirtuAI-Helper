import pyaudio
import keyboard
import wave

# Constants for audio recording configuration
FRAME_PER_BUFF = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # Audio format (8-bit, 16-bit , 24-bit, 32-bit)
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 16000  # Sampling rate in Hertz (samples per second)
OUTPUT_FILENAME = "recording.wav"  # Output file name for recorded audio


def record_voice():
    # Instantiate PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream for audio input
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAME_PER_BUFF,
    )

    frames = []  # List to store audio frames

    print("-----------------------\nPress 'v' to start recording...")
    while True:
        if keyboard.is_pressed("v"):
            # Disable the 'v' key to prevent repeated recording trigger
            keyboard.block_key("v")
            print("Recording...")

            while True:
                data = stream.read(FRAME_PER_BUFF)
                frames.append(data)

                # Check if the 'v' key is released to stop recording
                if not keyboard.is_pressed("v"):
                    # Unblock the 'v' key
                    keyboard.unblock_key("v")
                    break
            break

    print("Stopped recording")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio frames to a WAV file
    wave_file = wave.open(OUTPUT_FILENAME, "wb")
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()
