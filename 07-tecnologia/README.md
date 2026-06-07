# 07-tecnologia · Infraestructura tech de la finca

Módulo cross para toda la infraestructura tecnológica de Miramar: internet, IoT, cámaras, sensores, energía, backups.

## Filosofía

La finca de Rubiales se diseña como **finca IoT-ready desde el día 1**. Mejor invertir bien una vez que parchar después.

## Estructura

```
07-tecnologia/
├── 00-Memorias/
│   ├── pendientes.md       · Qué falta
│   ├── decisiones.md       · Por qué cada equipo / proveedor
│   └── arquitectura.md     · Diagrama del setup completo
├── starlink/               · Internet base · proveedor único hoy realista
├── camaras/                · CCTV galpón + acceso predio
├── sensores/               · Temperatura, humedad, agua, báscula
├── energia/                · UPS, inversor, solar futuro
└── README.md
```

## Estado actual

| Componente | Estado |
|---|---|
| Internet base (Starlink) | 🔍 En investigación · objetivo viernes 12-jun |
| Cámaras IP galpón | ⏳ Pendiente · post-arranque |
| Sensores ambientales | ⏳ Pendiente · post-arranque |
| Báscula conectada | ⏳ Pendiente |
| Energía respaldo | ⏳ UPS mínimo desde día 1 |
| Backup conectividad | ⏳ SIM celular Claro/Movistar como failover |

## Estrategia de despliegue por fases

### Fase A · Conectividad básica (semana 8-12 jun)
- Starlink kit en la finca
- Router con bypass CGNAT si aplica
- 1 cámara IP de prueba para validar acceso remoto
- UPS pequeño para mantener el Starlink en cortes

### Fase B · IoT operacional (post arranque del galpón)
- Cámaras CCTV galpón (4-6 puntos)
- Sensores temperatura/humedad galpón
- Sensor nivel pozo de agua
- Báscula de huevos o de alimento conectada

### Fase C · Autonomía energética (Fase 2 Finagro)
- Paneles solares
- Baterías
- Sistema unificado de energía 24/7

## Próximo paso inmediato

Esperar resultado de deep-research sobre Starlink Colombia · objetivo: tener kit en Bogotá viernes 12-jun para llevar a la finca.
