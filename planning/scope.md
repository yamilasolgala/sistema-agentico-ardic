# Scope

## In Scope

- Solo ARDIC.
- Orquestador + Administrativo (entregas y cotizaciones) + cola de aprobaciones + panel admin.
- Despues, en orden: Asistente financiero y CM/SEO.
- Trabajo sobre archivos exportados (CSV) y borradores de mail.

## Out of Scope (hasta despues del dia 28)

- CELVA y CIES.
- Impresion de etiquetas y certificados.
- Integracion con SAE, Thunderbird y portales de facturacion de clientes.
- Envio automatico de cualquier mensaje sin aprobacion (no existe en este alcance).
- WhatsApp (se evalua despues, verificando API oficial y plan).
- Base vectorial / RAG: no hace falta con los pocos documentos actuales.

## Scope Boundaries

- Un agente por proceso. Un agente nuevo solo si tiene herramientas, permisos o memoria distintos.
- Cada agente se prueba con 3 pedidos reales antes de pasar al siguiente.
- Si algo "parece util" y no esta aca, se frena y se le pregunta a Karina (Regla 6).
