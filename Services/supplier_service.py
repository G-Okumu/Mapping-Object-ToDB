from DAL.supplier_repository import SupplierRepository
import json

class SupplierService:
    @staticmethod
    def add_supplier(
        name: str,
        primary_mobile: str,
        location: str,
        secondary_mobile: str = None,
        primary_email: str = None,
    ) -> None:
        """
        Adds a new supplier to the database.
        """
        contact_info = json.dumps({
            'primary_mobile': primary_mobile,
            'secondary_mobile': secondary_mobile,
            'primary_email': primary_email,
        })
        
        supplier_id = SupplierRepository.create_supplier(name, location, contact_info)
        print(f"Supplier '{name}' from '{location}' added successfully with ID: {supplier_id}.")

    @staticmethod
    def get_all_suppliers() -> list:
        """
        Retrieves all suppliers from the database.
        """
        return SupplierRepository.get_all_suppliers()

    @staticmethod
    def search_supplier_by_name(name: str) -> list:
        """
        Searches for suppliers by their name.
        """
        return SupplierRepository.find_supplier_by_name(name)

    @staticmethod
    def get_supplier_by_id(supplier_id: int) -> dict:
        """
        Retrieves a supplier by their ID.
        """
        return SupplierRepository.find_supplier_by_id(supplier_id)

    @staticmethod
    def find_products_for_a_supplier(supplier_id: int) -> list:
        """
        Finds all products associated with a supplier.
        """
        return SupplierRepository.find_all_products_for_a_supplier(supplier_id)
