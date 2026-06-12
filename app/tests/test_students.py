def test_create_student(client):
    """POST /students should create and return a student record."""
    payload = {"reg_no": "2312102", "name": "Test Student", "course": "DevOps"}
    response = client.post("/students", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["reg_no"] == "2312102"
    assert data["name"] == "Test Student"
    assert "id" in data


def test_get_students_empty(client):
    """GET /students should return empty list when no records exist."""
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []


def test_get_students_after_create(client):
    """GET /students should return records after a POST."""
    payload = {"reg_no": "2312999", "name": "Another Student", "course": "Cloud"}
    client.post("/students", json=payload)
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_student_by_reg_no(client):
    """GET /students/{reg_no} should return the matching student."""
    payload = {"reg_no": "2312555", "name": "Specific Student", "course": "AI"}
    client.post("/students", json=payload)
    response = client.get("/students/2312555")
    assert response.status_code == 200
    assert response.json()["name"] == "Specific Student"


def test_get_student_not_found(client):
    """GET /students/{reg_no} should return 404 if not found."""
    response = client.get("/students/0000000")
    assert response.status_code == 404
