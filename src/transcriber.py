import os
from dotenv import load_dotenv
from deepgram import DeepgramClient, LiveTranscriptionEvents, LiveOptions, DeepgramClientOptions


load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

class LiveTranscriber:
    def __init__(self, gui):
        if not DEEPGRAM_API_KEY:
            raise ValueError("Deepgram API key not found. Please set it in the .env file.")
        
        # self.deepgram = DeepgramClient(DEEPGRAM_API_KEY, )
        self.deepgram = DeepgramClient(
            api_key=DEEPGRAM_API_KEY,
            config=DeepgramClientOptions(verbose=False),
        )
        self.connection = self.deepgram.listen.websocket.v("1")
        self.gui = gui

        self.connection.on(LiveTranscriptionEvents.Open, self.on_open)
        self.connection.on(LiveTranscriptionEvents.Transcript, self.on_message)
        self.connection.on(LiveTranscriptionEvents.Close, self.on_close)

    def on_open(self, *_):
        print("[INFO] Connection Open")

    def on_message(self, _, result, **kwargs):
        global is_finals

        sentence = result.channel.alternatives[0].transcript
        if len(sentence) == 0:
            return  # Ignore empty transcriptions

        if result.is_final and result.speech_final:  # Process only final confirmed text
            # print(f"[INFO] Final Speech: {sentence}")
            self.gui.update_transcription(sentence)  # Update GUI with final text

    def on_close(self, *_):
        print("[INFO] Connection Closed")

    def start_transcription(self):
        options = LiveOptions(
            model="nova-3",
            language="en-US",
            smart_format=True,
            encoding="linear16",
            channels=1,
            sample_rate=48000,
            interim_results=True,
        )
        
        if not self.connection.start(options):
            print("[ERROR] Failed to connect to Deepgram")
            return False
        return True
