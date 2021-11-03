short, long, steps = int(input()), int(input()), int(input())

# print(steps // (short + long) * 2)

# print(steps // (short + long) * 2 + 1 if long > steps % (short + long) else steps // (short + long) * 2)

if steps % (short + long):
    print(steps // (short + long) * 2 + 1)
else:
    print(steps // (short + long) * 2)
