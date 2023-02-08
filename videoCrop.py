from moviepy.editor import VideoFileClip

# Open the video file
clip = VideoFileClip("path/to/video.mp4")

# Define the starting point and dimensions for the crop
x = 317
y = 185
width = 1285
height = 595

# Crop the video
cropped_clip = clip.crop(x1=x, y1=y, x2=x+width, y2=y+height)

# Save the cropped video
cropped_clip.write_videofile("path/to/cropped_video.mp4")
