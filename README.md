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

# crear una nueva migración
alembic revision --autogenerate -m "init schema"

# aplicar migraciones pendientes
alembic upgrade head
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


## 🔐 Autenticación end-to-end con Clerk

Se integró Clerk en frontend y backend para proteger acciones de escritura (crear/editar rutas, comentar, votar y favoritos).

### Variables de entorno requeridas

#### Frontend (`frontend/.env.local`)
```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxx
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxx
```

> Puedes usar `frontend/.env.local.example` como plantilla.

#### Backend (`backend/.env`)
```bash
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rutas_ocultas
CLERK_ISSUER=https://your-clerk-domain.clerk.accounts.dev
CLERK_JWKS_URL=https://your-clerk-domain.clerk.accounts.dev/.well-known/jwks.json
CLERK_AUDIENCE=
```

> `CLERK_AUDIENCE` es opcional y solo se valida si lo configuras.

### Flujo completo

1. El usuario inicia sesión en Next.js mediante `SignInButton` (Clerk).
2. Clerk entrega sesión/token JWT al frontend.
3. El frontend envía el JWT como `Authorization: Bearer <token>` al backend.
4. FastAPI valida firma y claims del JWT contra el JWKS de Clerk (`CLERK_JWKS_URL`) y `CLERK_ISSUER`.
5. Con el `sub` del token se crea/actualiza el usuario local en tabla `users` usando `clerk_user_id`.
6. Endpoints protegidos usan `get_current_user` y bloquean acceso sin token válido.

### Endpoints protegidos

- `POST /api/routes`
- `PUT /api/routes/{route_id}`
- `POST /api/comments`
- `POST /api/votes`
- `POST /api/favorites`
