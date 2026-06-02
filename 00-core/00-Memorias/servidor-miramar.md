# Servidor Miramar · referencia operacional

> **⚠️ Las contraseñas NO viven en este archivo.** Todas las credenciales están en **1Password · vault Miramar**. Acá solo viven los identificadores estructurales (usernames, paths, puertos).

## Acceso

| Campo | Valor |
|---|---|
| **Cuenta AWS** | `zenderhub` |
| **Region** | `us-east-2` (Ohio) |
| **Instance ID** | `i-0fffc60275ebffa0f` |
| **Instance name** | `miramar-n8n` |
| **Tipo** | `t3.micro` (Free tier primer año) |
| **OS** | Ubuntu Server 24.04 LTS |
| **Public IPv4** | `18.226.86.66` (puede cambiar al detener/iniciar — considerar Elastic IP futuro) |
| **Disco** | 30 GB gp3 |
| **Swap** | 2 GB |
| **Zona horaria** | `America/Bogota` |

## SSH

```bash
ssh -i ~/Documents/ZenderBox/key/miramar-key.pem ubuntu@18.226.86.66
```

- **Usuario:** `ubuntu` (sudo sin password)
- **Key local:** `~/Documents/ZenderBox/key/miramar-key.pem` (permisos 400)
- **Key backup:** 1Password vault Miramar · item "miramar-key (EC2 SSH)"

## Security Group · AWS

Security group `launch-wizard-3` con reglas inbound:

| Puerto | Source | Notas |
|---|---|---|
| 22 (SSH) | `139.68.240.180/32` (IP de Juan) | **Si la IP de Juan cambia, hay que actualizar manualmente** |
| 80 (HTTP) | `0.0.0.0/0` | Anyone |
| 443 (HTTPS) | `0.0.0.0/0` | Anyone (pendiente activar SSL) |

UFW dentro del server: igual que arriba (22, 80, 443 abiertos).

## Postgres 16

Corriendo como servicio del host (`systemctl is-active postgresql`).

| DB | Usuario | Notas |
|---|---|---|
| `miramar` | `miramar_admin` | DB del negocio (datos del proyecto agropecuario) |
| `n8n_db` | `n8n_user` | DB de n8n (sus propios workflows/credenciales) |

- Configuración: `/etc/postgresql/16/main/postgresql.conf` (`listen_addresses = '*'` para que Docker se conecte vía bridge `172.17.0.1`)
- `pg_hba.conf` permite `172.17.0.0/16` con `scram-sha-256` (red Docker default)
- **Passwords en 1Password.**

Acceso desde el host:
```bash
sudo -u postgres psql
# o
psql -U miramar_admin -d miramar -h localhost
```

## Docker + n8n

- Docker version: 29.x · Docker Compose v5.x
- Stack: `/opt/miramar/n8n/docker-compose.yml`
- Container: `miramar-n8n`
- Puerto interno: `5678` (escucha solo en `127.0.0.1` — no expuesto a internet directo, se accede vía nginx proxy)
- Volumen de datos: `n8n_n8n_data` (workflows, credentials encryption key)
- Restart policy: `unless-stopped`

Comandos útiles:
```bash
cd /opt/miramar/n8n
sudo docker compose ps             # estado
sudo docker compose logs -f n8n    # logs en vivo
sudo docker compose restart n8n    # reiniciar
sudo docker compose pull && sudo docker compose up -d   # actualizar a versión nueva
```

## nginx

- Config principal: `/etc/nginx/sites-available/miramar` (linkeado en `sites-enabled/`)
- Root del dashboard: `/opt/miramar/web/` (sirve `index.html`, `data.json`)
- Proxy `/n8n/` → `http://127.0.0.1:5678/` (con WebSocket support)

Comandos:
```bash
sudo nginx -t                    # validar config
sudo systemctl reload nginx      # aplicar cambios
sudo tail -f /var/log/nginx/access.log
```

## Subir cambios del dashboard al servidor (manual por ahora)

Desde la Mac local, dentro del repo:

```bash
cd ~/Documents/Rubiales
scp -i ~/Documents/ZenderBox/key/miramar-key.pem \
  00-core/dashboard/index.html \
  00-core/dashboard/data.json \
  00-core/dashboard/README.md \
  ubuntu@18.226.86.66:/opt/miramar/web/
```

> **TODO F1:** automatizar deploy con un script `/deploy-miramar` (clon adaptado del `/deploy` del WMS).

## Pendientes para terminar F0

- [ ] Decidir subdominio definitivo provisional (`miramar.zenderhub.com` u otro)
- [ ] Crear registro A en Cloudflare → IP `18.226.86.66` (proxy OFF mientras se emite SSL)
- [ ] Instalar `certbot` y emitir certificado Let's Encrypt
- [ ] Configurar HTTPS en nginx + redirect HTTP → HTTPS
- [ ] (Opcional) Elastic IP para que la IP pública no cambie al reiniciar
- [ ] Snapshots automáticos del disco (Data Lifecycle Manager)

## F1 inmediatamente después

- [ ] Schema Postgres inicial: tablas `tasks`, `comments`, `photos`, `users`, `approvals`, `quotes`, etc.
- [ ] Webhooks n8n que exponen los datos del dashboard
- [ ] Migrar `data.json` a la DB con script idempotente
- [ ] Dashboard fetchea de `/api/...` en lugar de `/data.json`

## Backup / Disaster Recovery (pendiente F0 v2)

- Snapshots EBS automáticos (AWS Data Lifecycle Manager) · diarios, retención 7
- Dump de Postgres a S3 cada noche (cron + pg_dump + aws cli)
- Backup de `n8n_data` volume (workflows + credenciales encriptadas)
- Backup de `/etc/nginx/`, `/etc/postgresql/16/main/`

## Notas operacionales

- t3.micro tiene **CPU credits limitados** — si saturás, AWS te cobra extra. Monitorear en CloudWatch.
- 1 GB RAM + 2 GB swap es ajustado pero suficiente para esta carga. Si crece, upgrade a `t3.small` ($15/mes, sin downtime apreciable).
- Postgres 16 + Docker n8n + nginx + Postgres pueden compartir 1 GB RAM si no hay tráfico fuerte. Si llega a tener mucha actividad, separar Postgres a RDS managed.
