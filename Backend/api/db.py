"""
MongoDB client layer for SkillSwap backend.

This module provides a centralized MongoDB client with helper functions
for database operations and connection management.
"""

import logging
from typing import Optional
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

from skillswap.settings_env import get_mongodb_uri

logger = logging.getLogger(__name__)

# Global MongoDB client instance
_client: Optional[MongoClient] = None
_database: Optional[Database] = None


def get_client() -> MongoClient:
    """
    Get or create MongoDB client instance.
    
    Returns:
        MongoClient instance
        
    Raises:
        ConnectionFailure: If unable to connect to MongoDB
    """
    global _client
    
    if _client is None:
        try:
            mongodb_uri = get_mongodb_uri()
            logger.info(f"Connecting to MongoDB at: {mongodb_uri}")
            
            _client = MongoClient(
                mongodb_uri,
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                connectTimeoutMS=5000,
                socketTimeoutMS=5000
            )
            
            # Test the connection
            _client.admin.command('ping')
            logger.info("Successfully connected to MongoDB")
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise ConnectionFailure(
                f"Unable to connect to MongoDB. Please check your MONGODB_URI "
                f"and ensure MongoDB is running. Error: {e}"
            )
    
    return _client


def get_database(name: str = 'skillswap') -> Database:
    """
    Get database instance.
    
    Args:
        name: Database name (default: 'skillswap')
        
    Returns:
        Database instance
    """
    global _database
    
    if _database is None:
        client = get_client()
        _database = client[name]
        logger.info(f"Using database: {name}")
    
    return _database


def get_collection(name: str) -> Collection:
    """
    Get collection by name.
    
    Args:
        name: Collection name
        
    Returns:
        Collection instance
    """
    db = get_database()
    collection = db[name]
    logger.debug(f"Accessing collection: {name}")
    return collection


def health_check() -> bool:
    """
    Test MongoDB connection health.
    
    Returns:
        True if connection is healthy, False otherwise
    """
    try:
        client = get_client()
        # Ping the database
        client.admin.command('ping')
        logger.info("MongoDB health check passed")
        return True
    except Exception as e:
        logger.error(f"MongoDB health check failed: {e}")
        return False


def close_connection() -> None:
    """
    Gracefully close MongoDB connection.
    """
    global _client, _database
    
    if _client:
        try:
            _client.close()
            logger.info("MongoDB connection closed")
        except Exception as e:
            logger.error(f"Error closing MongoDB connection: {e}")
        finally:
            _client = None
            _database = None


def get_connection_info() -> dict:
    """
    Get MongoDB connection information.
    
    Returns:
        Dictionary with connection details
    """
    try:
        client = get_client()
        server_info = client.server_info()
        return {
            'connected': True,
            'version': server_info.get('version'),
            'host': client.address[0] if client.address else 'unknown',
            'port': client.address[1] if client.address else 'unknown',
            'database': get_database().name
        }
    except Exception as e:
        return {
            'connected': False,
            'error': str(e)
        }


# Initialize connection on module import
try:
    get_client()
    logger.info("MongoDB client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize MongoDB client: {e}")
    # Don't raise here to allow Django to start and show proper error messages
