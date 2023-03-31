class ATM:
    last_id = 0
    all_ATMs = []

    @classmethod
    def count_ATMs(cls):
        print(len(cls.all_ATMs))

    def __init__(self):
        self.id = ATM.last_id
        self._total = 0
        ATM.last_id += 1
        ATM.all_ATMs.append(self)

    def deposit(self, money):
        self._total += money
        print(f'a{money}')

    def withdraw(self, money):
        self._total -= money
        print(f'aa{money}')


a = ATM()
a1 = ATM()
a2 = ATM()

print(a.id)
print(a1.id)
print(a2.id)

ATM.count_ATMs()
