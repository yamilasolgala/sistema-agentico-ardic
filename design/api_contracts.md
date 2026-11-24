# API Contracts

Base: `/api/v1`. Auth: `Authorization: Bearer <token>`. Se implementa en IT-7 (FastAPI). Errores: `{ error, message }` sin datos sensibles.

```
POST /auth/login            public     { email, password } -> { token }
GET  /health                public     -> { status }
POST /orchestrator/ask      required   { text } -> { agent, answer }
GET  /approvals?estado=     required   -> [ { id, agente, tipo, destinatario, asunto, cuerpo, estado } ]
POST /approvals/{id}/approve  required -> { ok }
POST /approvals/{id}/reject   required -> { ok }
GET  /agents                required   -> [ { nombre, prioridad, construido } ]
GET  /credentials           required   -> [ { nombre, nivel, definida } ]   (nunca el valor)
PUT  /credentials/{nombre}  required   { valor } -> { ok }
GET  /activity              required   -> [ { fecha, actor, accion, referencia } ]
```
