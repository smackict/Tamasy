
import random

class TAX_CALCULATOR:
    def __init___(self):
        self.months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    def tax_diff(self, expected_tax, actual_tax):
        return actual_tax - expected_tax
    
    def taxgrowth_rate(self, previousMonthTax):
        return self.tax_diff() / previousMonthTax * 100
    
    def rnd_values(self):
        val = random.randint(10,50)        
        return abs(val)

