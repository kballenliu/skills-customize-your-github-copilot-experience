# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework in Python. You'll practice creating endpoints, handling HTTP methods, data validation, and API documentation while building a book library management system.

## 📝 Tasks

### 🛠️ Create a Book Library API

#### Description
Build a REST API for managing a book library system using FastAPI. The API should allow users to perform CRUD (Create, Read, Update, Delete) operations on books and provide automatic API documentation.

#### Requirements
Completed program should:

- Create FastAPI application with proper project structure
- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a specific book by ID
- Implement POST endpoint to add new books with data validation
- Implement PUT endpoint to update existing books
- Implement DELETE endpoint to remove books
- Use Pydantic models for request/response data validation
- Include proper HTTP status codes and error handling
- Generate automatic interactive API documentation (Swagger UI)

### 🛠️ Add Advanced Features

#### Description
Enhance your book library API with additional features to make it more robust and production-ready.

#### Requirements
Completed program should:

- Add search functionality to find books by title or author
- Implement pagination for the get all books endpoint
- Add input validation with custom error messages
- Include response models with proper typing
- Add basic authentication or API key protection
- Create comprehensive error handling for common scenarios
- Add database persistence using SQLite or in-memory storage
- Include unit tests for at least 3 endpoints
