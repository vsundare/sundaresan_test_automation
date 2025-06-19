import pytest
from src.flask_area_calculator.app import app


@pytest.fixture
def client():
    """Creates a test client for this application.
    Note that if you are testing for assertions or exceptions in your
        application code, you must set ``app.testing = True`` in order for the
        exceptions to propagate to the test client.  Otherwise, the exception
        will be handled by the application (not visible to the test client) and
        the only indication of an AssertionError or other exception will be a
        500 status code response to the test client."""
    app.config['TESTING'] = True

    """The test client can be used in a ``with`` block to defer the closing down
        of the context until the end of the ``with`` block.  This is useful if
        you want to access the context locals for testing:"""
    with app.test_client() as client:
        yield client