# UI Wireframes

## Navigation Structure
Barra lateral: Aprobaciones | Preguntarle al orquestador | Agentes | Credenciales | Actividad. Una sola pagina `frontend/index.html`.

## Screens
```
Page: Aprobaciones (inicio)   Route: #aprobaciones   Auth: required
  Layout: lista de tarjetas (destinatario, asunto, borrador completo editable)
  Actions: Aprobar | Rechazar | Editar texto antes de aprobar
  States: Empty: "No hay nada pendiente"  | Error: mensaje claro, sin datos sensibles
Page: Preguntarle al orquestador   Route: #chat
  Layout: caja de texto + respuesta + indicador de que agente respondio
  Actions: enviar pedido
  States: Empty: ejemplos ("como estan las entregas?") | Error: "no pude resolverlo"
Page: Agentes   Route: #agentes
  Layout: tabla (agente, prioridad, construido, ultima ejecucion)
Page: Credenciales   Route: #credenciales
  Layout: lista de nombres (modelo, Gmail) con estado "definida / falta"; nunca muestra el valor
  Actions: cargar / reemplazar
Page: Actividad   Route: #actividad
  Layout: tabla cronologica de propuestas y decisiones
```
