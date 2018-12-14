import csv

def login():
    print(7*"-", " Log In ", 7*"-", "\n")
    print('Please sign in')
    with open("Data/users.csv", encoding="utf-8") as csvfile:
        database = csv.DictReader(csvfile)
        loggedin = False
        while loggedin is not True:
            Username = input('Username: ').lower()
            Password = input('Password: ').lower()
            for row in database:
                Username_File = row['username']
                Password_File = row['password']
                user_access = row['access']
                if (Username_File == Username and
                    Password_File == Password and
                        user_access == 'user'):
                    loggedin = True
                    print('Succesfully logged in.')
                    return user_access
                if (Username_File == Username and
                    Password_File == Password and
                        user_access == 'admin'):
                    loggedin = True
                    print('Succesfully logged in as an admin.')
                    return user_access
            if loggedin == False:
                print('wrong username or password')
            csvfile.seek(0,0)