import cv2

# 웹캠에서 영상을 읽어온다.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)  # 세로 사이즈
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)  # 가로 사이즈

# 얼굴 인식, 눈 인식 캐스케이드 파일 읽는다.
face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
    # frame 별로 얼굴과 눈을 capture 한다
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)


    # 인식된 얼굴과 눈 갯수를 출력
    print(len(faces))
    print(len(eyes))

    # 인식된 얼굴과 눈에 사각형을 출력한다
    for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in eyes:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 화면에 출력한다
    cv2.imshow('OPENCV CAMERA', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()