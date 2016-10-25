#Cabin Rental

class CabinRental:
    
    def __init__(self, cnum, num_days):
        self.setCabinNumber(cnum)
        self.setWeekdayRate(cnum)
        self.setNumOfDays(num_days)
    
    #Mutator methods
    def setCabinNumber(self,cnum):
        if cnum in ('CR1', 'CR2', 'CR3', 'CR4', 'CR5', 'CR6'):
            self.__cabin_number = cnum
        else:
            raise ValueError ("Cabin number is invalid")
            
    def setWeekdayRate(self,cnum):
        if cnum in ('CR1', 'CR2', 'CR3'):
            self.__weekday_rental_rate = 250.0
        elif cnum in ('CR4', 'CR5', 'CR6'):
            self.__weekday_rental_rate = 400.0
            
    def setNumOfDays(self, num_days):
        self.__num_of_weekdays=num_days
        
    #Accessor Methods
    def getCabinNumber(self):
        return self.__cabin_number
        
    def getWeekdayRate(self):
        return self.__weekday_rental_rate
        
    def getNumOfDays(self):
        return self.__num_of_weekdays
    
    #Calculate Charge
    def calculateCharge(self):
        weekday_charge= self.getNumOfDays() * self.getWeekdayRate()
        return weekday_charge
        
    #String Method
    def __str__(self):
            
            cabin_string = "Cabin Number: %s\n" %self.getCabinNumber() +\
            "Weekday Rate: %.2f\n" %self.getWeekdayRate() +\
            "Number of days: %d\n" %self.getNumOfDays() +\
            "Charge: %.2f" %self.calculateCharge()
        
            return cabin_string
        