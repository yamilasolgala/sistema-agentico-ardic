# Design Summary: Sistema agentico de ARDIC

Estado: SEMILLA armada por Yami. Karina revisa y aprueba el plan en su primera sesion (`/init-agent-system`).

## Stack
- Backend: Python 3.9+, solo libreria estandar por ahora (sin dependencias). Carpeta `backend/app`.
- Datos: CSV en `data/real/` (ignorada por git) + SQLite para la cola de aprobaciones.
- Frontend / panel admin: pendiente (Regla 4: obligatorio). Ver IT-5.

## Modulos
- `llm.py`: adaptador unico de modelo (Regla 9). `mock` y `openai_compatible`.
- `approvals.py`: cola de aprobaciones. Nada sale sin OK de Karina.
- `orchestrator.py`: rutea por palabras clave a un especialista.
- `agents/administrativo.py`: entregas + cotizaciones (seguimiento 25 hs / 72 hs).
- `cli.py`: para probar desde la terminal.

## Patrones clave
- El codigo calcula, el modelo redacta.
- Los agentes solo proponen; aprobar es un paso humano.
- Config en `config/agents.json`, secretos en variables de entorno.

## Credential Map
- Level 1 (.env): ninguna todavia.
- Level 3: API key del modelo (variable `LLM_API_KEY`, hasta que exista el panel admin).

## Canales
Solo CLI. A definir.

## Agentes
Orquestador y Administrativo sembrados. Financiero y CM/SEO pendientes.
