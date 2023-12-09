from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# We are going to rebuild our coffee shop, but now with OOP!

# 1. Print the report
# 2. Check if resources are sufficient
# 3. Process coins
# 4. Check transaction successful?
# 5. Make coffee!

my_money_mcahine = MoneyMachine()
coffee_maker = CoffeeMaker()
# This is why OOP is awesome. We don't really have to care how it is all implemented behind the scenes. We import and use the vars and methods.
coffee_maker.report()
my_money_mcahine.report()

# We don't care how report works, just read the docs, find the method we want, and trust it will work
