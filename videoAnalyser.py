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

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
                f"These are frames of a video. Create a short voiceover script in the style of a football commentator For 5 seconds. Only include the narration.",
                # get every 322 frame
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::322]),
            ]
    }],
    max_tokens=500
)
result = response.choices[0].message.content
print(result)