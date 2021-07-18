import transcribe
import cv2
import threading
import testRecordAudio
import time
import combineAudioVideo

class Test2:
    def __init__(self, subtitle, isRecognizing):
        self.subtitle = subtitle
        self.isRecognizing = isRecognizing

    def stt(self):
        # The duration in seconds of the video captured
        capture_durationxx = 10
        start_timexx = time.time()
        while self.isRecognizing is False:
            print("ran thread1")
            try:
                self.isRecognizing = True
                transcribe.main()
                self.isRecognizing = False

            except Exception as e:
                print("Error :  " + str(e))

            if (int(time.time() - start_timexx) > capture_durationxx):
                break

    # def getSubtitle(self):
    #     print("get subtitle: "+self.subtitle)
    #     return self.subtitle

    def writeVideo(self):
        # The duration in seconds of the video captured
        capture_duration = 10

        cap = cv2.VideoCapture(0)

        out = cv2.VideoWriter('demo_divx.avi', cv2.VideoWriter_fourcc(
            'D', 'I', 'V', 'X'), 30, (1280, 720))

        outs = cv2.VideoWriter('demo_mjpg.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (1280, 720))

        while cap.isOpened():
            # print("ran thread 2")
            start_time = time.time()
            while (int(time.time() - start_time) < capture_duration):
                ret, frame = cap.read()
                if ret:
                    cv2.putText(frame, transcribe.getSTTresult(), (20, 620),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 0), 3)
                    # 寫入影格
                    out.write(frame)
                    outs.write(frame)

                    # cv2.imshow("Real Live Caption", frame)
                    #
                    # if cv2.waitKey(1) & 0xFF == ord('q'):
                    #     break
                else:
                    break
            break
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def recordAudio(self):
        testRecordAudio.main()


def test():
    temp = Test2("", False)
    # testRecordAudio.main()
    thread0 = threading.Thread(target=temp.recordAudio, name='T0')
    thread1 = threading.Thread(target=temp.writeVideo, name='T1')
    thread2 = threading.Thread(target=temp.stt, name='T2')
    thread0.start()
    thread1.start()
    thread2.start()
    thread0.join()
    thread1.join()
    thread2.join()
    combineAudioVideo.main()


if __name__ == "__main__":
    test()
