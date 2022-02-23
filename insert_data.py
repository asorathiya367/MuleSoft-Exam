from connection import *

try:
    #take values from user
    movie_name = input("Enter Movie Name : ")
    actor_name = input("Enter Actor Name : ")
    actress_name = input("Enter Actress Name : ")
    relese_year = int(input("Enter Relese Year : "))
    director_name = input("Enter Director Name : ")

    #insert taken value
    con.execute("insert into movies (movie_name,leadactor_name,actress_name,yearofrelese,director_name) values (?,?,?,?,?)",(movie_name,actor_name,actress_name,relese_year,director_name))
    con.commit()
    print("Data Inserted Successfuly")
except:
    #error in inserion
    print("Error in insertion")