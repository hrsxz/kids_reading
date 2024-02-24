import os

from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
from pathlib import Path


project_root_path = Path(__file__).resolve().parent.parent.parent

load_dotenv()

client = OpenAI()
client.api_key = os.environ.get("OPENAI_API_KEY")


def stream_and_play(text):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)

    # Lod the audio file
    audio = AudioSegment.from_file(speech_file_path)
    play(audio)


if __name__ == "__main__":
    # text = input("Enter the text to be converted to speech:")
    text = "Anan, sollen wir jetzt schlafen gehen? 安安, 现在我们去睡觉吗?"
    stream_and_play(text)
