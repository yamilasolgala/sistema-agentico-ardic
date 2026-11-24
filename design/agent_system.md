# Agent System Design: ARDIC

> Borrador sembrado desde el Workbook de Karina. `/init-agent-system` lo revisa con ella y lo completa. Lo que dice SUPUESTO hay que confirmarlo.

## Org Chart

```
Karina (aprueba todo lo que sale hacia afuera)
   |
Orquestador  (recibe el pedido, elige especialista, NO ejecuta nada afuera)
   |-- Administrativo     [prioridad 1, sembrado]  entregas + cotizaciones
   |-- Asistente financiero [prioridad 2, pendiente] pagos, morosos, consecutivo de facturacion
   |-- CM / SEO            [prioridad 3, pendiente]  leads (web + LinkedIn)
```

Fuera de alcance hasta despues del dia 28: CELVA y CIES.

## Agents

| Agent | Role (one process) | Memory / DB | Integrations | Model | Credential level | Permissions (read / write / never) | Build priority |
|-------|--------------------|-------------|--------------|-------|------------------|------------------------------------|----------------|
| Orquestador | Recibe el pedido y lo rutea | Cola de aprobaciones (SQLite) | Ninguna | Via adaptador (config) | L3 (key del modelo) | Lee: pedidos. Escribe: cola de aprobaciones. Nunca: enviar nada | 1 |
| Administrativo | Seguimiento de entregas y cotizaciones (25 hs / 72 hs) | CSV exportados de Excel (`data/real/`) | Ninguna al inicio; luego Gmail (borradores) | Via adaptador | L3 | Lee: entregas.csv, cotizaciones.csv. Escribe: borradores en la cola. Nunca: enviar, borrar, cambiar precios | 1 |
| Asistente financiero | Pagos, morosos, consecutivo | CSV de pagos y consecutivo; luego SAE | Luego SAE / mail | Via adaptador | L3 | Lee: pagos y consecutivo. Escribe: borradores. Nunca: mover dinero, emitir facturas | 2 |
| CM / SEO | Generar leads | Notas de marca (markdown) | Luego web / LinkedIn | Via adaptador | L3 | Escribe: borradores de posts. Nunca: publicar | 3 |

## Memory & Data per Agent

- **Entregas y cotizaciones**: datos exactos (fechas, OCs, clientes) = relacional. Para empezar alcanza con los Excel exportados a CSV. SUPUESTO: migrar a Airtable o Supabase recien cuando el volumen o el uso multiusuario lo pida.
- **Conocimiento de ARDIC** (clientes, precios, procesos documentados): hoy son archivos. Una base vectorial **NO hace falta todavia**: con pocos documentos se leen directo.
- **Estado de aprobaciones**: SQLite local (ya implementado).

## Model Provider Layer (Rule 9)

Ya implementado en `backend/app/llm.py`. Config en `config/agents.json`. Provider por defecto: `mock` (sin IA, para probar sin gastar). Cambiar de proveedor = cambiar `provider`, `model`, `base_url` y la variable de entorno con la key. Test de intercambio pendiente (IT-2).

## Quality & Guardrails

- Las cuentas (fechas, horas) las hace codigo, no el modelo. El modelo solo redacta.
- Nunca inventar datos. Nunca mezclar datos de una empresa con otra.
- Linea roja de Karina: enviar mails, mandar cotizaciones o precios, responder a un cliente enojado, borrar archivos o conversaciones, compartir informacion de las empresas. Todo eso pasa por la cola de aprobaciones.

## Channels & Runtime

- **Channels**: hoy solo linea de comandos. A definir con Karina: Telegram, WhatsApp o web.
- **Runtime**: local en su compu para empezar. Servidor mas adelante (dias 17-18 del programa).
