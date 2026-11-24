"""Linea de comandos para probar el sistema (desde la carpeta backend/):

  python3 -m app.cli pedir "como estan las entregas y cotizaciones?"
  python3 -m app.cli aprobaciones
  python3 -m app.cli aprobar 1
  python3 -m app.cli rechazar 1
"""
import argparse
from datetime import datetime

from .approvals import Aprobaciones
from .config import default_data_dir, load_config
from .llm import LLM
from .orchestrator import Orquestador


def main(argv=None):
    ap = argparse.ArgumentParser(prog="ardic")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pedir")
    p.add_argument("texto")
    p.add_argument("--ahora", help="fecha/hora simulada: YYYY-MM-DD HH:MM")
    sub.add_parser("aprobaciones")
    for c in ("aprobar", "rechazar"):
        sub.add_parser(c).add_argument("id", type=int)
    a = ap.parse_args(argv)

    cfg = load_config()
    aprob = Aprobaciones()
    if a.cmd == "pedir":
        datos = default_data_dir()
        print("(datos: %s)\n" % datos.name)
        orq = Orquestador(cfg, LLM(cfg["model_default"]), aprob, datos)
        ahora = datetime.strptime(a.ahora, "%Y-%m-%d %H:%M") if a.ahora else None
        print(orq.atender(a.texto, ahora))
    elif a.cmd == "aprobaciones":
        filas = aprob.listar()
        if not filas:
            print("No hay nada pendiente de aprobar.")
        for id_, agente, tipo, dest, asunto, cuerpo in filas:
            print("#%d [%s] %s -> %s\n  Asunto: %s\n  %s\n" % (id_, agente, tipo, dest, asunto, cuerpo.replace("\n", "\n  ")))
    else:
        estado = "aprobada" if a.cmd == "aprobar" else "rechazada"
        ok = aprob.decidir(a.id, estado)
        print(("Listo: #%d %s." % (a.id, estado)) if ok else "No encontre un pendiente con ese numero.")
        if ok and estado == "aprobada":
            print("Todavia no hay conexion de envio (tarea IT-4). Copia el borrador y mandalo vos.")


if __name__ == "__main__":
    main()
