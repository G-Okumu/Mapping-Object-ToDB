from config import CONN, CURSOR

class SupplierRepository:
    @staticmethod
    def create_table():
        sql_query = """
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            contact_info TEXT NOT NULL
        )
        """
        CURSOR.execute(sql_query)
        CONN.commit()
        print("Table 'suppliers' has been successfully created.")

    @staticmethod
    def create_supplier(name: str, location: str, contact_info: str) -> int:
        """Insert a new supplier into the suppliers table and return its ID."""
        CURSOR.execute(
            "INSERT INTO suppliers (name, location, contact_info) VALUES (?, ?, ?)",
            (name, location, contact_info),
        )
        CONN.commit()
        print(f"Supplier '{name}' has been added.")
        return CURSOR.lastrowid

    @staticmethod
    def get_all_suppliers() -> list:
        """Retrieve all suppliers."""
        return CURSOR.execute("SELECT * FROM suppliers").fetchall()

    @staticmethod
    def find_supplier_by_name(name: str) -> list:
        """Find suppliers by their name."""
        suppliers = CURSOR.execute("SELECT * FROM suppliers WHERE name LIKE ?", (name + '%',)).fetchall()
        if suppliers:
            return suppliers
        print(f"No suppliers found with the name: {name}")
        return []

    @staticmethod
    def find_supplier_by_id(supplier_id: int) -> dict:
        """Find a supplier by its ID."""
        supplier = CURSOR.execute("SELECT * FROM suppliers WHERE id = ?", (supplier_id,)).fetchone()
        if supplier:
            return supplier
        print(f"No supplier found with ID: {supplier_id}")
        return None

    @staticmethod
    def find_all_products_for_a_supplier(supplier_id: int) -> list:
        """Retrieve all products associated with a supplier."""
        supplier = SupplierRepository.find_supplier_by_id(supplier_id)
        if supplier:
            products = CURSOR.execute(
                "SELECT * FROM products WHERE supplier_id = ?", (supplier_id,)
            ).fetchall()
            if products:
                return products
            print(f"No products found for supplier ID: {supplier_id}")
            return []
        print(f"No supplier found with ID: {supplier_id}")
        return []
    
    @staticmethod
    def drop_table():
        CURSOR.execute("DROP TABLE IF EXISTS suppliers")
        CONN.commit()
