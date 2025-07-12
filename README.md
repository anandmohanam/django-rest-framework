# Product Review System API

A RESTful API built using Django and Django REST Framework to manage products and allow users to submit authenticated reviews.

---

## Features

- **User Registration/Login/Logout**
- **Admin-only product management**
- **Authenticated reviews**
- **Average product rating**
- **Review edit/delete only by owner**
- **Permissions based on user roles**

---

##  API Endpoints

### Auth
- `POST /api/register/` — Register a new user
- `POST /api/login/` — Get auth token
- `POST /api/logout/` — Logout (invalidate token)

###  Products
- `GET /api/products/` — List all products
- `GET /api/products/<id>/` — Get a product
- `POST /api/products/` — Create (Admin only)
- `PUT /api/products/<id>/` — Update (Admin only)
- `DELETE /api/products/<id>/` — Delete (Admin only)

###  Reviews
- `GET /api/reviews/` — List all reviews
- `POST /api/reviews/` — Create (Authenticated user only, one per product)
- `PUT /api/reviews/<id>/` — Update (Review owner only)
- `DELETE /api/reviews/<id>/` — Delete (Review owner only)

---

##  Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/product-review-api.git
cd product-review-api

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate DB
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run server
python manage.py runserver


Default Admin Page: http://127.0.0.1:8000/admin
username:admin
password:admin