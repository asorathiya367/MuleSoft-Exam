from sqlite3 import *

try:
    #database create
    con = connect("movie_db.db")
    print("Database movie_db is created")
    #create table movies
    con.execute("create table if not exists movies(id integer primary key autoincrement,movie_name text,leadactor_name text,actress_name text,yearofrelese integer,director_name text)")
except:
    #if error occures
    print("Error in database or table creation")

