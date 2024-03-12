import sqlite3 

connector = sqlite3.connect('Deutsch_Words.db')

c = connector.cursor()

# c.execute("ALTER TABLE GermanW add id integer")
# # c.execute("""CREATE TABLE GermanW( 
# #           first text,
# #           last text,
#             id integer)
# #            """)

c.execute("""INSERT INTO GermanW VALUES ('aussuchen','To choose',3), 
                                        ('sich sehnen','To yearn or crave',4),
                                        ('sich überlegen','To think or deliberate',5),
                                        ('geliebt werden','To be loved',6),
                                        ('verliebt sein','To be enamored',7),
                                        ('beißen','To bite',8),
                                        ('bieten','To offer or provide',9),
                                        ('bitten','To request, beg, or ask',10)""")



c.execute("SELECT * FROM GermanW")
names = [description[0] for description in c.description]
print(names)
print(c.fetchall())

connector.commit()
connector.close()
