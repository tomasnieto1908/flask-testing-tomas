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



def test_delete_user(client, auth, app):
    auth.login()
    
    # Realiza la solicitud POST para eliminar al usuario con ID 1
    response = client.post("/delete-user/1")
    
    # Verifica que la respuesta redirige a la página principal (o la ruta que corresponda)
    assert response.headers["Location"] == "/"
    
    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE id = 1").fetchone()
        
        # Verifica que el usuario ha sido eliminado de la base de datos
        assert user is None


