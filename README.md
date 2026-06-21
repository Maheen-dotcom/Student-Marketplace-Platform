# Student Marketplace Platform

## Project Overview

Student Marketplace Platform is a full-stack web application developed to help students buy and sell academic resources. The platform provides a dedicated marketplace where students can exchange books, notes, calculators, laptops, and other educational materials.

The project was developed as part of the Operating Systems and Software Development course project and demonstrates frontend development, backend API development, database integration, version control, and deployment.

---

## Live Project Links

### Frontend Website

https://student-marketplace-platform.vercel.app/

### Backend API

https://student-marketplace-platform-production.up.railway.app

### API Documentation (Swagger)

https://student-marketplace-platform-production.up.railway.app/docs

### GitHub Repository

https://github.com/Maheen-dotcom/Student-Marketplace-Platform

---

## Problem Statement

Students often struggle to find affordable academic resources. Existing online marketplaces are designed for general users and do not specifically address student needs.

This project provides a dedicated platform that allows students to connect with one another and exchange educational resources in a simple and organized manner.

---

## Objectives

* Provide a marketplace for students.
* Enable user registration and login.
* Allow students to add, update, and delete products.
* Support product search and filtering.
* Store data securely using PostgreSQL.
* Demonstrate full-stack web application development.

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* FastAPI
* Python

### Database

* PostgreSQL
* Supabase

### Version Control

* Git
* GitHub

### Deployment

* Railway (Backend)
* Vercel (Frontend)

---

## Project Features

### User Management

* User Registration
* User Login
* View User Profile
* Update User Profile

### Product Management

* Add Product
* View Products
* Update Product
* Delete Product

### Marketplace Features

* Product Search
* Product Filtering
* Marketplace Dashboard

### Dashboard

* Total Users Count
* Total Products Count

---

## API Endpoints

### User APIs

| Method | Endpoint      |
| ------ | ------------- |
| POST   | /register     |
| POST   | /login        |
| GET    | /users        |
| GET    | /profile/{id} |
| PUT    | /profile/{id} |

### Product APIs

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /products      |
| GET    | /products      |
| GET    | /products/{id} |
| PUT    | /products/{id} |
| DELETE | /products/{id} |

### Additional APIs

| Method | Endpoint   |
| ------ | ---------- |
| GET    | /search    |
| GET    | /filter    |
| GET    | /dashboard |

---

## Database Design

### User Table

* id
* full_name
* email
* password
* phone
* role

### Product Table

* id
* title
* description
* category
* price
* seller_name

---

## Project Structure

StudentMarketplace

├── backend

│ ├── main.py

│ ├── database.py

│ ├── models.py

│ ├── schemas.py

│ └── requirements.txt

│

├── frontend

│ ├── index.html

│ ├── about.html

│ ├── login.html

│ ├── marketplace.html

│ ├── dashboard.html

│ ├── manage.html

│ ├── script.js

│ └── style.css

│

├── screenshots

├── README.md

└── .gitignore

---

## Screenshots

Project screenshots are available inside the screenshots folder.

---

## Future Enhancements

* Product Image Upload
* JWT Authentication
* Chat System
* Wishlist Feature
* Product Reviews and Ratings
* Advanced Search Filters

---

## Author

Maheen Maqsood

BS Cyber Security

University of Management and Technology (UMT)

Lahore, Pakistan
