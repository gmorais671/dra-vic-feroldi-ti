import type { Metadata } from "next";
import localFont from "next/font/local";
import { Themes } from "@/components/ThemeControls";
import "./globals.css";
const inter = localFont({ src: "./fonts/inter-latin.woff2", variable: "--font-inter", weight: "100 900", display: "swap" });
const lora = localFont({ src: "./fonts/lora-latin.woff2", variable: "--font-lora", weight: "400 700", display: "swap" });
export const metadata: Metadata = {
  metadataBase: new URL("https://dravictorianunesferoldi.com.br"),
  title: "Dra. Victoria Nunes Feroldi | Cuidado em saúde mental",
  description: "Médica pós-graduada em psiquiatria. Conheça as modalidades de atendimento e os canais de agendamento online, em Taubaté e Campos do Jordão.",
  robots: { index: false, follow: false },
  openGraph: { title: "Dra. Victoria Nunes Feroldi", description: "Cuidado em saúde mental. Atendimento online e presencial.", locale: "pt_BR", type: "website" },
};
export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="pt-BR" suppressHydrationWarning><body className={`${inter.variable} ${lora.variable}`}><Themes>{children}</Themes></body></html>;
}
