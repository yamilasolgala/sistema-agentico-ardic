# Decision Log

### DEC-01: Foco solo en ARDIC
- **Date**: 2026-11-24. **Context**: 3 empresas y mas de 8 agentes posibles. **Decision**: solo ARDIC hasta el dia 28. **Rationale**: ahi esta el dolor y el proceso ya documentado. **Alternatives**: repartir en las 3 (se dispersa). **Consequences**: CELVA y CIES quedan para despues.

### DEC-02: El codigo calcula, el modelo redacta
- **Date**: 2026-11-24. **Context**: riesgo de que la IA invente fechas o datos. **Decision**: plazos, fechas y cuentas en codigo; el modelo solo escribe el borrador. **Consequences**: resultados reproducibles y testeables.

### DEC-03: Todo lo saliente pasa por la cola de aprobaciones
- **Date**: 2026-11-24. **Context**: linea roja de Karina. **Decision**: los agentes solo proponen; aprobar es humano; el primer envio real es un borrador de Gmail, nunca un envio. **Alternatives rechazadas**: envio automatico con reglas.

### DEC-04: Datos en CSV y SQLite, sin base vectorial
- **Date**: 2026-11-24. **Decision**: CSV exportados + SQLite. **Rationale**: un usuario, poco volumen, pocos documentos. **Rechazado**: Airtable/Supabase (innecesario hoy), base vectorial (sin corpus que lo justifique). **Revisar**: si se suman empresas o usuarios.

### DEC-05: Adaptador de modelo propio, interfaz OpenAI-compatible
- **Date**: 2026-11-24. **Decision**: `llm.py` con `provider/model/base_url`, `mock` por defecto. **Rationale**: Regla 9, sin lock-in, se puede probar sin gastar. **Rechazado**: SDK de un proveedor directo; LiteLLM (dependencia extra por ahora).

### DEC-06: Codigo sembrado antes de aprobar el plan
- **Date**: 2026-11-24. **Decision**: Yami siembra adaptador, cola, orquestador y un agente; Karina aprueba el plan completo antes de `/start-execution`. Nada nuevo se construye sin su aprobacion.
