from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from api.db import health_check, get_connection_info
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def root_view(request):
    """
    Root view that displays API status and available endpoints.
    """
    try:
        # Test SQLite connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            sqlite_status = "connected"
    except Exception as e:
        sqlite_status = f"error: {str(e)}"
        logger.error(f"SQLite health check failed: {e}")
    
    # Test MongoDB connection
    mongodb_healthy = health_check()
    mongodb_info = get_connection_info()
    
    return JsonResponse({
        'message': 'Welcome to SkillSwap Backend API',
        'status': 'healthy' if mongodb_healthy and sqlite_status == "connected" else 'unhealthy',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'api_health': '/api/health/',
            'api_root': '/api/'
        },
        'databases': {
            'sqlite': {
                'status': sqlite_status,
                'type': 'Django ORM (admin, auth, sessions)'
            },
            'mongodb': {
                'status': 'connected' if mongodb_healthy else 'disconnected',
                'type': 'PyMongo (application data)',
                'info': mongodb_info
            }
        },
        'documentation': 'See README.md for API documentation'
    })

def health_check_view(request):
    """
    Health check endpoint that verifies both SQLite and MongoDB connections.
    """
    try:
        # Test SQLite connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            sqlite_status = "connected"
    except Exception as e:
        sqlite_status = f"error: {str(e)}"
        logger.error(f"SQLite health check failed: {e}")
    
    # Test MongoDB connection
    mongodb_healthy = health_check()
    mongodb_info = get_connection_info()
    
    return JsonResponse({
        'status': 'healthy' if mongodb_healthy and sqlite_status == "connected" else 'unhealthy',
        'databases': {
            'sqlite': {
                'status': sqlite_status,
                'type': 'Django ORM (admin, auth, sessions)'
            },
            'mongodb': {
                'status': 'connected' if mongodb_healthy else 'disconnected',
                'type': 'PyMongo (application data)',
                'info': mongodb_info
            }
        },
        'message': 'SkillSwap backend is ready' if mongodb_healthy and sqlite_status == "connected" else 'Some services are unavailable'
    })
