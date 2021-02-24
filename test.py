requiredData = 0
code = "3519"
name = "Lijen"
designation = ""
faculty = ""
bstop = ""
bno = ""
cell = ""
edited = False

with open('data.txt', 'r') as file:

    finalarray = []
    controlarray = []
    array = []
    content = file.readlines()
    x = 0
    row = 0

    for line in content:

        row += 1
        array = line.split(",")

        array[-1] = array[-1].strip()

        finalarray.append(array)

for x in range(len(finalarray)):
    if code == finalarray[x][0]:
        break

if name != "":
    finalarray[x][1] = name
    edited = True

if designation != "":
    finalarray[x][2] = designation
    edited = True

if faculty != "":
    finalarray[x][3] = faculty
    edited = True

if bstop != "":
    finalarray[x][4] = bstop
    edited = True

if bno != "":
    finalarray[x][5] = bno
    edited = True

if cell != "":
    finalarray[x][6] = cell
    edited = True

if edited:

    with open('data.txt', 'w') as file:
        i = []

        for j in range(len(finalarray)):
            line = code + "," + finalarray[j][1] + "," + \
                finalarray[j][2] + "," + finalarray[j][3] + "," + \
                finalarray[j][4] + "," + \
                finalarray[j][5] + "," + finalarray[j][6]

            file.write(line + "\n")

print(finalarray)
print(controlarray)
print(edited)
print(name)