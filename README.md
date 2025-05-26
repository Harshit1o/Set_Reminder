# RemindMeLater - Reminder API Service

![RemindMeLater Logo](https://via.placeholder.com/200x60?text=RemindMeLater)

A powerful Django REST API service for scheduling and managing reminders via Email and SMS.

## Features

- Schedule reminders with specific date and time.
- Support for both Email and SMS notifications.
- RESTful API for easy integration with any frontend or mobile app
- Admin interface for managing reminders
- API documentation with Swagger/ReDoc
- Status tracking of sent reminders

## Table of Contents

- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Making API Requests](#making-api-requests)
- [Admin Interface](#admin-interface)
- [Extending the Project](#extending-the-project)

## Installation

1. Clone the repository:
   ```bash
   git clone
   cd Symplique_assignment
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On MacOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/admin/` to access the admin interface

## Environment Setup

The project uses environment variables for configuration. An `.env` file is included with default settings for development:

```
DEBUG=True
SECRET_KEY=<your-secret-key>
ALLOWED_HOSTS=localhost,127.0.0.1

# Email settings (required for sending email reminders)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password

# Database settings (SQLite by default)
# For PostgreSQL or other databases, uncomment and modify these:
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=remindmelater
# DB_USER=postgres
# DB_PASSWORD=yourpassword
# DB_HOST=localhost
# DB_PORT=5432

TIME_ZONE=UTC
```

To enable email reminders, configure the EMAIL_* settings in the `.env` file.

## Project Structure

```
Symplique_assignment/
│
├── remindmelater/             # Main project directory
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── asgi.py                # ASGI configuration
│   └── wsgi.py                # WSGI configuration
│
├── reminders/                 # Reminders app directory
│   ├── models.py              # Data models for reminders
│   ├── serializers.py         # REST API serializers 
│   ├── views.py               # API views
│   ├── urls.py                # App URL patterns
│   └── admin.py               # Admin interface configuration
│
├── manage.py                  # Django management script
└── .env                       # Environment variables
```

## 📡 API Endpoints

The API provides RESTful endpoints for managing reminders:

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/api/reminders/` | GET | List all reminders |
| `/api/reminders/` | POST | Create a new reminder |
| `/api/reminders/{id}/` | GET | Retrieve a specific reminder |
| `/api/reminders/{id}/` | PUT | Update a reminder (all fields) |
| `/api/reminders/{id}/` | PATCH | Partially update a reminder |
| `/api/reminders/{id}/` | DELETE | Delete a reminder |

API documentation is available at:
- `/redoc/` - ReDoc API documentation

## Models

### Reminder Model

The `Reminder` model manages reminder data with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Optional title for the reminder |
| message | TextField | The content of the reminder message |
| reminder_date | DateField | Date when the reminder should be sent |
| reminder_time | TimeField | Time when the reminder should be sent |
| reminder_type | CharField | Type of reminder: 'EMAIL' or 'SMS' |
| recipient | CharField | Email address or phone number of the recipient |
| created_at | DateTimeField | When the reminder was created (auto-set) |
| is_sent | BooleanField | Whether the reminder has been sent |

## Making API Requests

### Creating a Reminder

```python
import requests
import json

url = "http://localhost:8000/api/reminders/"
data = {
    "title": "Meeting with Client",
    "message": "Don't forget about our meeting at the office!",
    "reminder_date": "2025-05-15",
    "reminder_time": "14:30:00",
    "reminder_type": "EMAIL",
    "recipient": "user@example.com"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
```

### Sample API Response

```json
{
    "id": 1,
    "title": "Meeting with Client",
    "message": "Don't forget about our meeting at the office!",
    "reminder_date": "2025-05-15",
    "reminder_time": "14:30:00",
    "reminder_type": "EMAIL",
    "recipient": "user@example.com",
    "created_at": "2025-05-10T12:00:00Z",
    "is_sent": false
}
```

## Admin Interface

The Django admin interface is configured to provide an easy way to manage reminders. It offers:

- Listing all reminders with key information
- Filtering reminders by type, status, and date
- Search functionality by title, message, and recipient
- Date hierarchy navigation

Access the admin at `http://localhost:8000/admin/` after creating a superuser.

## Extending the Project

### Adding SMS Functionality

To implement SMS sending capability:
1. Install a suitable SMS service library (e.g., Twilio)
2. Create a service class for sending SMS messages
3. Implement a task scheduler to check for pending reminders

### Setting Up a Task Scheduler

To automatically send reminders, you should set up a task scheduler:
1. Install Celery and Redis/RabbitMQ
2. Configure periodic tasks to check for due reminders
3. Implement the sending logic based on reminder type

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ for Symplique Assignment
