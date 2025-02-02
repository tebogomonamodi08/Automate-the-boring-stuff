#Regualar expressions are about simplifying your search.
  For example we are going to find if a string is a canadian phone number or not. A canadian number has the following pattern. 333-222-2433.

1. File 1 will be using a function for this.

########PSEUDOCODE####################
define a function that accepts text.
IF string is greater than 12 then False
IF index value from 0-2 are not decimal return False
IF the undex value for 4 is not hyphen return False
IF the index value of the range 4-6 is not decimal return False
IF the index value of range 8-11 is not decimal retun False
Return True

###############################################################