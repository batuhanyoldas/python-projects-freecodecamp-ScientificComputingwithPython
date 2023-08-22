class Category:
  #Constructor method
  def __init__(self, name):
    self.name = name
    self.ledger = []
  #String representation  
  def __str__(self):
    title = self.name.center(30,"*") + "\n"
    transaction_text = ""
    for transaction in self.ledger:
      transaction_text += transaction["description"][0:23].ljust(23) + ('{:.2f}'.format(transaction["amount"])).rjust(7) + "\n"
    balance = self.get_balance()
    balance_text = "Total: " + str(balance)
    return title + transaction_text + balance_text
  #Methods
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
  def withdraw(self, amount, description = ""):
    has_fund = self.check_funds(amount)
    if has_fund:
      balance = self.get_balance()
      if balance >= amount: 
        self.ledger.append({"amount": -amount, "description": description})
    return has_fund
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction["amount"]
    return balance
  def transfer(self, amount, category):
    deposit_description = "Transfer from " + self.name
    withdraw_description = "Transfer to " + category.name
    category.deposit(amount,deposit_description)
    return self.withdraw(amount, withdraw_description)
  def check_funds(self,amount):
    balance = self.get_balance()
    if balance >= amount:
      return True
    else:
      return False

def create_spend_chart(categories):
  top_text = "Percentage spent by category\n"
  #Top part of the graph
  percentage = [i*10 for i in range(11)]
  percentage.sort(reverse=True)
  percentage_lines = []
  for line in percentage:
    percentage_lines.append(str(line).rjust(3) + "|" +" ")
  spendings = []
  for category in categories:
    total_spending_per_category = 0
    for transaction in category.ledger:
      if transaction["amount"] < 0:
        total_spending_per_category += transaction["amount"]
    spendings.append(total_spending_per_category)
  total_spending = sum(spendings)
  for spending in spendings:
    percent = (spending / total_spending) * 100 //10
    i = 0
    for line in percentage_lines:
      if i >= (10-percent):
        percentage_lines[i] = line + "o  "
      else:
        percentage_lines[i] = line + "   "
      i += 1  
  #Seperation lines
  mid_lines = "    "+ "-"*((len(categories)*3)+1)
  #Bottom part of the graph (labels)
  max_name_length = 0
  for category in categories:
    if max_name_length < len(category.name):
      max_name_length = len(category.name)
  bottom_lines = []
  names = []
  for category in categories:
    names.append(category.name.ljust(max_name_length))
  for x in range(max_name_length):
    bottom_lines.append("     ")
    for name in names:
      bottom_lines[x] += name[x] + "  "
  return top_text + '\n'.join(percentage_lines)+ "\n" + mid_lines + "\n" + '\n'.join(bottom_lines)