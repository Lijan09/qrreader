from PIL import Image, ImageDraw, ImageFont

codeSize = (64, 64)
busNoFont = ImageFont.truetype('arial.ttf', 50)
font = ImageFont.truetype('arial.ttf', 12)


def makeStudentID():

    name = 'Aashish Kadel'

    # Image.open('static/code.png')
    image = Image.open('static/student.png')

    draw = ImageDraw.Draw(image)

    draw.text((180, 118), 'H', (0, 0, 0), font=busNoFont)
    draw.text((76, 179), name, (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 18))
    draw.text((124, 209), '3513', (0, 0, 0), font=font)
    draw.text((140, 235), '+2 Science', (0, 0, 0), font=font)
    draw.text((125, 261), 'Putalisadak', (0, 0, 0), font=font)
    draw.text((100, 287), '9840030767', (0, 0, 0), font=font)
    draw.text((118, 313), "August 2050", (0, 0, 0), font=font)

    # image.paste('static/code.png', (59, 298))

    image.save('static/studentSave.png')

    image1 = Image.open('static/studentSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


def makeTeacherID():
    name = 'Raj Kumar Maharjan'
    width = int
    height = int

    # Image.open('static/code.png')
    image = Image.open('static/teacher.png')

    draw = ImageDraw.Draw(image)

    if len(name) >= 18:
        width = 88
        height = 224
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) >= 15:
        width = 91
        height = 224
        draw.text((width, height), name, (0, 0, 0), font=font)
    elif len(name) >= 13:
        width = 93
        height = 224
        draw.text((width, height), name, (0, 0, 0), font=font)
    else:
        width = 102
        height = 224
        draw.text((width, height), name, (0, 0, 0), font=font)

    draw.text((105, 236), 'faculty', (0, 0, 0), font=font)

    # image.paste('static/code.png', (58, 254))

    image.save('static/teacherSave.png')

    image1 = Image.open('static/teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


def makeAdminID():
    name = 'Faisal Ahvbskdbvsd'
    width = int
    height = int

    # Image.open('static/code.png')
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

    # image.paste('static/code.png', (58, 254))

    image.save('static/adminSave.png')

    image1 = Image.open('static/adminSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


# makeStudentID()
makeAdminID()
# makeTeacherID()
