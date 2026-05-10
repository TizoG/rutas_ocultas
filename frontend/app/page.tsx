import {
  BookOpen,
  Brain,
  CalendarClock,
  ChartSpline,
  CircleCheck,
  CircleDot,
  Play,
  Timer,
} from "lucide-react";

const reviewItems = [
  { concept: "Acción en Derecho Penal", delay: "+2 días", state: "revisar" },
  { concept: "Tipicidad", delay: "hoy", state: "progreso" },
  { concept: "Causalidad", delay: "+5 días", state: "urgente" },
];

const activity = [
  "Hace 2 horas: Completaste evaluación de Acción [85%]",
  "Hace 5 horas: Dominaste Tipicidad",
  "Ayer: Completaste 3 ejercicios",
];

export default function Home() {
  return (
    <main className="min-h-screen bg-opo-bg text-opo-text">
      <header className="sticky top-0 z-20 border-b border-opo-border bg-white/90 backdrop-blur">
        <div className="mx-auto flex h-16 w-full max-w-6xl items-center justify-between px-4 md:px-6">
          <div className="flex items-center gap-2 font-bold text-opo-blue-dark">
            <Brain className="h-5 w-5" /> OpoMaster
          </div>
          <div className="hidden text-sm text-opo-text-secondary md:block">Policía Nacional · 2026</div>
          <button className="rounded-lg border border-opo-border px-3 py-2 text-sm">Perfil</button>
        </div>
      </header>

      <section className="mx-auto grid w-full max-w-6xl gap-6 px-4 py-6 md:grid-cols-[1.4fr_1fr] md:px-6">
        <article className="rounded-xl bg-opo-blue p-6 text-white shadow-opo">
          <p className="mb-2 text-sm text-white/80">Recomendación del día</p>
          <h1 className="text-3xl font-bold">Hoy debes estudiar: Acción en Derecho Penal</h1>
          <p className="mt-3 text-sm text-white/90">Es crítico [90%] + Ya olvidaste [40%]</p>
          <div className="mt-5 flex flex-wrap gap-3">
            <button className="inline-flex items-center gap-2 rounded-lg bg-white px-4 py-2 font-semibold text-opo-blue-dark">
              <Play className="h-4 w-4" /> Empezar ahora
            </button>
            <button className="rounded-lg border border-white/50 px-4 py-2">Ver más recomendaciones</button>
          </div>
        </article>

        <article className="rounded-xl border border-opo-border bg-white p-6 shadow-opo">
          <p className="text-sm text-opo-text-secondary">Progreso general</p>
          <div className="mt-3 flex items-center gap-4">
            <div className="grid h-24 w-24 place-items-center rounded-full border-8 border-opo-green text-xl font-bold text-opo-blue-dark">65%</div>
            <ul className="space-y-1 text-sm">
              <li>12 conceptos dominados</li>
              <li>8 en repaso</li>
              <li>5 sin empezar</li>
            </ul>
          </div>
        </article>
      </section>

      <section className="mx-auto grid w-full max-w-6xl gap-6 px-4 pb-12 md:grid-cols-3 md:px-6">
        <article className="rounded-xl border border-opo-border bg-white p-5 shadow-opo md:col-span-2">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-lg font-semibold">Próximos repasos</h2>
            <CalendarClock className="h-5 w-5 text-opo-text-secondary" />
          </div>
          <div className="space-y-3">
            {reviewItems.map((item) => (
              <div key={item.concept} className="flex items-center justify-between rounded-lg border border-opo-border p-3">
                <div className="flex items-center gap-2">
                  <CircleDot className="h-4 w-4 text-opo-orange" />
                  <span>{item.concept}</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="rounded-full bg-opo-gray px-2 py-1 text-xs text-opo-text-secondary">{item.delay}</span>
                  <button className="text-sm font-medium text-opo-blue">Repasar</button>
                </div>
              </div>
            ))}
          </div>
        </article>

        <article className="rounded-xl border border-opo-border bg-white p-5 shadow-opo">
          <h2 className="mb-4 text-lg font-semibold">Últimas actividades</h2>
          <ul className="space-y-3 text-sm text-opo-text-secondary">
            {activity.map((item) => (
              <li key={item} className="flex gap-2"><CircleCheck className="mt-0.5 h-4 w-4 text-opo-teal" />{item}</li>
            ))}
          </ul>
        </article>

        <article className="rounded-xl border border-opo-border bg-white p-5 shadow-opo">
          <h3 className="mb-3 flex items-center gap-2 font-semibold"><BookOpen className="h-4 w-4" /> Temario</h3>
          <p className="text-sm text-opo-text-secondary">Vista de lista + grafo interactivo con estado por concepto.</p>
        </article>
        <article className="rounded-xl border border-opo-border bg-white p-5 shadow-opo">
          <h3 className="mb-3 flex items-center gap-2 font-semibold"><ChartSpline className="h-4 w-4" /> Analytics</h3>
          <p className="text-sm text-opo-text-secondary">Predicción de aprobado, conceptos tramposos y evolución semanal.</p>
        </article>
        <article className="rounded-xl border border-opo-border bg-white p-5 shadow-opo">
          <h3 className="mb-3 flex items-center gap-2 font-semibold"><Timer className="h-4 w-4" /> Spaced repetition</h3>
          <p className="text-sm text-opo-text-secondary">Repasos urgentes, plan semanal y métricas SM-2.</p>
        </article>
      </section>

      <nav className="fixed bottom-0 left-0 right-0 border-t border-opo-border bg-white p-2 md:hidden">
        <ul className="grid grid-cols-4 text-center text-xs">
          <li className="font-semibold text-opo-blue">Inicio</li>
          <li>Temario</li>
          <li>Progreso</li>
          <li>Perfil</li>
        </ul>
      </nav>
    </main>
  );
}
