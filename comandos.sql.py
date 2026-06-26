import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

# cursor.execute('''
#                ALTER TABLE professores ADD COLUMN endereco TEXT
#                        ''')

# cursor.execute(''' ALTER TABLE professores ADD COLUMN cidade TEXT
#                ''')

# cursor.execute('''ALTER TABLE professores ADD COLUMN estado TEXT
#                ''')
cursor.execute('''DROP TABLE professores''')

conecao.commit()
conecao.close()
