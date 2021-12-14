                        
     
                         
            ,--,              
          ,--.'|              
          |  |,               
   ,---.  `--'_       ,---.   
  /     \ ,' ,'|     /     \  
 /    / ' '  | |    /    / '  
.    ' /  |  | :   .    ' /   
'   ; :__ '  : |__ '   ; :__  
'   | '.'||  | '.'|'   | '.'| 
|   :    :;  :    ;|   :    : 
 \   \  / |  ,   /  \   \  /  
  `----'   ---`-'    `----'   



Compound Interest Calcuator



# Contact: https://www.linkedin.com/in/steadfastpine/

# Release Date: 2019-06-14
# Version: .1



Description

	Output the total sum of compound interest applied over time.


	Compound interest formula:

		T = P[ 1 + (r/c) ]^cy

		T = total
		P = principle
		r - rate
		c = compounds_per_year
		y = years

	
	Python Class:

		CompoundInterest(principle,rate,compounds_per_year,years)



Prerequisites

	Python 3



Installation

	Download and unzip the program files, then change working directory to them:

		# cd compound-interest-calcuator


	# Import the compoundinterest.py file

		from compoundinterest import *


	# Create an object from the class with the required input variables
	# Format: CompoundInterest(principle,rate,compounds_per_year,years)

		test1 = CompoundInterest(5000,.03,12,6)


	# Print the total calculated amount

		print(test1.total)

		5984.742337665309


License 

	This program is licensed under the GPL License, view the LICENSE.md file for more information.














