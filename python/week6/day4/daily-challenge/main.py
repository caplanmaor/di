from datetime import date
from datetime import datetime
today = datetime.today()
user_input = input("whats your birthdate DD/MM/YYYY ?: ")
# call to strptime() parses the first argument 
# according to the format specified in the second, so those two need to match.
birthdate = datetime.strptime(user_input,"%d/%m/%Y")
# calculating age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
candles_count = str(age)[1]
candles_string = ""
for candle in range(int(candles_count)):
    candles_string += "i"
# making the sides of the candles (cake top)
top_length = 12
half_top = (12 - int(candles_count) )/ 2
half_top_string = ""
for i in range(int(half_top)):
    half_top_string += "_"
# printing the cake
print(f'    {half_top_string}{candles_string}{half_top_string}')
print('   | H:A:P:P:Y  |')
print(' |^^^^^^^^^^^^^^^^|')
print(' | B:i:r:t:h:d:a:y|')
print(' |                |')
print(' ~~~~~~~~~~~~~~~~~~')