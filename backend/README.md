# Backend

Python 3.9+, sin dependencias externas por ahora.

```
cd backend
python3 -m unittest discover -s tests
python3 -m app.cli pedir "como estan las entregas y cotizaciones?" --ahora "2026-11-24 12:00"
python3 -m app.cli aprobaciones
python3 -m app.cli aprobar 1
```

Sin datos propios usa `data/ejemplo/` (ficticios). Con tus CSV en `data/real/` usa esos.
