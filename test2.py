import transcribe
import cv2
import threading


class Test2:
    def __init__(self, subtitle, isRecognizing):
        self.subtitle = subtitle
        self.isRecognizing = isRecognizing

    def stt(self):
        while self.isRecognizing is False:
            print("ran thread1")
            try:
                self.isRecognizing = True
                transcribe.main()
                self.isRecognizing = False

            except Exception as e:
                print("Error :  " + str(e))

    # def getSubtitle(self):
    #     print("get subtitle: "+self.subtitle)
    #     return self.subtitle

    def writeVideo(self):
        cap = cv2.VideoCapture(0)

        out = cv2.VideoWriter('001.avi', cv2.VideoWriter_fourcc(
            'M', 'J', 'P', 'G'), 5, (1280, 720))

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        outs = cv2.VideoWriter('001s.mp4', fourcc, 5, (1280, 720))

        while cap.isOpened():
            # print("ran thread 2")
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


def test():
    temp = Test2("", False)
    thread1 = threading.Thread(target=temp.writeVideo, name='T1')
    thread2 = threading.Thread(target=temp.stt, name='T2')
    thread1.start()
    thread2.start()


if __name__ == "__main__":
    test()
