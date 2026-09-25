# 🏛️ Political Party Management System

A role-based web application built with **Django** for managing members, volunteers, administrators, events, news, gallery content, leadership information, and other organizational data through a centralized platform.

The project focuses on **role-based access control, member management, content management, and a responsive web interface**.

---

## ✨ Features

### 👤 User & Member Management

* Custom user authentication
* Role-based user management
* Member registration
* Member profile management
* Membership ID generation
* QR-code based membership identification
* Member verification
* Membership card generation

### 🔐 Role-Based Access Control

The system supports different user roles with separate permissions and dashboards:

* **Super Admin**
* **Admin**
* **Member**
* **Volunteer**

Each role can access functionality according to its assigned permissions.

### 📊 Admin Dashboard

Administrators can manage:

* Members
* Events
* Gallery
* Leaders
* Manifesto items
* News
* Contact messages

### 📰 Content Management

The CMS module provides management for:

* News
* Events
* Gallery
* Leadership
* Manifesto
* About page
* Contact page
* Donation page

### 🎨 Responsive UI

* Responsive web interface
* Bootstrap-based design
* Custom CSS styling
* Reusable navbar and footer components
* Mobile-friendly layouts

### 🌐 Multilingual Support

The project includes Django internationalization support with Hindi translation resources.

---

## 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend programming       |
| Django     | Web framework             |
| SQLite     | Database                  |
| HTML5      | Page structure            |
| CSS3       | Styling                   |
| JavaScript | Client-side functionality |
| Bootstrap  | Responsive UI             |
| QR Code    | Membership identification |
| Git        | Version control           |
| GitHub     | Source code hosting       |

---

## 📁 Project Structure

```text
PoliticalPartyManagement/
│
├── PoliticalPartyManagement/     # Main Django configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/                     # Authentication & user management
│
├── adminapp/                     # Admin dashboard & management
│
├── members/                      # Member management
│
├── cms/                          # Website content management
│
├── templates/                    # HTML templates
│
├── static/                       # CSS, JavaScript & static assets
│
├── locale/                       # Translation files
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/suryabhushankumar562-a11y/Political-Party-Management-System.git
```

### 2. Navigate to the project

```bash
cd Political-Party-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

After creating a superuser, access the Django admin panel at:

```text
http://127.0.0.1:8000/admin/
```

The project also contains a custom admin application for managing organizational content and members.

---

## 🧩 Main Modules

### Accounts

Handles:

* User authentication
* Custom user model
* User roles
* Account-related functionality

### Members

Handles:

* Member registration
* Member profiles
* Membership IDs
* QR codes
* Verification
* Membership cards

### Admin App

Provides administrative functionality for:

* Member management
* Events
* Gallery
* Leaders
* Manifesto
* News
* Messages

### CMS

Manages public-facing content such as:

* Home
* About
* Events
* Gallery
* Leadership
* News
* Manifesto
* Contact
* Donation

---

## 🔒 Security Notes

Sensitive information should not be committed to the repository.

For production deployment:

* Store `SECRET_KEY` in environment variables
* Configure `DEBUG=False`
* Configure `ALLOWED_HOSTS`
* Use a production database
* Configure secure static/media file handling
* Protect credentials and API keys
* Use HTTPS

---

## 🚀 Future Improvements

Some possible improvements for future versions:

* PostgreSQL database integration
* Email/OTP verification
* Advanced member search and filtering
* Notification system
* REST API
* Online payment integration
* Advanced analytics dashboard
* Cloud deployment
* Automated testing
* CI/CD pipeline

---

## 👨‍💻 Developer

**Ravi Bhushan**

Software Developer | Python • Django • C++ | Web Development

Interested in building practical software solutions and continuously improving development and problem-solving skills.

---

## 📄 License

This project is intended for educational and portfolio purposes.
