# Questions & Assumptions

## Blocking Questions (para Karina, antes de construir mas)

1. El archivo "Pendientes de entrega": como es hoy? Pasame las columnas reales (o un ejemplo con datos tapados) y en que programa lo llevas (Excel, SAE).
2. Las cotizaciones: donde queda registrado cuando se envia una y cuando el cliente responde? Hoy el agente asume `data/real/cotizaciones.csv`.
3. Los plazos de 25 hs y 72 hs: son hs corridas desde que enviaste la cotizacion? Que se hace en cada uno (primer recordatorio, segundo, llamado)?
4. Que modelo de IA queres usar y que presupuesto mensual tenes (en USD)?

## Non-Blocking Questions

- Por donde queres hablarle al sistema: Telegram, WhatsApp, web?
- Isaac y Maricruz van a usar el sistema? Con que permisos?
- Para el agente financiero: que formato tiene el archivo Consecutivo y que exporta SAE?

## Assumptions (validar con Karina)

- El foco es ARDIC; CELVA y CIES quedan para despues del dia 28.
- Los plazos de 25 hs y 72 hs son horas corridas desde el envio de la cotizacion.
- "Esta semana" para entregas = proximos 7 dias.
- Para empezar se trabaja sobre CSV exportados, sin conectar Thunderbird, SAE ni portales.
- El envio de mails real no se conecta hasta que la cola de aprobaciones este probada.
