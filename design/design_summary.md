# Design Summary: Sistema agentico de ARDIC

Estado: PLAN COMPLETO (init-agent-system ya corrido) + semilla de codigo. Falta la aprobacion de Karina.

## Stack
- Backend: Python 3.9+, solo libreria estandar por ahora (sin dependencias). Carpeta `backend/app`.
- Datos: CSV en `data/real/` (ignorada por git) + SQLite para la cola de aprobaciones.
- API: FastAPI (IT-7). Panel admin: HTML simple, `frontend/index.html` (IT-5, Regla 4). SQLite como base; sin base vectorial.

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

## Orden de construccion
UJ-1 con datos reales (victoria rapida) -> IT-2 swap test -> IT-7 API -> IT-5 panel -> IT-4 borradores Gmail -> IT-6 Docker -> UJ-2 financiero -> UJ-3 CM/SEO.

## Riesgos top
Mail saliente sin validar (cola de aprobaciones), datos inventados (el codigo calcula), datos de clientes en GitHub (`data/real/` ignorada).
