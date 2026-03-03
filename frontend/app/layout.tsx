import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Rutas Ocultas",
  description: "Explora rutas auténticas y poco turísticas alrededor del mundo.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
