#!/usr/bin/env python3
"""
Simple startup script for Django + FastAPI application
"""

import uvicorn
import os
import sys

if __name__ == "__main__":
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    
    # Run the application
    uvicorn.run(
        "mysite.asgi:application",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 