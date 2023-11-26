import mysql.connector
#open a connection to the MySQL server
cnx = mysql.connector.connect(user='user',
                              password='Benetellemara1!',
                              host='localhost',
                              database='movies')
#create a new cursor
cursor = cnx.cursor()
# store the SELECT query
query = "SELECT * from studio"
# execute the operation stored in the query
cursor.execute(query)
# fetches all rows from the last statement on the cursor.
result=cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
# loop through the rows and print required columns
for row in result:
    print("Studio ID:",row[0])
    print("Studio Name:",row[1])
    print(" ")

#display genere
query = "SELECT * from genre"
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result:
    print("Genre ID:",row[0])
    print("Genre Name:",row[1])
    print(" ")
#displays films with 2 hour run time
query = "SELECT film_name,film_runtime from film where film_runtime<120 "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for row in result:
    print("Film Name:",row[0])
    print("Runtime:",row[1])
    print(" ")
#display directors info in the order of their name
query = "SELECT film_name,film_director from film order by film_director "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
    print("Film Name:",row[0])
    print("Director:",row[1])
    print(" ")
# close the cursor
cursor.close()
# close the connection
cnx.close()