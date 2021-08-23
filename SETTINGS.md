# **Settings**.py — Example
> 
```py
import os
import sys

from core.roles import ROLES

# Include apps/
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Include Core Apps
INSTALLED_APPS += [
    # Filters
    "django_filters",
    # GraphQL
    "graphene_django",
    # GraphDJ
    "graphdj",
    # CORS
    #"corsheaders",
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
    "LOGGING": True,
    "ROLES_ACCESS": ROLES,
    "DEFAULT_ROLE": 1,
    "QUERIES_INFO": "Awesome Queries!",
    "MUTATIONS_INFO": "Awesome Mutations!",
    "ROLES": {
        0: "admin",
        1: "customer",
        2: "employee",
        3: "manager",
        # etc . . . 
    },
    "APPS": [
        "app_1",
        "app_2",
        "app_3",
        # etc . . . 
    ],
}
INSTALLED_APPS.extend(GRAPHDJ["APPS"])
```