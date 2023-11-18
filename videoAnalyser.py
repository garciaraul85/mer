import cv2
import base64
import openai

# Initialize OpenAI client
client = openai.OpenAI()

### VIDEO TO TEXT ###
video = cv2.VideoCapture("football.mp4")

# Read frames and encode to base64
base64Frames = []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break

    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
# Release video object
video.release()
print(len(base64Frames), "frames read.")
