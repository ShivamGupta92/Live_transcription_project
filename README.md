# 🎤 Live Speech-to-Text Transcription using Deepgram

This project is a real-time **Speech-to-Text (STT) Transcription** application using **Deepgram's WebSocket API**. It captures live audio through a microphone, transcribes it, and displays the results in a **GUI window** built with Tkinter.

## Features
- **Real-time Speech Recognition** using Deepgram API
- **Live GUI Display** for transcription results
- **Handles Interim & Final Transcriptions**
- **Automatic Speech Detection & Endpointing**
- **Multi-threaded Execution** to prevent UI freezing

## Installation & Setup

### Clone the Repository
```sh
$ git clone <this repo link>
$ cd deepgram_live_transcription (optional)
```

### Install Dependencies
```sh
$ pip install -r requirements.txt
```

### Set Up API Key
- Create a `.env` file in the root directory.
- Add your **Deepgram API Key**:
```plaintext
DEEPGRAM_API_KEY=your_api_key_here
```

### Run the Application
```sh
$ python main.py
```

---
## 🛠️ How It Works
1. The program establishes a **WebSocket** connection to Deepgram.
2. Captures audio from the **microphone**.
3. Sends audio data to Deepgram API.
4. Receives **real-time transcription results**.
5. Displays results in the **GUI window**.
6. Stops when the user **clicks the Exit button**.

---
## Key Functionalities
### 🎤 **Live Transcription with Deepgram API**
- Captures live speech using `Microphone()`.
- Sends raw audio (`linear16`, `16kHz`) to Deepgram.
- Receives **interim & final results**.

### 🖥️ **GUI Window with Tkinter**
- Displays live transcriptions in a text box.
- "Exit" button to **stop transcription** and close the app.
- Multi-threading prevents GUI freezing.

---
## ⚙️ Configuration Options
Modify the transcription options in `transcriber.py`:
```python
options: LiveOptions = LiveOptions(
    model="nova-2",
    language="en-US",
    smart_format=True,
    encoding="linear16",
    sample_rate=16000,
    interim_results=True,
    utterance_end_ms="1000",
    vad_events=True,
    endpointing=300,
)
```

**Feel free to contribute & improve this project!** 🔥


## For Linux/Mac users
if getting an error in PyAudio
- sudo apt-get install portaudio19-dev
- pip install pyaudio

if getting an error in tk or tkinter
- sudo apt-get install python3-tk
