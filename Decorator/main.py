class Coffee:
    description = "unknown"

    def cost(self):
        pass

    def get_description(self):
        return self.description


class Cappuccino(Coffee):
    def __init__(self):
        self.description = "cappuccino"

    def cost(self):
        return 75


class Latte(Coffee):
    def __init__(self):
        self.description = "latte"

    def cost(self):
        return 89


class Americano(Coffee):
    def __init__(self):
        self.description = "americano"

    def cost(self):
        return 58


class Espresso(Coffee):
    def __init__(self):
        self.description = "espresso"

    def cost(self):
        return 100


class Decorator(Coffee):
    pass


class Milk(Decorator):
    def __init__(self, coffee1):
        self.coffee1 = coffee1

    def get_description(self):
        return self.coffee1.get_description() + ", milk"

    def cost(self):
        return 15 + self.coffee1.cost()


class Syrop(Decorator):
    def __init__(self, coffee1):
        self.coffee1 = coffee1

    def get_description(self):
        return self.coffee1.get_description() + ", syrop"

    def cost(self):
        return 25 + self.coffee1.cost()


class Sugar(Decorator):
    def __init__(self, coffee1):
        self.coffee1 = coffee1

    def get_description(self):
        return self.coffee1.get_description() + ", sugar"

    def cost(self):
        return 5 + self.coffee1.cost()


if __name__ == "__main__":
    coffee2 = Latte()
    print(coffee2.get_description(), "-", coffee2.cost())

    coffee3 = Cappuccino()
    coffee3 = Milk(coffee3)
    coffee3 = Sugar(coffee3)
    print(coffee3.get_description(), "-", coffee3.cost())
