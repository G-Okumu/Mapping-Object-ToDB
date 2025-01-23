from Services.supplier_service import SupplierService
from DAL.supplier_repository import SupplierRepository

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
                print("\nProduct management is under development.")
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

if __name__ == "__main__":
    
    """
    Run these once
    
        #DROP if exists
        SupplierRepository.drop_table();
        
        # Re-Create the tables
        SupplierRepository.create_table();
    
    """
    
    
    Main.main_menu()
