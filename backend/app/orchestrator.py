"""Orquestador: recibe el pedido de Karina y lo manda al especialista correcto.

Por ahora rutea por palabras clave (simple y predecible). Mas adelante puede
rutear con el modelo. No ejecuta nada hacia afuera: eso lo frena la cola de aprobaciones.
"""
from .agents.administrativo import Administrativo

RUTAS = {
    "administrativo": ["entrega", "cotiz", "pendiente", "seguimiento", "resumen", "oc ", "orden de compra", "produccion"],
    "financiero": ["pago", "moroso", "cobr", "factur", "consecutivo"],
    "cm_seo": ["lead", "linkedin", "web", "seo", "contenido", "post"],
}


class Orquestador:
    def __init__(self, config, llm, aprobaciones, data_dir):
        self.config = config
        self.especialistas = {
            "administrativo": Administrativo(llm, aprobaciones, data_dir,
                                             tuple(config.get("seguimiento_cotizaciones_horas", [25, 72])))
        }

    def elegir(self, texto):
        t = texto.lower() + " "
        for nombre, claves in RUTAS.items():
            if any(c in t for c in claves):
                return nombre
        return None

    def atender(self, texto, ahora=None):
        nombre = self.elegir(texto)
        if nombre is None:
            return "No estoy seguro de que especialista corresponde. Podes decirme si es sobre entregas/cotizaciones, pagos/facturacion o leads?"
        if nombre not in self.especialistas:
            prio = self.config["agents"][nombre]["prioridad"]
            return "Eso le toca al agente '%s', que todavia no esta construido (prioridad %d en el plan)." % (nombre, prio)
        return self.especialistas[nombre].resumen(ahora)
