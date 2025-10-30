class Purse:
    def __init__(self,name="no name",money=0.00,volute="USD"):
        self.money = money
        self.name = name.lower()
        self.volute = volute

    def info(self):
        print(f"""{"-"*40}
name: {self.name} \nmoney: {self.money} {self.volute}.
{"-"*40}""")

    def top_up_balance(self,howmoney):
        if howmoney < 0:
            raise ValueError("иди погуляй дружок, будешь бабусю так наёбывать с своим минусом(-)")
        else:
            self.money += howmoney

    def top_down_balance(self,howmoney):
        if self.money < howmoney:
            raise ValueError("пошёл на х*й, нет на этом кошильке столько ")
        else:
            self.money -= howmoney

    def __del__(self):
        print(f"хуйня все ваши денежки спиздила. {self.name}")


y = Purse("steev", 20)
x = Purse("jobs", 10)
x.top_up_balance(1000)
y.info()
x.info()


