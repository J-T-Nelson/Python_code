# just want to do a little practice of re module and have a space to refere to my past exercises: 
import re

st = """Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""

sts = st.replace("\n", ' ').replace(",", '').split(" ")
print(sts)

print(re.search(sts[0], st))

if re.search(sts[1], st):
    print("The re match object itself can act as a boolean")


if not re.search("DOGHAM", st):
    print("The re match object itself can act as a boolean") # both of these end up printing meaning that the result of re.search() may be an object but that object somehow is coerced into a boolean when appropriate... How the fuck? 



