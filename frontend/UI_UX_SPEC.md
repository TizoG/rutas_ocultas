# UI/UX Blueprint — OpoMaster (Fase 1 + Fase 2)

## 1) Dirección visual
- Estilo: **premium + claro + motivador**.
- Inspiración: limpieza tipo Notion + feedback gamificado tipo Duolingo.
- Prioridad: mobile-first (80% uso).

## 2) Paleta tokenizada
- `--color-primary`: `#0066CC`
- `--color-primary-dark`: `#004499`
- `--color-bg`: `#F5F5F5`
- `--state-mastered`: `#22C55E`
- `--state-review`: `#F59E0B`
- `--state-progress`: `#FBBF24`
- `--state-new`: `#9CA3AF`
- `--state-urgent`: `#EF4444`

## 3) Tipografía
- Heading/Body: Inter + Segoe UI fallback.
- Escala: H1 32, H2 24, H3 20, Body 16, Small 14, Tiny 12.

## 4) Sistema de spacing
- Base: 4px.
- Espaciado estándar: 8 / 12 / 16 / 24 / 32.
- Touch targets: mínimo 44x44.

## 5) Componentes core
1. Button (Primary / Secondary / Danger; sm/md/lg)
2. Badge estado (No iniciado, En progreso, Revisar, Dominado, Nuevo, Urgente)
3. Progress bar (lineal + circular)
4. Card (radius 12, shadow suave)
5. Inputs con validación inline
6. Modal con overlay
7. Toast (5 segundos)
8. Skeleton + spinner

## 6) Arquitectura de pantallas
### Fase 1
- Onboarding (3)
- Auth (2)
- Home dashboard
- Temario: lista, grafo, detalle
- Ejercicios: selector, MCQ, abierta, resultado, análisis
- Progreso: resumen, plan semanal, tramposos, historial
- Contenido: biblioteca, visor, upload
- Perfil/config/notificaciones

### Fase 2
- Spaced repetition (3)
- Búsqueda semántica (2)
- Novedades legislativas (2)
- Dynamic KG (2)
- Learning analytics (3)
- Exercise generator (2)
- Intelligent recommender (2)

## 7) Flujos prioritarios de prototipo
1. Nuevo usuario (registro → primer ejercicio → feedback)
2. Rutina diaria (dashboard → recomendación → repaso)
3. Semana pre-examen (predicción → top 5 críticos → mejora)

## 8) Microinteracciones
- Page transition 200ms fade+slide.
- Botones hover 100ms.
- Modal open 150ms scale+fade.
- Confetti al dominar concepto.

## 9) Accesibilidad
- WCAG 2.1 AA.
- Contraste >= 4.5:1.
- No depender solo de color (icono + texto + color).

## 10) Entregables de diseño
- Figma con 40+ pantallas Fase 1 + 25+ Fase 2.
- Librería de componentes y variantes.
- Prototipo clickable de 3 flujos.
- Guía de handoff (tokens Tailwind/CSS, spacing, estados, motion).
