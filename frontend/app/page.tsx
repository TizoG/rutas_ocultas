import {
  BadgeCheck,
  CalendarDays,
  CircleChevronRight,
  Compass,
  Globe,
  Instagram,
  Menu,
  Plane,
  Star,
  Users,
} from "lucide-react";
import type { ReactNode } from "react";

import { NavAuth } from "@/components/nav-auth";

const bookingSteps = [
  {
    id: "01",
    title: "Choose Destination",
    description:
      "Selecciona tu destino ideal entre experiencias de playa, montaña y aventura.",
  },
  {
    id: "02",
    title: "Make Payment",
    description:
      "Reserva de forma segura con confirmación inmediata y soporte personalizado.",
  },
  {
    id: "03",
    title: "Ready For Travelling",
    description:
      "Recibe itinerario, recomendaciones y checklist para viajar sin preocupaciones.",
  },
];

const destinations = ["Maldivas", "Indonesia", "Bali", "Mauricio", "París"];

const testimonials = [
  { name: "Daniel Smith", text: "Una experiencia impecable, desde la reserva hasta el regreso." },
  { name: "Emma Watson", text: "Me encantó la atención y lo visual de cada propuesta de viaje." },
];

export default function Home() {
  return (
    <main className="bg-[#edf4f3] text-[#0f5d5f]">
      <header className="sticky top-0 z-40 border-b border-white/10 bg-black/95 text-white backdrop-blur">
        <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div className="text-3xl font-semibold italic tracking-tight">
            Travelor<span className="text-lime-400">.</span>
          </div>
          <ul className="hidden gap-8 text-sm font-medium md:flex">
            {"Home About Us Pages Destination Tours Blog Contact".split(" ").map((item) => (
              <li key={item} className="cursor-pointer text-white/90 transition hover:text-lime-300">
                {item}
              </li>
            ))}
          </ul>
          <div className="flex items-center gap-4">
            <NavAuth />
            <Menu className="h-5 w-5" />
          </div>
        </nav>
      </header>

      <section className="relative overflow-hidden bg-[#0c6666] text-white">
        <div className="absolute inset-0 opacity-25 [background:radial-gradient(circle_at_top_right,#fff_0%,transparent_45%)]" />
        <div className="mx-auto grid max-w-6xl gap-10 px-6 py-20 md:grid-cols-[1.1fr_1fr] md:py-24">
          <div className="space-y-6">
            <p className="font-semibold tracking-wide text-white/90">Discover</p>
            <h1 className="text-5xl font-black leading-tight md:text-7xl">The World</h1>
            <p className="max-w-md text-lg text-white/90">
              El home sigue el mismo lenguaje visual de tu referencia: tipografías grandes,
              acentos amarillo/lima y bloques con textura de viaje.
            </p>
            <button className="rounded-full bg-lime-400 px-8 py-3 font-semibold text-slate-900 transition hover:bg-lime-300">
              Get In Touch
            </button>
          </div>
          <div className="relative flex items-end justify-center">
            <img
              src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=900&q=80"
              alt="Traveler"
              className="relative z-10 h-[380px] w-[280px] rounded-[2rem] object-cover shadow-2xl md:h-[470px] md:w-[340px]"
            />
            <div className="absolute -left-6 top-8 h-44 w-44 rounded-full border border-white/40" />
            <div className="absolute -right-3 top-1/2 hidden rounded-2xl bg-white/90 px-4 py-3 text-right text-[#0c6666] md:block">
              <p className="text-xs uppercase">Get up to</p>
              <p className="text-3xl font-bold">50%</p>
              <p className="text-sm font-medium">Discount</p>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-auto grid max-w-6xl gap-10 px-6 py-16 md:grid-cols-2">
        <div className="space-y-5">
          <h2 className="text-4xl font-bold leading-tight text-[#0d6d6d]">
            We Recommend <span className="text-[#e4ac16]">Beautiful</span> Destinations
          </h2>
          <p className="text-slate-600">
            Reproducimos el patrón del mockup: texto a la izquierda, tarjetas descriptivas y
            collage fotográfico a la derecha.
          </p>
          <div className="space-y-4">
            <article className="rounded-2xl border border-[#d9e5e4] bg-white p-5 shadow-sm">
              <h3 className="font-semibold text-[#0f5d5f]">Trusted travel guide</h3>
              <p className="text-sm text-slate-600">Información clara para planear rutas seguras.</p>
            </article>
            <article className="rounded-2xl border border-[#d9e5e4] bg-white p-5 shadow-sm">
              <h3 className="font-semibold text-[#0f5d5f]">Mission &amp; Vision</h3>
              <p className="text-sm text-slate-600">Conectar personas con experiencias transformadoras.</p>
            </article>
          </div>
        </div>
        <div className="grid grid-cols-2 gap-4">
          {["1", "2", "3", "4"].map((i) => (
            <img
              key={i}
              src={`https://images.unsplash.com/photo-150${i}60094789-cb6d3f4f1f9f?auto=format&fit=crop&w=500&q=80`}
              alt={`Destino ${i}`}
              className="h-40 w-full rounded-3xl object-cover shadow"
            />
          ))}
        </div>
      </section>

      <section className="bg-white py-16">
        <div className="mx-auto max-w-6xl px-6">
          <h2 className="text-center text-4xl font-bold">
            Easy Steps <span className="text-[#e4ac16]">For Bookings</span>
          </h2>
          <div className="mt-10 grid gap-5 md:grid-cols-3">
            {bookingSteps.map((step) => (
              <article key={step.id} className="rounded-2xl border border-[#e7ecec] p-6 shadow-sm">
                <div className="mb-4 inline-flex rounded-lg bg-[#0f6a6b] px-4 py-2 text-3xl font-bold text-white">
                  {step.id}
                </div>
                <h3 className="text-xl font-semibold text-[#0f5d5f]">{step.title}</h3>
                <p className="mt-2 text-sm text-slate-600">{step.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 py-16">
        <div className="rounded-3xl bg-[#0f6a6b] p-8 text-white">
          <div className="flex items-center justify-between gap-4">
            <h2 className="text-3xl font-bold">Destination</h2>
            <button className="inline-flex items-center gap-2 rounded-full bg-lime-400 px-5 py-2 font-semibold text-slate-900">
              View More <CircleChevronRight className="h-4 w-4" />
            </button>
          </div>
          <div className="mt-8 grid gap-4 md:grid-cols-5">
            {destinations.map((item) => (
              <article key={item} className="rounded-2xl border border-white/15 bg-white/5 p-4">
                <div className="mb-3 h-28 rounded-xl bg-gradient-to-br from-[#82c6c6] to-[#145d5d]" />
                <h3 className="font-semibold">{item}</h3>
                <p className="text-sm text-white/70">20 Listing</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-[#dff0ef] py-16">
        <div className="mx-auto max-w-6xl px-6">
          <h2 className="text-center text-4xl font-bold">Our Client <span className="text-[#e4ac16]">Says!</span></h2>
          <div className="mt-10 grid gap-6 md:grid-cols-2">
            {testimonials.map((item) => (
              <article key={item.name} className="rounded-2xl bg-white p-6 shadow-sm">
                <div className="mb-3 flex gap-1 text-[#e4ac16]">
                  {Array.from({ length: 5 }).map((_, idx) => (
                    <Star key={idx} className="h-4 w-4 fill-current" />
                  ))}
                </div>
                <h3 className="text-3xl font-semibold italic">{item.name}</h3>
                <p className="mt-3 text-slate-600">{item.text}</p>
              </article>
            ))}
          </div>

          <div className="mt-12 grid gap-4 rounded-2xl bg-[#0f6a6b] p-6 text-white md:grid-cols-4">
            <Stat icon={<BadgeCheck className="h-5 w-5" />} label="Awards Winning" value="3,600+" />
            <Stat icon={<Users className="h-5 w-5" />} label="Happy Traveler" value="7,634+" />
            <Stat icon={<Compass className="h-5 w-5" />} label="Tours Success" value="2.5K" />
            <Stat icon={<Globe className="h-5 w-5" />} label="Our Experience" value="25+" />
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 py-16">
        <div className="flex items-center justify-between gap-4">
          <h2 className="text-4xl font-bold">Explore <span className="text-[#e4ac16]">Latest News</span></h2>
          <button className="rounded-full bg-lime-400 px-6 py-2 font-semibold text-slate-900">See More Articles</button>
        </div>
        <div className="mt-8 grid gap-5 md:grid-cols-3">
          {["05", "06", "07"].map((day) => (
            <article key={day} className="overflow-hidden rounded-2xl bg-[#0f6a6b] text-white">
              <div className="h-44 bg-gradient-to-br from-[#8ec9c9] to-[#0d4f4f]" />
              <div className="space-y-3 p-5">
                <span className="inline-flex items-center gap-1 rounded-md bg-white/15 px-3 py-1 text-xs"><CalendarDays className="h-3 w-3" /> {day} June</span>
                <h3 className="text-2xl font-semibold">The Best Ways to Travel with Your Significant Other</h3>
              </div>
            </article>
          ))}
        </div>
      </section>

      <footer className="bg-[#f5f5e8] pt-14 text-[#0f5d5f]">
        <div className="mx-auto max-w-6xl px-6">
          <h3 className="text-center text-4xl font-bold">Follow Instagram</h3>
          <div className="mt-7 grid grid-cols-2 gap-3 sm:grid-cols-4 md:grid-cols-8">
            {Array.from({ length: 8 }).map((_, idx) => (
              <div key={idx} className="aspect-square rounded-xl bg-gradient-to-br from-[#8ec9c9] to-[#0f6a6b]" />
            ))}
          </div>

          <div className="mt-14 grid gap-8 border-t border-[#dce3d9] py-10 md:grid-cols-4">
            <div>
              <div className="text-3xl font-semibold italic">Travelor<span className="text-lime-500">.</span></div>
              <p className="mt-3 text-sm text-[#457a7a]">Estrategia de viajes y experiencias auténticas.</p>
              <div className="mt-4 flex gap-3">
                <SocialIcon icon={<Instagram className="h-4 w-4" />} />
                <SocialIcon icon={<Plane className="h-4 w-4" />} />
                <SocialIcon icon={<Globe className="h-4 w-4" />} />
              </div>
            </div>
            <FooterCol title="Explore" links={["About Us", "FAQ's", "Services", "Team", "News & Articles"]} />
            <FooterCol title="Destinations" links={["Tokyo", "France", "Dubai", "Kenya", "Vietnam"]} />
            <FooterCol title="Legal" links={["Terms & Condition", "Privacy Policy", "Contact", "Careers", "Help"]} />
          </div>

          <div className="mb-10 flex flex-col items-center justify-between gap-4 rounded-2xl bg-[#0f6a6b] p-5 text-white md:flex-row">
            <h4 className="text-3xl font-bold">Subscribe <span className="text-[#e4ac16]">Now!</span></h4>
            <div className="flex w-full max-w-md items-center rounded-full bg-white p-2">
              <input className="w-full bg-transparent px-4 py-2 text-sm text-slate-700 outline-none" placeholder="Email address" />
              <button className="rounded-full bg-[#0f6a6b] p-3 text-white"><CircleChevronRight className="h-4 w-4" /></button>
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}

function Stat({
  icon,
  label,
  value,
}: {
  icon: ReactNode;
  label: string;
  value: string;
}) {
  return (
    <div className="rounded-xl border border-white/10 bg-white/5 p-4">
      <div className="mb-2 inline-flex rounded-full bg-white/10 p-2">{icon}</div>
      <p className="text-sm text-white/70">{label}</p>
      <p className="text-3xl font-bold text-[#e4ac16]">{value}</p>
    </div>
  );
}

function FooterCol({ title, links }: { title: string; links: string[] }) {
  return (
    <div>
      <h5 className="text-2xl font-semibold">{title}</h5>
      <ul className="mt-3 space-y-2 text-[#457a7a]">
        {links.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

function SocialIcon({ icon }: { icon: ReactNode }) {
  return <span className="rounded-full border-2 border-[#e4ac16] bg-[#0f6a6b] p-2 text-white">{icon}</span>;
}
