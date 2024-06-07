from user import User

jane = User("Bingham university", "Karu, Nassarawa")
jane.show()

user = User()
user.register("james", "123", "abc", "abc")

email = input("Enter email: ")

password = input("Enter Password: ")
print(user.login(email, password))
