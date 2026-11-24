# Infrastructure Tasks & User Journeys

Orden de construccion: valor primero (UJ-1 por CLI), despues panel y conexiones.

## Infrastructure Tasks

### IT-1: Adaptador de modelo (Regla 9) — HECHO (semilla)
- **Components**: `backend/app/llm.py`, `config/agents.json`. **Acceptance**: `mock` devuelve fallback; proveedor desconocido falla claro; test pasa. **Security**: key solo por variable de entorno; errores sin detalle de la respuesta.

### IT-3: Cola de aprobaciones — HECHO (semilla)
- **Components**: `backend/app/approvals.py`. **Acceptance**: propone sin duplicar; aprobar/rechazar una sola vez; tests pasan. **Security**: consultas parametrizadas.

### IT-2: Test de intercambio de proveedor
- **Purpose**: demostrar la Regla 9. **Components**: script de prueba con 3 pedidos fijos. **Acceptance**: corre con 2 proveedores cambiando solo `config/agents.json`. **Security**: keys por entorno. **Depende de**: Karina elige proveedor y consigue una key.

### IT-7: API HTTP + login
- **Components**: FastAPI, JWT + bcrypt, endpoints de `api_contracts.md`. **Acceptance**: login funciona, rutas protegidas devuelven 401 sin token, `/health` responde. **Security**: rate limit en login, validacion de entradas.

### IT-5: Panel admin (Regla 4)
- **Components**: `frontend/index.html` con las pantallas de `ui_wireframes.md`; credenciales Nivel 3 cifradas; registro de actividad. **Acceptance**: Karina entra, ve y aprueba un borrador, carga una key y no puede verla despues. **Security**: cifrado en reposo, nunca se devuelve el valor, escapar contenido (XSS).

### IT-4: Conexion de envio (Gmail, solo borradores)
- **Purpose**: que "aprobar" cree un borrador en su Gmail (nunca envia). **Acceptance**: aprobar en el panel deja el borrador en Gmail. **Security**: permisos minimos. **Nota**: verificar en la doc oficial el MCP/API y los permisos antes de construir; no inventar.

### IT-6: Docker y deploy
- **Components**: Dockerfile, docker-compose, guia. **Acceptance**: levanta con un comando. Dias 17-18 del programa.

## User Journeys

### UJ-1: "Que entregas vencen y que cotizaciones seguir"  (M1)
- **Description**: Karina pide el resumen; ve entregas vencidas/proximas y cotizaciones a seguir; revisa y aprueba los borradores.
- **Backend**: `agents/administrativo.py` (hecho con datos de ejemplo), lector adaptado a sus CSV reales. **Frontend**: pantalla Aprobaciones + Preguntarle.
- **Acceptance**: con sus archivos reales y 3 pedidos reales, el resumen es correcto contra su Excel; nada sale sin aprobar; borrador sin precios.
- **Tests**: fechas limite (24/25 hs, 71/72 hs), archivo vacio, columnas faltantes.

### UJ-2: Asistente financiero  (M2)
- **Description**: lista pagos vencidos (morosos) con borrador de recordatorio; controla el consecutivo de facturacion y avisa saltos o duplicados.
- **Acceptance**: correcto contra sus archivos reales; no emite facturas ni mueve dinero.

### UJ-3: CM/SEO  (M3, solo si hay tiempo)
- **Description**: propone borradores de posts para LinkedIn y web a partir de lo que ARDIC ya documento. **Acceptance**: nunca publica; Karina aprueba cada pieza.
