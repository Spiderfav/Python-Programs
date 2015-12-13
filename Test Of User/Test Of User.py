while True:
    print ("What user are you?")
    user = input()
    if user == "1":
        print ("What is the password?")
        password = input()
        if password == "Admin":
           print ("You are my primary user!")
           break

        else:
            print ("Password incorrect! Please try again.")

    elif user == "0":
        print("Ok. Go on.")
        break

    else:
        print ("Not an option. Try again.")
