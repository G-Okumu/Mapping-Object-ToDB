# Product Inventory System

## Overview
The Product Inventory System is an interactive Python-based application for managing suppliers and products. It is designed to streamline the process of adding, viewing, and searching for suppliers, with planned future enhancements for product management.

## Features
### Current Functionality
1. **Supplier Management**
   - Add new suppliers with details such as name, location, and contact information.
   - View all suppliers stored in the database.
   - Search for suppliers by name.
   - Retrieve supplier details using their unique ID.

### Planned Features
2. **Product Management** (Under Development)
   - Manage products linked to suppliers.
   - Add, view, and search for products.

## Project Structure
## Layered Architecture

The application follows a layered architecture pattern to ensure separation of concerns, improve maintainability, and facilitate scalability. Below is an explanation of each layer:

### 1. **Data Access Layer (DAL)**
   - **Purpose**: 
     - Handles all interactions with the database.
     - Encapsulates database queries and CRUD operations.
   - **Key Responsibilities**:
     - Define and execute SQL queries.
     - Perform operations such as creating tables, inserting data, fetching records, and updating or deleting data.
   - **Example**: 
     - The `supplier_repository.py` file contains methods to interact with the `suppliers` table in the database, such as creating the table, adding suppliers, or retrieving supplier records.

### 2. **Service Layer**
   - **Purpose**: 
     - Acts as a bridge between the Data Access Layer and the Presentation Layer.
     - Contains business logic and ensures data consistency.
   - **Key Responsibilities**:
     - Validate input data.
     - Coordinate complex operations that may involve multiple repository methods.
     - Return meaningful results to the Presentation Layer.
   - **Example**: 
     - The `supplier_service.py` file provides methods to add suppliers, retrieve all suppliers, or search for suppliers by name using the DAL methods.

### 3. **Presentation Layer**
   - **Purpose**: 
     - Provides an interface for users to interact with the system.
     - Handles user input and output.
   - **Key Responsibilities**:
     - Display menus and prompt users for input.
     - Call appropriate service layer methods based on user actions.
     - Format and display the results to the user.
   - **Example**: 
     - The `main.py` file contains interactive menus for supplier management and calls the methods from `SupplierService`.

### Layered Architecture Flow
The flow of data and operations between the layers is as follows:
1. **User Interaction**:
   - Users interact with the system via the Presentation Layer (`main.py`).
2. **Service Layer**:
   - The Presentation Layer calls methods from the Service Layer (`supplier_service.py`) to process user requests.
   - Business logic is applied here.
3. **Data Access Layer**:
   - The Service Layer interacts with the Data Access Layer (`supplier_repository.py`) to fetch or modify data in the database.
4. **Results**:
   - The results flow back from the DAL to the Service Layer, then to the Presentation Layer, where they are displayed to the user.

### Advantages of This Architecture
1. **Separation of Concerns**:
   - Each layer has a distinct responsibility, making the system easier to maintain and extend.
2. **Scalability**:
   - New features or modules can be added without affecting other layers.
3. **Testability**:
   - Each layer can be tested independently.
4. **Reusability**:
   - DAL and Service Layer methods can be reused in different contexts.

