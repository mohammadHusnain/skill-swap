"""
Centralized environment configuration loader for SkillSwap backend.

This module provides a centralized way to load and validate environment variables
with fail-fast behavior and descriptive error messages.
"""

import os
from typing import Optional, Union
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class EnvironmentError(Exception):
    """Custom exception for environment configuration errors."""
    pass


def get_env(key: str, required: bool = True, default: Optional[str] = None) -> str:
    """
    Get environment variable with validation and fail-fast behavior.
    
    Args:
        key: Environment variable name
        required: Whether the variable is required (default: True)
        default: Default value if variable is not set and not required
        
    Returns:
        Environment variable value as string
        
    Raises:
        EnvironmentError: If required variable is missing or empty
    """
    value = os.getenv(key)
    
    # Check if value is missing or empty
    if not value:
        if required:
            raise EnvironmentError(
                f"Required environment variable '{key}' is not set or is empty. "
                f"Please check your .env file and ensure all required variables are configured."
            )
        else:
            return default or ""
    
    return value


def validate_required_env_vars() -> None:
    """
    Validate all required environment variables at module import.
    
    This function is called automatically when the module is imported to ensure
    all required configuration is present before Django starts.
    
    Raises:
        EnvironmentError: If any required variables are missing
    """
    required_vars = [
        'SECRET_KEY',
        'MONGODB_URI', 
        'JWT_SECRET',
        'STRIPE_SECRET_KEY',
        'STRIPE_PUBLISHABLE_KEY',
        'HF_TOKEN'
    ]
    
    missing_vars = []
    
    for var in required_vars:
        try:
            get_env(var, required=True)
        except EnvironmentError:
            missing_vars.append(var)
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}. "
            f"Please check your .env file and ensure all required variables are configured. "
            f"See env.example for reference."
        )


# Validate environment variables on import
validate_required_env_vars()


# Convenience functions for common environment variables
def get_secret_key() -> str:
    """Get Django SECRET_KEY."""
    return get_env('SECRET_KEY')


def get_mongodb_uri() -> str:
    """Get MongoDB connection URI."""
    return get_env('MONGODB_URI')


def get_jwt_secret() -> str:
    """Get JWT signing secret."""
    return get_env('JWT_SECRET')


def get_stripe_secret_key() -> str:
    """Get Stripe secret key."""
    return get_env('STRIPE_SECRET_KEY')


def get_stripe_publishable_key() -> str:
    """Get Stripe publishable key."""
    return get_env('STRIPE_PUBLISHABLE_KEY')


def get_hf_token() -> str:
    """Get Hugging Face API token for ML model integration."""
    return get_env('HF_TOKEN')


def get_debug() -> bool:
    """Get DEBUG setting (optional, defaults to False)."""
    debug_value = get_env('DEBUG', required=False, default='False')
    return debug_value.lower() in ('true', '1', 'yes', 'on')
