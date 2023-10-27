class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    
  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    
  def withdraw(self, amount, description=''):
    if(self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return  True
    else:
      return False
      
  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    else:
       return False
      
  def get_balance(self):
    balance = 0
    for expense in self.ledger:
      balance += expense["amount"]
    return balance
    
  def transfer(self, amount, to):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + to.name)
      to.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def __str__(self) -> str:
    nameLength = len(self.name)
    startLength = round((30 - nameLength) / 2)
    firstLine = "*" * startLength + self.name + "*" * (30 - startLength - nameLength)

    def line(dictionary):
        lenOfDesc = len(dictionary["description"])
        amountStr = str('%.2f' % dictionary["amount"])
        desc = dictionary["description"]
        lenOfAmount = len(amountStr)
        if lenOfAmount > 7:
            amountStr = amountStr[:7]
            lenOfAmount = 7
        if lenOfDesc > 23:
            desc = desc[0:23]
            lenOfDesc = 23
        theLine = desc + " " * (30 - lenOfAmount - lenOfDesc) + amountStr
        return theLine
    totalAmt = '%.2f' % self.get_balance()
    return firstLine + '\n' + '\n'.join(map(line, self.ledger)) + '\n' + f'Total: {totalAmt}'

def create_spend_chart(categories):
  category_list = []
  spend_amount = []
  total_amount = 0
  percent_amount = []
  for category in categories:
      category_list.append(category.name)
      amount = 0
      for i in category.ledger:
          if i["amount"] < 0:
              amount += abs(i["amount"])
      spend_amount.append(amount)
      total_amount += amount
  for i in spend_amount:
      percent_amount= list(map(lambda amount: int((((amount / total_amount) * 10) // 1) * 10), spend_amount))
  Line = "Percentage spent by category\n"
  for value in reversed(range(0, 101, 10)):
      if value == 0:
          string = "  " + str(value) + "|"
      elif value < 100:
          string = " " + str(value) + "|"
      else:
          string = str(value) + "|"
      for i in percent_amount:
          if i >= value :
              string += " o "
          else:
              string += "   "
      Line += string + ' \n'
  dashLength = len(spend_amount) * 3 + 1
  Line += "    " + "-" * dashLength + '\n'
  longestStr = max(category_list, key=len)
  longestStrNum = len(longestStr)
  for value in range(0, longestStrNum):
      Line += "    "
      number = 1
      for category in category_list:
          if len(category) > value:
              Line += (" " + category[value] + " ")
              if number == len(category_list):
                  Line+=" "
          else:
              Line += "   "
          number+=1
      Line += "\n"
  Line = Line.rstrip()
  Line += "  "
  return Line