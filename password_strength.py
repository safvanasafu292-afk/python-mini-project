def get_password():
    password = input("Enter a password: ")
    return password


def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check_special_character(password):
    characters = ["!", "@", "#", "$", "%", "^", "&", "*",
                  "(", ")", "_", "+", "-", "=", "?", "/"]

    for c in characters:
        if c in password:
            return True

    return False


def check_numbers(password):
    numbers = ["0", "1", "2", "3", "4",
               "5", "6", "7", "8", "9"]

    for n in numbers:
        if n in password:
            return True

    return False


def display_strength(length_ok, special_ok, number_ok):

    if length_ok == True:
        print("Length: ✅ (Pass - 8 chars)")
    else:
        print("Length: ❌ (Fail - Less than 8 chars)")

    if special_ok == True:
        print("Character: ✅ (Pass)")
    else:
        print("Character: ❌ (Fail - None found)")

    if number_ok == True:
        print("Number: ✅ (Pass)")
    else:
        print("Number: ❌ (Fail - None found)")


password = get_password()

length_ok = check_length(password)
special_ok = check_special_character(password)
number_ok = check_numbers(password)

display_strength(length_ok, special_ok, number_ok)

      
    
    

   

