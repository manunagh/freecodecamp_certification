class Category:
    def __init__(self, name):
        self.name= name
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount" : amount, "description" : description})
    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount" : -amount, "description" : description})
        return True
    def get_balance(self):
        balance = 0
        for dictionary in self.ledger:
            balance += dictionary["amount"]
        return balance
    def transfer(self, amount, Category):
        if not self.withdraw(amount, f"Transfer to {Category.name}"):
            return False
        Category.deposit(amount, f"Transfer from {self.name}")
        return True
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True
    def __str__(self):
        items = ""
        title = self.name.center(30, "*") + "\n"
        for dictionary in self.ledger:
            desc = dictionary["description"]
            amount = f"{dictionary['amount']:.2f}"
            desc_resume = f"{desc[:23]:<23}{amount:>7}\n"
            items += desc_resume
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    for category in categories:
        for dictionary in category.ledger:
            if dictionary["amount"] < 0:
                total_spent += - dictionary["amount"]

    percentages = []
    for category in categories:
        spent = 0
        for dictionary in category.ledger:
            if dictionary["amount"] < 0:
                spent += -dictionary["amount"]
        percent = int((spent / total_spent) * 100 // 10) * 10
        percentages.append(percent)

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -1):
        if i % 10 == 0:
            chart += f"{i:>3}| "
            for percent in percentages:
                if percent >= i:
                    chart += "o  "
                else:
                    chart += "   "
            chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_len = max([len(cat.name) for cat in categories])
    for i in range(max_len):
        chart += "     "  
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
    return chart
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))
