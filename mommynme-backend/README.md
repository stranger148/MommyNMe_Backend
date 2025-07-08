# MommynMe Backend

A modular Flask + PostgreSQL backend for the MommynMe website and admin dashboard.

## Features
- Admin and user APIs
- PostgreSQL (pgAdmin compatible)
- Modular project structure

## Setup
1. Create and activate a virtual environment:
   - Windows PowerShell:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate
     ```
2. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
3. Create the PostgreSQL database (in pgAdmin or psql):
   ```sql
   CREATE DATABASE mommynme_db;
   ```
4. Configure your PostgreSQL URI in `config.py` (default is for user `postgres` and password `2004`).
5. Run the backend server:
   ```powershell
   python run.py
   ```
6. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the welcome message.

## API Endpoints

### Root
- `GET /` — Welcome message (browser-friendly)

### Admin Routes
- `POST /admin/category` — Add a new category
- `POST /admin/product` — Add a new product
- `GET /admin/orders?status=pending|shipped` — Get all orders (optionally filter by status)

### User Routes
- `GET /products/<category_id>` — Fetch products by category
- `POST /cart` — Add items to cart (stub)
- `POST /order` — Place an order