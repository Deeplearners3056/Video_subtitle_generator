from flask import Flask, request, render_template, send_file
from transformers import pipeline
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import ffmpeg

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Load Whisper pipeline
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")     

def extract_audio_from_video(video_path):
    """Extract audio from a video file."""
    audio_path = video_path.replace('.mp4', '.wav')
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar=16000)
        .overwrite_output()
        .run()
    )
    return audio_path

def generate_subtitles(video_path):
    """Generate subtitles using Hugging Face's Whisper pipeline."""
    # Extract audio
    audio_path = extract_audio_from_video(video_path)
    
    # Perform transcription
    result = pipe(audio_path)
    transcription = result["text"]

    # Write transcription to SRT file
    subtitles_path = video_path.replace('.mp4', '.srt')
    with open(subtitles_path, 'w', encoding='utf-8') as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:10,000\n")  # Dummy timing for simplicity
        f.write(f"{transcription}\n")
    
    os.remove(audio_path)  # Clean up
    return subtitles_path

def embed_subtitles(video_path, subtitles_path):
    """Embed subtitles into the video."""
    video = VideoFileClip(video_path)
    subs = []

    with open(subtitles_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        text = lines[2].strip()
        subtitle = TextClip(text, fontsize=24, color='white', bg_color='black', size=video.size)
        subtitle = subtitle.set_position(('center', 'bottom')).set_duration(video.duration)
        subs.append(subtitle)

    final_video = CompositeVideoClip([video, *subs])
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], os.path.basename(video_path))
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files:
            return "No video file uploaded!"
        
        video_file = request.files['video']
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
        video_file.save(video_path)
        
        # Generate subtitles
        subtitles_path = generate_subtitles(video_path)
        
        # Embed subtitles into video
        final_video_path = embed_subtitles(video_path, subtitles_path)
        
        return send_file(final_video_path, as_attachment=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
