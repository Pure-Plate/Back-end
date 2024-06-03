# CORS (Cross-Origin Resource Sharing) settings
# Settings for enabling Cross-Origin Resource Sharing, allowing resources to be shared across different origins

CORS_ORIGIN_ALLOW_ALL = True  # Allow CORS for all origins

CORS_ALLOW_CREDENTIALS = True  # Allow credentials for CORS requests

# List of allowed origins (domains)
# This is used instead of CORS_ALLOW_ORIGIN setting, and '*' allows all origins
CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',  # Allow from localhost:3000
    'http://127.0.0.1:3001',  # Allow from localhost:3001
    'https://www.pureplate.site:80',  # Allow from pureplate.site (http) on port 80
    'https://pureplate.site:80',  # Allow from pureplate.site (http) on port 80
    'http://www.pureplate.site:80',  # Allow from pureplate.site (http) on port 80
    'http://pureplate.site:80',  # Allow from pureplate.site (http) on port 80
    'https://www.pureplate.site:443',  # Allow from pureplate.site (https) on port 443
    'https://pureplate.site:443',  # Allow from pureplate.site (https) on port 443
    'http://www.pureplate.site:443',  # Allow from pureplate.site (https) on port 443
    'http://pureplate.site:443',  # Allow from pureplate.site (https) on port 443
)

CORS_ALLOW_METHODS = [
    'DELETE',  # Allow DELETE method
    'GET',  # Allow GET method
    'OPTIONS',  # Allow OPTIONS method
    'PATCH',  # Allow PATCH method
    'POST',  # Allow POST method
    'PUT',  # Allow PUT method
]

CORS_ALLOW_HEADERS = [
    'accept',  # Allow accept header
    'accept-encoding',  # Allow accept-encoding header
    'authorization',  # Allow authorization header
    'content-type',  # Allow content-type header
]
