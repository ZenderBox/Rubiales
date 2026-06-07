# Decisiones — 07-tecnologia

> Por qué cada equipo / proveedor. Para no re-discutir lo ya cerrado.

## 2026-06-07

### D01 · Crear módulo 07-tecnologia
- **Decisión:** infraestructura tech vive en un módulo cross propio (no en 01-galpon ni 06-proveedores).
- **Por qué:** la red Starlink + IoT atraviesa galpón, plátano, energía, regulatorio. Tener un solo dueño técnico evita decisiones contradictorias.
- **Owner técnico:** Juan.

### D02 · Starlink como internet base (no fibra ni 4G)
- **Decisión:** Starlink es la primera opción.
- **Por qué:**
  - Fibra: no hay cobertura en vereda Santa Helena (Puerto Gaitán rural).
  - 4G/5G: cobertura irregular, latencia alta para videollamadas con Juan.
  - Starlink: 100% cobertura satelital + latencia LEO razonable (40-60ms típico).
- **Verificación pendiente:** confirmar disponibilidad Residential en coordenadas exactas (deep-research en curso).

### D03 · IoT-ready desde día 1
- **Decisión:** dimensionar la red para 5-15 dispositivos IoT desde el arranque.
- **Por qué:** cambiar router/red después es más caro que comprar bien una vez.

### D04 · UPS obligatorio para Starlink + router
- **Decisión:** UPS de mínimo 800VA para el rack de red.
- **Por qué:** la finca tiene cortes frecuentes de energía. Sin UPS, la conectividad se cae con cada bajón → cámaras pierden grabación, sensores desincronizan.
