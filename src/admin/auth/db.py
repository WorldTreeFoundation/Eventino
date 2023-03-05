from db import get_db_conn


class AuthDB:
    @staticmethod
    def server_has_admin() -> bool:
        """Check if server has admin

        Returns:
            bool
        """
        conn, cur = get_db_conn()
        cur.execute("SELECT count(*) FROM admin")
        result = cur.fetchone()[0] > 0
        cur.close()
        conn.close()
        return result

    @staticmethod
    def set_admin(user_id: int) -> bool:
        """Set server's admin

        Returns:
            bool: ok status
        """
        conn, cur = get_db_conn()
        cur.execute("INSERT INTO admin VALUES (%s)", (user_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True
