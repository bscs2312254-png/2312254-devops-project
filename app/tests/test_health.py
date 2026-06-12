def test_health_returns_ok(client):
    """GET /health should return status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["student"] == "2312102"


def test_health_contains_db_field(client):
    """GET /health should include a db connection field."""
    response = client.get("/health")
    data = response.json()
    assert "db" in data
