import csv


def login():
    print('Please sign in')

    with open("Data/users.csv", encoding="utf-8") as csvfile:
        database = csv.DictReader(csvfile)
        loggedin = False
        while loggedin is not True:
            Username = input('Username: ')
            Password = input('Password: ')
            for row in database:
                Username_File = row['username']
                Password_File = row['password']
                Function_File = row['access']
                if (Username_File == Username and
                    Password_File == Password and
                        Function_File == 'user'):
                    loggedin = True
                    print('Succesfully logged in.')
                    # patientmenu()  # we will add this later on
                if (Username_File == Username and
                    Password_File == Password and
                        Function_File == 'admin'):
                    loggedin = True
                    print('Succesfully logged in as an admin.')
                    # artsmenu()     # we will add this later on
                if loggedin == False:
                    print('wrong username or password')

# ---- Main ---- #
login()