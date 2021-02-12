from PIL import Image, ImageDraw, ImageFont


busNoFont = ImageFont.truetype('arial.ttf', 50)
font = ImageFont.truetype('arial.ttf', 11)
code = Image.open('code.png')
codeSize = (64, 64)
code = code.resize(codeSize)


def makeStudentID():
    global code

    image = Image.open('student.png')

    draw = ImageDraw.Draw(image)

    draw.text((120, 60), "?", (0, 0, 0), font=busNoFont)
    draw.text((35, 121), "Aashish Kadel", (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 14))
    draw.text((74, 144), "3513", (0, 0, 0), font=font)
    draw.text((89, 166), "[Programme]", (0, 0, 0), font=font)
    draw.text((76, 189), "[Bus Stop]", (0, 0, 0), font=font)
    draw.text((55, 210), "[Cell]", (0, 0, 0), font=font)
    draw.text((70, 233), "August 2050", (0, 0, 0), font=font)

    image.paste(code, (27, 246))

    image.save('studentSave.png')


def makeTeacherID():
    global code

    image = Image.open('teacher.png')

    draw = ImageDraw.Draw(image)

    draw.text((52, 180), "Prakash Shrestha", (0, 0, 0), font=font)
    draw.text((80, 192), "[Faculty]", (0, 0, 0), font=font)

    image.paste(code, (27, 205))

    image.save('teacherSave.png')

    image1 = Image.open('teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')


def makeAdminID():
    image = Image.open('admin.png')

    draw = ImageDraw.Draw(image)

    draw.text((60, 180), "Faisal Ahmed", (0, 0, 0), font=font)
    draw.text((80, 192), "[Office]", (0, 0, 0), font=font)

    image.save('adminSave.png')


# makeStudentID()
makeTeacherID()
# makeAdminID()
