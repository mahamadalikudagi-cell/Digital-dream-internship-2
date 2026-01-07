valid_username = "dd_admin"
valid_password = "dd@2025"

# Accept user input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Authentication check
if username == valid_username and password == valid_password:
    print("Login Successful")
else:
    print("Access Denied")
