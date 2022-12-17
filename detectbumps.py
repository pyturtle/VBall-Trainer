import math
from helperfuncs import compute_distance

def detect_bumps(landmarks, image):
    '''
    Points needed to detect a bump
    21 - left thumb (to make sure they are close enough to set the ball)
    22 - right thumb (to make sure they are close enough to set the ball)
    13 - left elbow (to make sure they are raised)
    14 - right elbow (to make sure they are raised)
    '''
    # isSet = False
    if landmarks:
        left_length_c = compute_distance(landmarks[15], landmarks[11])
        left_length_b = compute_distance(landmarks[13], landmarks[11])
        left_length_a = compute_distance(landmarks[15], landmarks[13])
        left_angle = math.acos((left_length_c**2 - left_length_a**2 - left_length_b**2) / (-2 * (left_length_a) * (left_length_b)))

        right_length_c = compute_distance(landmarks[16], landmarks[12])
        right_length_b = compute_distance(landmarks[14], landmarks[12])
        right_length_a = compute_distance(landmarks[16], landmarks[14])
        right_angle = math.acos((right_length_c**2 - right_length_a**2 - right_length_b**2) / (-2 * (right_length_a) * (right_length_b)))

        print(left_angle)

        if left_angle >= 1.8 and right_angle >= 1.8:
            return "Bump"
        if left_angle < 1.8 and right_angle < 1.8:
            return "Try to extend your arm out"
        # if left_length < 2 and right_length < 2.0:
        #     return "Bump"
        # else:
        #     return "Try extending your arm outside"
        # if left_angle > 1.6 and left_angle < 2.4 and right_angle > 1.6 and right_angle < 2.4 and landmarks[22].y < landmarks[14].y and landmarks[21].y < landmarks[13].y:
        #     return "Bump"
        #     # print(left_angle)
        #     # isSet = True
        # elif int(landmarks[11].x) == int(landmarks[13].x):
        #     # print("Try raising your arms above your head")
        #     return "Try to extend your arm out"
        # elif int(landmarks[12].x) == int(landmarks[14].x):
        #     # print("Try raising your arms above your head")
        #     return "Try to extend your arm out"
    # if isSet:
    #     return True
    # else:
    #     return False
    return None
