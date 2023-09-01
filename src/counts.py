import sys

# Read all the input into a string, spaces, newlines and all, but
# I remove the newlines since these are annoying to print...
# stdin will be read until newline. Modify this if you please. 

x = ""
for line in sys.stdin:
    x += line
    if line[-1] == "\n":
        break
x = x.replace("\n", "")

# Count the characters in `x`` and put the counts in `counts`.
# Your code goes here.
table = {}
for c in x:
    if c not in table:
        table[c] = 1
    else: 
        table[c] += 1

# Get the keys, i.e., the characters, in sorted order
# and print the count
for a in sorted(table):
    print(f"{a}: {table[a]}")


