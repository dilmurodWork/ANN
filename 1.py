import numpy as np


def act(x) -> int:
    return 0 if x < 0.5 else 1


def go(attr: int, smk: int, house: int) -> bool:
    x = np.array([attr, smk, house])
    w11 = [0, 0.3, 0.3]
    w12 = [1, 0.4, 0.4]

    weight1 = np.array([w11, w12])  # matrix 2x3
    weight2 = np.array([-1, 1])     # vector 1x2

    sum_hidden = np.dot(weight1, x)

    out_hidden = np.array([act(x) for x in sum_hidden])

    sum_end = np.dot(weight2, out_hidden)

    y = act(sum_end)
    return bool(y)


attr = int(input("Он крассив ?: "))
smk = int(input("Вредные прывички?: "))
house = int(input("Квартиры имеет?: "))

res = go(attr, smk, house)

if res:
    print("Ты прикольный")
else:
    print("Созвонимся")
