# ADR 0001 — Stack técnico de Miramar

> **Fecha:** 2026-06-01
> **Status:** Adoptado
> **Owner:** Juan
> **Tipo:** Decisión estructural cross-módulo (infraestructura)

## Contexto

Miramar arrancó con un dashboard estático servido por **Cloudflare Pages** (read-only · alimentado por `data.json` editado vía PR). Suficiente para mostrar el estado a Juan y papá, pero insuficiente para:

- Que papá pueda **editar** desde el dashboard (marcar tareas, agregar notas, subir fotos)
- Flujo de **approval** (papá propone → Juan aprueba)
- Crecer a módulos de **contabilidad, operaciones**, etc.

El dashboard debe ser la **herramienta operacional de la familia para los próximos años**, no un MVP. Juan también va a comprar PC a papá, lo que indica intención de uso diario serio.

## Alternativas evaluadas

### A · Stack 100% Cloudflare (Workers + D1 + R2 + Access)
- **Pros:** $0-$5/mes, cero ops, serverless, encaja con el dashboard estático actual
- **Contras:** D1 (SQLite) tiene límites en consultas complejas, vendor lock-in, Juan no domina el stack

### B · Stack idéntico al ZenderBox WMS · instancia compartida
- **Pros:** cero curva de aprendizaje, máxima reutilización
- **Contras:** acopla negocios (legal, contable, operacional), dolor para desacoplar si Juan vende ZenderBox o separa contabilidades, mezcla de datos sensibles

### C · Stack idéntico al WMS · instancia separada ⭐ ADOPTADA
- Mismo stack tecnológico (Ubuntu + Postgres + n8n + nginx) pero **EC2 dedicado a Miramar** dentro de la cuenta AWS de **ZenderHub** (no ZenderBox)
- **Pros:**
  - Cero curva (Juan ya opera ese stack en el WMS)
  - Patrones reutilizables (deploy script, hub/*.html, /guardar commands)
  - Postgres > SQLite para crecimiento
  - n8n para workflows visuales (notificaciones, integraciones contables futuras)
  - Separación legal/contable entre negocios
- **Contras:** $20/mes (vs $0-5 de Cloudflare), responsabilidad operacional (patches, backups)

## Decisión

**Stack C.** Razones de peso:

1. Juan ya domina operacionalmente el stack n8n+Postgres+EC2 — el conocimiento es activo del proyecto
2. La separación entre cuenta AWS (zenderhub) y cuenta ZenderBox protege compliance y futura sucesión
3. n8n permite construir flows visuales para contabilidad/operaciones sin escribir backend custom para cada feature
4. Costo $20/mes es marginal para un sistema operacional de 10 años

## Implementación (F0)

- **AWS:** cuenta `zenderhub`, región `us-east-2` (Ohio · misma que ZenderHub para consistencia operacional)
- **EC2:** `miramar-n8n` · `t3.micro` (Free tier primer año) · Ubuntu 24.04 · 30 GB gp3 · IP pública `18.226.86.66`
- **Key pair:** `miramar-key.pem` (RSA · backup en 1Password vault Miramar · local en `~/Documents/ZenderBox/key/`)
- **Stack instalado:**
  - Postgres 16 (DB `miramar` para datos del negocio · DB `n8n_db` para n8n)
  - Docker + Docker Compose (29.x)
  - n8n self-hosted en container (`miramar-n8n` · port 5678 local) con Basic Auth + Postgres backend
  - nginx (sirve dashboard estático en `:80` + proxy a n8n en `/n8n/`)
  - UFW firewall (ports 22/80/443 abiertos) + Security Group AWS
- **Swap:** 2GB (crítico para t3.micro de 1GB RAM)
- **Zona horaria:** America/Bogota

## Implicaciones

- El dashboard de Cloudflare Pages (`rubiales.pages.dev`) sigue funcionando temporalmente. Se desactiva cuando el servidor propio tenga SSL + DNS y papá ya esté usando la nueva URL.
- Próximos pasos para terminar F0: DNS (subdominio en Cloudflare) + SSL (Let's Encrypt).
- F1 (DB schema + API endpoints sobre n8n) arranca después de F0 cerrada.
- Comando `/deploy` del WMS no aplica todavía — se va a clonar/adaptar a `/deploy-miramar` cuando F1 esté lista.

## Documentos relacionados

- Detalles de servidor y credenciales: `00-core/00-Memorias/servidor-miramar.md`
- Aprendizajes operacionales del setup: `00-core/00-Memorias/aprendizajes.md` (sección "Sobre AWS / EC2")
- Decisión D17 (rebrand a Miramar): `00-core/00-Memorias/decisiones.md`
