"""Cola de aprobaciones: nada sale hacia afuera sin el OK de Karina.

Los agentes SOLO proponen. Aprobar marca la accion; el envio real todavia
no esta conectado (tarea IT-4 del tracker).
"""
import sqlite3
from datetime import datetime
from pathlib import Path

from .config import ROOT

DB_DEFAULT = ROOT / "data" / "estado.db"


class Aprobaciones:
    def __init__(self, db_path=None):
        db_path = Path(db_path) if db_path else DB_DEFAULT
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(db_path))
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS aprobaciones ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, creado TEXT, agente TEXT, tipo TEXT,"
            "destinatario TEXT, asunto TEXT, cuerpo TEXT, estado TEXT DEFAULT 'pendiente',"
            "decidido TEXT)"
        )
        self.db.commit()

    def proponer(self, agente, tipo, destinatario, asunto, cuerpo):
        """Crea una propuesta pendiente. Si ya hay una igual pendiente, no duplica."""
        row = self.db.execute(
            "SELECT id FROM aprobaciones WHERE estado='pendiente' AND tipo=? "
            "AND destinatario=? AND asunto=?", (tipo, destinatario, asunto)).fetchone()
        if row:
            return row[0]
        cur = self.db.execute(
            "INSERT INTO aprobaciones (creado, agente, tipo, destinatario, asunto, cuerpo) "
            "VALUES (?,?,?,?,?,?)",
            (datetime.now().isoformat(timespec="seconds"), agente, tipo,
             destinatario, asunto, cuerpo))
        self.db.commit()
        return cur.lastrowid

    def listar(self, estado="pendiente"):
        return self.db.execute(
            "SELECT id, agente, tipo, destinatario, asunto, cuerpo FROM aprobaciones "
            "WHERE estado=? ORDER BY id", (estado,)).fetchall()

    def decidir(self, id_, estado):
        assert estado in ("aprobada", "rechazada")
        cur = self.db.execute(
            "UPDATE aprobaciones SET estado=?, decidido=? WHERE id=? AND estado='pendiente'",
            (estado, datetime.now().isoformat(timespec="seconds"), id_))
        self.db.commit()
        return cur.rowcount == 1
