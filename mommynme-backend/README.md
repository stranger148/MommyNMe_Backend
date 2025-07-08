# MommynMe Backend

## File Structure
```
Backend/mommynme-backend/
├── app/
│   ├── __init__.py                # Flask app factory, blueprint registration
│   ├── models.py                  # SQLAlchemy models (all DB tables)
│   ├── static/
│   │   └── uploads/
│   │       ├── hero1.jpg, ...     # Uploaded images (products, featured)
│   │       └── featured/          # Featured update images
│   ├── routes/
│   │   ├── admin_routes.py        # (if used)
│   │   ├── category_routes.py     # Category endpoints
│   │   ├── product_routes.py      # Product endpoints
│   │   ├── cart_routes.py         # Cart endpoints
│   │   ├── orders_routes.py       # Order endpoints (pending, shipped, stats, graph)
│   │   ├── contact_routes.py      # Contact form endpoints
│   │   └── featured_update_routes.py # Featured updates endpoints
│   └── utils/
│       └── db_utils.py            # (if used)
├── config.py                      # Flask/DB config
├── requirements.txt               # Python dependencies
├── run.py                         # Entry point to run the backend server
├── README.md                      # This file
└── venv/                          # Python virtual environment (not required to commit)
```

## How to Run the Backend
1. **Set up the database:**
   - Ensure PostgreSQL is installed and running.
   - Create a database (e.g., `mommynme_db`).
   - (Optional) Use the provided SQL in this README to create tables manually, or let SQLAlchemy create them on first run.
2. **Configure the backend:**
   - Edit `config.py` to set your PostgreSQL URI, user, and password.
3. **Install dependencies:**
   - Create and activate a Python virtual environment (optional but recommended):
     ```
     python -m venv venv
     source venv/bin/activate  # or .\venv\Scripts\activate on Windows
     ```
   - Install requirements:
     ```
     pip install -r requirements.txt
     ```
4. **Run the backend server:**
   - From `Backend/mommynme-backend/`, run:
     ```
     python run.py
     ```
   - The backend will be available at `http://localhost:5000`

## Requirements
- Python 3.8+
- PostgreSQL
- All Python dependencies in `requirements.txt`

## Notes
- All images (products, featured updates) are stored in `app/static/uploads/`.
- See `models.py` for all table definitions.
- All API endpoints are documented in the code and this README.
- For the featured updates table, use:
```sql
CREATE TABLE featured_updates (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
```