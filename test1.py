from PIL import Image, ImageDraw, ImageFont

codeSize = (64, 64)
busNoFont = ImageFont.truetype('arial.ttf', 50)
font = ImageFont.truetype('arial.ttf', 11)


def makeStudentID():

    name = 'Aashish Kadel'

    # Image.open('static/code.png')
    image = Image.open('static/student.png')

    draw = ImageDraw.Draw(image)

    draw.text((152, 95), 'H', (0, 0, 0), font=busNoFont)
    draw.text((68, 155), name, (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 14))
    draw.text((108, 176), '3513', (0, 0, 0), font=font)
    draw.text((122, 196), '+2 Science', (0, 0, 0), font=font)
    draw.text((109, 219), 'Putalisadak', (0, 0, 0), font=font)
    draw.text((89, 240), '9840030767', (0, 0, 0), font=font)
    draw.text((104, 260), "August 2050", (0, 0, 0), font=font)

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

    image.paste('static/code.png', (58, 254))

    image.save('static/teacherSave.png')

    image1 = Image.open('static/teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


def makeAdminID():
    name = 'Faisal Ahmed'
    width = int
    height = int

    # Image.open('static/code.png')
    image = Image.open('static/admin.png')

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
    draw.text((100, 236), "[Admin Office]", (0, 0, 0), font=font)

    image.paste('static/code.png', (58, 254))

    image.save('static/adminSave.png')

    image1 = Image.open('static/adminSave.png')
    im1 = image1.convert('RGB')
    im1.save('static/printing.pdf')


makeStudentID()
# makeAdminID()
# makeStudentID()
