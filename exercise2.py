user_input = input("Please enter e-mail:")
def valid_or_not(x):
    email_check = x
    y = False
    z = False
    for i in email_check:
        if i=="@":
            y = True
        elif i==".":
            z=True
    return y and z
if valid_or_not(user_input):
    print("This is a valid e-mail.")
else:
    print("This is not a valid e-mail.")


