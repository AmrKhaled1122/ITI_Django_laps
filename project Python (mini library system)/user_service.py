import bcrypt

class UserService:
    def __init__(self, conn):
        self.conn = conn

    def register_user(self, username, password, role="user"):
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                    (username, hashed_pw, role)
                )
            self.conn.commit()
            print("Registration successful.")
        except Exception as e:
            print("Error during registration:", e)
            self.conn.rollback()

    def authenticate(self, username, password):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, password, role FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result and bcrypt.checkpw(password.encode(), result[1].encode()):
                return {'id': result[0], 'username': username, 'role': result[2]}
        return None
