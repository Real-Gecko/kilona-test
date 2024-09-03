# Database settings are read from environment variables
import os

POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")

# Assert that settings are set
assert POSTGRES_PASSWORD
assert POSTGRES_USER
assert POSTGRES_DB
assert POSTGRES_HOST
