import math
from helperfuncs import compute_distance

def detect_sets(landmarks, image):
    '''
    Points needed to detect a set
    21 - left thumb (to make sure they are close enough to set the ball)
    22 - right thumb (to make sure they are close enough to set the ball)
    13 - left elbow (to make sure they are raised)
    14 - right elbow (to make sure they are raised)
    '''
    isSet = False
    if landmarks:
        left_length_c = compute_distance(landmarks[15], landmarks[11])
        left_length_b = compute_distance(landmarks[13], landmarks[11])
        left_length_a = compute_distance(landmarks[15], landmarks[13])
        left_angle = math.acos((left_length_c**2 - left_length_a**2 - left_length_b**2) / (-2 * (left_length_a) * (left_length_b)))

        right_length_c = compute_distance(landmarks[16], landmarks[12])
        right_length_b = compute_distance(landmarks[14], landmarks[12])
        right_length_a = compute_distance(landmarks[16], landmarks[14])
        right_angle = math.acos((right_length_c**2 - right_length_a**2 - right_length_b**2) / (-2 * (right_length_a) * (right_length_b)))

        if left_angle > 1.6 and left_angle < 2.4 and right_angle > 1.6 and right_angle < 2.4 and landmarks[22].y < landmarks[14].y and landmarks[21].y < landmarks[13].y:
            print("Set")
            print(left_angle)
            isSet = True
        elif landmarks[22].y > landmarks[14].y:
            print("Try raising your arms above your head")
        elif landmarks[21].y > landmarks[13].y:
            print("Try raising your arms above your head")
    if isSet:
        return True
    else:
        return False
