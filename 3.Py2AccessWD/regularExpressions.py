import re

x = "My 2 favorites numbres are 19 and 42"
# re.findall recive dos paramtros(Regular expression, data a analisar)
y = re.findall("[0-9]+", x)
print(y)

x = "From: Using the: character"
y = re.findall("^F.+:", x)
print(y)
y = re.findall("^F.+?:", x)
print(y)

# x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# y = re.findall("\S+@\S+", x)
# print(y)

# x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# y = re.findall("^From (\S+@\S+)", x)
# print(y)

# x = "We just received $10.00"
# y = re.findall("\$[0-9.]+", x)
# print(y)