"""Pytest for FastAPI"""
from fastapi.testclient import TestClient
from hivebox.main import app

client = TestClient(app)

def test_version():
    """Test Version"""
    r = client.get("/version")
    assert r.status_code == 200
    assert "version" in r.json()

def test_temperature():
    """Test Temperature"""
    r = client.get("/temperature")
    assert r.status_code == 200
    assert "average_temperature" in r.json()
    assert "sources_used" in r.json()
    assert "timestamp_checked" in r.json()
