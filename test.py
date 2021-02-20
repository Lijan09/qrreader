# --- Progoram to test the formatting of info on the templates. Please don't delete. ---


from PIL import Image, ImageDraw, ImageFont

codeSize = (64, 64)
busNoFont = ImageFont.truetype('arial.ttf', 50)
font = ImageFont.truetype('arial.ttf', 11)


def makeStudentID(name, code, bno, faculty, bstop, cell):

    image = Image.open('student.png')

    draw = ImageDraw.Draw(image)

    draw.text((156, 102), bno, (0, 0, 0), font=busNoFont)
    draw.text((64, 165), name, (0, 0, 0),
              font=ImageFont.truetype('arial.ttf', 14))
    draw.text((108, 188), code, (0, 0, 0), font=font)
    draw.text((122, 212), faculty, (0, 0, 0), font=font)
    draw.text((109, 235), bstop, (0, 0, 0), font=font)
    draw.text((87, 258), cell, (0, 0, 0), font=font)
    draw.text((102, 282), "August 2050", (0, 0, 0), font=font)

    # image.paste(qrcode, (59, 298))

    image.save('studentSave.png')

    image1 = Image.open('studentSave.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')


def makeTeacherID(name, faculty):
    width = int
    height = int

    image = Image.open('teacher.png')

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

    draw.text((105, 236), faculty, (0, 0, 0), font=font)

    # image.paste(qrcode, (58, 254))

    image.save('teacherSave.png')

    image1 = Image.open('teacherSave.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')


def makeAdminID(name):
    width = int
    height = int

    image = Image.open('admin.png')

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

    # image.paste(qrcode, (58, 254))

    image.save('adminSave.png')

    image1 = Image.open('adminSave.png')
    im1 = image1.convert('RGB')
    im1.save('printing.pdf')


# makeStudentID('Aashish Kadel', '3513', 'H',
#               '2 Science', 'Putalisadak', '9840030767')
# makeTeacherID('THIKTHK thikthik', '+2 Science')
# makeAdminID('Santosh Siwakoti')
