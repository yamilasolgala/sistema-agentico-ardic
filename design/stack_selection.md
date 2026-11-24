# Stack Selection

## Backend
- **Language**: Python 3.9+. **Framework**: stdlib hoy; FastAPI para la API del panel (IT-7). **Query**: sqlite3 de la libreria estandar.
- **Rationale**: sin dependencias hasta que haga falta; Python es lo mas simple para trabajar con CSV y fechas. Mismo stack que el sistema TutorIA de las clases.

## Frontend
- **Framework**: ninguno (HTML + JS simple en `frontend/index.html`). **CSS**: glassmorphism claro/oscuro segun `style_guide.md`. **State**: estado local de la pagina.
- **Rationale**: el panel son 3 vistas (aprobaciones, agentes, credenciales); un framework seria sobre-ingenieria.

## Database
- **Engine**: SQLite. **Rationale**: un solo usuario, bajo volumen, cero instalacion. Cuando se sumen empresas o usuarios simultaneos, migrar a Postgres/Supabase. Base vectorial: NO hace falta todavia.

## Additional Tools
- Tests: `unittest` (ya andando). Cifrado de credenciales: libreria `cryptography` (a instalar en IT-5). Contenedor: Docker.

## AI / Model Provider (Rule 9)
- **Abstraction**: adaptador propio con interfaz OpenAI-compatible y `base_url` configurable (`backend/app/llm.py`).
- **Default**: `mock` hasta que Karina elija proveedor y presupuesto (pregunta bloqueante). **Alternates**: cualquiera compatible.
- **Config shape**: `{ provider, model, base_url, api_key_env }`; la key es Nivel 3.
- **Rationale**: sin lock-in; cambiar de proveedor no toca prompts, datos ni integraciones.
