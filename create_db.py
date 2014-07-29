import sqlite3

conn = sqlite3.connect('scrapey.db')

print ('Opened DB successfully')

conn.execute('''CREATE TABLE ADS(

					link TEXT,
					description TEXT,
					posted TEXT

                     );
                  ''')

print('Table Created Successfully')

conn.close()
