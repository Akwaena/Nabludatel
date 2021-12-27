work = 504
counter = 0
while work > 0:
    if counter % 3 == 0:
        work -= 10
    elif counter % 10 == 0:
        work += 15
    counter += 1
    work -= 1

print(counter)
