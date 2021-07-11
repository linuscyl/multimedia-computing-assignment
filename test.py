import transcribe
import cv2
import time

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('1551.avi', fourcc, 20.0, (1280, 720))

# subtitle = transcribe.main()

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # cv2.putText(frame, subtitle, (20, 20),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 0), 3)

        cv2.imshow("Real Live Caption", frame)

        # 寫入影格
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


# cap.release()
# out.release()
# cv2.destroyAllWindows()
