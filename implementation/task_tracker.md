# Task Tracker

## Tracking Table

| ID | Type | Name | Milestone | Status | Security Checked | Review Passed | Notes |
|----|------|------|-----------|--------|------------------|---------------|-------|
| IT-1 | IT | Adaptador de modelo (Regla 9) | M0 | completed (semilla) | no | no | `backend/app/llm.py`. Falta probar con key real |
| IT-3 | IT | Cola de aprobaciones | M0 | completed (semilla) | no | no | `backend/app/approvals.py`, con tests |
| IT-2 | IT | Test de intercambio de proveedor | M0 | pending | no | no | Requiere proveedor y key de Karina |
| IT-7 | IT | API HTTP + login | M0 | pending | no | no | FastAPI |
| IT-5 | IT | Panel admin + credenciales cifradas | M0 | pending | no | no | Regla 4 |
| IT-4 | IT | Envio como borrador de Gmail | M0 | pending | no | no | Verificar MCP/API oficial antes |
| IT-6 | IT | Docker + deploy | M0 | pending | no | no | Dias 17-18 |
| UJ-1 | UJ | Resumen de entregas y seguimiento de cotizaciones | M1 | in_progress | no | no | Funciona por CLI con datos de ejemplo. Falta: datos reales + 3 pedidos reales |
| UJ-2 | UJ | Asistente financiero | M2 | pending | no | no | Prioridad 2 |
| UJ-3 | UJ | CM/SEO | M3 | pending | no | no | Prioridad 3 |

Orden de ejecucion: UJ-1 con datos reales primero (victoria rapida), despues IT-2, IT-7, IT-5, IT-4, IT-6, y recien ahi UJ-2 y UJ-3.

## Milestones
- **M0: Foundation**: IT-1 a IT-7. **M1**: UJ-1. **M2**: UJ-2. **M3**: UJ-3. Correr `/review` al cerrar cada uno.

## Status Values
`pending` / `in_progress` / `completed` / `blocked`
