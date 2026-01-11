export const metadata = {
  title: 'Notes Manager',
  description: 'Notes Manager App',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* Tailwind CDN */}
        <script src="https://cdn.tailwindcss.com"></script>
      </head>
      <body className="bg-gray-50">{children}</body>
    </html>
  );
}
