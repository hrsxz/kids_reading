"""
An app that allows kids to scan the book's and read the book.
"""
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
from pathlib import Path


project_root_path = Path(__file__).resolve().parent.parent.parent

load_dotenv()

client = OpenAI()
client.api_key = os.environ.get("OPENAI_API_KEY")


class kidsreading(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.text_input = toga.TextInput(style=Pack(flex=1))
        read_button = toga.Button('Read Book', on_press=self.read_book, style=Pack(padding=5))
        input_box = toga.Box(children=[self.text_input, read_button], style=Pack(direction=ROW, padding=5))

        main_box.add(input_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def read_book(self, widget):
        """Read the book's text aloud."""
        text = self.text_input.value
        self.stream_and_play(text)

    def stream_and_play(self, text):
        """Convert text to speech and play."""
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(speech_file_path)

        # Load and play the audio file
        audio = AudioSegment.from_file(speech_file_path)
        play(audio)


def main():
    return kidsreading('Kids Reading', 'org.example.kidsreading')


if __name__ == '__main__':
    main().main_loop()
