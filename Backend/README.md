# SkillSwap Backend

A Django REST Framework backend for the SkillSwap skill exchange platform.

## Features

- Django REST Framework for API endpoints
- MongoDB integration using djongo
- JWT authentication with SimpleJWT
- Django Channels for WebSocket support (ready for messaging)
- CORS configuration for frontend integration
- Stripe integration for payments (test mode)

## Local Setup

### Prerequisites

- Python 3.8+
- MongoDB (local installation or MongoDB Compass)
- Virtual environment (recommended)

### Installation

1. **Clone the repository and navigate to backend:**
   ```bash
   cd Backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables:**
   ```bash
   cp env.example .env
   ```
   Edit `.env` file with your configuration values.

5. **Setup MongoDB:**
   - Install MongoDB locally or use MongoDB Compass
   - Default connection string: `mongodb://localhost:27017/skillswap`
   - Update `MONGODB_URI` in `.env` if using different connection

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## MongoDB Compass Connection

To connect MongoDB Compass to your local database:

1. Open MongoDB Compass
2. Use connection string: `mongodb://localhost:27017/skillswap`
3. Click "Connect"

## API Endpoints

- Admin: `http://localhost:8000/admin/`
- API Root: `http://localhost:8000/api/`

## Project Structure

```
Backend/
├── skillswap/          # Django project settings
├── api/                # Main API application
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── env.example         # Environment variables template
└── .gitignore         # Git ignore rules
```

## Dependencies

- Django 5.2.7
- Django REST Framework
- djongo (MongoDB integration)
- django-cors-headers
- djangorestframework-simplejwt
- channels (WebSocket support)
- dj-rest-auth
- stripe (payment processing)
- python-dotenv
