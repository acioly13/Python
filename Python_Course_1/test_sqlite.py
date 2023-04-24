import sqlite3

# Connect to the database
conn = sqlite3.connect('my_db.db')

# Create a cursor
c = conn.cursor()


# Create a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS cars(name TEXT, year INTEGER, price REAL)')


# Insert data into the table
def insert_entry(name, year, price):
    c.execute("INSERT INTO cars VALUES(?, ?, ?)", (name, year, price))
    conn.commit()


# Show all the data in the table
def show_all():
    print('\nExibindo todos os dados da tabela:\n')
    c.execute("SELECT * FROM cars")
    rows = c.fetchall()
    for row in rows:
        print(row)


def show_entry(name):
    print('\nExibindo o dado %s\n' % name)
    c.execute("SELECT * FROM cars WHERE name = ?", (name,))
    row = c.fetchone()
    if row:
        print(row)


def update_name(old_name, new_name):
    print('\nAtualizando o nome %s para %s\n' % (old_name, new_name))
    c.execute("UPDATE cars SET name = ? WHERE name = ?", (new_name, old_name))
    conn.commit()


# Cria a tabela
create_table()

# Insere dados na tabela
insert_entry('Camaro', 2016, 200000)
insert_entry('Fusca', 1970, 10000)
insert_entry('Ferrari', 2017, 500000)

# Exibe todos os dados da tabela
show_all()

# Exibe o dado 'Fusca'
show_entry('Fusca')

# Atualiza o nome 'Fusca' para 'Jaguar'
update_name('Fusca', 'Jaguar')

# Fecha a conexão
c.close()
conn.close()
