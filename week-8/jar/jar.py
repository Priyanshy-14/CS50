class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 :
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("Too many cookies")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not enough cookies")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


def main():
    jar = Jar(6)
    print("Initial jar:", jar)
    print("Capacity:", jar.capacity)

    jar.deposit(3)
    print("After depositing 3:", jar)

    jar.withdraw(1)
    print("After withdrawing 1:", jar)

    print("Current size:", jar.size)


if __name__ == "__main__":
    main()