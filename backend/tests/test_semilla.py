import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from app.approvals import Aprobaciones
from app.config import ROOT, load_config
from app.llm import LLM, LLMError
from app.orchestrator import Orquestador

AHORA = datetime(2026, 11, 24, 12, 0)
EJEMPLO = ROOT / "data" / "ejemplo"


def armar(tmp):
    cfg = load_config()
    aprob = Aprobaciones(Path(tmp) / "t.db")
    return Orquestador(cfg, LLM(cfg["model_default"]), aprob, EJEMPLO), aprob


class Semilla(unittest.TestCase):
    def test_llm_mock_devuelve_fallback(self):
        self.assertEqual(LLM({"provider": "mock"}).complete("s", "u", fallback="hola"), "hola")

    def test_proveedor_desconocido_falla_claro(self):
        with self.assertRaises(LLMError):
            LLM({"provider": "x"}).complete("s", "u")

    def test_resumen_detecta_entregas_y_cotizaciones(self):
        with tempfile.TemporaryDirectory() as tmp:
            orq, aprob = armar(tmp)
            a = orq.especialistas["administrativo"].analizar(AHORA)
            self.assertEqual([e["oc"] for e in a["vencidas"]], ["OC-1002"])
            self.assertEqual([e["oc"] for e in a["semana"]], ["OC-1001"])
            niveles = {c["cotizacion"]: c["nivel"] for c in a["seguimientos"]}
            self.assertEqual(niveles, {"COT-501": 2, "COT-502": 1, "COT-503": 2})  # 505 es de hace 4 hs, 504 ya respondida

    def test_nada_sale_sin_aprobacion_y_no_duplica(self):
        with tempfile.TemporaryDirectory() as tmp:
            orq, aprob = armar(tmp)
            orq.atender("como van las cotizaciones", AHORA)
            orq.atender("como van las cotizaciones", AHORA)
            pend = aprob.listar()
            self.assertEqual(len(pend), 3)
            self.assertTrue(aprob.decidir(pend[0][0], "aprobada"))
            self.assertFalse(aprob.decidir(pend[0][0], "rechazada"))

    def test_ruteo(self):
        with tempfile.TemporaryDirectory() as tmp:
            orq, _ = armar(tmp)
            self.assertEqual(orq.elegir("quien me debe plata, morosos"), "financiero")
            self.assertIn("todavia no esta construido", orq.atender("morosos"))
            self.assertIsNone(orq.elegir("hola"))


if __name__ == "__main__":
    unittest.main()
