import configparser
import os
import pathlib
import sys

BASE_DIR = pathlib.Path(sys.argv[0]).parents[0].resolve()
ENV_FILE = BASE_DIR / ".env"

if not os.path.isfile(ENV_FILE):
    ENV_FILE = BASE_DIR / ".env.cfg"


def dotenv(filepath=ENV_FILE):
    """Load Environment Variables"""

    # Load
    __config = configparser.ConfigParser()
    with open(filepath, "r") as file:
        text = file.read()
        text = f"[env]\n{text}"
    __config.read_string(text)

    # Config
    config = __config["env"]
    # Set-Environment Variables
    for (key, val) in config.items():
        os.environ.setdefault(key, val)
