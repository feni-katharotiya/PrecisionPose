import cv2
import mediapipe as mp
from mediapipe.python.solutions import drawing_utils
from mediapipe.python import solution_base
import landmark_distance_calculator

# Load the custom graph
mp_pose = mp.solutions.pose

# Create a MediaPipe Pose instance with the custom graph
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Load an image
image = cv2.imread('input_image_2.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert the image to RGB

# Process the image through the MediaPipe pipeline
results = pose.process(image_rgb)
 
# Check if landmarks were found
if results.pose_landmarks:
    # Draw landmarks on the image for visualization
    drawing_utils.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

# Show the output image
cv2.imshow('Pose Estimation', image)

cv2.imwrite("output_image_2.png",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
