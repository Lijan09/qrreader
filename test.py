# fuck aashish
import log

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

print(absenteeList)
