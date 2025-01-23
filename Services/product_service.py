from DAL.product_repository import ProductRepository
import json

class ProductService:
    @staticmethod
    def add_supplier(
        name: str,
        description: str,
        stock_count: int,
        supplier_id: int,
        date_created,
    ) -> None:
        """
        Adds a new product to the database.
        """
        
        supplier_id = ProductRepository.create_supplier(name, description, stock_count, date_created)
        print(f"Product '{name}' from '{supplier_id}' added successfully")

    @staticmethod
    def get_all_products() -> list:
        """
        Retrieves all products from the database.
        """
        return ProductRepository.get_all_products()

    @staticmethod
    def search_product_by_name(name: str) -> dict:
        """
        Searches for suppliers by their name.
        """
        return ProductRepository.find_product_by_name(name)


    @staticmethod
    def list_products_with_their_suppliers() -> list:
        """
        List all products with their suppliers
        """
        return ProductRepository.print_all_products_with_their_suppliers()
