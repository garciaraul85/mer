import cv2
import base64
import openai
from moviepy.editor import VideoFileClip, AudioFileClip

# Initialize OpenAI client
client = openai.OpenAI()

### VIDEO TO TEXT ###
video = cv2.VideoCapture("football.mp4")


# Calculate video length
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
video_length_seconds = length / fps

print(f'Video length: {video_length_seconds:.2f} seconds')


# Get the frame rate of the video
fps = video.get(cv2.CAP_PROP_FPS)
# Calculate the number of frames for 11 seconds
frames_for_11_seconds = int(fps * 11)

# Read frames and encode to base64
base64Frames = []
frame_count = 0

while video.isOpened(): #and frame_count < frames_for_11_seconds:
    success, frame = video.read()
    if not success:
        break

    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
    frame_count += 1
# Release video object
video.release()
print(len(base64Frames), "frames read.")


# Prompt
prompt = f"These are frames from a football match video lasting {video_length_seconds:.2f} seconds. I need a scripted voiceover for a football commentary segmented by timestamps. Each segment should start with a timestamp, like this: [00:00] 'Commentary segment...' [00:08] 'Next commentary segment...' [00:15] 'Another commentary segment...' Please ensure each part of the commentary has a timestamp at the beginning. The content doesn't have to be real-time but should be in the style of a football game commentary."

# Set a higher temperature for creativity, if desired
temperature = 0.9

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
                prompt,
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::222]),
            ]
    }],
    max_tokens=500
)
result = response.choices[0].message.content
print(result)


## Text to Speech ##
#speech_file_path = "football.mp3"
#response = client.audio.speech.create(
#    model="tts-1",
#    voice="onyx",
#    input=result
#)

#response.stream_to_file(speech_file_path)


## Merge video and audio ##

#video_clip = VideoFileClip("football.mp4")
#audio_clip = AudioFileClip("football.mp3")
#final_clip = video_clip.set_audio(audio_clip)
#final_clip.write_videofile("football_with_commentary.mp4", codec='libx264', audio_codec='aac')
#video_clip.close()
#audio_clip.close()
#final_clip.close()