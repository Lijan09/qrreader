with open('raw_log.txt', 'r+') as textfile:
    backwardlines = []
    lines = textfile.readlines()
    for line in reversed(lines):
        line = line.strip()
        backwardlines.append(line)

with open('log.txt', 'w+') as textfile:
    for line in backwardlines:
        textfile.write(line + "\n")
