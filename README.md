# LittleLemon API Testing Guide

Welcome to the LittleLemon project! This project is a full-stack restaurant reservation system built using Django and RESTful principles. Below are the API paths you can use to test the functionality of the project.

## API Paths for Testing

1. **Menu Items**
   - GET/POST: `/restaurant/menu/`
   - GET/PUT/DELETE: `/restaurant/menu/<int:pk>/`

2. **Booking Tables**
   - GET/POST/PUT/DELETE: `/restaurant/booking/tables/`

3. **Authentication**
   - Obtain Token: `/restaurant/api-token-auth/`
   - User Registration: `/auth/users/`
   - Login: `/auth/token/login/`
   - Logout: `/auth/token/logout/`

4. **Static HTML Page**
   - Access the homepage: `/`

---

## Project Setup Instructions

To set up and run the project locally, follow these steps:

1. **Navigate to the Project Directory**  
   Open your terminal and navigate to the `littlelemon` folder:
   ```bash
   cd /Users/ashishsharma/codes/LittleLemon/littlelemon
   ```

2. **Install Dependencies**  
   Ensure you have `pipenv` installed. If not, install it using:
   ```bash
   pip install pipenv
   ```
   Then, install the required dependencies:
   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**  
   Activate the virtual environment created by `pipenv`:
   ```bash
   pipenv shell
   ```

4. **Run Database Migrations**  
   Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**  
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**  
   Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

### Accessing the Static HTML Page

Once the development server is running, you can access the static HTML homepage by navigating to:

```plaintext
http://127.0.0.1:8000/
```

## Testing the APIs

You can use tools like Postman or curl to test the APIs. Ensure you have the necessary authentication tokens for endpoints that require authentication.

## Additional Notes

- The project uses MySQL as the database. Ensure you have MySQL installed and configured with the credentials provided in `settings.py`.
- Static files are served using Django's static file handling. Ensure you have run `collectstatic` if deploying to production.

---

Happy testing!
