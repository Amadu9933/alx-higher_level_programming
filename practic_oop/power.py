class Power:

    def pow(self, x, n):

        if n == 0:

            return 1

        if n == 1:

            return x

        return x * self.pow(x, n-1)



power = Power()

print(power.pow(2, 3))  # 8

print(power.pow(3, 4))  # 81

print(power.pow(5, 2))  # 25

print(power.pow(10, 0))  # 1

print(power.pow(2, 8))  # 256
