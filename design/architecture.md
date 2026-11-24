# System Architecture

## Overview

```
Karina --(CLI hoy / panel web despues)--> API --> Orquestador --> [Administrativo | Financiero | CM-SEO]
                                                       |                 |
                                                       |                 +--> propone --> COLA DE APROBACIONES --(OK de Karina)--> envio (borrador Gmail)
                                                       +--> Adaptador de modelo (config) --> proveedor de IA
Datos: data/real/*.csv  |  Estado: SQLite (aprobaciones, actividad, credenciales cifradas)
```

El orquestador y los agentes son el producto; La Maquinaria es el taller que los construye.

## Module Structure

- `backend/app/llm.py` adaptador de modelo. `approvals.py` cola. `orchestrator.py` ruteo. `agents/` un archivo por agente. `cli.py` pruebas.
- Pendiente: `api.py` (FastAPI), `auth.py`, `credentials.py` (cifrado), `connectors/gmail.py`.
- `frontend/index.html`: panel admin (una pagina, sin framework).

## Technology Choices

Ver `stack_selection.md`.

## Credential Level Mapping

- **Level 1 (.env)**: `JWT_SECRET`, `ENCRYPTION_KEY`, `DATABASE_URL` (SQLite local).
- **Level 2 (deployment)**: `APP_ENV`, `APP_PORT`, URLs del servicio.
- **Level 3 (panel admin, cifrado)**: API key del modelo, credenciales de Gmail (OAuth), a futuro SAE/WhatsApp.

## Model Provider Layer (Rule 9)

- **Adapter**: `backend/app/llm.py` (`LLM.complete`). Ningun agente llama a un SDK directo.
- **Config-driven**: `config/agents.json` -> `model_default` `{provider, model, base_url, api_key_env}`; se puede sobreescribir por agente. La key es Nivel 3.
- **Supported providers**: `mock` (pruebas) y `openai_compatible` (OpenAI, OpenRouter, Ollama, Google y Anthropic por su endpoint compatible; verificar el base_url vigente en la doc oficial al configurarlo).
- **Swap touches**: solo la config. No los manuales de agentes, ni los datos, ni las integraciones.
- **Isolated in adapter**: formato de respuesta, limites de contexto, errores. Hoy no se usa tool calling: los agentes calculan en codigo.
- **Swap test (IT-2)**: correr los mismos 3 pedidos con dos proveedores distintos; debe funcionar cambiando solo la config.

## Infrastructure

- Local en la compu de Karina al inicio. Docker + servidor (EasyPanel/VPS) cuando el programa llegue a deploy (dias 17-18).
- Base: SQLite local.
