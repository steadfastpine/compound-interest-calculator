# Program Name:		Compound Interest Calculator
# Program Author:	Scott Forsberg
# Creation Date:	2019-06-14
# Python Version:	3.7.1

# compound interest formula:
#
# T = P[ 1 + (r/c) ]^cy
#
# T = total
# P = principle
# r - rate
# c = compounds_per_year
# y = years



class CompoundInterest:
    
    def __init__(self,principle,rate,compounds_per_year,years):
        
        self.principle=principle
        self.rate=rate
        self.compounds_per_year=compounds_per_year
        self.years=years
        self.total=float(principle*( 1 + (rate/compounds_per_year) )**(compounds_per_year*years))

























