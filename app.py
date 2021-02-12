from flask import Flask, render_template, url_for, Response, redirect, request
import qrcodeReader
import os
from time import sleep, localtime, strftime
from random import randint
from encryptor import encrypt
import pyqrcode
from PIL import Image
import cv2

app = Flask(__name__)
time = str


def printer():
    file_path = "printing.pdf"
    os.startfile(file_path, "print")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template('signup.html')


@app.route("/register", methods=["GET", "POST"])
def registerdata():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        code = request.form["code"]
        designation = request.form["designation"]
        d = designation.lower()

        if d == "student":
            d = "001"
        elif d == "council":
            d = "002"
        elif d == "teacher":
            d = "003"
        elif d == "admin":
            d = "004"

        with open('data.txt', 'a+') as file:
            line = code + "," + fname + " " + lname + "," + designation

            file.write(line + "\n")

        code = str(randint(100, 1000)) + code + \
            d + fname.lower() + lname.lower()
        encrypted = encrypt(code)

        qr = pyqrcode.create(encrypted)
        qr.png("code.png", scale=10)

        image1 = Image.open('code.png')
        im1 = image1.convert('RGB')
        im1.save('printing.pdf')

    sleep(0.5)

    return redirect(url_for("printornot"))


@app.route("/printornot")
def printornot():
    return render_template("printer.html")


@app.route("/printing")
def printing():
    printer()
    return render_template("printing.html")


@app.route("/scanner")
def scanner():
    global time
    qrcodeReader.qrreader()
    if (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode != "004"):
        t = localtime()
        current_time = strftime("%H:%M:%S %A %x", t)
        a = current_time
        time = a[0:9]
        return redirect(url_for("login"))
    elif (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode == "004"):
        t = localtime()
        current_time = strftime("%H:%M:%S %A %x", t)
        a = current_time
        time = a[0:9]
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("error"))


@app.route("/admin")
def admin():
    global time

    with open("data.txt") as file:

        finalarray = []
        array = []
        content = file.readlines()
        code = []
        designation = str
        name = str

        row = 0
        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

        for i in range(len(finalarray)):
            code.append(finalarray[i][0])

        for x in range(len(code)):
            if qrcodeReader.requiredCode == code[x]:
                name = finalarray[x][1]
                designation = finalarray[x][2]

    return render_template("admin.html", time=time, code=qrcodeReader.requiredCode, designation=designation, name=name)


@app.route("/home")
def login():
    global time

    with open("data.txt") as file:

        finalarray = []
        array = []
        content = file.readlines()
        code = []
        designation = str
        name = str

        row = 0
        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

        for i in range(len(finalarray)):
            code.append(finalarray[i][0])

        for x in range(len(code)):
            if qrcodeReader.requiredCode == code[x]:
                name = finalarray[x][1]
                designation = finalarray[x][2]

    return render_template("login.html", time=time, code=qrcodeReader.requiredCode, designation=designation, name=name)


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/delete", methods=["GET", "POST"])
def deletedata():
    if request.method == "POST":
        deletecode = request.form["code"]

        with open('data.txt', 'r') as file:

            finalarray = []
            array = []
            content = file.readlines()
            code = []
            x = 0

            row = 0
            for line in content:

                row += 1
                array = line.split(",")

                array[-1] = array[-1].strip()

                finalarray.append(array)

            for i in range(len(finalarray)):
                code.append(finalarray[i][0])

        with open('data.txt', 'w') as file:
            file.truncate(0)

        with open('data.txt', 'a+') as file:

            for x in range(len(finalarray)):
                if deletecode != code[x]:
                    line = finalarray[x][0] + "," + \
                        finalarray[x][1] + "," + finalarray[x][2]
                    file.write(line + "\n")

    return redirect(url_for("delete"))


if __name__ == "__main__":
    app.run(debug=True)
