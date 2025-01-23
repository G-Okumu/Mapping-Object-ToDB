from Services.supplier_service import SupplierService
from  Services.product_service import ProductService

from DAL.product_repository import ProductRepository

class Main:
    @staticmethod
    def main_menu():
        while True:
            print("\nWelcome to the Product Inventory System:")
            print("1. Manage Suppliers")
            print("2. Manage Products")
            print("0. Exit")
            
            menu_selected = input("\nChoose an option: ").strip()

            if menu_selected == '1':
                Main.supplier_menu()
            elif menu_selected == '2':
                Main.product_menu()
            elif menu_selected == '0':
                print("\nExiting the system. Goodbye!")
                break
            else:
                print("\nInvalid selection. Please choose a valid option.")
    
    @staticmethod
    def supplier_menu():
        while True:
            print("\n--- Manage Suppliers ---")
            print("1. Add Supplier")
            print("2. View All Suppliers")
            print("3. Search Supplier by Name")
            print("4. Get Supplier by ID")
            print("0. Return to Main Menu")
            
            submenu_selected = input("\nChoose an option: ").strip()

            if submenu_selected == '1':
                name = input("Enter the supplier's name: ").strip()
                primary_mobile = input("Enter the supplier's primary mobile: ").strip()
                location = input("Enter the supplier's location: ").strip()
                secondary_mobile = input("Enter the supplier's secondary mobile (optional): ").strip() or None
                primary_email = input("Enter the supplier's primary email (optional): ").strip() or None
                
                SupplierService.add_supplier(name, primary_mobile, location, secondary_mobile, primary_email)
            
            elif submenu_selected == '2':
                suppliers = SupplierService.get_all_suppliers()
                if suppliers:
                    print("\n--- List of Suppliers ---")
                    for supplier in suppliers:
                        print(f"ID: {supplier[0]}, Name: {supplier[1]}, Location: {supplier[2]}, Contact Info: {supplier[3]}")
                else:
                    print("\nNo suppliers found.")
            
            elif submenu_selected == '3':
                name = input("Enter the name of the supplier to search: ").strip()
                suppliers = SupplierService.search_supplier_by_name(name)
                if suppliers:
                    print("\n--- Search Results ---")
                    for supplier in suppliers:
                        print(f"ID: {supplier[0]}, Name: {supplier[1]}, Location: {supplier[2]}, Contact Info: {supplier[3]}")
                else:
                    print(f"\nNo suppliers found with the name '{name}'.")
            
            elif submenu_selected == '4':
                try:
                    supplier_id = int(input("Enter the supplier ID: ").strip())
                    supplier = SupplierService.get_supplier_by_id(supplier_id)
                    if supplier:
                        print("\n--- Supplier Details ---")
                        print(f"ID: {supplier[0]}, Name: {supplier[1]}, Location: {supplier[2]}, Contact Info: {supplier[3]}")
                    else:
                        print(f"\nNo supplier found with ID '{supplier_id}'.")
                except ValueError:
                    print("\nInvalid ID. Please enter a numeric value.")
            
            elif submenu_selected == '0':
                print("\nReturning to the main menu.")
                break
            else:
                print("\nInvalid selection. Please choose a valid option.")
    
    
    
    @staticmethod
    def product_menu():
        while True:
            print("\n--- Manage Products ---")
            print("1. Add Product")
            print("2. View All Products")
            print("3. Search Product by Name")
            print("4. View All Products with their Suppliers")
            print("5. Update Product")
            print("0. Return to Main Menu")
            
            submenu_selected = input("\nChoose an option: ").strip()

            if submenu_selected == '1':
                name = input("Enter the product's name: ").strip()
                description = input("Type the description of the product MAX(10 chrs): ").strip()
                price = int(input("Amount for each Item: "))
                stock_count = input("Enter stock quantity: ").strip()
                supplier_id = input("Enter the id of the supplier: " ).strip()
                ProductService.add_product(name, description, price, stock_count, supplier_id)
            
            elif submenu_selected == '2':
                products = ProductService.get_all_products()
                if products:
                    print("\n--- List of Products ---")
                    for product in products:
                        print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: {product[3]}, Stock Available: {product[4]} Created On: {product[6]}")
                else:
                    print("\n 0")
            
            elif submenu_selected == '3':
                name = input("Enter the name of the product to search: ").strip()
                product = ProductService.search_product_by_name(name)
                if product:
                    print("\n--- Search Results ---")
                    print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: {product[3]}, Stock Available: {product[4]} Created On: {product[6]}")
                else:
                    print(f"\nNo products found with the name '{name}'.")
            
            elif submenu_selected == '4':
                products = ProductService.list_products_with_their_suppliers()
                if products:
                    print("\n--- List of Products and associated Suppliers---")
                    for product in products:
                        print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: {product[3]}, Stock Available: {product[4]} Created On: {product[5]}")
                        print(f"Supplier\n Name: {product[6]}, Location: {product[7]}\n")
                else:
                    print("\n 0")
            elif submenu_selected == '5':
                print("Coming Soon")
            elif submenu_selected == '0':
                print("\nReturning to the main menu.")
                break
            else:
                print("\nInvalid selection. Please choose a valid option.")

if __name__ == "__main__":
    
    """
    Run these once
    
        #DROP if exists
        SupplierRepository.drop_table();
        
        # Re-Create the tables
        SupplierRepository.create_table();
        
        ProductRepository.drop_table()
        ProductRepository.create_table()
    
    """

    
    Main.main_menu()
