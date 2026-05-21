import type React from "react"
import type { Metadata } from "next"
import "./globals.css"
import { Navigation } from "@/components/navigation"
import { LocationProvider } from "@/contexts/location-context"

export const metadata: Metadata = {
  title: "智慧社区服务平台 | YYC³ Smart City",
  description: "集快递收发、社区购物、物业服务于一体的便民平台",
  icons: {
    icon: [
      { url: "/favicon-16x16.png", sizes: "16x16", type: "image/png" },
      { url: "/favicon-32x32.png", sizes: "32x32", type: "image/png" },
      { url: "/favicon.ico", sizes: "any" },
    ],
    apple: "/apple-touch-icon.png",
  },
  manifest: "/yyc3-app-icons/pwa/manifest.json",
  openGraph: {
    title: "智慧社区服务平台 | YYC³ Smart City",
    description: "让生活更智能、更便捷、更温暖",
    images: ["/Family-001.png"],
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh-CN">
      <body className="font-sans">
        <LocationProvider>
          {children}
          <Navigation />
          <div className="pb-16 md:pb-0" />
        </LocationProvider>
      </body>
    </html>
  )
}
