import cv2
import numpy as np
from pyzbar.pyzbar import decode
from encryptor import decrypt

output = str
data = str
requiredCode = str
loginCode = str
result = str


def qrreader():
    global output, data, requiredCode, loginCode, result
    isNotScanned = True
    cap = cv2.VideoCapture(0)
    cap.set(3, 680)
    cap.set(4, 680)

    with open("data.txt") as file:

        finalarray = []
        array = []
        content = file.readlines()
        code = []

        row = 0
        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

        for i in range(len(finalarray)):
            code.append(finalarray[i][0])

    isNotScanned = True
    while isNotScanned:

        success, img = cap.read()
        for qrcode in decode(img):
            data = qrcode.data.decode('utf-8')
            data = decrypt(data)
            loginCode = data[7:10]
            data = data[3:7]

            if data in code:
                output = "Authorized"
                color = (0, 255, 0)
                isNotScanned = False
            else:
                output = "Unauthorized"
                color = (0, 0, 255)
                isNotScanned = False

            pts = np.array([qrcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, color, 5)
            pts2 = qrcode.rect
            cv2.putText(img, output, (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow('Scan Your QR Code', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        # ret, buffer = cv2.imencode('.png', img)
        # img = buffer.tobytes()
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()

    result = output.lower()
    requiredCode = data
    return requiredCode, loginCode, result


result = result
loginCode = loginCode
requiredCode = requiredCode
