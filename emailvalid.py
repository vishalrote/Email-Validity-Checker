
# =================================================================
#    1. Email should be greater than 6 alphabets
#    2. First letter should be always alphabet
#    3. There should be only one @ in the email ID
#    4. There should be .com or .in present in the email ID
#    5. NO space in the email and no uppercase
#    6. Only _ and . is allowed in the Email ID
# =================================================================

email = input("Enter your Email ID : ")
k, j, d = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():  # chect if first letter is alphabet
        # there should be @ in email and there can be only one @
        if ("@" in email) and (email.count("@") == 1):
            # condition for .com or it can be .in {^ is xor}
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():  # no space and no uppercase
                        k = 1
                    elif i.isalpha():  # check alhabets
                        if i == i.upper():  # upper case check
                            j = 1
                    elif i.isdigit():  # check if there is digit
                        continue
                    elif i == "_" or i == "." or i == "@":  # if these contain then only continue
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print(
                        "Invalid Email (space,!,#,$,%,^,&,*,etc not allowed)")
                else:
                    print("Correct Email")
            else:
                print("Invalid Email (mistake in .com or .in)")
        else:
            print("Invalid Email (@ should be used once)")
    else:
        print("Invalid Email (first letter should be alphabet) ")
else:
    print("Invalid Email (Length should be more than 6) ")
