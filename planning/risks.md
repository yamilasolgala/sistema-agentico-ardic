# Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| R-01 | Un mail o cotizacion sale a un cliente sin validar (linea roja de Karina) | Med | High | Los agentes solo proponen; cola de aprobaciones obligatoria; no hay conexion de envio hasta probar la cola (IT-4 despues de IT-5); primer envio solo como borrador de Gmail |
| R-02 | El modelo inventa datos (fechas, precios, clientes) | Med | High | El codigo calcula, el modelo solo redacta; los borradores no incluyen precios; Karina revisa cada uno |
| R-03 | Datos de clientes terminan en GitHub | Med | High | `data/real/` ignorada por git; repo privado; revisar `git status` antes de cada push |
| R-04 | API key del modelo filtrada | Low | High | Solo variable de entorno / panel cifrado (Nivel 3); nunca en chat ni en archivos |
| R-05 | Mezcla de datos entre empresas (ARDIC/CELVA/CIES) | Low | High | Foco solo ARDIC; si se suman otras, un espacio de datos por empresa |
| R-06 | Los archivos reales de Karina no coinciden con las columnas asumidas | High | Med | Preguntas bloqueantes en `planning/questions.md`; el agente lee columnas por nombre, adaptar el lector al archivo real |
| R-07 | Karina se frena por dispersion (3 empresas, poco tiempo) | Med | Med | Victoria rapida primero (resumen diario); una sola cosa a la vez; foco ARDIC |
| R-08 | Dependencia de un proveedor de IA (precio, caida, cambios) | Med | Med | Adaptador unico + test de intercambio (IT-2) |
| R-09 | Sobre-ingenieria (panel, Docker, DB) antes de ver valor | Med | Med | Orden de construccion: valor primero (UJ-1 por CLI), panel despues |
