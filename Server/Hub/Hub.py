from Server.LocalStorageService.Connection import get_db
from Server.LocalStorageService.Models import create_all, ActiveConnections, drop_all


class Hub:
    create_db_file = open("LocalStorageService/LocalStorage/storage.db", "a+")
    drop_all()
    create_all()
    conn = get_db()

    def add_connection(self, origin_host, origin_port, state):
        new_conn = ActiveConnections(
            origin_url=origin_host,
            origin_port=origin_port,
            state=state
        )
        self.conn.add(new_conn)
        self.conn.commit()
        return new_conn.id

    def del_connection(self, origin_service):
        connection = self.conn.query(ActiveConnections).filter(ActiveConnections.origin_url == origin_service).first()
        self.conn.delete(connection)
        self.conn.commit()

    def get_target_session(self, target_host):
        session = (self.conn.query(ActiveConnections.id).filter(ActiveConnections.origin_url == target_host)
                   .first())
        return session
