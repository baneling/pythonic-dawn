# Python Basic Data Types

# Integer
13, 015, 0x0D

# Float
13.0, 13E0, 0.13E2

# String
"a"

"a string does not have to be short"

'also-a-string'

""" 
Multiline strings.
Work with either of the parentheses, tripled on each end.
"""

'''
So this is similar,
to the multi-line string mentioned,
above.
'''

# List
# 'Basic array of data'
# Items in hooked [   ] brackets. Items seperated by ","
# Lists can store basically anything. 
# Also big objects you will build in classes, later on...
[1, 2, 3, 4]
["Dog", "Cat", "Goldfish"]
["You can store mixed data types", 2, 3.0, ["Even", "Another", "List"]]

# Tuple
# 'Array of data which cannot be edited'
# Items inside (    ) braces. Items seperated by ",".
# Behave like lists BUT data is immutable.
#>Once a tuple is defined, you can access the data, but you cannot change the data inside of the tuple.
(1, 2, 3, 4)
("Dog", "Cat", ["Some", "List"], ("Some", "Tuple"))

# Dictionary
# 'Array of data, with a keyword bound to every argument'
# Items inside {    } brackets. Items seperated by ","
# Keyword and entries seperatied by ":"
# Keys cant be lists. But can be tuples, integers, strings; must be unique.
# Only 1 entry per key allowed. 
member = {'username': 'Kerrigan90', 'email': 'jointheswarm@charhosting.com'}

