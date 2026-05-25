# MiramarBox — Proyecto Avícola Rubiales

> Sistema de gestión del proyecto avícola free-range + plátano de la Sociedad Agropecuaria Miramar (Jaime Acuña e Hijos).
> Rubiales, Puerto Gaitán, Meta — Colombia.

**Repo provisional:** `ZenderBox/Rubiales` (se renombra a `MiramarBox` cuando el dominio del nombre quede aprobado).

## Estructura

Sigue el patrón modular de ZenderBox WMS: cada dominio tiene su propia carpeta numerada, y dentro vive `00-Memorias/` con pendientes y decisiones.

```
00-core/          Cross al proyecto: pendientes globales, decisiones cross,
                  incidentes, fotos de terreno, dashboard, editables (.docx).
01-galpon/        Construcción del galpón, planos, referencias técnicas,
                  lotes de gallinas, sanidad, postura.
02-platano/       Plántulas, potreros, cosechas.
03-finanzas/      Aportes de capital, banco agrario, Finagro, contadora,
                  snapshots mensuales.
04-regulatorio/   ICA, Cormacarena, FENAVI.
05-comercial/     Duflo y futuros canales (Bogotá, exportación).
06-proveedores/   Gallinas (Colaves, San Marino, Toscana), plántulas
                  (Agrosavia), construcción.
data/             CSV/JSON estructurados (postura diaria, mortalidad,
                  ventas, gastos). Vacío por ahora.
_pesados/         Local solamente (ignorado en git). Para archivos >10MB
                  cuando los haya. Por ahora vacío.
```

## Workflow

- **Branch por sesión** — nunca commit directo a `main`.
- **PR siempre** — el owner (Juan) mergea.
- **`/guarda-finca`** cierra la sesión: actualiza memorias, hace commit y push, abre PR.

## Estado del proyecto

Ver `00-core/Pendientes/README.md` para el estado actual y bloqueadores críticos.

## Documentos base

- Plan Maestro Finagro $200M — `03-finanzas/finagro/Proyecto Rubiales-Finagro200M.pdf`
- Setup Técnico (galpón, sistemas, plátano) — `01-galpon/construccion/SetupTecnico_Rubiales.pdf`
- Anexo Planos Visuales — `01-galpon/planos/Anexo2_Planos_Visuales_Rubiales.pdf`
- Hoja de Visita Proveedores Gallinas — `06-proveedores/gallinas/HojaVisita_Gallinas_ParaPapa.pdf`

## Confidencial

Este repo contiene información financiera, regulatoria y comercial sensible. **Privado.** No compartir credenciales, no incluir documentos personales (declaraciones de renta, cédulas) — esos van por canal directo al banco/contadora.
