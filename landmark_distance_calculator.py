import math
import mediapipe as mp

def calculate_distance(landmark1, landmark2):
    return math.sqrt(
        (landmark1.x - landmark2.x) ** 2 +
        (landmark1.y - landmark2.y) ** 2 +
        (landmark1.z - landmark2.z) ** 2
    )

class LandmarkDistanceCalculator:
    def process(self, landmarks):
        left_shoulder = landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER]
        
        # Calculate the distance between left and right shoulders
        distance = calculate_distance(left_shoulder, right_shoulder)
        return distance
