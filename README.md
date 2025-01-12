Whisper Video Subtitle Generator
This project uses the Whisper model from Hugging Face to generate subtitles from video files and embed them into the video. The app is built with Flask and uses MoviePy for video processing. The video’s audio is transcribed to text, then converted to subtitles in the .srt format and added to the video.

Features
Extracts audio from video.
Generates subtitles from the audio using the Whisper model.
Embeds subtitles into the video and saves the final result.
A simple Flask web app to upload videos and download the subtitled video.
Requirements
Python 3.x (Recommended: Python 3.8+)
Required Libraries:
Flask
Transformers
MoviePy
ffmpeg-python
pysrt
torch (for Whisper)
ffmpeg (for audio extraction)
ImageMagick (for subtitle overlay in MoviePy)
Installation Steps
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/whisper-video-subtitle-generator.git
cd whisper-video-subtitle-generator
Step 2: Create a Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Dependencies:

Flask
Transformers
MoviePy
ffmpeg-python
torch
pysrt
ffmpeg
ImageMagick (for subtitle overlay)
Step 4: Install ImageMagick
Download and install ImageMagick from here for your platform. During installation, make sure to check the box to add ImageMagick to the system PATH.

Step 5: Set Up FFMPEG
Make sure FFmpeg is installed and added to the system's PATH. FFmpeg is used to extract audio from videos.

Download FFmpeg from here.
Add FFmpeg’s bin directory to your system’s PATH.
Step 6: Run the Flask App
bash
Copy code
python app.py
This will start the Flask web server, and you can visit the app at http://127.0.0.1:5000/ in your web browser.

Step 7: Upload a Video
On the web page, you can upload a video, and the application will:

Extract the audio.
Generate subtitles using the Whisper model.
Embed the subtitles into the video.
Allow you to download the subtitled video.
File Structure
plaintext
Copy code
whisper-video-subtitle-generator/
├── app.py                # Main Flask app
├── uploads/              # Folder for uploaded videos
├── output/               # Folder for outputted videos with subtitles
├── ffmpeg.exe            # FFmpeg binaries (for audio extraction)
├── ffplay.exe            # FFPlay (optional, for video playback)
├── ffprobe.exe           # FFProbe (optional, for media info)
├── videoplayback.mp4     # Sample video file
└── templates/
    └── index.html        # HTML template for the Flask app
