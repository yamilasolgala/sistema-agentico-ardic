# Start Project

> Completado a partir del Workbook de Karina (ver `Contexto/perfil-karina.md`). Karina: revisalo y corregí lo que esté mal. `/init-agent-system` ya fue corrido por Yami: el plan está en `design/` y `planning/`.

---

## Project Description

**Project Name**: Sistema agéntico de ARDIC

**Project Type**: Equipo de agentes (orquestador + especialistas). Usar `/init-agent-system`.

**Description**: ARDIC (empaque flexible grado alimenticio) depende 100% de Karina. No hay seguimiento de cotizaciones ni de entregas, hay errores logísticos y ella es la única que imprime etiquetas. El sistema le da un empleado digital que hace el seguimiento y le prepara todo para que ella solo apruebe.

**Key Features** (en orden de construcción):
1. **Orquestador**: recibe lo que Karina pide, lo manda al especialista correcto y nunca ejecuta nada hacia afuera sin su OK.
2. **Agente Administrativo** (primero): lee el archivo "Pendientes de entrega" y las cotizaciones, y arma cada día un resumen de qué entrega vence esta semana y qué cotización lleva más de 72 hs sin respuesta, con borrador de mail de seguimiento.
3. **Agente Asistente financiero** (segundo): seguimiento de pagos y morosos, consecutivo de facturación.
4. **Agente CM/SEO** (tercero, solo si hay tiempo): leads vía web y LinkedIn.

**Users/Roles**: Karina (dueña y única aprobadora en ARDIC). Isaac (planta) y Maricruz (administrativa) pueden consultar más adelante, sin permisos de aprobación.

**Integrations**: Arranca sin integraciones complejas, solo archivos Excel/CSV exportados y mail en Gmail (borradores). Después: SAE, WhatsApp, Thunderbird. No inventar integraciones: verificar cada una antes de prometerla.

**Constraints**:
- Karina tiene nivel bajo en IA y alto en procesos: explicarle cada decisión y por qué.
- Al principio, cada acción pide confirmación.
- Línea roja: nunca, sin su validación, enviar mails, mandar cotizaciones o precios, responder a un cliente enojado, borrar archivos o conversaciones, ni compartir información de las empresas.
- Foco 100% ARDIC hasta el día 28. CELVA y CIES quedan afuera.
- Datos de clientes: nunca al repositorio de GitHub (carpeta `data/real/` ignorada por git).
- El modelo de IA es un enchufe (Regla 9): se cambia solo por configuración.

---

## What Happens Next

1. El sistema entra en Planning Mode (`/init-agent-system`)
2. Se analizan los requisitos y se hacen preguntas
3. Se propone la arquitectura, el stack y los recorridos de usuario
4. Se presenta un plan para tu aprobación
5. Solo después de tu aprobación empieza la construcción
