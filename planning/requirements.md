# Requirements

> Generado en `/init-agent-system` (corrida por Yami con las respuestas del Workbook). Karina revisa y aprueba. SUPUESTO = confirmar con ella.

## Functional Requirements

**FR-1 Orquestador.** Recibe un pedido en lenguaje natural, elige el especialista y devuelve la respuesta. No ejecuta acciones hacia afuera.
**FR-2 Agente Administrativo (prioridad 1).**
- FR-2.1 Lee entregas pendientes y lista las vencidas y las que vencen en 7 dias.
- FR-2.2 Lee cotizaciones y detecta las sin respuesta a las 25 hs y a las 72 hs (SUPUESTO: horas corridas).
- FR-2.3 Redacta un borrador de mail de seguimiento por cada una y lo deja en la cola de aprobaciones.
- FR-2.4 Arma un resumen diario para Karina.
**FR-3 Cola de aprobaciones.** Todo lo que sale hacia afuera (mail, WhatsApp, cotizacion, precio) queda pendiente hasta que Karina aprueba o rechaza.
**FR-4 Asistente financiero (prioridad 2).** Seguimiento de pagos y morosos; control del consecutivo de facturacion. Solo propone, nunca emite facturas ni mueve dinero.
**FR-5 CM/SEO (prioridad 3, opcional).** Borradores de contenido para web y LinkedIn. Nunca publica.
**FR-6 Panel admin (Regla 4).** Login, vista de aprobaciones, vista de agentes y su estado, gestion de credenciales (keys del modelo, cifradas), registro de actividad.
**FR-7 Modelo intercambiable (Regla 9).** Cambiar de proveedor solo por configuracion.

## Non-Functional Requirements

Ver `docs/nfr.md`.

## Datos de entrada (de Karina)

- Archivo "Pendientes de entrega" (Excel) y registro de cotizaciones: se exportan a CSV en `data/real/`.
- Mail: Gmail (borradores). Thunderbird y SAE quedan para despues.
