# Task Tracker

## Tracking Table

| ID | Type | Name | Milestone | Status | Security Checked | Review Passed | Notes |
|----|------|------|-----------|--------|------------------|---------------|-------|
| IT-1 | IT | Adaptador de modelo (Regla 9), provider `mock` y `openai_compatible` | M0 | completed (semilla) | no | no | `backend/app/llm.py`. Falta probar con una key real |
| IT-2 | IT | Test de intercambio de proveedor (cambiar solo config) | M0 | pending | no | no | Requiere key real de al menos un proveedor |
| IT-3 | IT | Cola de aprobaciones | M0 | completed (semilla) | no | no | `backend/app/approvals.py`, con tests |
| IT-4 | IT | Conexion de envio real (Gmail, solo borradores primero) | M0 | pending | no | no | Verificar MCP/API oficial antes. No inventar |
| IT-5 | IT | Panel admin con credenciales y vista de aprobaciones | M0 | pending | no | no | Regla 4. Reemplaza el CLI para Karina |
| IT-6 | IT | Docker + deploy | M0 | pending | no | no | Dias 17-18 del programa |
| UJ-1 | UJ | "Que entregas vencen y que cotizaciones seguir" de punta a punta | M1 | in_progress | no | no | Funciona por CLI con datos de ejemplo. Falta: datos reales de Karina y probar con 3 pedidos reales |
| UJ-2 | UJ | Agente Asistente financiero (pagos, morosos, consecutivo) | M2 | pending | no | no | Prioridad 2 |
| UJ-3 | UJ | Agente CM/SEO (leads) | M3 | pending | no | no | Prioridad 3, solo si hay tiempo |

## Milestones

- **M0: Foundation**: IT-1 a IT-6
- **M1: Administrativo de ARDIC**: UJ-1 (victoria rapida: resumen diario + borradores para aprobar)
- **M2: Financiero**: UJ-2
- **M3: CM/SEO**: UJ-3

Correr `/review` al terminar cada milestone.

## Types

- `IT`: Infrastructure Task (fundacional, sin interfaz)
- `UJ`: User Journey (accion completa de punta a punta)

## Status Values

- `pending` / `in_progress` / `completed` / `blocked`
