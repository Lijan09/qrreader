deletecode = "6842"

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

# print(finalarray)
# print(code)

with open('data.txt', 'w') as file:
    file.truncate(0)

with open('data.txt', 'a+') as file:

    for x in range(len(finalarray)):
        if deletecode != code[x]:
            line = finalarray[x][0] + "," + \
                finalarray[x][1] + "," + finalarray[x][2]
            file.write(line + "\n")
