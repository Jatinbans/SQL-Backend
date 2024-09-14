# Fruit.ai Backend

This repository contains the backend for the **Fruit.ai** product, a health manager application. The backend is built using Flask and provides basic CRUD functionality for FAQs related to fruits. The API interacts with the frontend, handling all the server-side logic and database operations.

## Features

- **CRUD Operations**: Create, Read, Update, Delete FAQs.
- **Error Handling**: Robust error handling for both client and server errors.
- **Database Integration**: Uses SQLite for lightweight storage.
- **Modular Design**: Follows a clean architecture with separate files for models and routes.

## Technologies Used

- **Flask**: Micro-framework for building web applications.
- **SQLAlchemy**: ORM for database management.
- **SQLite**: Lightweight database used for local storage.
- **Postman**: Tool for API testing and development.
- **Python 3.8+**

## API Endpoints

| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| GET    | `/faqs`        | Fetch all FAQs               |
| GET    | `/faqs/<id>`   | Fetch a single FAQ by ID     |
| POST   | `/faqs`        | Create a new FAQ             |
| PUT    | `/faqs/<id>`   | Update an existing FAQ       |
| DELETE | `/faqs/<id>`   | Delete a FAQ by ID           |

## Error Handling

- **404 Not Found**: Returned when the requested resource does not exist.
- **500 Internal Server Error**: Returned for any unhandled server-side exceptions.
- **400 Bad Request**: Returned when invalid data is provided.

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/fruit-ai-backend.git
    cd fruit-ai-backend
    ```

2. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Linux/macOS
    # OR
    venv\Scripts\activate      # For Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**
    - Initialize the SQLite database:
    ```bash
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

5. **Run the Application**
    ```bash
    python app.py
    ```

   The application will be running on `http://localhost:5000`.

## Project Structure

```bash
fruit-ai-backend/
├── app.py               # Main Flask application
├── models.py            # Database models for FAQs
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── venv/                # Virtual environment (not included in Git)
```

## Design Decisions

- **Flask Framework**: Chosen for its simplicity and flexibility, making it ideal for rapid development.
- **SQLAlchemy ORM**: Provides a high-level abstraction for database management, making it easier to perform CRUD operations.
- **SQLite**: Selected for its lightweight nature, perfect for a small-scale application like this.
- **Postman**: Utilized for API testing to ensure that all endpoints function correctly and meet the requirements.

## License

This project is licensed under the MIT License.
