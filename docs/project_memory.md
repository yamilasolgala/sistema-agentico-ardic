# Project Memory

## Current State

- **Project**: Sistema agentico de ARDIC (Karina Ardizzi)
- **Phase**: SEMILLA ARMADA, esperando que Karina revise y apruebe el plan
- **Last Completed**: IT-1 (adaptador de modelo), IT-3 (cola de aprobaciones), orquestador, agente Administrativo con datos de ejemplo. 5 tests pasando.
- **Next Step**: Karina corre `/session-start`, revisa `START_PROJECT_PROMPT.md` y `design/agent_system.md`, responde `planning/questions.md`, aprueba el plan y se sigue con `/start-execution` (primero IT-2, despues UJ-1 con sus datos reales)

## Nota sobre la Regla 1 (Planning Gate)

El codigo que hay lo sembro Yami como punto de partida (adaptador, cola de aprobaciones, orquestador minimo, un agente). El plan sigue sin aprobar: nada de lo que viene se construye antes de que Karina lo apruebe.

## Blockers

- Falta el archivo real "Pendientes de entrega" y el registro de cotizaciones (ver `planning/questions.md`).
- Falta definir proveedor de modelo y key.

## Key Context for Next Session

- Contexto del negocio: `Contexto/perfil-karina.md`
- Como probarlo: `cd backend && python3 -m app.cli pedir "como estan las entregas y cotizaciones?"`
- Tests: `cd backend && python3 -m unittest discover -s tests`
- Datos reales van en `data/real/` (nunca se suben a GitHub).
