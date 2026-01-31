# 🔗 Django URL Shortener

A simple and secure URL Shortener web application built with **Django**, featuring user authentication, URL management, and basic analytics.

This project was developed as part of a **Junior Backend Engineer (Python)** technical assignment to demonstrate backend fundamentals, Django best practices, and clean code structure.

---

## 🚀 Features

### ✅ Core Features
* **User Registration & Auth:** Secure login/logout system.
* **URL Management:** Authenticated users can create, view, and delete their own short URLs.
* **Base62 Generation:** Automatic short code generation for clean URLs.
* **Redirection:** Seamlessly redirect short URLs to original destinations.
* **Click Tracking:** Real-time click count tracking for each link.
* **Dashboard:** Manage all your links and see their creation timestamps.
---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (default, can be replaced)
* **Authentication:** Django built-in auth system
* **Frontend:** Django Templates (HTML)
* **Tools:** Developed using **VS Code**
* **Others:** Pillow, qrcode (optional bonus)

---

## 📂 Project Structure
```text
urlshortener/
├── shortener/
│   ├── migrations/
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── create.html
│   │   └── registration/
│   │       └── login.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── utils.py
├── urlshortener/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions
1️⃣ Clone the Repository
    <pre>git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    </pre>
2️⃣ Create Virtual Environment
    <pre>python -m venv venv
    source venv/bin/activate
    # Windows:
    # venv\Scripts\activate
    </pre>
3️⃣ Install Dependencies
    <pre>pip install django pillow qrcode
    </pre>
4️⃣ Apply Migrations
    <pre>python manage.py makemigrations
    python manage.py migrate
</pre>
5️⃣ Create Superuser (Optional)
    <pre>python manage.py createsuperuser
</pre>
6️⃣ Run Development Server
    <pre>python manage.py runserver
</pre>
Open browser:
  <pre>http://127.0.0.1:8000/
</pre>
---

## 🔐 Authentication
 * Only authenticated users can:
     * Create short URLs
     * View their dashboard
     * Manage (delete) their URLs
 * Django’s built-in authentication system is used for secure session handling.

---

## 🔁 How URL Shortening Works
 * When a user submits a long URL:
     * A Base62 random string is generated as the short code
     * The short code is stored uniquely in the database
 * When the short URL is accessed:
     * User is redirected to the original URL
     * Click count is incremented
 * If expiration time is set and exceeded: 
     * The URL becomes inaccessible

---

## 📊 Analytics
 * Each shortened URL tracks:
     * Total number of clicks
     * Creation date
     * Expiration status (if enabled)
 * This data is visible in the user dashboard.

---

## 🔒 Security Considerations
 * Users can only view and manage their own URLs
 * Protected routes use @login_required
 * Django ORM prevents SQL injection
 * Server-side validation for custom short URLs
 
---

## 🌐 Deployment
The application can be deployed on:
 * Render
 * Railway
 * PythonAnywhere
Make sure:
 * DEBUG = False
 * Set ALLOWED_HOSTS
 * Use environment variables for secrets

---

## 📌 Future Improvements
 * URL edit functionality
 * Detailed analytics (IP, timestamp)
 * REST API version (Django REST Framework)
 * Rate limiting
 * Custom domain support

---

## 🧑‍💻 Author
GitHub: https://github.com/mesworup

---

## 📄 License
This project is created for evaluation and learning purposes.
