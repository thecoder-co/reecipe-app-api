"""
Test custom django mamagement commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error