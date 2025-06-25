
# 🏢 Booking App API

A role-based workspace booking system built with Django Rest Framework, designed to streamline the process of reserving and managing office spaces. This API allows users to view workspace availability, book rooms based on permissions, and prevent conflicts through intelligent scheduling rules.

## 🚀 Features

- 📅 **Real-Time Booking** – Reserve workspaces based on up-to-date availability.
- 🧑‍💼 **Role-Based Access** – Different roles with different levels of booking and viewing permissions (Admin, Manager, Staff).
- 🚫 **Conflict Prevention** – Logic to prevent overlapping or duplicate bookings.
- 🔍 **Advanced Filtering** – Filter by time, date, workspace type, location, and more.
- 🔐 **Secure Authentication** – JWT-based login with protected routes.


---

## ⚙️ Technologies Used

- **Python 3.11+**
- **Django 5+**
- **Django REST Framework**
- **SQLite**
- **JWT Authentication**

---

## 📁 Project Structure

```
booking_app/
├── bookings/           # Booking logic, availability rules
├── workspaces/         # Workspace types and metadata
├── users/              # Custom user roles and permissions
├── core/               # Project-level configs and middleware
├── requirements.txt
└── manage.py
```

---

## 🔐 Authentication & Roles

**JWT Authentication** is used for all protected routes. Each user has an assigned role:

- Admin: Manage users, bookings, workspaces
- Manager: Book and view all workspaces in hub
- Staff: View availability and make personal bookings

```bash
# Get JWT Token
POST /api/token/




---

## 📦 API Endpoints Overview

| Method | Endpoint                        | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| GET    | /api/bookings/                   | View bookings (filtered by role)            |
| POST   | /api/bookings/                   | Create a new booking                        |
| PUT    | /api/bookings/<id>/              | Update a booking                            |
| DELETE | /api/bookings/<id>/              | Cancel a booking                            |
| GET    | /api/workspaces/                 | List all workspaces                         |
| GET    | /api/workspaces/available/       | Filter available spaces                     |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- PostgreSQL
- pip

### Setup

```bash
git clone https://github.com/Akins-Coded/booking-app-api.git
cd booking-app-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🎯 Business Logic Highlights

- ⏳ Time-slot-based availability logic
- 🚦 Prevent double bookings per user and per room
- 🎯 Auto-assign user’s workspace permissions upon registration
- 🔁 Centralized workspace/hub model supports scalability

---

## 🌐 Future Improvements

- 📅 Calendar UI integration for frontend
- 🔔 Email or in-app booking reminders
- 📊 Admin analytics dashboard
- 🏢 Multi-org & multi-hub support

---

## 🤝 Contributing

Have an idea or improvement? Open a pull request or issue!

---

## 📬 Contact

**Akindipe Muheez Omogbolahan**  
📧 Email: [akindipemuheez@outlook.com](mailto:akindipemuheez@outlook.com)  
🌐 [Linktree](https://linktr.ee/akinscoded)  
🔗 [LinkedIn](https://www.linkedin.com/in/akinscoded)  
💻 [GitHub](https://github.com/Akins-Coded)

---

_Part of my portfolio showcasing scalable backend solutions for real-world use cases._
