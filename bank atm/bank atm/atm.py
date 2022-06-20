class Atm:
  """
    blueprint of atm
  """

  def __init__(self, cardnumber, pin):
    self.cardnumber = cardnumber
    self.pin = pin

  def check_balance(self):
    print("Your current balance is 10000000")

  def withdrawl(self,amount):
    withdrawl_amount = 10000000 - amount
    print("you have withdrawn amount"+(amount))

def main():
      card_number=input("insert your card number-")
      pin_number=input("insert your card number-")

      user=Atm(car_number, pin_number)

      print("1.Balance inquiry  2.Withdrawl")
      activity=int(input("enter activity number="))

      if(activity==1):
        user.check_balance()
      elif(activity==2):
        amount=int(input("enter the amount-"))
        user.withdrawl(amount)
      else:
        print("Enter the valid number-")    
  
main()