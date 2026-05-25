# CLAUDE.md — Instrucciones para Claude en MiramarBox

Este archivo se carga automáticamente cuando Claude entra a este repo. Define el contrato de trabajo.

## Contexto rápido

- **Proyecto:** granja avícola free-range + plátano Dominico Hartón, Rubiales (Puerto Gaitán, Meta).
- **Sociedad:** Sociedad Agropecuaria Miramar — Jaime Acuña e Hijos.
- **Socios:** Juan Acuña 64% (Miami, estrategia/finanzas) · Alejandro Acuña 33% · Jaime Acuña (papá, gestor en campo).
- **Comprador:** Duflo.
- **Financiación objetivo:** Finagro $200M.
- **Estado:** pre-arranque — definiendo trámites (ICA, Cormacarena), proveedores y financiación inicial.

## Estructura

Patrón clonado del WMS ZenderBox: módulos numerados, cada uno con `00-Memorias/`.

| Carpeta | Para qué |
|---|---|
| `00-core/` | Cross al proyecto: dashboard, pendientes globales, decisiones cross, incidentes, fotos. |
| `01-galpon/` | Todo lo del galpón: construcción, planos, lotes, sanidad, postura. |
| `02-platano/` | Plántulas, potreros, cosechas. |
| `03-finanzas/` | Aportes, banco, Finagro, contadora. |
| `04-regulatorio/` | ICA, Cormacarena, FENAVI. |
| `05-comercial/` | Duflo y futuros canales. |
| `06-proveedores/` | Gallinas, plántulas, construcción. |
| `data/` | CSV/JSON estructurados (futuro). |
| `_pesados/` | Local, ignorado en git. |

## Reglas de trabajo

1. **Nunca commit directo a `main`.** Siempre branch + PR. El owner (Juan) mergea.
2. **Nunca `git add .`** — agregar archivos específicos.
3. **Conventional commits**: `feat(modulo): ...`, `docs(modulo): ...`, `fix(modulo): ...`.
4. **Memorias siempre en español** — papá y contadora deben poder leerlas.
5. **Cerrar sesión con `/guarda-finca`** — actualiza memorias + commit + push + PR.
6. **No tocar `_pesados/`** desde claude — es local del owner.
7. **No incluir documentos personales** en el repo (declaraciones de renta, cédulas, fotos privadas).
8. **Decisiones estratégicas se discuten con el owner antes de codificarlas** — no asumir.

## Memorias — dónde escribir qué

- **Pendientes de un módulo** → `<modulo>/00-Memorias/pendientes.md`
- **Pendientes globales / semanales** → `00-core/Pendientes/semana-YYYY-MM-DD.md`
- **Decisiones de un módulo** → `<modulo>/00-Memorias/decisiones.md`
- **Decisiones cross-módulo** → `00-core/06-Decisiones/NNNN-titulo-fecha.md`
- **Incidente sanitario / operativo** → `00-core/07-Incidentes/YYYY-MM-DD_titulo.md`
- **Contactos** → `00-core/00-Memorias/contactos.md`
- **Aprendizajes operativos** → `00-core/00-Memorias/aprendizajes.md`
- **Contexto general del proyecto** → `00-core/00-Memorias/contexto-proyecto.md`

## Lo crítico del proyecto

1. **Cormacarena (permiso de agua)** es el bloqueador #1. Sin agua no hay ICA. Sin ICA no hay proyecto.
2. **Banco Agrario** debe reactivarse para recibir el aporte USD 10K de Juan desde Miami.
3. **Asincronía Juan–Papá–Alejandro** es el problema operativo. El dashboard (en construcción) lo resuelve.
4. **Free-range NO está prohibido en Colombia** — ver `04-regulatorio/ica/regulatorio-ica.md`. La certificación seria es la Resolución ICA 16409 de 2024 (Bienestar Animal).

## Antes de cualquier sesión nueva

1. Leer `00-core/Pendientes/README.md` (estado actual + bloqueadores).
2. Leer `00-core/00-Memorias/contexto-proyecto.md` si es la primera vez.
3. Confirmar con el owner en qué módulo se va a trabajar.
