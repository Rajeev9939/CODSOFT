import random
import string

length=int(input("Enter the length of the password:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.punctuation

all=lower+upper+num

a = random.sample(all,length)
password="".join(a)
print(password)