import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        opo: {
          blue: "#0066CC",
          "blue-dark": "#004499",
          bg: "#F5F7FB",
          white: "#FFFFFF",
          gray: "#F5F5F5",
          green: "#22C55E",
          orange: "#F59E0B",
          yellow: "#FBBF24",
          neutral: "#9CA3AF",
          red: "#EF4444",
          error: "#DC2626",
          info: "#3B82F6",
          purple: "#A855F7",
          teal: "#14B8A6",
          text: "#1F2937",
          "text-secondary": "#6B7280",
          border: "#E5E7EB",
        },
      },
      boxShadow: {
        opo: "0 10px 24px rgba(0,0,0,0.08)",
      },
      borderRadius: {
        card: "12px",
      },
    },
  },
  plugins: [],
};

export default config;
