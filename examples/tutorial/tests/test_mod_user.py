from flask import session
import pytest
from flaskr.db import get_db

def test_update_email(client, auth, app):
    auth.login()
    
    assert client.get("/auth/updateemail").status_code == 200

    client.post("/auth/updateemail", data={"new_email": "updated@example.com"})
    
    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        

        assert user["email"] == "updated@example.com"



def test_delete_user(client, auth, app):
    auth.login()
    response = client.post("/auth/deleteUser")

    assert "Location" in response.headers
    assert response.headers["Location"] == "/"
     
    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        
        assert user is None

