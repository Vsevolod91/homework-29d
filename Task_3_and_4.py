class MyInt():
    isdigit_ = True

    def __init__(self, num):
        self.num = self.verify(num)

    def __repr__(self):
        return f"{object.__class__(self)}: {self.num}"

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return MyInt(self.num + self.verify(other))

    def __radd__(self, other):
        return MyInt(self.num + self.verify(other))

    def __iadd__(self, other):
        self.num = self.num + self.verify(other)
        return self

    def __sub__(self, other):
        return MyInt(self.num - self.verify(other))

    def __rsub__(self, other):
        return MyInt(self.num - self.verify(other))

    def __isub__(self, other):
        self.num = self.num - self.verify(other)
        return self

    def __mul__(self, other):
        return MyInt(self.num * self.verify(other))

    def __rmul__(self, other):
        return MyInt(self.num * self.verify(other))

    def __imul__(self, other):
        self.num = self.num * self.verify(other)
        return self

    def __truediv__(self, other):
        return MyInt(self.num / self.verify(other))

    def __rtruediv__(self, other):
        return MyInt(self.num / self.verify(other))

    def __itruediv__(self, other):
        self.num = self.num / self.verify(other)
        return self

    def __eq__(self, other):
        return self.num == self.verify(other)

    def __ne__(self, other):
        return self.num != self.verify(other)

    def __lt__(self, other):
        return self.num < self.verify(other)

    def __le__(self, other):
        return self.num <= self.verify(other)

    def __gt__(self, other):
        return self.num > self.verify(other)

    def __ge__(self, other):
        return self.num >= self.verify(other)


    @classmethod
    def verify(cls, num):
        if isinstance(num, str):
            if cls.isdigit_ != num.isdigit():
                raise TypeError(f"Вместо {num} ведите число")
            else:
                return int(num)
        elif isinstance(num, (int, float)):
            return num

a = MyInt(100)

a = a + 10
a = a + "10"
a = 10 + a
a = "10" + a
a += 10
a += "10"
print(a)
print(type(a))

a = a - 10
a = a - "10"
a = 10 - a
a = "10" - a
a -= 10
a -= "10"
print(a)
print(type(a))

a = a * 10
a = a * "10"
a = 10 * a
a = "10" * a
a *= 10
a *= "10"
print(a)
print(type(a))

b = MyInt(10)
c = MyInt(10)

a = a / 10
a = a / "10"
a = 1000000000 / b
a = "1000000000" / c
a /= 10
a /= "10"
print(a)
print(type(a))

y = MyInt(100)
y = 2*y + 10 + "10" - 10 - 10
print(y)
print(type(y))


x = MyInt(10)

print(x > "100")
print(x > 100)
print(x < 100)
print(x > "100")
print(x >= 10)
print(x <= "100")
print(x >= "100")
print(x <= "5")
print(x >= 10)
print(x <= "100")
print(x >= "10")
print(x <= "10")



