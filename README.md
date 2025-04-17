# 📦 Inventory Management System

The **Inventory Management System** is a web-based application built with **Django**, designed to help organizations manage and track inventory efficiently. With support for managing **people**, **places**, and **stock items**, the system includes full **CRUD operations**, user authentication, and a clean user interface.


## 🚀 Project Overview

This system enables businesses, teams, or departments to:

- Track **who** is responsible for items (People)
- Monitor **where** items are stored or used (Places)
- Manage **what** items are available, in stock, or out of stock (Inventory)

Ideal for use in small to mid-sized organizations, this project provides centralized control over physical or digital inventory and asset management.

![admin dashboard](https://github.com/user-attachments/assets/b40dd88e-d9ae-4a3e-b592-5810494a8628)


## 🔐 User Authentication

Secure access is enforced using Django’s built-in authentication system:

- Only registered users can access the dashboard.
- Admins can manage users and permissions.
- Secure login and logout functionality is built in.

![log in page](https://github.com/user-attachments/assets/79b4f197-f6e3-4ea4-a2cb-887ac7884f5a)

![registration page](https://github.com/user-attachments/assets/f331cd84-c20f-438c-9de6-6a4f49c3bf50)

## ✨ Key Features

- 🧑‍💼 Manage People and their roles or responsibilities.
- 📍 Manage Places (warehouses, locations, departments).
- 📦 Track Stock Levels for all inventory items.
- ✏️ Full CRUD Functionality for all major entities.
- 🔐 User Authentication and protected views.
- 🧹 Clean, user-friendly HTML/CSS frontend.
- ⚙️ Django Admin Panel for backend management.

---

## ✏️ Detailed CRUD Operations

The application includes Create, Read, Update, and Delete (CRUD) operations for all core modules:

### 🔹 People Management
- **Create**: Add new individuals with names, contact info, and roles.
- **Read**: View all registered people in a searchable list.
- **Update**: Edit existing person records to update contact info or roles.
- **Delete**: Remove people no longer active in the system.

- ![user editing page](https://github.com/user-attachments/assets/a3ed6fbe-fd6d-4106-a1ab-d2a7e25cebf4)


### 🔹 Inventory / Stock Management
- **Create**: Add new inventory items with quantity, category, and price.
- **Read**: View and search all inventory with filtering by category or location.
- **Update**: Modify stock quantities, or rename items.
- **Delete**: Remove outdated or discontinued items from inventory.
- 
![products page](https://github.com/user-attachments/assets/404d57fa-ee6a-4236-9e12-6c8baefe3fda)

### 🎉 Additional Functionalities
- **Form Validation**: Prevents submission of incomplete or incorrect forms.
- **Flash Messages**: Feedback for success/failure on actions.
- **Admin Dashboard**: Full control over the database from Django's admin panel.

![incorrect_forms](https://github.com/user-attachments/assets/2f08d472-881a-4f2b-99bb-3e7fd63fa135)


## 🛠️ Technologies Used

| Layer         | Technology     |
|---------------|----------------|
| Framework     | Django (Python)|
| Frontend      | HTML5, CSS3    |
| Backend       | Python         |
| Database      | SQLite         |
| Authentication| Django Auth    |

---

