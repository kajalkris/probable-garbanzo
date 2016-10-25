#Holiday CabinRental

from CabinRental import CabinRental

class HolidayCabinRental(CabinRental):
    
    def __init__(self, cnum, num_wkdays, num_holidays):
        super().__init__(cnum,num_wkdays)
        self.setHolidayRate()
        self.setNumOfHolidays(num_holidays)
        
    #Mutator Methods
    def setHolidayRate(self):
        self.__holiday_rental_rate = super().getWeekdayRate() + 150.0
        
    def setNumOfHolidays(self, num_holidays):
        self.__number_of_holidays = num_holidays
        
    #Accessor Methods
    def getHolidayRate(self):
        return self.__holiday_rental_rate
        
    def getNumOfHolidays(self):
        return self.__number_of_holidays
        
    #Calculate Charge    
    def calculateCharge(self):
        total_charge= super().calculateCharge() + self.getNumOfHolidays() * self.getHolidayRate()
        return total_charge
        
    #String Method
    def __str__(self):
        holiday_string = super().__str__() + "\n" +\
        "Number of Holiday: %d\n" %self.getNumOfHolidays() +\
        "Holiday Rate: %.2f\n" %self.getHolidayRate() +\
        "Total Charge: %.2f" %self.calculateCharge()
        
        return holiday_string