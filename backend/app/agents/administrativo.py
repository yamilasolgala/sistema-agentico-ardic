"""Agente Administrativo de ARDIC (prioridad 1).

Hace UNA cosa: seguimiento de entregas y de cotizaciones.
- Las cuentas (fechas, horas) las hace el codigo, no la IA: asi no inventa.
- La IA (via el adaptador) solo redacta el borrador del mail.
- Nunca envia nada: deja el borrador en la cola de aprobaciones.
"""
import csv
from datetime import datetime, timedelta
from pathlib import Path

SYSTEM = ("Sos el asistente administrativo de ARDIC (empaque flexible grado alimenticio). "
          "Redactas mails de seguimiento breves, formales y cordiales, en espanol, sin emojis. "
          "No menciones precios ni inventes datos que no esten en el pedido.")


def _leer(path):
    p = Path(path)
    if not p.exists():
        return []
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class Administrativo:
    nombre = "administrativo"

    def __init__(self, llm, aprobaciones, data_dir, horas_seguimiento=(25, 72)):
        self.llm = llm
        self.aprobaciones = aprobaciones
        self.data_dir = Path(data_dir)
        self.h1, self.h2 = horas_seguimiento

    def analizar(self, ahora=None):
        ahora = ahora or datetime.now()
        hoy = ahora.date()
        entregas = [e for e in _leer(self.data_dir / "entregas.csv")
                    if e["estado"].strip().lower() != "entregada"]
        vencidas, semana = [], []
        for e in entregas:
            f = datetime.strptime(e["fecha_compromiso"], "%Y-%m-%d").date()
            if f < hoy:
                vencidas.append(e)
            elif f <= hoy + timedelta(days=7):
                semana.append(e)
        seguimientos = []
        for c in _leer(self.data_dir / "cotizaciones.csv"):
            if c["respondida"].strip().lower() == "si":
                continue
            horas = (ahora - datetime.strptime(c["fecha_envio"], "%Y-%m-%d %H:%M")).total_seconds() / 3600
            if horas >= self.h1:
                c = dict(c, horas=int(horas), nivel=2 if horas >= self.h2 else 1)
                seguimientos.append(c)
        return {"vencidas": vencidas, "semana": semana, "seguimientos": seguimientos}

    def _borrador(self, c):
        asunto = "Seguimiento de cotizacion %s" % c["cotizacion"]
        base = ("Estimados %s:\n\nLes escribo para dar seguimiento a la cotizacion %s que les enviamos. "
                "Quedamos atentos a cualquier consulta o ajuste que necesiten.\n\nSaludos cordiales,\nARDIC"
                % (c["cliente"], c["cotizacion"]))
        pedido = "Redacta un mail de seguimiento para la cotizacion %s del cliente %s (enviada hace %d horas). Segundo recordatorio: %s." % (
            c["cotizacion"], c["cliente"], c["horas"], "si" if c["nivel"] == 2 else "no")
        return asunto, self.llm.complete(SYSTEM, pedido, fallback=base)

    def resumen(self, ahora=None):
        a = self.analizar(ahora)
        lineas = ["RESUMEN ADMINISTRATIVO ARDIC", ""]
        lineas.append("Entregas vencidas: %d" % len(a["vencidas"]))
        lineas += ["  - %(oc)s | %(cliente)s | %(producto)s | comprometida %(fecha_compromiso)s" % e for e in a["vencidas"]]
        lineas.append("Entregas que vencen en los proximos 7 dias: %d" % len(a["semana"]))
        lineas += ["  - %(oc)s | %(cliente)s | %(producto)s | comprometida %(fecha_compromiso)s" % e for e in a["semana"]]
        lineas.append("Cotizaciones sin respuesta para seguir: %d" % len(a["seguimientos"]))
        for c in a["seguimientos"]:
            asunto, cuerpo = self._borrador(c)
            id_ = self.aprobaciones.proponer(self.nombre, "mail_seguimiento", c["email"], asunto, cuerpo)
            lineas.append("  - %s | %s | %d hs sin respuesta | seguimiento %d | borrador #%d esperando tu OK"
                          % (c["cotizacion"], c["cliente"], c["horas"], c["nivel"], id_))
        return "\n".join(lineas)
