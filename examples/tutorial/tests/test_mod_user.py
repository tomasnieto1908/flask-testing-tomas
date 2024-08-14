import pytest
from flaskr.db import get_db

def test_update_email(client, auth, app):
    auth.login()
    
    assert client.get("/update-email/1").status_code == 200

    client.post("/update-email/1", data={"email": "updated@example.com"})
    
    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE id = 1").fetchone()
        

        assert user["email"] == "updated@example.com"


