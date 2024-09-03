# crear la base de datos en mysql: supermercado_db

import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='supermercado_db'
)

cursor = conexion.cursor()

# Crear las tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS country (
    country_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS province (
    province_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS department (
    department_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    province_id INT,
    FOREIGN KEY (province_id) REFERENCES province(province_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS locality (
    locality_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS supermarket_chain (
    supermarket_chain_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS supermarket (
    supermarket_id INT PRIMARY KEY,
    name VARCHAR(100),
    supermarket_chain_id INT,
    FOREIGN KEY (supermarket_chain_id) REFERENCES supermarket_chain(supermarket_chain_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS supermarket_address (
    supermarket_address_id INT PRIMARY KEY,
    supermarket_id INT,
    street VARCHAR(100),
    door_number VARCHAR(10),
    floor VARCHAR(10),
    department VARCHAR(10),
    locality_id INT,
    FOREIGN KEY (supermarket_id) REFERENCES supermarket(supermarket_id),
    FOREIGN KEY (locality_id) REFERENCES locality(locality_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS brand (
    brand_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    brand_id INT,
    FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS supermarket_chain_product (
    supermarket_chain_product_id INT PRIMARY KEY,
    supermarket_chain_id INT,
    product_id INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (supermarket_chain_id) REFERENCES supermarket_chain(supermarket_chain_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banking_institution_type (
    banking_institution_type_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS banking_institution (
    banking_institution_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    banking_institution_type_id INT,
    FOREIGN KEY (banking_institution_type_id) REFERENCES banking_institution_type(banking_institution_type_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS card_type (
    card_type_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS card_category (
    card_category_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
    person_id INT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_birth DATE NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS card (
    card_id INT PRIMARY KEY,
    banking_institution_id INT,
    card_type_id INT,
    card_name_id INT,
    person_id INT,
    FOREIGN KEY (banking_institution_id) REFERENCES banking_institution(banking_institution_id),
    FOREIGN KEY (card_type_id) REFERENCES card_type(card_type_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS discount (
    discount_id INT PRIMARY KEY,
    product_id INT,
    supermarket_chain_id INT,
    banking_institution_id INT,
    card_type_id INT,
    card_category_id INT,
    discount_percentage DECIMAL(5, 2),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (supermarket_chain_id) REFERENCES supermarket_chain(supermarket_chain_id),
    FOREIGN KEY (banking_institution_id) REFERENCES banking_institution(banking_institution_id),
    FOREIGN KEY (card_type_id) REFERENCES card_type(card_type_id),
    FOREIGN KEY (card_category_id) REFERENCES card_category(card_category_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS person_address (
    person_address_id INT PRIMARY KEY,
    person_id INT,
    street VARCHAR(100),
    door_number VARCHAR(10),
    floor VARCHAR(10),
    department VARCHAR(10),
    locality_id INT,
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    FOREIGN KEY (locality_id) REFERENCES locality(locality_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);
''')

# Confirmar y cerrar la conexión
conexion.commit()
conexion.close()