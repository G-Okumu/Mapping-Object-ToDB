from config import CONN, CURSOR


class ProductRepository:
    @staticmethod
    def create_table():
        """Create the products table if it doesn't already exist."""
        sql_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            description TEXT,
            price REAL,
            stock_count INTEGER,
            supplier_id INTEGER,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (supplier_id) REFERENCES suppliers (id) -- one to many 
        )
        """
        CURSOR.execute(sql_query)
        CONN.commit()
        print("Products table created successfully.")

    @staticmethod
    def create_product(name: str, description: str, price: float, stock_count: int, supplier_id: int):
        """
        Insert a new product into the products table and return its ID.
        """
        CURSOR.execute(
            """
            INSERT INTO products (name, description, price, stock_count, supplier_id) 
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, description, price, stock_count, supplier_id),
        )
        CONN.commit()
        return CURSOR.lastrowid

    @staticmethod
    def get_all_products() -> list:
        """Retrieve all products from the database."""
        return CURSOR.execute("SELECT * FROM products").fetchall()

    @staticmethod
    def find_product_by_name(name: str) -> dict:
        """
        Find a product by its name.
        """
        product = CURSOR.execute("SELECT * FROM products WHERE name LIKE ?", (name + '%',)).fetchone()
        if product:
            return product
        print(f"No product found with the name: {name}")
        return {}

    @staticmethod
    def print_all_products_with_their_suppliers() -> list:
        """
        Retrieve all products with their associated supplier details.
        """
        query = """
        SELECT 
            p.id,
            p.name AS product_name, 
            p.description, 
            p.price, 
            p.stock_count,
            p.date_created,
            s.name AS supplier_name, 
            s.location AS supplier_location
        FROM 
            products p
        LEFT JOIN 
            suppliers s 
        ON 
            p.supplier_id = s.id
        """
        return CURSOR.execute(query).fetchall()

    @staticmethod
    def drop_table():
        """Drop the products table."""
        CURSOR.execute("DROP TABLE IF EXISTS products")
        CONN.commit()
        print("Products table dropped successfully.")


