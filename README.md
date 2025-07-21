
---

## Audio Transcription using AssemblyAI API

This Python project allows you to **automatically transcribe audio files** into text using the [AssemblyAI Speech-to-Text API](https://www.assemblyai.com/). It supports large audio files by uploading them in chunks and periodically polling the API for transcription status.

---

### Project Structure

```bash
├── transcribe.py            # Main transcription script
├── api_secrets.py           # Stores your AssemblyAI API key
└── README.md                # Project documentation
```

---

### Features

* Uploads audio files in chunks (for large files)
* Sends audio URL to AssemblyAI API for transcription
* Polls the API every 30 seconds for transcription status
* Saves the final transcript as a `.txt` file
* Simple and easy to run from the command line

---

### Requirements

* Python 3.6+
* `requests` library

Install dependencies using:

```bash
pip install requests
```

---

### API Key Setup

Create a file called `api_secrets.py` in the same directory and store your API key like this:

```python
API_KEY_ASSEMBLYAI = "your_api_key_here"
```

---

### Usage

To transcribe an audio file:

```bash
python transcribe.py your_audio_file.wav
```

Once completed, a text file named `your_audio_file.wav.txt` will be created in the same directory containing the transcription.

---

###  How It Works

1. **Upload**: The file is uploaded to AssemblyAI’s servers using their chunked upload endpoint.
2. **Transcribe**: The audio URL is sent to AssemblyAI to initiate transcription.
3. **Poll**: The script continuously checks the status of the transcription job every 30 seconds.
4. **Save**: Once complete, the transcript is saved to a local `.txt` file.

---

###  Example Output

If you transcribe `interview.wav`, the output will be saved as:

```
interview.wav.txt
```

Containing:

```
[Transcribed text from the audio]
```

---


