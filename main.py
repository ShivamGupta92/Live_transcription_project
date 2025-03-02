from src.transcriber import LiveTranscriber
from src.mic_input import MicrophoneStream
from src.gui import TranscriptionGUI
import threading

def main():
    gui = TranscriptionGUI()  # GUI must run in main thread
    transcriber = LiveTranscriber(gui)

    if not transcriber.start_transcription():
        return

    def mic_callback(in_data, frame_count, time_info, status):
        transcriber.connection.send(in_data)
        return (None, 0)

    mic = MicrophoneStream(callback=mic_callback)
    mic_thread = threading.Thread(target=mic.start, daemon=True)
    mic_thread.start()

    print("\n[INFO] Press Exit button in GUI to stop recording...\n")
    gui.start_gui() 

    mic.stop()
    transcriber.connection.finish()
    print("\n[INFO] Transcription Stopped.")

if __name__ == "__main__":
    main()
