import time

class facebook:

    _user_id = 1

    def __init__(self):
        # self.menu()
        self.id = facebook._user_id
        facebook._user_id += 1
        self.__username = "Default User" #Encapsulation
        self.password = ""
        self.logged_in = False
    
    @staticmethod
    def get_id():
        return facebook._user_id
    
    @staticmethod
    def set_id(value):
        facebook._user_id = value



    def menu(self):
        num = input("""
                    Welcome to Facebook!, please select an option:
                        1. Press 1 to create an account
                        2. Press 2 to login
                        3. press 3 to write a post
                        4. Press 4 to message a friend
                        5. Press any other key to exit
                        : """)
        
        if num == "1":
            self.signup()
        elif num == "2":
            self.login()
        elif num == "3":
            self.write_post()
        elif num == "4":
            self.message_friend()
        else:   
            print("Exiting...")
            time.sleep(1)
            exit()

    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"Account created for {self.username}")
        print("")
        self.menu()


    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            print(f"Welcome back {self.username}")
            self.logged_in = True
        else:
            print("Invalid credentials, please try again")
            self.login()
        print("")
        self.menu()

    def write_post(self):
        if self.logged_in:
            post = input("Write your post: ")
            print(f"Post created: {post} \n by {self.username}")
        else:
            print("You need to login first")
            self.login()
        print("")
        self.menu()

    def message_friend(self):
        if self.logged_in == True:
            txt = input("Enter your message: ")
            frnd = input("Enter your friend's name: ")
        else :
            print("You need to sign in first")
        print("")
        self.menu()
        

    
# a1 = facebook()