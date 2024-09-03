# Datos de prueba para la base de datos supermercado_db

import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='supermercado_db'
)

cursor = conexion.cursor()




# Insertar datos en la tabla country
cursor.execute("INSERT INTO country (country_id, name) VALUES (1, 'Argentina'), (2, 'Brasil');")

# Insertar datos en la tabla province
cursor.execute("INSERT INTO province (province_id, name, country_id) VALUES (1, 'Buenos Aires', 1), (2, 'Santa Fe', 1), (3, 'São Paulo', 2), (4, 'Rio de Janeiro', 2);")

# Insertar datos en la tabla department
cursor.execute("INSERT INTO department (department_id, name, province_id) VALUES (1, 'La Plata', 1), (2, 'Rosario', 2), (3, 'São Paulo', 3), (4, 'Rio', 4);")

# Insertar datos en la tabla locality
cursor.execute("INSERT INTO locality (locality_id, name, department_id) VALUES (1, 'City Bell', 1), (2, 'Funes', 2), (3, 'Santo Amaro', 3), (4, 'Copacabana', 4);")

# Insertar datos en la tabla supermarket_chain
cursor.execute("INSERT INTO supermarket_chain (supermarket_chain_id, name) VALUES (1, 'Carrefour'), (2, 'Walmart');")

# Insertar datos en la tabla supermarket
cursor.execute("INSERT INTO supermarket (supermarket_id, name, supermarket_chain_id) VALUES (1, 'Carrefour La Plata', 1), (2, 'Walmart Rosario', 2);")

# Insertar datos en la tabla supermarket_address
cursor.execute("INSERT INTO supermarket_address (supermarket_address_id, supermarket_id, street, door_number, floor, department, locality_id) VALUES (1, 1, 'Calle 1', '123', NULL, NULL, 1), (2, 2, 'Calle 2', '456', NULL, NULL, 2);")

# Insertar datos en la tabla brand
cursor.execute("INSERT INTO brand (brand_id, name) VALUES (1, 'Coca-Cola'), (2, 'Pepsi');")

# Insertar datos en la tabla product
cursor.execute("INSERT INTO product (product_id, name, brand_id) VALUES (1, 'Coca-Cola 1L', 1), (2, 'Pepsi 1L', 2);")

# Insertar datos en la tabla supermarket_chain_product
cursor.execute("INSERT INTO supermarket_chain_product (supermarket_chain_product_id, supermarket_chain_id, product_id, price) VALUES (1, 1, 1, 1.50), (2, 2, 2, 1.40);")

# Insertar datos en la tabla banking_institution_type
cursor.execute("INSERT INTO banking_institution_type (banking_institution_type_id, name) VALUES (1, 'Banco Nacional'), (2, 'Banco Privado');")

# Insertar datos en la tabla banking_institution
cursor.execute("INSERT INTO banking_institution (banking_institution_id, name, banking_institution_type_id) VALUES (1, 'Banco Nación', 1), (2, 'Banco Santander', 2);")

# Insertar datos en la tabla card_type
cursor.execute("INSERT INTO card_type (card_type_id, name) VALUES (1, 'Débito'), (2, 'Crédito');")

# Insertar datos en la tabla card_category
cursor.execute("INSERT INTO card_category (card_category_id, name) VALUES (1, 'Clásica'), (2, 'Oro');")

# Insertar datos en la tabla person
cursor.execute("INSERT INTO person (person_id, dni, first_name, last_name, date_birth) VALUES (1, '12345678', 'Juan', 'Pérez', '1980-01-01'), (2, '87654321', 'Maria', 'González', '1990-02-02');")

# Insertar datos en la tabla card
cursor.execute("INSERT INTO card (card_id, banking_institution_id, card_type_id, card_name_id, person_id) VALUES (1, 1, 1, 1, 1), (2, 2, 2, 2, 2);")

# Insertar datos en la tabla discount
cursor.execute("INSERT INTO discount (discount_id, product_id, supermarket_chain_id, banking_institution_id, card_type_id, card_category_id, discount_percentage) VALUES (1, 1, 1, 1, 1, 1, 10.00), (2, 2, 2, 2, 2, 2, 15.00);")

# Insertar datos en la tabla person_address
cursor.execute("INSERT INTO person_address (person_address_id, person_id, street, door_number, floor, department, locality_id) VALUES (1, 1, 'Calle Falsa', '123', NULL, NULL, 1), (2, 2, 'Av. Siempre Viva', '742', NULL, NULL, 2);")

# Insertar datos en la tabla users
cursor.execute("INSERT INTO users (user_id, username, password, email, person_id) VALUES (1, 'jperez', 'password123', 'jperez@example.com', 1), (2, 'mgonzalez', 'password456', 'mgonzalez@example.com', 2);")

# Confirmar y cerrar la conexión
conexion.commit()
conexion.close()