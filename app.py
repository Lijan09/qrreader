from flask import Flask, render_template, url_for, Response, redirect, request
import qrcodeReader
import os
from time import sleep, localtime, strftime
from random import randint
from encryptor import encrypt
import pyqrcode
from PIL import Image, ImageDraw, ImageFont
import cv2
import edit
import log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
backwardlines = list
codeSize = (76, 76)
busNoFont = ImageFont.truetype('arial.ttf', 50)
font = ImageFont.truetype('arial.ttf', 11)
token = 500


def printer():
    file_path = r"C:\Users\Lijan\Desktop\Projects\qrreader\static/printing.pdf"
    os.startfile(file_path, "print")


def makeStudentID(name, code, qrcode, bno, faculty, bstop, cell):

    image = Image.open('static/student.png')

    draw = ImageDraw.Draw(image)

    draw.text((180, 118), bno, (0, 0, 0), font=busNoFont)
    draw.text((76, 179), name, (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 14))
    draw.text((124, 209), code, (0, 0, 0), font=font)
    draw.text((140, 235), faculty, (0, 0, 0), font=font)
    draw.text((125, 261), bstop, (0, 0, 0), font=font)
    draw.text((100, 287), cell, (0, 0, 0), font=font)
    draw.text((118, 313), "August 2050", (0, 0, 0), font=font)

    image.paste(qrcode, (74, 326))

    image.save('static/studentSave.png')

    image1 = Image.open('static/studentSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


def makeTeacherID(name, qrcode, faculty):
    width = int
    height = int

    image = Image.open('static/teacher.png')

    draw = ImageDraw.Draw(image)

    if len(name) >= 18:
        width = 100
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) < 18 and len(name) >= 15:
        width = 98
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) < 15 and len(name) >= 13:
        width = 97
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    else:
        width = 114
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)

    draw.text((114, 263), faculty, (0, 0, 0), font=font)

    image.paste(qrcode, (74, 281))

    image.save('static/teacherSave.png')

    image1 = Image.open('static/teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


def makeAdminID(name, qrcode):
    width = int
    height = int

    image = Image.open('static/admin.png')

    draw = ImageDraw.Draw(image)

    if len(name) >= 18:
        width = 100
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) < 18 and len(name) >= 15:
        width = 98
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) < 15 and len(name) >= 13:
        width = 97
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    else:
        width = 114
        height = 250
        draw.text((width, height), name, (0, 0, 0), font=font)
    draw.text((114, 263), "[Admin Office]", (0, 0, 0), font=font)

    image.paste(qrcode, (74, 281))

    image.save('static/adminSave.png')

    image1 = Image.open('static/adminSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


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
        faculty = request.form["faculty"]
        bno = request.form["bno"]
        bstop = request.form["bstop"]
        cell = request.form["cell"]
        d = designation.lower()

        if bno == "":
            bno = "?"

        if bstop == "":
            bstop = "Nil"

        log.logdata(code)

        if log.code == code:
            return render_template("codeerror.html")

        if d == "student":
            d = "001"
        elif d == "council":
            d = "002"
        elif d == "teacher":
            d = "003"
        elif d == "admin":
            d = "004"

        with open('data.txt', 'a+') as file:
            line = code + "," + fname + " " + lname + "," + \
                designation + "," + faculty + "," + bstop + "," + bno + "," + cell + "," + "0"

            file.write(line + "\n")

        ecode = str(randint(100, 1000)) + code + \
            d + fname.lower() + lname.lower()
        encrypted = encrypt(ecode)

        qr = pyqrcode.create(encrypted)
        qr.png("static/code.png", scale=1)

        qrcode = Image.open('static/code.png')
        qrcode = qrcode.resize(codeSize)
        image = None
        name = fname + " " + lname

        if (d == "001") or (d == "002"):
            makeStudentID(name, code, qrcode, bno, faculty, bstop, cell)
            return redirect(url_for("studentPreview"))

        elif (d == "003"):
            makeTeacherID(name, qrcode, faculty)
            return redirect(url_for("teacherPreview"))

        elif (d == "004"):
            makeAdminID(name, qrcode)
            return redirect(url_for("adminPreview"))


@app.route("/studentPreview")
def studentPreview():
    return render_template("studentPreview.html")


@app.route("/teacherPreview")
def teacherPreview():
    return render_template("teacherPreview.html")


@app.route("/adminPreview")
def adminPreview():
    return render_template("adminPreview.html")


@app.route("/printing")
def printing():
    printer()
    return render_template("printing.html")


@app.route("/scanner")
def scanner():
    global backwardlines
    qrcodeReader.qrreader()
    if (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode != "004"):
        t = localtime()
        current_time = strftime("%H:%M:%S %A %x", t)
        a = current_time
        time = a[0:9]

        attendanceTime = int(time[0:2] + time[3:5])
        if attendanceTime > 1100:
            attendance = "Absent"
        else:
            attendance = "Present"

        with open("raw_log.txt", "a+") as log:
            log.write(time.strip() + "," +
                      qrcodeReader.requiredCode + "," + attendance + "\n")

        with open('raw_log.txt', 'r+') as textfile:
            backwardlines = []
            lines = textfile.readlines()
            for line in reversed(lines):
                line = line.strip()
                backwardlines.append(line)

        with open('log.txt', 'w+') as textfile:
            for line in backwardlines:
                textfile.write(line + "\n")

        return redirect(url_for("login"))
    elif (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode == "004"):
        return render_template("admincheck.html")
    else:
        return render_template("error.html")


@app.route("/adminscanner")
def adminscanner():
    global backwardlines
    qrcodeReader.qrreader()
    if (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode == "004"):
        t = localtime()
        current_time = strftime("%H:%M:%S %A %x", t)
        a = current_time
        time = a[0:9]

        attendanceTime = int(time[0:2] + time[3:5])
        if attendanceTime > 1100:
            attendance = "Absent"
        else:
            attendance = "Present"

        with open("raw_log.txt", "a+") as log:
            log.write(time.strip() + "," +
                      qrcodeReader.requiredCode + "," + attendance + "\n")

        with open('raw_log.txt', 'r+') as textfile:
            backwardlines = []
            lines = textfile.readlines()
            for line in reversed(lines):
                line = line.strip()
                backwardlines.append(line)

        with open('log.txt', 'w+') as textfile:
            for line in backwardlines:
                textfile.write(line + "\n")

        return redirect(url_for("admin"))
    elif (qrcodeReader.result == "authorized") and (qrcodeReader.loginCode != "004"):
        return render_template("adminerror.html")
    else:
        return render_template("error.html")


@app.route("/admin")
def admin():

    log.logdata(qrcodeReader.requiredCode)

    return render_template("admin.html", code=log.code, name=log.name)


@app.route("/home")
def login():

    log.logdata(qrcodeReader.requiredCode)

    return render_template("login.html", time=log.time, code=log.code, designation=log.designation, name=log.name, faculty=log.faculty, cell=log.cell, bno=log.bno, bstop=log.bstop, fee=log.fee)


@app.route("/adminprint")
def adminprint():
    return render_template("adminprint.html")


@app.route("/adminprint", methods=["GET", "POST"])
def adminprintdata():
    if request.method == "POST":
        givenCode = request.form["code"]

        log.logdata(givenCode)

        if log.code != givenCode:
            return render_template("printerror.html")
        else:
            d = log.designation.lower()
            codename = log.name.replace(" ", "")

            if d == "student":
                d = "001"
            elif d == "council":
                d = "002"
            elif d == "teacher":
                d = "003"
            elif d == "admin":
                d = "004"

            ecode = str(randint(100, 1000)) + givenCode + \
                d + codename.lower()
            encrypted = encrypt(ecode)

            qr = pyqrcode.create(encrypted)
            qr.png("static/code.png", scale=20)

            qrcode = Image.open('static/code.png')
            qrcode = qrcode.resize(codeSize)
            image = None

            if (d == "001") or (d == "002"):
                makeStudentID(log.name, givenCode, qrcode, log.bno,
                              log.faculty, log.bstop, log.cell)
                return redirect(url_for("adminStudentPreview"))

            elif (d == "003"):
                makeTeacherID(log.name, qrcode, log.faculty)
                return redirect(url_for("adminTeacherPreview"))

            elif (d == "004"):
                makeAdminID(log.name, qrcode)
                return redirect(url_for("adminAdminPreview"))


@app.route("/adminStudentPreview")
def adminStudentPreview():
    return render_template("adminStudentPreview.html")


@app.route("/adminTeacherPreview")
def adminTeacherPreview():
    return render_template("adminTeacherPreview.html")


@app.route("/adminAdminPreview")
def adminAdminPreview():
    return render_template("adminAdminPreview.html")


@app.route("/searchlog")
def searchlog():
    return render_template("searchlog.html")


@app.route("/searchlog", methods=["GET", "POST"])
def searchLogData():
    if request.method == "POST":
        givenCode = request.form["code"]

        log.logdata(givenCode)

        if log.code != givenCode:
            return render_template("logerror.html")
        else:
            return redirect(url_for("showdata"))


@app.route("/log")
def showdata():
    return render_template("logdata.html", name=log.name, designation=log.designation, code=log.code, time=log.time, faculty=log.faculty, cell=log.cell, bno=log.bno, bstop=log.bstop)


@app.route("/data")
def data():

    with open("data.txt", 'r') as file:

        array = []
        finalarray = []
        content = file.readlines()
        row = 0

        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

    for x in range(len(finalarray)):
        del finalarray[x][-1]

    return render_template("data.html", li=finalarray)


@app.route("/data", methods=["GET", "POST"])
def datadata():
    if request.method == "POST":

        requiredList = []

        with open("data.txt", 'r') as file:

            array = []
            finalarray = []
            content = file.readlines()
            row = 0

            for line in content:

                row += 1
                array = line.split(",")

                array[-1] = array[-1].strip()

                finalarray.append(array)

        requiredDesignation = request.form["designation"]

        if requiredDesignation != "All":
            for x in finalarray:
                if requiredDesignation == x[2]:
                    requiredList.append(x)

            for x in range(len(finalarray)):
                del requiredList[x][-1]

            return render_template("data.html", li=requiredList)
        else:
            return redirect(url_for("data"))


@app.route("/absentees")
def absentee():

    with open("data.txt", 'r') as file:

        array = []
        finalarray = []
        content = file.readlines()
        codeli = []
        attendanceList = []
        absenteeList = []

        row = 0
        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

    for i in range(len(finalarray)):
        codeli.append(finalarray[i][0])

    for x in codeli:

        requiredCode = x

        with open('log.txt', 'r') as textfile:

            finalarray = []
            array = []
            content = textfile.readlines()
            logcode = []

            row = 0
            for line in content:

                row += 1
                array = line.split(",")

                array[-1] = array[-1].strip()

                finalarray.append(array)

            for i in range(len(finalarray)):
                logcode.append(finalarray[i][1])

            for x in range(len(logcode)):
                attendance = ""
                if requiredCode == logcode[x]:
                    time = finalarray[x][0]
                    attendance = finalarray[x][2]
                    break

        if attendance == "":
            attendance = "Absent"

        li = [requiredCode, attendance]
        attendanceList.append(li)

    for j in range(len(attendanceList)):

        if attendanceList[j][1].lower() == "absent":
            with open("data.txt", 'r') as file:

                array = []
                finalarray = []
                content = file.readlines()
                codeli = []

                row = 0
                for line in content:

                    row += 1
                    array = line.split(",")

                    array[-1] = array[-1].strip()

                    finalarray.append(array)

                for i in range(len(finalarray)):
                    codeli.append(finalarray[i][0])

                for x in range(len(codeli)):
                    if attendanceList[j][0] == codeli[x]:
                        code = finalarray[x][0]
                        name = finalarray[x][1]
                        designation = finalarray[x][2]
                        faculty = finalarray[x][3]
                        bstop = finalarray[x][4]
                        bno = finalarray[x][5]
                        cell = finalarray[x][6]
                        break

            line = code + "," + name + "," + designation + "," + \
                faculty + "," + bstop + "," + bno + "," + cell

            array = line.split(",")

            absenteeList.append(array)

    return render_template("absentee.html", li=absenteeList)


@app.route("/absentees", methods=["GET", "POST"])
def absenteedata():
    if request.method == "POST":

        requiredList = []

        with open("data.txt", 'r') as file:

            array = []
            finalarray = []
            content = file.readlines()
            codeli = []
            attendanceList = []
            absenteeList = []

            row = 0
            for line in content:

                row += 1
                array = line.split(",")

                array[-1] = array[-1].strip()

                finalarray.append(array)

        for i in range(len(finalarray)):
            codeli.append(finalarray[i][0])

        for x in codeli:

            requiredCode = x

            with open('raw_log.txt', 'r') as textfile:

                finalarray = []
                array = []
                content = textfile.readlines()
                logcode = []

                row = 0
                for line in content:

                    row += 1
                    array = line.split(",")

                    array[-1] = array[-1].strip()

                    finalarray.append(array)

                for i in range(len(finalarray)):
                    logcode.append(finalarray[i][1])

                for x in range(len(logcode)):
                    attendance = ""
                    if requiredCode == logcode[x]:
                        time = finalarray[x][0]
                        attendance = finalarray[x][2]
                        break

            if attendance == "":
                attendance = "Absent"

            li = [requiredCode, attendance]
            attendanceList.append(li)

        for j in range(len(attendanceList)):

            if attendanceList[j][1].lower() == "absent":
                with open("data.txt", 'r') as file:

                    array = []
                    finalarray = []
                    content = file.readlines()
                    codeli = []

                    row = 0
                    for line in content:

                        row += 1
                        array = line.split(",")

                        array[-1] = array[-1].strip()

                        finalarray.append(array)

                    for i in range(len(finalarray)):
                        codeli.append(finalarray[i][0])

                    for x in range(len(codeli)):
                        if attendanceList[j][0] == codeli[x]:
                            code = finalarray[x][0]
                            name = finalarray[x][1]
                            designation = finalarray[x][2]
                            faculty = finalarray[x][3]
                            bstop = finalarray[x][4]
                            bno = finalarray[x][5]
                            cell = finalarray[x][6]
                            break

                line = code + "," + name + "," + designation + "," + \
                    faculty + "," + bstop + "," + bno + "," + cell

                array = line.split(",")

                absenteeList.append(array)

        requiredDesignation = request.form["designation"]

        if requiredDesignation != "All":
            for x in absenteeList:
                if requiredDesignation == x[2]:
                    requiredList.append(x)

            return render_template("absentee.html", li=requiredList)
        else:
            return redirect(url_for("absentee"))


@app.route("/edit")
def edited():
    return render_template("edit.html")


@app.route("/edit", methods=["GET", "POST"])
def editdata():
    if request.method == "POST":

        code = request.form["code"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        designation = request.form["designation"]
        faculty = request.form["faculty"]
        bno = request.form["bno"]
        bstop = request.form["bstop"]
        cell = request.form["cell"]
        name = fname + " " + lname

        log.logdata(code)

        if log.code != code:
            return render_template("editerror.html")
        else:
            edit.editcode(code, name, designation, faculty, bstop, bno, cell)
            return redirect(url_for("edited"))


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
                        finalarray[x][1] + "," + finalarray[x][2] + "," + finalarray[x][3] + \
                        "," + finalarray[x][4] + "," + \
                        finalarray[x][5] + "," + \
                        finalarray[x][6] + "," + finalarray[x][7]
                    file.write(line + "\n")

    return redirect(url_for("delete"))


@app.route("/canteen")
def canteen():
    return render_template("canteenhome.html")


@app.route("/canteenscan")
def canteenscanner():
    global token
    qrcodeReader.qrreader()
    if (qrcodeReader.result == "authorized"):
        token = token + 1
        return redirect(url_for("canteenhome"))
    else:
        return render_template("canteenerror.html")


@app.route("/canteenhome")
def canteenhome():
    global token
    return render_template("canteen.html", token=token)


@app.route("/canteenhome", methods=["GET", "POST"])
def canteenhomedata():
    global token

    if request.method == "POST":

        momo = int(request.form["momo"])
        chowmein = int(request.form["chowmein"])
        fries = int(request.form["fries"])
        khanaSet = int(request.form["khanaSet"])
        code = qrcodeReader.requiredCode

        total = momo * 120 + chowmein * 90 + fries * 100 + khanaSet * 170

        with open("canteentoken.txt", "a+") as file:
            file.write(str(token) + "," + str(momo) + "," + str(chowmein) +
                       "," + str(fries) + "," + str(khanaSet) + "\n")

        with open('data.txt', 'r') as file:

            finalarray = []
            array = []
            content = file.readlines()
            row = 0

            for line in content:

                row += 1
                array = line.split(",")

                array[-1] = array[-1].strip()

                finalarray.append(array)

        for x in range(len(finalarray)):
            if code == finalarray[x][0]:
                break

        amount = finalarray[x][7]

        finalarray[x][7] = str(total + int(amount))

        with open('data.txt', 'w') as file:

            for j in range(len(finalarray)):
                line = finalarray[j][0] + "," + finalarray[j][1] + "," + \
                    finalarray[j][2] + "," + finalarray[j][3] + "," + \
                    finalarray[j][4] + "," + \
                    finalarray[j][5] + "," + \
                    finalarray[j][6] + "," + finalarray[j][7]

                file.write(line + "\n")

        return redirect(url_for("canteen"))


@app.route("/canteenorder")
def canteenorder():

    with open("canteentoken.txt", "r") as file:

        finalarray = []
        array = []
        content = file.readlines()
        row = 0

        for line in content:

            row += 1
            array = line.split(",")

            array[-1] = array[-1].strip()

            finalarray.append(array)

    finalorder = []

    for x in range(len(finalarray)):

        orders = []

        orders.append(finalarray[x][0])

        if finalarray[x][1] == "0":
            momoline = ""
        else:
            momoline = "Momo x" + finalarray[x][1] + ", "

        if finalarray[x][2] == "0":
            chowmeinline = ""
        else:
            chowmeinline = "Chowmein x" + finalarray[x][2] + ", "

        if finalarray[x][3] == "0":
            friesline = ""
        else:
            friesline = "Chilli Fries x" + finalarray[x][3] + ", "

        if finalarray[x][4] == "0":
            khanaline = ""
        else:
            khanaline = "Khana Set x" + finalarray[x][4] + ", "

        line = momoline + chowmeinline + friesline + khanaline

        orders.append(line)

        finalorder.append(orders)

    return render_template("canteenorder.html", li=finalorder)


@app.route("/canteenorder", methods=["GET", "POST"])
def orderdata():
    if request.method == "POST":

        token = request.form["token"]

        with open('canteentoken.txt', 'r') as file:

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

        with open('canteentoken.txt', 'w') as file:
            ctr = 1
            file.truncate(0)

        with open('canteentoken.txt', 'a+') as file:

            for x in range(len(finalarray)):
                if token != code[x]:
                    line = finalarray[x][0] + "," + \
                        finalarray[x][1] + "," + finalarray[x][2] + "," + finalarray[x][3] + \
                        "," + finalarray[x][4]
                    file.write(line + "\n")

        return redirect(url_for("canteenorder"))


if __name__ == "__main__":
    app.run(debug=True)
