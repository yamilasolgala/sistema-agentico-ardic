"""Adaptador unico de modelo (Regla 9).

Ningun agente conoce al proveedor: todos llaman a LLM.complete().
Cambiar de proveedor = cambiar config/agents.json, nada mas.
"""
import json
import os
import urllib.request


class LLMError(Exception):
    pass


class LLM:
    def __init__(self, model_cfg):
        self.provider = model_cfg.get("provider", "mock")
        self.model = model_cfg.get("model", "")
        self.base_url = (model_cfg.get("base_url") or "").rstrip("/")
        self.api_key = os.environ.get(model_cfg.get("api_key_env", "LLM_API_KEY"), "")

    def complete(self, system, user, fallback=""):
        """Devuelve texto. Con provider 'mock' devuelve `fallback` (sin llamar a ninguna IA)."""
        if self.provider == "mock":
            return fallback
        if self.provider == "openai_compatible":
            return self._openai_compatible(system, user)
        raise LLMError("Proveedor no soportado: %s" % self.provider)

    def _openai_compatible(self, system, user):
        if not (self.base_url and self.api_key and self.model):
            raise LLMError("Falta base_url, model o la API key (variable de entorno).")
        body = json.dumps({
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }).encode("utf-8")
        req = urllib.request.Request(
            self.base_url + "/chat/completions",
            data=body,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + self.api_key},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
        except Exception as e:  # el detalle puede traer datos: no lo volcamos al log
            raise LLMError("Fallo la llamada al modelo (%s)" % type(e).__name__)
