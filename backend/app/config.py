"""Carga de configuracion. El proveedor de IA vive aca, nunca en el codigo (Regla 9)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_config(path=None):
    path = Path(path) if path else ROOT / "config" / "agents.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def default_data_dir():
    """Usa data/real si Karina puso sus archivos ahi; si no, los de ejemplo."""
    real = ROOT / "data" / "real"
    if any(real.glob("*.csv")):
        return real
    return ROOT / "data" / "ejemplo"
