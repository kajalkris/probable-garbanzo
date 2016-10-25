#Program to test CabinRental Hierarchy

from CabinRental import CabinRental
from HolidayCabinRental import HolidayCabinRental

def main():
    
    #Good Cabins
    try:
        #CabinRental objects
        cr1 = CabinRental("CR1", 2)
        cr2 = CabinRental("CR2", 1)
        
        #HolidayCabinRental objects
        hcr3 = HolidayCabinRental("CR3", 2,3)
        hcr4 = HolidayCabinRental("CR4", 1,4)
        
    
    except ValueError as ve:
        print(ve)
        
    else:
    #Create a list of CabinRental objects
        cabin_list=[cr1, cr2, hcr3, hcr4]
        #Display cabin details
        print()
        for cabin in cabin_list:
            print(cabin)
            print()
    
    #Error Cabins
    try:
        #CabinRental objects
        cr7 = CabinRental("CR7", 2)
    
    except ValueError as ve:
        print(ve)
        
    else:
    #Create a list of CabinRental objects
        cabin_list=[cr7]
        #Display cabin details
        print()
        for cabin in cabin_list:
            print(cabin)
            print()
    
main()