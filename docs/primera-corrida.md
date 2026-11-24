# Primera corrida del sistema (datos de ejemplo)

Corrida por Yami el 2026-11-24 con los datos ficticios de `data/ejemplo/`, simulando la fecha 2026-11-24 12:00. Con modelo `mock` (sin IA): los borradores son plantilla fija.

```
$ python3 -m app.cli pedir "como estan las entregas y cotizaciones?" --ahora "2026-11-24 12:00"
(datos: ejemplo)

RESUMEN ADMINISTRATIVO ARDIC

Entregas vencidas: 1
  - OC-1002 | Alimentos Muestra SRL | Film termoformable 30cm | comprometida 2026-11-21
Entregas que vencen en los proximos 7 dias: 1
  - OC-1001 | Empacadora Ejemplo SA | Bolsa laminada 25x35 cal 80 | comprometida 2026-11-26
Cotizaciones sin respuesta para seguir: 3
  - COT-501 | Empacadora Ejemplo SA | 98 hs sin respuesta | seguimiento 2 | borrador #1 esperando tu OK
  - COT-502 | Alimentos Muestra SRL | 27 hs sin respuesta | seguimiento 1 | borrador #2 esperando tu OK
  - COT-503 | Cliente Ficticio SA | 285 hs sin respuesta | seguimiento 2 | borrador #3 esperando tu OK

$ python3 -m app.cli pedir "quien me debe plata, morosos"
(datos: ejemplo)

Eso le toca al agente 'financiero', que todavia no esta construido (prioridad 2 en el plan).
```

Los borradores quedan en la cola; nada se envia. Ver con `python3 -m app.cli aprobaciones`.
