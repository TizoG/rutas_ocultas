# Plan de implementación del Home (estilo Travelor)

Este plan toma como referencia visual las capturas compartidas y busca replicar su estilo:

- Paleta principal teal + acentos amarillo/lima.
- Secciones amplias y visualmente diferenciadas.
- Tipografía de alto contraste para titulares.
- Tarjetas, bloques estadísticos y CTA redondeados.

## 1) Dirección visual

- **Color base**: gamas de verde petróleo (`#0f6a6b`, `#0f5d5f`) para hero y bloques destacados.
- **Acentos**: amarillo (`#e4ac16`) y lima (`#a3e635`) para llamados de acción y métricas.
- **Fondos alternos**: marfil claro y verde pálido para separar secciones.
- **Jerarquía tipográfica**: títulos grandes, subtítulos breves y cuerpo compacto.

## 2) Estructura de secciones (Home)

1. **Header fijo** en negro con marca y navegación.
2. **Hero** con mensaje principal, CTA y visual dominante.
3. **Bloque informativo** (recomendaciones, misión/visión y collage).
4. **Pasos de reserva** en 3 tarjetas.
5. **Destinos destacados** en bloque teal con grilla.
6. **Testimonios** con cards y estrellas.
7. **Métricas** (awards, viajeros, tours, experiencia).
8. **Noticias/blog** con 3 cards.
9. **Instagram + footer** con enlaces y suscripción.

## 3) Componentes reutilizables sugeridos

- `HeaderNav`
- `HeroSection`
- `FeatureCards`
- `BookingSteps`
- `DestinationGrid`
- `Testimonials`
- `StatsBar`
- `NewsGrid`
- `Footer`

> En la implementación actual se hizo una versión inicial en una sola página para validar look & feel.

## 4) Próximas mejoras recomendadas

- Integrar imágenes propias del proyecto para consistencia de marca.
- Añadir carruseles reales en destinos/categorías.
- Implementar variantes responsive más finas para móvil.
- Añadir microanimaciones (hover, reveal, scroll).
- Conectar contenido a CMS/API para datos dinámicos.

## 5) Criterio de fidelidad

Para considerar “fiel” el home respecto a la referencia:

- Debe conservar la misma **energía visual** (composición, contraste, bloques).
- Debe respetar **paleta y ritmo** de secciones.
- Debe incluir elementos clave: hero potente, cards de servicios, destinos, testimonios, noticias y footer robusto.
