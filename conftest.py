"""
Shared pytest fixtures for UPI Fraud Detector tests.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    """FastAPI test client with lifespan events (startup) triggered."""
    with TestClient(app, raise_server_exceptions=True) as test_client:
        yield test_client


@pytest.fixture
def sample_transaction():
    """A valid sample transaction request body for testing."""
    return {
        "user_id": "U12345",
        "amount": 3686.0,
        "session_duration": 156,
        "receiver_transaction_history": 40,
        "transaction_amount_vs_sender_history": 1.5,
        "geographic_disparity": 10009.0,
        "transaction_time_of_day": 10,
        "time_between_link_click_and_transaction": 0,
        "input_timing_consistency": 0.89,
        "keyboard_input_speed": 0.96,
        "input_pause_patterns": 0.10,
        "screen_active_time": 351,
        "geographic_location_vs_ip": 9982.0,
        "background_data_usage": 0.26,
        "pin_entry_speed": 1.21,
        "request_amount_roundness": 1.0,
        "request_acceptance_rate": 0.0,
        "time_to_respond_to_request": 0
    }