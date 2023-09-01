import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
print(password)
# Do all the requirement checks here.
isvalid = all([any(char.islower() for char in password),
                any(char.isupper() for char in password), 
                any(char.isnumeric() for char in password), 
                "$" in password or "#" in password or "@" in password,
                len(password)>5,
                len(password)<17])
print(isvalid)

