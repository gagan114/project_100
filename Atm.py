class atm(object):
  """
    blueprint for atm
  """

  def __init__(self, company, CashWidhdrawl, BalanceEnquriy ):
    self.CashWidhdrawl = CashWidhdrawl
    self.BalanceEnquriy = BalanceEnquriy
    self.company = company
    

  def atm_card_number(self):
    print("014255672")

  def atm_pin_number(self):
    print("1245")

  

IDBI = atm( "contact to bank", "IDBI", 10000)

print(IDBI.CashWidhdrawl)
