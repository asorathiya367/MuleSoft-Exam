from connection import *

try:
    #fetch data
    cur = con.execute("select * from movies")
    rows = cur.fetchall()
    #fetch all data
    for details in rows:
        print(details)
except:
    #error in data fetch
    print("Error in data fetch")