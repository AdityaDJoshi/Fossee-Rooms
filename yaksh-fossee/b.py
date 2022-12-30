from mimetypes import init


class LinearEquation:

    def __init__(self, a=0, b=0, c=0) -> None:
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __add__(self, eq):
        return LinearEquation(self.a+eq.a, self.b+eq.b, self.c+eq.c)

    def __str__(self) -> str:
        ans = ""
        ans += str(self.a)
        ans += 'x'
        if self.b < 0:
            ans += ' - '
            self.b = -self.b
        else:
            ans += ' + '
        ans += str(self.b)
        ans += 'y = '
        ans += str(self.c)
        return ans

    def __repr__(self) -> str:
        ans = ""
        ans += str(self.a)
        ans += 'x'
        if self.b < 0:
            ans += ' - '
            self.b = -self.b
        else:
            ans += ' + '
        ans += str(self.b)
        ans += 'y = '
        ans += str(self.c)
        return ans

    def isparallel(self, eqn):
        det = (self.a*eqn.b)-(eqn.a*self.b)
        if det == 0:
            return True
        return False

    def intersects(self, eqn):
        det = (self.a*eqn.b)-(eqn.a*self.b)
        if det == 0:
            return False
        return True

    def overlaps(self, eqn):
        return True


eqn1 = LinearEquation(1, 1, 0)
eqn2 = LinearEquation(2, 3, 4)
# eq = LinearEquation(3, 4, 4)
eqn3 = eqn1+eqn2
print(eqn3.a)
print(eqn3.b)
print(eqn3.c)
eqn = LinearEquation(2, -3, 5)
print(str(eqn))
