# Dashboard MiramarBox · v1

Vista única del estado del proyecto. Lee `data.json` y renderiza bloqueadores, fases, módulos, KPIs y actividad reciente.

## Cómo usar local

El navegador bloquea `fetch()` sobre `file://`. Levantá un servidor local:

```bash
cd ~/Documents/Rubiales/00-core/dashboard
python3 -m http.server 8765
# abrir http://localhost:8765
```

## Cómo actualizar

**Solo se toca `data.json`.** El HTML/JS no se toca salvo que se agregue una sección nueva.

Campos clave:

- `meta.lastUpdate` — fecha YYYY-MM-DD del último cambio
- `meta.currentPhase` — fase actual (F0 / F1 / ...)
- `meta.nextMilestone` — próximo hito visible en la cinta gradiente
- `blockers[]` — bloqueadores críticos (rojos). `severity`: `critical` o `high`
- `phases[]` — pasos del roadmap. `status`: `done` / `in-progress` / `pending`
- `modules[]` — un objeto por módulo del repo. `status`: `active` / `quoting` / `blocked` / `pending` / `done`
- `kpis.production.active` — `false` mientras no haya postura. Cuando llegue el primer lote, pasar a `true` y llenar `kpis.items[].value`
- `activity[]` — últimos 6-8 eventos del proyecto (PRs, decisiones, llamadas importantes)

## Deploy futuro · GitHub Pages

Cuando esté listo:

1. Mover `index.html` y `data.json` al root del repo o configurar Pages a `/00-core/dashboard/`
2. Settings → Pages → Source: `main`, folder: `/00-core/dashboard`
3. URL queda `https://zenderbox.github.io/Rubiales/`
4. Repo es privado — Pages solo lo verán colaboradores invitados (org plan)

## Stack

- HTML vanilla + Plus Jakarta Sans (Google Fonts)
- Tokens del Design System de ZenderBox (cyan, navy, lime, ink-scale)
- JS vanilla con `fetch` + template literals
- Sin build, sin npm, sin dependencias

## Roadmap del propio dashboard

- **v1 (actual)** — read-only, alimentado por `data.json` manual
- **v2** — auto-pull de tareas desde los `00-Memorias/pendientes.md` de cada módulo (parser ligero)
- **v3** — captura de postura diaria desde formulario → `data/postura-diaria.csv` → KPIs en vivo
- **v4** — webhook desde n8n para entrada de datos vía WhatsApp del papá

No saltar fases. Evolucionar por dolor real.
