class CoffeeMachine:
    def __init__(self):
        self.water = 400  # количество воды в мл
        self.milk = 540  # количество молока в мл
        self.coffee_beans = 120  # количество кофейных зерен в граммах
        self.sugar = 50  # количество сахара в кубиках
        self.money = 550  # количество денег в рублях
        self.cups = 10  # количество стаканчиков

    def remaining(self):
        print(f"The coffee machine has: {self.water} of water, {self.milk} of milk, {self.sugar} of sugar,{self.money} of money, {self.coffee_beans} of coffee beans, {self.cups} of cups")

    def buy(self):
        choice = input("What do you want to buy?\n1 - espresso\n2 - latte\n3 - cappuccino\n")
        if choice == "1":
            self.make_coffee(250, 0, 16, 0, 10, 1)
        elif choice == "2":
            self.make_coffee(350, 75, 20, 3, 25, 1)
        elif choice == "3":
            self.make_coffee(200, 100, 12, 2, 20, 1)
        else:
            print("Invalid choice!")

    def make_coffee(self, water_needed, milk_needed, coffee_beans_needed, sugar_needed, cost, cups_needed):
        if self.water >= water_needed \
                and self.milk >= milk_needed \
                and self.coffee_beans >= coffee_beans_needed \
                and self.sugar >= sugar_needed \
                and self.cups >= cups_needed:
            print("Making coffee! Enjoy your drink!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= coffee_beans_needed
            self.money += cost
            self.cups -= cups_needed
        else:
            print("Sorry, not enough ingredients to make coffee.")

    def fill(self):
        self.water += int(input("How much water do you want to add?\n"))
        self.milk += int(input("How much milk do you want to add?\n"))
        self.coffee_beans += int(input("How much coffee beans do you want to add?\n"))
        self.sugar += int(input("How much sugar do you want to add?\n"))
        self.money += int(input("How much money do you want to add?\n"))
        self.cups += int(input("How much cups do you want to add?\n"))

    def take(self):
        print(f"Here is {self.money} RUB")
        self.money = 0

    def start(self):
        while True:
            action = input("Choose action: buy, fill, take, remaining, exit\n")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break
            else:
                print("Invalid action!")

machine = CoffeeMachine()
machine.start()
