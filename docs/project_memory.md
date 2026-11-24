# Project Memory

## Current State

- **Project**: Sistema agentico de ARDIC (Karina Ardizzi)
- **Phase**: PLAN COMPLETO (`/init-agent-system` ya corrido por Yami), esperando la aprobacion de Karina
- **Last Completed**: Planning Mode entero (requirements, scope, risks, nfr, architecture, stack, data model, API, wireframes, IT/UJ, decisiones DEC-01 a DEC-06). Semilla: IT-1, IT-3, orquestador y agente Administrativo funcionando con datos de ejemplo (ver `docs/primera-corrida.md`).
- **Next Step**: Karina revisa el plan (`design/design_summary.md` primero), responde `planning/questions.md`, aprueba o corrige, y escribe `/start-execution`. Primero se construye UJ-1 con sus datos reales.

## Nota sobre la Regla 1 (Planning Gate)

El codigo que hay lo sembro Yami como punto de partida. El plan NO esta aprobado: nada de lo que viene se construye antes de que Karina lo apruebe.

## Blockers

- Falta el archivo real "Pendientes de entrega" y el registro de cotizaciones.
- Falta elegir proveedor de modelo, presupuesto y key.

## Key Context for Next Session

- Negocio: `Contexto/perfil-karina.md`. Supuestos a confirmar: `planning/questions.md`.
- Probar: `cd backend && python3 -m app.cli pedir "como estan las entregas y cotizaciones?"`
- Tests: `cd backend && python3 -m unittest discover -s tests`
- Datos reales en `data/real/` (nunca a GitHub).
