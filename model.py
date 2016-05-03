data = open("example.txt")
probabilities=data.readlines()
while True:
    for line in probabilities:
        print(line.strip())
        r = raw_input()
    if r == 'n':
        break
