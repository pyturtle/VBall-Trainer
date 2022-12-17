import cv2
import mediapipe as mp
from detectsets import detect_sets
from detectbumps import detect_bumps
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(1)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    if results.pose_landmarks is not None:  
        landmarks = results.pose_landmarks.landmark
        if landmarks:
            if landmarks[15].y > landmarks[11].y and landmarks[16].y > landmarks[12].y:
              # Then it's a bump
              isBump = detect_bumps(landmarks, image)
              if isBump is not None:
                font = cv2.FONT_HERSHEY_SIMPLEX
                if isBump == "Try extending your arm outside":
                  cv2.putText(image, isBump, (1000, 600), font, 3, (0, 255, 0), 12, cv2.LINE_AA) 
                  # cv2.imshow('MediaPipe Pose', image)
                  # continue
                else:
                  cv2.putText(image, isBump, (400, 600), font, 3, (0, 255, 0), 12, cv2.LINE_AA)
                  # cv2.imshow('MediaPipe Pose', image)
                  # continue
          
            else:
              isSet = detect_sets(landmarks, image)
              if isSet is not None:
                font = cv2.FONT_HERSHEY_SIMPLEX
                if isSet == "Try raising your arms above your head":
                  cv2.putText(image, isSet, (40, 600), font, 3, (0, 255, 0), 12, cv2.LINE_AA)
                else:
                  cv2.putText(image, isSet, (900, 600), font, 3, (0, 255, 0), 12, cv2.LINE_AA)

    cv2.imshow('MediaPipe Pose', image)
            

            
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

