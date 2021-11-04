import cv2 as cv

WIDTH: int = 320
HEIGHT: int = 240

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)

print("Width = ", cap.get(cv.CAP_PROP_FRAME_WIDTH))
print("Height = ", cap.get(cv.CAP_PROP_FRAME_HEIGHT))  

while True:
    # 1フレームずつ読み込む
    ret, frame = cap.read()

    # フレームが正しく読み込まれない場合
    if not ret:
        print("Can't receive frame")
        break
    
    # 読み込んだフレームを表示
    cv.imshow("frame", frame) 
    
    #「q」キーが押されたらウィンドウを閉じる
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
