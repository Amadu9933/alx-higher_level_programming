#Pasword generator


import random

lower= "abcdefghijkmnopqrstuvwxyz"



upper=  "ABCDEFGHIJKMNOPQRSTUVWXYZ"



numbers= "0123456789"



symbols= "{}[]()*;/,._-"



all= lower + upper + numbers + symbols



lenth = 16



password = "".join(random.sample(all,lenth))



print(password)


