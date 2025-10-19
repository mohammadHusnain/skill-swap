# SkillSwap - Module 1: Project Foundation

## Project Overview

**SkillSwap** is a full-stack crowd-powered skill exchange network web application that connects people to teach and learn skills from each other. Unlike traditional tutoring marketplaces, SkillSwap focuses on peer-to-peer skill sharing where users can both teach and learn skills in a collaborative environment.

### Core Concept
- **Not a tutoring marketplace** - Users exchange skills mutually
- **Crowd-powered** - Community-driven skill sharing
- **Peer-to-peer** - Direct connections between users
- **Skill-based matching** - Smart algorithm connects compatible users

## Tech Stack

### Backend
- **Framework**: Django 5.2.7 with Django REST Framework
- **Database**: MongoDB (using djongo for Django integration)
- **Authentication**: JWT with SimpleJWT
- **Real-time**: Django Channels for WebSocket support
- **Payments**: Stripe API (test mode)
- **CORS**: django-cors-headers for frontend integration

### Frontend
- **Framework**: Next.js 15 with App Router
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Animations**: Framer Motion, GSAP, React Spring
- **HTTP Client**: Axios
- **Language**: JavaScript (ES6+)

### Development Tools
- **Version Control**: Git
- **Environment Management**: python-dotenv
- **Package Management**: pip (Python), npm (Node.js)

## Module 1: Project Foundation ✅

This module establishes the complete project foundation with both backend and frontend setup.

### Backend Setup ✅

#### 1. Django Project Structure ✅
- **Project**: `skillswap` (main Django project)
- **App**: `api` (main API application)
- **Configuration**: Complete Django settings with MongoDB integration

#### 2. Dependencies & Configuration ✅
- **requirements.txt**: All necessary packages installed
  - Django 5.2.7
  - Django REST Framework
  - djongo (MongoDB integration)
  - django-cors-headers
  - djangorestframework-simplejwt
  - channels (WebSocket support)
  - dj-rest-auth
  - stripe (payment processing)
  - python-dotenv

#### 3. Database Configuration ✅
- **MongoDB**: Configured with djongo
- **Connection**: `mongodb://localhost:27017/skillswap`
- **Environment Variables**: MongoDB URI configurable via .env

#### 4. Authentication Setup ✅
- **JWT Authentication**: SimpleJWT configured
- **Token Settings**: 60-minute access, 7-day refresh
- **Security**: Token rotation and blacklisting enabled

#### 5. API Configuration ✅
- **REST Framework**: JSON rendering, pagination
- **CORS**: Configured for localhost:3000 (frontend)
- **Permissions**: Authenticated users by default

#### 6. WebSocket Support ✅
- **ASGI**: Configured for real-time communication
- **Channels**: Ready for messaging system
- **Routing**: WebSocket URL routing prepared

#### 7. Stripe Integration ✅
- **Test Mode**: Configured for development
- **Environment Variables**: Secret and publishable keys
- **Payment Processing**: Ready for future implementation

#### 8. Project Files ✅
- **settings.py**: Complete Django configuration
- **urls.py**: URL routing setup
- **asgi.py**: ASGI application configuration
- **env.example**: Environment variables template
- **.gitignore**: Python/Django specific ignores
- **README.md**: Comprehensive backend documentation

### Frontend Setup ✅

#### 1. Next.js 15 Project ✅
- **Framework**: Next.js 15 with App Router
- **Language**: JavaScript (ES6+)
- **Routing**: File-based routing system
- **Performance**: Server Components by default

#### 2. Styling & UI ✅
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: Modern, accessible UI components
- **Responsive**: Mobile-first design approach

#### 3. Animation Libraries ✅
- **Framer Motion**: Declarative animations
- **GSAP**: High-performance animations
- **React Spring**: Physics-based animations
- **Axios**: HTTP client for API communication

#### 4. Project Structure ✅
```
Frontend/skillswap-frontend/
├── src/
│   └── app/                 # Next.js App Router
│       ├── globals.css      # Global styles
│       ├── layout.js        # Root layout
│       └── page.js          # Home page
├── public/                  # Static assets
├── package.json            # Dependencies and scripts
├── next.config.mjs         # Next.js configuration
├── tailwind.config.js      # Tailwind CSS configuration
├── components.json         # shadcn/ui configuration
└── env.example            # Environment variables template
```

#### 5. Environment Configuration ✅
- **API Integration**: Backend API URL configuration
- **WebSocket**: Real-time communication setup
- **Stripe**: Frontend payment integration
- **App Settings**: Branding and configuration

#### 6. Documentation ✅
- **README.md**: Comprehensive frontend documentation
- **Setup Instructions**: Complete installation guide
- **Environment Variables**: Clear configuration examples
- **Integration Guide**: Backend connection details

## Project Architecture

### Directory Structure
```
skill-swap/
├── Backend/
│   ├── skillswap/          # Django project
│   ├── api/                # API application
│   ├── manage.py           # Django management
│   ├── requirements.txt     # Python dependencies
│   ├── env.example         # Environment template
│   └── README.md           # Backend documentation
├── Frontend/
│   └── skillswap-frontend/ # Next.js application
│       ├── src/app/        # App Router
│       ├── public/         # Static assets
│       ├── package.json    # Node dependencies
│       ├── env.example     # Environment template
│       └── README.md       # Frontend documentation
├── LICENSE
└── README.md               # Project overview
```

### Data Flow
1. **Frontend** (Next.js) → **API Calls** (Axios) → **Backend** (Django)
2. **Backend** (Django) → **Database** (MongoDB) → **Response** (JSON)
3. **Real-time** (WebSocket) → **Channels** → **Frontend** (React)

## Development Workflow

### Backend Development
1. **Virtual Environment**: `python -m venv venv`
2. **Dependencies**: `pip install -r requirements.txt`
3. **Environment**: Copy `env.example` to `.env`
4. **Database**: Start MongoDB service
5. **Server**: `python manage.py runserver`

### Frontend Development
1. **Dependencies**: `npm install`
2. **Environment**: Copy `env.example` to `.env.local`
3. **Server**: `npm run dev`
4. **Build**: `npm run build`

## Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
MONGODB_URI=mongodb://localhost:27017/skillswap
JWT_SECRET=your-jwt-secret-key-here
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key_here
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key_here
NEXT_PUBLIC_APP_NAME=SkillSwap
NEXT_PUBLIC_APP_DESCRIPTION=A crowd-powered skill exchange network
```

## Module 2: Environment & Config Loader + MongoDB Client ✅

This module implements centralized configuration management with validation and a dedicated MongoDB client layer.

### Backend Implementation ✅

#### 1. Centralized Environment Configuration ✅
- **File**: `Backend/skillswap/settings_env.py`
- **Function**: `get_env(key, required=True, default=None)` with fail-fast behavior
- **Validation**: All required environment variables validated at Django startup
- **Error Handling**: Descriptive error messages for missing variables

**Required Environment Variables:**
- `SECRET_KEY` - Django secret key
- `MONGODB_URI` - MongoDB connection string  
- `JWT_SECRET` - JWT signing secret
- `STRIPE_SECRET_KEY` - Stripe secret key (test mode)
- `STRIPE_PUBLISHABLE_KEY` - Stripe publishable key (test mode)
- `HF_TOKEN` - Hugging Face API token for ML model integration

**Optional Variables:**
- `DEBUG` - Debug mode (defaults to False)

#### 2. MongoDB Client Layer ✅
- **File**: `Backend/api/db.py`
- **Client**: `pymongo.MongoClient` with connection validation
- **Helper Functions**:
  - `get_database()` - Returns database instance
  - `get_collection(name)` - Returns collection by name
  - `health_check()` - Tests MongoDB connection
  - `close_connection()` - Gracefully closes connection
  - `get_connection_info()` - Returns connection details

#### 3. Updated Django Settings ✅
- **File**: `Backend/skillswap/settings.py`
- **Integration**: Uses `settings_env.get_env()` instead of `os.getenv()`
- **Validation**: Environment variables validated at Django startup
- **Fail-Fast**: Application fails with clear error messages if required vars missing

#### 4. Environment Template ✅
- **File**: `Backend/env.example`
- **Added**: `HF_TOKEN` for Hugging Face API integration
- **Complete**: All required variables documented with examples

### Frontend Implementation ✅

#### 5. Environment Variable Validation ✅
- **File**: `Frontend/skillswap-frontend/next.config.mjs`
- **Validation**: Required variables checked at dev/build start
- **Fail-Fast**: Process exits with descriptive error if variables missing
- **Required Variables**:
  - `NEXT_PUBLIC_API_URL` - Backend API URL
  - `NEXT_PUBLIC_WS_URL` - WebSocket URL
  - `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` - Stripe publishable key

### QA Acceptance Criteria ✅

#### Backend Validation ✅
- ✅ Starting backend without required keys throws descriptive error messages
- ✅ Error messages clearly indicate which keys are missing
- ✅ All required environment variables validated on app start
- ✅ MongoDB connection tested at startup
- ✅ Fail-fast behavior prevents Django from starting with invalid config

#### Frontend Validation ✅
- ✅ Frontend validation works at dev start
- ✅ Missing environment variables cause build to fail with clear messages
- ✅ All required variables validated before application starts

### Usage Examples

#### Backend Environment Configuration
```python
from skillswap.settings_env import get_env, get_mongodb_uri, get_hf_token

# Get required variable (fails if missing)
secret_key = get_env('SECRET_KEY')

# Get optional variable with default
debug = get_env('DEBUG', required=False, default='False')

# Use convenience functions
mongodb_uri = get_mongodb_uri()
hf_token = get_hf_token()
```

#### MongoDB Client Usage
```python
from api.db import get_database, get_collection, health_check

# Get database and collection
db = get_database()
users = get_collection('users')

# Health check
if health_check():
    print("MongoDB connection is healthy")

# Use collection
user_doc = users.find_one({'email': 'user@example.com'})
```

#### Frontend Environment Validation
```javascript
// next.config.mjs automatically validates these at startup:
// NEXT_PUBLIC_API_URL=http://localhost:8000/api
// NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws  
// NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
```

### Error Handling Examples

#### Backend Missing Variables
```
EnvironmentError: Required environment variable 'HF_TOKEN' is not set or is empty. 
Please check your .env file and ensure all required variables are configured.
```

#### Frontend Missing Variables
```
❌ Missing required environment variables:
   - NEXT_PUBLIC_API_URL
   - NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY

💡 Please check your .env.local file and ensure all required variables are configured.
   See env.example for reference.
```

### Integration Benefits

1. **Centralized Configuration**: Single source of truth for environment variables
2. **Fail-Fast Validation**: Immediate feedback on configuration issues
3. **Clear Error Messages**: Descriptive errors help developers fix issues quickly
4. **MongoDB Client Layer**: Reusable database operations with connection management
5. **Development Safety**: Prevents applications from starting with invalid configuration
6. **Production Ready**: Robust error handling and validation for deployment

Module 2 successfully establishes robust configuration management and database connectivity for the SkillSwap application.

## Next Steps (Future Modules)

### Module 3: User Management
- User registration and authentication
- Profile management
- Skill categorization system

### Module 4: Skill Matching
- Smart matching algorithm
- Skill compatibility scoring
- User recommendation system

### Module 5: Messaging System
- Real-time chat implementation
- WebSocket integration
- Message history and persistence

### Module 6: Payment Integration
- Stripe payment processing
- Skill exchange transactions
- Payment history and receipts

### Module 7: Advanced Features
- Skill verification system
- Rating and review system
- Advanced search and filtering

## Testing & Quality Assurance

### Backend Testing
- Django test framework
- API endpoint testing
- Database integration tests

### Frontend Testing
- Next.js testing utilities
- Component testing
- Integration testing

## Deployment Considerations

### Backend Deployment
- Django production settings
- MongoDB Atlas integration
- Environment variable management
- Static file serving

### Frontend Deployment
- Next.js production build
- Static site generation
- CDN integration
- Performance optimization

## Security Considerations

### Authentication
- JWT token security
- Password hashing
- Session management

### API Security
- CORS configuration
- Rate limiting
- Input validation

### Data Protection
- Environment variable security
- Database access control
- API key management

## Performance Optimization

### Backend
- Database query optimization
- Caching strategies
- API response optimization

### Frontend
- Code splitting
- Image optimization
- Bundle size optimization
- Animation performance

## Conclusion

Module 1 successfully establishes a solid foundation for the SkillSwap application with:

✅ **Complete Backend Setup**: Django with MongoDB, JWT auth, WebSocket support
✅ **Modern Frontend Setup**: Next.js 15 with Tailwind CSS and animation libraries
✅ **Development Environment**: Proper configuration and documentation
✅ **Integration Ready**: Backend and frontend properly configured to work together
✅ **Scalable Architecture**: Clean separation of concerns and modern tech stack

The project is now ready for Module 2 development, focusing on user management and authentication systems.
