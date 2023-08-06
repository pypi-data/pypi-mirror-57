"""Tests for :mod:`ligo.requests.user_agent`."""
import pytest

from .. import __version__
from .. import Session

# FIXME: Python 2
pytest.importorskip('pytest_httpserver')


def test_user_agent(socket_enabled, httpserver):
    expected_user_agent = 'ligo.requests/{}'.format(__version__)

    httpserver.expect_oneshot_request(
        '/', headers={'User-Agent': expected_user_agent}
    ).respond_with_data(
        'OK'
    )

    url = httpserver.url_for('/')
    client = Session(url)
    with httpserver.wait():
        client.get(url)
