class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < self.n:
            result = self.a ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

gen = PowerGenerator(2, 5)
for value in gen:
    print(value)