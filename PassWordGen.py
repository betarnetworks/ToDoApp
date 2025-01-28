newPass = input('Enter a new password: ')

passwo = {"less": True, 'digits': True, "cap": True}

if len(newPass) < 8:
    passwo['less'] = False
else:
    passwo['less'] = True

digit = False
for char in newPass:
    if char.isdigit():
        digit = True
    passwo['digits'] = digit

caps = False
for car in newPass:
    if car.isupper():
        caps = True
    passwo['cap'] = caps

print(all(passwo.values()))



