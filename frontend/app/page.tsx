import { Compass, MapPinned } from "lucide-react";

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-5xl flex-col items-center justify-center gap-6 px-6 text-center">
      <div className="inline-flex items-center gap-2 rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300">
        <Compass className="h-4 w-4" />
        Frontend listo con Next.js + Tailwind + shadcn/ui base
      </div>
      <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
        Rutas Ocultas Platform
      </h1>
      <p className="max-w-2xl text-slate-300">
        Proyecto preparado para construir una experiencia de descubrimiento de rutas
        auténticas con animaciones, componentes reutilizables y arquitectura escalable.
      </p>
      <div className="inline-flex items-center gap-2 text-emerald-300">
        <MapPinned className="h-5 w-5" />
        Siguiente paso: conectar con el backend FastAPI.
      </div>
    </main>
  );
}
