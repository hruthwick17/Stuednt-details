username = input("Enter Student Name: ")
usn = input("Enter USN: ")
password = input("Enter Password: ")
if usn == "4AL25CS048" and password == "12345":
    print("\nLogin Successful!")
    print("Welcome", username)
    print("USN:", usn)
else:
    print("\nInvalid USN or Password")