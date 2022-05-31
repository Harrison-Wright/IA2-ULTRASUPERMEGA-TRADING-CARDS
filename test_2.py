from User import UserDB

uc = UserDB()


#print(uc.create_user("monty","tester@mail.com", "password"))

#print(UserDB.user_login("harry", "password"))


print(uc.user_login("harry", "password"))

print(uc.check_stats())