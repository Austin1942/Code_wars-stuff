#It's time to create an autocomplete function! Yay!
#The autocomplete function will take in an input string and a dictionary array and return the values from the dictionary that start 
#with the input string. If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.

    ########
    #  EX  #  # autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
    ########  
            
import string
def autocomplete(input_, dictionary):
    letters = ("".join([x for x in input_ if x in string.ascii_letters])).lower()
    return [y for y in dictionary if y[0:len(letters)].lower() == letters][:5]

dictionary=[ 'abnormal',
  'arm-wrestling',
  'absolute',
  'airplane',
  'airport',
  'amazing',
  'apple',
  'ball' ]

print(autocomplete('ai', dictionary))