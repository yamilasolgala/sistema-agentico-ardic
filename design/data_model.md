# Data Model

## Entities

**Archivos de entrada (CSV en `data/real/`, vienen de los Excel de Karina)**
```
Entity: Entrega   (entregas.csv)
  oc, cliente, producto, fecha_compromiso (YYYY-MM-DD), estado (pendiente|entregada)
Entity: Cotizacion (cotizaciones.csv)
  cotizacion, cliente, email, fecha_envio (YYYY-MM-DD HH:MM), respondida (si|no)
```
(SUPUESTO: las columnas reales de Karina pueden diferir; adaptar el lector al archivo real.)

**Base SQLite (`data/estado.db`)**
```
Entity: Aprobacion
  id PK, creado, agente, tipo, destinatario, asunto, cuerpo, estado (pendiente|aprobada|rechazada), decidido
  Index: (estado, tipo, destinatario, asunto) para no duplicar pendientes
Entity: Actividad   (IT-5)
  id PK, fecha, actor (agente|karina), accion, referencia
Entity: Credencial  (IT-5)
  id PK, nombre, nivel (3), valor_cifrado, creado, actualizado
Entity: Usuario     (IT-5)
  id PK, email, hash_password, rol (admin)
```

## Relationship Diagram

Aprobacion -> (referencia por tipo) -> Cotizacion o Entrega, solo por texto; no hay claves foraneas porque los CSV no son tablas.

## Stores y por que

- Exactos (entregas, cotizaciones): CSV hoy; a Airtable/Supabase solo si crece.
- Conocimiento (precios, procesos): archivos, leidos directo. Sin base vectorial por ahora.
- Preferencias/estado: SQLite.
