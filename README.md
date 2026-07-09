# ✨ Mini Social Media App

A sleek, lightweight, and interactive social media platform built using **Django** for the backend and polished with a dreamy, frosted-glass **Aesthetic Sparkly Blue** frontend UI using pure HTML, CSS, and JavaScript.

## 🚀 Features
*   **👥 User Directory & Profiles:** Explore a dedicated directory of all platform users and click their handles to visit their public account dashboards.
*   **➕ Real-Time Follow System:** Follow or unfollow other creators asynchronously with real-time stat-counter updates without reloading the page.
*   **📝 Posts Feed:** A collective hub to read updates from platform creators.
*   **👍 Asynchronous Likes:** Dynamic post-interaction with instantaneous updates powered by JavaScript's Fetch API.

## 🛠️ Tech Stack
*   **Backend:** Django (Python)
*   **Database:** SQLite (Default ORM handling relationships through an implicit junction table architecture)
*   **Frontend:** Custom HTML5, modern CSS3 (Linear gradients, backdrop filters), and Vanilla JavaScript (AJAX/Fetch API)

## 📦 Local Installation Guide

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd mini_social_media
2. **Set Up a Virtual Environment**
Create and activate an isolated environment to manage dependencies securely.
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate on Windows (Command Prompt/PowerShell)
    .venv\Scripts\activate

    # Activate on macOS/Linux
    source .venv/bin/activate

3. **Install Dependencies**
    ```bash
    python -m pip install --upgrade pip
    pip install django pillow
 
4. **Run Migrations**
Set up your local SQLite database tables using Django's built-in migration sytem.
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **reate an Admin Account (Superuser)**
Generate an administrative credential to access the Django admin panel, populate mock data, or manage user accounts.
    ```bash
    python manage.py createsuperuser
(Follow the terminal prompts blindly to define a username, email, and password).

6. **Launch the Local Server**
    ```bash
    python manage.py runserver
Once the server spins up, open your browser and navigate to:
Application Feed and Admin Dashboard Panel

### Security & Optimization Note
This repository includes a strict .gitignore file configuration. Local development components such as temporary runtime directories (__pycache__/), application media states, and the specific database file (db.sqlite3) are explicitly excluded to maintain a production-clean code delivery structure.
