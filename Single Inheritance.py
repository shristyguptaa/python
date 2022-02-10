# A python program showing single inheritance in which two sub classes are derived from a single base class

# single inheritance
class Bank(object):
    cash = 100000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    pass

class StateBank(Bank):
    cash = 20000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)

a = AndhraBank()
a.available_cash()

s = StateBank()
s.available_cash()
