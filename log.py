name = str
designation = str
code = ""
time = ""
faculty = str
bstop = str
bno = str
cell = str


def logdata(givenCode):
    global name, designation, time, code, faculty, bstop, bno, cell

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
            if givenCode == logcode[x]:
                time = finalarray[x][0]
                break

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
            if givenCode == codeli[x]:
                code = finalarray[x][0]
                name = finalarray[x][1]
                designation = finalarray[x][2]
                faculty = finalarray[x][3]
                bstop = finalarray[x][4]
                bno = finalarray[x][5]
                cell = finalarray[x][6]
                break
    
    if time == "":
        time = "Nil"

    return name, designation, code, time, faculty, bstop, bno, cell


name = name
designation = designation
code = code
time = time
faculty = faculty
bstop = bstop
bno = bno
cell = cell
