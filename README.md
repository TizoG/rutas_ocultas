# 🌍 Rutas Ocultas Platform

Plataforma web de viajes centrada en el descubrimiento y la compartición de rutas auténticas, alternativas y poco turísticas alrededor del mundo.

El objetivo del proyecto es inspirar a viajeros a explorar destinos desde una perspectiva diferente, priorizando experiencias locales, culturales y fuera de los circuitos masificados.

---

# ✨ Features

- 🔎 Exploración de rutas por países y ciudades  
- 🧭 Filtros por tipo de turismo (aventura, cultural, naturaleza, gastronómico, etc.)  
- 🔥 Ranking de rutas en tendencia (Trending Top)  
- 📍 Detalle completo de itinerarios con mapa  
- 👥 Comunidad de viajeros  
- 👍 Sistema de votos y valoraciones  
- 💬 Comentarios en rutas  
- ➕ Publicación de rutas por usuarios  
- ❤️ Guardado de rutas favoritas  
- 📰 Newsletter de nuevas rutas  

---

# 🧱 Tech Stack

## Frontend
- **Next.js 14+ (App Router)**
- **TypeScript**
- **Tailwind CSS**
- **shadcn/ui**
- **Framer Motion**
- **Lucide Icons**

## Backend
- Next.js API Routes / Server Actions

## Database
- **PostgreSQL**
- **Prisma ORM**

## Auth
- Clerk

## Storage
- Cloudinary

## Maps
- Mapbox / Google Maps API

## Email / Newsletter
- Resend / SendGrid

## Deploy
- Vercel  
- Railway / Render

---

# 🗂️ Project Structure

```bash
/app
  /(marketing)
  /(platform)
  /routes
  /community
  /trending
  /search
  /newsletter

/components
  /ui
  /routes
  /community

/lib
  /db
  /auth
  /utils

/prisma
  schema.prisma

/public
