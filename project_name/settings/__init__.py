"""[ OPTIONS ]:
    * development
    * production
    * staging
"""

import os

DJANGO_ENVIRONMENT = os.environ.get("DJANGO_ENVIRONMENT")
ENVIRONMENT = DJANGO_ENVIRONMENT.lower()

# Production
if ENVIRONMENT == "production":
    from .production import *
# Staging
elif ENVIRONMENT == "staging":
    from .staging import *
# Development
else:
    from .development import *
