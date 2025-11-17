# -*- coding: utf-8 -*-
import os, sqlite3
from datetime import datetime

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineRightIconListItem, IconRightWidget


class DB:
    def __init__(self, db_path: str):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._ensure_schema()

    def _conn(self):
        return sqlite3.connect(self.db_path)

    def _ensure_schema(self):
        with self._conn() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS tareas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    texto TEXT NOT NULL,
                    ts   TEXT NOT NULL
                )
            """)

    def agregar(self, texto: str):
        if not texto.strip():
            return
        with self._conn() as con:
            con.execute(
                "INSERT INTO tareas(texto, ts) VALUES(?, ?)",
                (texto.strip(), datetime.now().isoformat(timespec="seconds"))
            )

    def borrar(self, tarea_id: int):
        with self._conn() as con:
            con.execute("DELETE FROM tareas WHERE id=?", (tarea_id,))

    def listar(self):
        with self._conn() as con:
            cur = con.execute("SELECT id, texto, ts FROM tareas ORDER BY id DESC")
            return cur.fetchall()


class MiappApp(MDApp):
    def build(self):
        self.title = "Mis Tareas (SQLite)"
        self.theme_cls.primary_palette = "Blue"
        # No usamos Builder; Kivy cargará automáticamente miapp.kv por el nombre de la clase
        return super().build()

    def on_start(self):
        # Ruta interna persistente (funciona en Windows/Android sin platform/Clock/ListProperty)
        db_dir = os.path.join(self.user_data_dir, "data")
        self._db = DB(os.path.join(db_dir, "tareas.db"))
        self.refrescar_lista()

    # ============ LÓGICA DE UI ============
    def agregar_tarea(self, texto: str):
        if not texto.strip():
            Snackbar(text="Escribe algo primero").open()
            return
        self._db.agregar(texto)
        self.root.ids.input_tarea.text = ""
        self.refrescar_lista()
        Snackbar(text="Guardado").open()

    def borrar_tarea(self, tarea_id: int):
        self._db.borrar(tarea_id)
        self.refrescar_lista()
        Snackbar(text="Tarea borrada").open()

    def refrescar_lista(self):
        cont = self.root.ids.lista
        cont.clear_widgets()
        for (tarea_id, texto, ts) in self._db.listar():
            item = OneLineRightIconListItem(text=f"{texto}  · {ts}")
            icon = IconRightWidget(
                icon="trash-can-outline",
                on_release=lambda w, tid=tarea_id: self.borrar_tarea(tid)
            )
            item.add_widget(icon)
            cont.add_widget(item)


if __name__ == "__main__":
    MiappApp().run()
