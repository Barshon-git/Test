is_male= True
is_tall= False

if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("you are a male or tall or both")
else:
    print("You are neither male nor tall")

print("\n")

is_male= True
is_tall= False

if is_male and is_tall:
    print("you are a male or tall or both")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are neither male nor tall")

