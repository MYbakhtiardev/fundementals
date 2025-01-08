# import mymodule as mm
from mymodule import calculateInterest, calculateTotal as ci #can be renamed as one variable
import utilities.utility as ut
from utilities.utility import calculateNumTotal

print(ci(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

interest = ci(10000, 10, 5)
print(f"Interest is  {interest:.2f}")

interest = ut.calculateSimpleInterest(10000, 10, 5)
print("Interest is  %.2f", interest)