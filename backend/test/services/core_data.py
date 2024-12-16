"""Helper data file that is used commonly for users, roles, and permissions.

Rather than importing each of these data insertion fixtures directly into tests,
this module serves as a helper to bring them all in at once.
"""

import pytest
from sqlalchemy.orm import Session
from .demo_data import insert_demo_data

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

@pytest.fixture(autouse=True)
def setup_insert_data_fixture(db_session: Session):
    insert_demo_data(db_session)
    db_session.commit()
    yield
