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

    draw.text((156, 102), "?", (0, 0, 0), font=busNoFont)
    draw.text((64, 165), "Aashish Kadel", (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 14))
    draw.text((108, 188), "3513", (0, 0, 0), font=font)
    draw.text((122, 212), "[Programme]", (0, 0, 0), font=font)
    draw.text((109, 235), "[Bus Stop]", (0, 0, 0), font=font)
    draw.text((87, 258), "[Cell]", (0, 0, 0), font=font)
    draw.text((102, 282), "August 2050", (0, 0, 0), font=font)

    image.paste(code, (59, 298))

    image.save('studentSave.png')


def makeTeacherID():
    global code

    image = Image.open('teacher.png')

    draw = ImageDraw.Draw(image)

    draw.text((88, 224), "Prakash Shrestha", (0, 0, 0), font=font)
    draw.text((109, 236), "[Faculty]", (0, 0, 0), font=font)

    image.paste(code, (58, 254))

    image.save('teacherSave.png')

    image1 = Image.open('teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')


def makeAdminID():
    global code

    image = Image.open('admin.png')

    draw = ImageDraw.Draw(image)

    draw.text((88, 224), "Faisal Ahmed", (0, 0, 0), font=font)
    draw.text((109, 236), "[Office]", (0, 0, 0), font=font)

    image.paste(code, (58, 254))

    image.save('adminSave.png')


# makeStudentID()
# makeTeacherID()
makeAdminID()
