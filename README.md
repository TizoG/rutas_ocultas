# 🌍 Rutas Ocultas Platform

Plataforma web de viajes centrada en descubrir y compartir rutas auténticas, alternativas y poco turísticas.

Este repositorio quedó preparado con:
- **Frontend en Next.js 14 + TypeScript + Tailwind**.
- **Backend en FastAPI (Python)**.
- **Base de datos recomendada: PostgreSQL**.

---

## ✅ Decisión de base de datos: ¿MongoDB o PostgreSQL?

Para este proyecto, **PostgreSQL es la mejor opción inicial**.

### PostgreSQL (recomendado)
**Ventajas para Rutas Ocultas:**
- Datos relacionales claros: usuarios, rutas, comentarios, votos, favoritos, newsletter.
- Integridad referencial (FK, constraints) útil para evitar inconsistencias.
- Buen rendimiento en consultas complejas (trending, filtros combinados, rankings).
- Escalable y estándar para apps web con analítica y reportes.

### MongoDB (cuándo sí elegirlo)
- Si el esquema cambia constantemente y necesitas mucha flexibilidad documental.
- Si priorizas almacenamiento tipo documento con joins mínimos.

### Conclusión
- **Empieza con PostgreSQL** para tener base sólida y consistente.
- MongoDB puede considerarse después para módulos específicos (ej. eventos o logs), pero no como core principal.

---

## 🧱 Tech Stack

### Frontend
- **Next.js 14+ (App Router)**
- **TypeScript**
- **Tailwind CSS**
- **shadcn/ui (base preparada)**
- **Framer Motion**
- **Lucide Icons**

### Backend
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **Pydantic Settings**
- **Uvicorn**

### Base de datos
- **PostgreSQL**

---

## 🗂️ Estructura del proyecto

```bash
/backend
  /app
    /api
      routes.py
    /core
      config.py
    /db
      session.py
    main.py
  requirements.txt
  .env.example

/frontend
  /app
    layout.tsx
    page.tsx
    globals.css
  /lib
    utils.ts
  package.json
  tailwind.config.ts
```

---

## ⚙️ Instalación del entorno (ya preparada)

> Requisitos del sistema:
- Python 3.11+
- Node.js 20+
- npm 10+
- PostgreSQL 15+

### 1) Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

API disponible en:
- `http://localhost:8000`
- Docs Swagger: `http://localhost:8000/docs`

### 2) Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

Frontend disponible en:
- `http://localhost:3000`

### 3) Conexión frontend ↔ backend

Usa el backend en `http://localhost:8000` y llama endpoints como:
- `GET /api/health`

---

## 🧪 Comandos útiles

### Backend
```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm run dev
npm run lint
```

---

## 🚀 Próximos pasos sugeridos

1. Definir modelos SQLAlchemy (`User`, `Route`, `Comment`, `Vote`, `Favorite`).
2. Configurar migraciones con Alembic.
3. Implementar autenticación (Clerk/JWT).
4. Conectar mapas (Mapbox/Google Maps).
5. Añadir módulos de comunidad y trending.
