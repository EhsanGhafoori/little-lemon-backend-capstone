# Little Lemon Backend Capstone

Django REST API for the Little Lemon restaurant (table bookings, menu).  
Back-end developer capstone project.

## API paths to test

See **Readme.txt** for the list of API paths peers should test.

## Setup

1. **Clone and enter the project**
   ```bash
   git clone https://github.com/EhsanGhafoori/little-lemon-backend-capstone
   cd little-lemon-backend-capstone
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate   # Linux/macOS
   pip install -r requirements.txt
   ```

3. **Create the MySQL database**
   - Create a database named `littlelemon` in MySQL.
   - If your MySQL user/password differ, update `littlelemon/settings.py` `DATABASES` accordingly.

4. **Run migrations and server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Optional: create a superuser for the admin**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run tests**
   ```bash
   python manage.py test reastaurant
   ```
   (Tests use an in-memory SQLite database so MySQL is not required for testing.)

## Peer review

Use the endpoints listed in `Readme.txt` with Insomnia (or similar) to verify the API.
