import os
import pyqrcode
from random import randint
from encryptor import encrypt
from PIL import Image

def signup():
    with open("data.txt", "a+" ) as file:
        redg_no = '6842'
        f_name = 'Faisal'
        l_name = 'Ahmed'
        designation = 'Admin'
        d = designation.lower()

        if  d == "student":
            d = "001"
        elif d == "council":
            d="002"
        elif d == "teacher":
            d = "003"
        elif d == "admin":
            d="004"
        else:
            print("Error!")
            exit()

        line = redg_no + "," + f_name + " " + l_name + ","  + designation

        file.write(line + "\n" )

    code = str(randint(100,1000)) + redg_no + d + f_name.lower() + l_name.lower()
    encrypted = encrypt(code)

    qr = pyqrcode.create(encrypted)
    qr.png("code.png", scale=10)

    image1 = Image.open('code.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')

    print(encrypted)

def printer():
        file_path = "printing.pdf"
        os.startfile(file_path, "print")

signup()
