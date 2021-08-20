from core.roles import ROLES

from .base import *
from .i18n import *

# Change Default Account Handler
AUTH_USER_MODEL = "users.User"

# Include Core Apps
INSTALLED_APPS += [
    # Filters
    "django_filters",
    # GraphQL
    "graphene_django",
    # GraphDJ
    "graphdj",
    # CORS
    # "corsheaders",
]

# GraphQL -> Graphene
GRAPHENE = {
    "ATOMIC_MUTATIONS": True,
    "RELAY_CONNECTION_MAX_LIMIT": 100,
}

# Add your <project-apps> here.
GRAPHDJ = {
    "ADMIN": True,
    "CAMELCASE": True,
    "ROLES_ACCESS": ROLES,
    "DEFAULT_ROLE": 0,
    "QUERIES_INFO": "Awesome Queries!",
    "MUTATIONS_INFO": "Awesome Mutations!",
    "ROLES": {
        # ...
    },
    "APPS": [
        # ...
    ],
}
INSTALLED_APPS.extend(GRAPHDJ["APPS"])
