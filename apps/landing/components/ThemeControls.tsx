"use client";
import { ThemeProvider, useTheme } from "next-themes";
import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";
export function Themes({ children }: { children: React.ReactNode }) {
  return <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>{children}</ThemeProvider>;
}
export function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => { const id = requestAnimationFrame(() => setMounted(true)); return () => cancelAnimationFrame(id); }, []);
  const dark = mounted && theme === "dark";
  return <button className="theme-toggle" aria-label={dark ? "Ativar tema claro" : "Ativar tema escuro"} aria-pressed={dark} onClick={() => setTheme(dark ? "light" : "dark")}>{dark ? <Sun size={20}/> : <Moon size={20}/>}</button>;
}
