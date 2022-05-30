import sqlite3


#username = input("whats ya name: ")
file = "Users.db"
conn = sqlite3.connect(file)
cursor = conn.cursor()

user_match = 0
results_modified = []
"""
cursor.execute(

SELECT user_name FROM user

)
results = cursor.fetchall()
for record in results:
    if record[0] == name:
        print("fuuck cunt")
#if name in results:
     #print("fuck moi")


cursor.execute(
                
                SELECT match_ID, win_loss, ai_dif 
                FROM winloss
                wHERE user_ID 
                IN (SELECT user_ID 
                    FROM user 
                    WHERE user_name = :username)
                ,
                {
                    "username": username 
                }
            )

results = cursor.fetchall()
print(results)
for record in results:
    user_match = user_match + 1
    match_result = record[1]
    match_dif = record [2]
    match_tuple = (user_match, match_result, match_dif)
    results_modified.append(match_tuple)
    

print(results_modified)
"""
user_ID = 3

username="max"
email="max@mail.com"
password="spatula"


cursor.execute(
    """
    INSERT INTO user
    VALUES (:ID, :name, :email, :password)
    """,
    {
       "ID": user_ID, 
       "name": username,
       "email": email,
       "password": password
    }
)
conn.commit()