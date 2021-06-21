

class A:
    def __init__(self):
        self.a = 24
    def __add__(self, other):
        self.a += other

test = A()
test.__add__(2)
print(test.a)

