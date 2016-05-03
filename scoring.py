import math
from subprocess import Popen, PIPE

test_data = open("data.txt")
p = Popen(["python", "-u", "model.py"], stdin=PIPE, stdout=PIPE)
score = 0
c = 1
for line in test_data:
    row_values = line.split(",")
    row_values = [int(a) for a in row_values]
    row_score = 0
    for value in row_values:
        probabilities = p.stdout.readline()
        probabilities = probabilities.split(",")
        probabilities = [float(a) for a in probabilities]
        if sum(probabilities) <= 1.1:
            row_score += math.log(probabilities[value])
        else:
            print "holy shmoly"
            break
        print>>p.stdin, value
    print row_score
    score += row_score
    print c
    c += 1
print>>p.stdin, "n\n"
print("total score: ", score)
