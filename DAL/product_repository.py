from config import CONN, CURSOR


class ProductRepository:

    
    @staticmethod
    def create_table():
        sql_query1 = """

        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            stock INTEGER,
            supplier_id INTEGER
        )
        """
        
        CURSOR.execute(sql_query1)
        CONN.commit()
        
        print("Tables done created.")
        
    