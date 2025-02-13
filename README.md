# FastAPI User Management API

## Overview
This is a FastAPI-based User Management system that supports authentication and authorization with MySQL as the database. It implements JWT token-based authentication using bcrypt. The system supports two roles: **Admin** and **Normal User**, with different access permissions.

---

## Features
- **User Authentication & Authorization**
- **JWT Token-based Access Control**
- **Role-based Access Management (Admin & Normal User)**
- **CRUD Operations on Users (Admin only)**
- **Password Encryption using bcrypt**
- **MySQL Database Integration with SQLAlchemy ORM**

---

## Technologies Used
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- bcrypt
- Python 3.10+

---

## Installation & Setup
### 1. Clone the Repository
```sh
    git clone <repository_url>
    cd fastapi_crud
```

### 2. Create and Activate a Virtual Environment
```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
    pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the `fastapi_crud` directory and add the following:
```ini
DATABASE_URL="mysql+pymysql://username:password@localhost/dbname"
SECRET_KEY="your_new_secret_key"
```

### 5. Apply Migrations
```sh
    alembic upgrade head
```

### 6. Run the FastAPI Server
```sh
    uvicorn main:app --reload
```

The server will start at: **http://127.0.0.1:8000**

---

## API Endpoints

### **User Authentication**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/login` | POST | User login (returns JWT token) |

### **Admin-Only User Management**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users` | POST | Create a new user |
| `/api/users/{id}` | GET | Retrieve user details |
| `/api/users/{id}` | PATCH | Update user details |
| `/api/users/{id}` | DELETE | Delete a user |

### **Normal User Access**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/{id}` | GET | User can only view their own details |

---

## Project Structure
```
fastapi_crud/
│── fastapi_crud/
│   ├── auth.py          # Authentication logic
│   ├── config.py        # Configuration settings
│   ├── database.py      # Database connection setup
│   ├── .env             # Environment variables
│   ├── main.py          # FastAPI application entry point
│   ├── models/
│   │   ├── access_token.py # Access token model
│   │   ├── user.py      # User model
│   │   ├── base.py      # Base model
│   ├── routes/
│   │   ├── users.py     # User CRUD routes
│   │   ├── auth.py      # Login route
│   ├── schemas/
│   │   ├── user.py      # Pydantic schemas for users
│   │   ├── access_token.py # Pydantic schemas for tokens
```

---

## Authentication & Authorization Workflow
1. **User Registration** (Only Admin can create users).
2. **User Login**: User provides `cellnumber` & `password` to receive a JWT token.
3. **Token Storage**: JWT token is stored in the `AccessToken` table with an expiry time.
4. **Protected Endpoints**: Only Admins can access CRUD operations.
5. **Normal Users** can only view their own profile.

---

## Security Features
- **Bcrypt for Password Hashing**: User passwords are stored in an encrypted format.
- **JWT Token Authentication**: Ensures secure access to APIs.
- **Role-Based Authorization**: Restricts access based on user roles.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any queries, please reach out at [your_email@example.com]

