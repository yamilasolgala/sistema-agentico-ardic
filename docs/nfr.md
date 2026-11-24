# Non-Functional Requirements

## Performance
- Un resumen diario se genera en menos de 30 segundos con hasta ~500 filas por archivo. Sin requisitos de alta concurrencia (1 a 3 usuarios).

## Security
- Auth del panel: JWT + bcrypt; un solo rol admin (Karina) al inicio.
- Keys del modelo: Nivel 3, cifradas en reposo en el panel; hasta entonces, variable de entorno.
- Ningun dato de clientes en logs ni mensajes de error. `data/real/` fuera de git.
- Acciones hacia afuera: siempre por la cola de aprobaciones.

## Accessibility
- Panel legible, contraste suficiente, navegable por teclado. Idioma: espanol.

## Observability
- Registro de cada propuesta, aprobacion y rechazo (quien, cuando). Registro de errores sin datos sensibles.

## Scalability
- Una empresa, pocos usuarios. SQLite alcanza. Migrar a Postgres/Supabase solo si se suman empresas o usuarios simultaneos.
