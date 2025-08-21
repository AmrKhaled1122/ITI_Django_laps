class BorrowService:
    def __init__(self, conn):
        self.conn = conn

    def borrow_book(self, user_id, book_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id FROM books WHERE id = %s", (book_id,))
                if not cur.fetchone():
                    print("Book not found.")
                    return

                cur.execute("SELECT id FROM borrowed WHERE user_id = %s AND book_id = %s", (user_id, book_id))
                if cur.fetchone():
                    print("You already borrowed this book.")
                    return

                cur.execute("SELECT COUNT(*) FROM borrowed WHERE user_id = %s", (user_id,))
                if cur.fetchone()[0] >= 3:
                    print("You can only borrow up to 3 books.")
                    return

                cur.execute("INSERT INTO borrowed (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
            self.conn.commit()
            print("Book borrowed successfully.")
        except Exception as e:
            print("Error borrowing book:", e)
            self.conn.rollback()

    def return_book(self, user_id, book_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id FROM borrowed WHERE user_id = %s AND book_id = %s", (user_id, book_id))
                if not cur.fetchone():
                    print("You didn't borrow this book.")
                    return

                cur.execute("DELETE FROM borrowed WHERE user_id = %s AND book_id = %s", (user_id, book_id))
            self.conn.commit()
            print("Book returned.")
        except Exception as e:
            print("Error returning book:", e)
            self.conn.rollback()

    def get_user_borrowed_books(self, user_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT b.id, b.title, b.author
                FROM books b
                JOIN borrowed br ON b.id = br.book_id
                WHERE br.user_id = %s
            """, (user_id,))
            return cur.fetchall()
