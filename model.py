probabilities = ["0.99"]
probabilities.extend([str(0.01/99) for i in range(0, 99)])
while True:
    print(','.join(probabilities).strip('[]'))
    r = raw_input()
    if r == 'n':
        break
