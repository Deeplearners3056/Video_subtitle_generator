# Whisper Video Subtitle Generator

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Hugging Face Transformers](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow)](https://huggingface.co/transformers/)

This project provides a simple web application to generate subtitles for video files using the powerful [Whisper](https://github.com/openai/whisper) model from Hugging Face's [Transformers](https://huggingface.co/transformers/) library. The application, built with Flask, allows you to upload a video, transcribe its audio, generate subtitles in the `.srt` format, and embed these subtitles directly into the video file.

## Features

* **Effortless Audio Extraction:**  Automatically extracts audio from uploaded video files.
* **AI-Powered Transcription:** Leverages the state-of-the-art Whisper model for accurate audio transcription.
* **Subtitle Generation:** Converts the transcribed text into standard `.srt` subtitle files.
* **Seamless Embedding:** Embeds the generated subtitles directly into the video, creating a single output file.
* **User-Friendly Web Interface:**  A straightforward Flask web application for easy video uploading and downloading.
* **Customizable Whisper Model:** (Potentially - depending on implementation) Allows selection of different Whisper model sizes for varying accuracy and speed.

## Requirements

* **Python:**  Version 3.8 or higher is recommended.
* **Dependencies:** Listed in `requirements.txt`.
* **FFmpeg:**  Essential for audio extraction and video manipulation. Ensure it's installed and accessible in your system's PATH.
* **ImageMagick:** Required by MoviePy for overlaying subtitles onto the video. Ensure it's installed and added to your system's PATH.

## Installation Steps

Follow these steps to set up and run the Whisper Video Subtitle Generator on your local machine.

**Step 1: Clone the Repository**

```bash
git clone https://github.com/your-username/whisper-video-subtitle-generator.git
cd whisper-video-subtitle-generator
```

**Step 2: Create a Virtual Environment (Recommended)**

It's best practice to work within a virtual environment to isolate project dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

* **On Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```
* **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

**Step 3: Install Dependencies**

Install the necessary Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**Step 4: Install ImageMagick**

ImageMagick is crucial for the subtitle overlay process.

1. **Download:**  Visit the official ImageMagick website ([https://imagemagick.org/download/](https://imagemagick.org/download/)) and download the appropriate version for your operating system.
2. **Install:** Follow the installation instructions for your platform.
3. **Add to PATH:**  During the installation, **ensure you select the option to add ImageMagick to your system's PATH environment variable.** This allows MoviePy to find the necessary executables. If you missed this during installation, you'll need to manually add the ImageMagick installation directory (containing `convert.exe` or similar) to your PATH.

**Step 5: Set Up FFmpeg**

FFmpeg is used for extracting audio from videos.

1. **Download:** Download FFmpeg from the official website or using your system's package manager. Some common methods include:
   * **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`
   * **Linux (Fedora):** `sudo dnf install ffmpeg`
   * **macOS (Homebrew):** `brew install ffmpeg`
   * **Windows:** Download pre-built binaries from websites like [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html). Choose a suitable build (e.g., "gyan.dev" or "BtbN").
2. **Add to PATH:**  After downloading and extracting FFmpeg (if necessary), you need to add the directory containing the `ffmpeg` executable to your system's PATH environment variable.

   * **Windows:**
     1. Search for "Environment Variables" in the Start Menu.
     2. Click on "Edit the system environment variables".
     3. Click the "Environment Variables..." button.
     4. Under "System variables", find and select the "Path" variable, then click "Edit...".
     5. Click "New" and add the path to the directory where `ffmpeg.exe` is located (e.g., `C:\ffmpeg\bin`).
     6. Click "OK" on all open windows.
   * **Linux/macOS:**
     You can typically add the FFmpeg bin directory to your `~/.bashrc`, `~/.zshrc`, or a similar shell configuration file. Add a line like:
     ```bash
     export PATH="/path/to/ffmpeg/bin:$PATH"
     ```
     Replace `/path/to/ffmpeg/bin` with the actual path to the FFmpeg binaries. After editing the file, run `source ~/.bashrc` or `source ~/.zshrc` (or restart your terminal) to apply the changes.

**Step 6: Run the Flask App**

Navigate to the project directory in your terminal and start the Flask application.

```bash
python app.py
```

This will launch the Flask development server. You can access the application in your web browser by navigating to `http://127.0.0.1:5000/`.

**Step 7: Generate Subtitles**

1. **Upload Video:** On the web page, click the "Choose File" button and select the video file you want to subtitle.
2. **Process:** Click the "Generate Subtitles" button.
3. **Wait for Processing:** The application will extract the audio, transcribe it using the Whisper model, generate subtitles, and embed them into the video. This may take some time depending on the video length and your system's resources.
4. **Download:** Once the process is complete, a download link for the subtitled video will be available. Click the link to download the new video file.

## File Structure

```
whisper-video-subtitle-generator/
├── app.py                # Main Flask application file
├── uploads/              # Directory to store uploaded video files
├── output/               # Directory to store output videos with embedded subtitles
├── requirements.txt      # List of Python dependencies
├── templates/
│   └── index.html        # HTML template for the web interface
└── static/               # Directory for static files (e.g., CSS)
```

**Note:** The `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe` files listed in the original description are not typically placed directly in the project directory. Instead, they should be installed system-wide and accessible through the PATH environment variable, as described in Step 5. You can remove these from the listed file structure in your actual repository if you are following best practices.

## Configuration

* **Whisper Model:** The `app.py` file likely contains the code for loading and using the Whisper model. You might be able to configure which Whisper model size (`tiny`, `base`, `small`, `medium`, `large`) to use by modifying the relevant lines in `app.py`. Larger models generally offer better accuracy but require more computational resources and processing time.

## Troubleshooting

* **FFmpeg or ImageMagick not found:**  This is the most common issue. Double-check that you have installed both FFmpeg and ImageMagick correctly and that their respective `bin` directories are added to your system's PATH environment variable. Restart your terminal or computer after modifying the PATH.
* **Permission Errors:** Ensure that the Flask application has write permissions to the `uploads/` and `output/` directories.
* **Large Videos:** Processing large video files can take a significant amount of time. Be patient or consider using a more powerful machine.
* **Out of Memory Errors:** For very long videos, the transcription process might require a lot of memory. Consider using a smaller Whisper model or a machine with more RAM.
* **Inaccurate Subtitles:** The accuracy of the subtitles depends on the quality of the audio and the Whisper model used. Experiment with different model sizes if needed.

## Contributing

Contributions to this project are welcome! If you find a bug, have a suggestion, or want to add a new feature, please feel free to:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications and commit them.
4. Push your branch to your fork.
5. Submit a pull request.

