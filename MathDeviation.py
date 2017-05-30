import math


class MathDeviation:
    def solve_ABC(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"

if __name__ == '__main__':
    mathDeviation = MathDeviation()

    while True:
        a = int(input("a "))
        b = int(input("b "))
        c = int(input("c "))
        result = mathDeviation.solve_ABC(a, b, c)
        print(result)