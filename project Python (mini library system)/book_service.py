class BookService:
    def __init__(self, conn):
        self.conn = conn

    def add_book(self, title, author):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO books (title, author) VALUES (%s, %s)",
                    (title, author)
                )
            self.conn.commit()
            print("Book added successfully.")
        except Exception as e:
            print("Error adding book:", e)
            self.conn.rollback()

    def remove_book(self, book_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM borrowed WHERE book_id = %s", (book_id,))
                cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
            self.conn.commit()
            print("Book removed.")
        except Exception as e:
            print("Error removing book:", e)
            self.conn.rollback()

    def get_all_books(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, title, author FROM books")
            return cur.fetchall()
