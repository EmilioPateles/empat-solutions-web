# EMPAT Solutions - Zrzut Kodu

### Plik: `astro.config.mjs`
```astro
// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()]
  }
});
```

### Plik: `src/layouts/Layout.astro`
```astro
---
import Header from '../components/Header.astro';
import '../styles/global.css';

interface Props {
  title: string;
  lang?: string;
}

const { title, lang = 'pl' } = Astro.props;
---

<!doctype html>
<html lang={lang}>
  <head>
    <meta charset="UTF-8" />
    <meta name="description" content="EMPAT Solutions - Rozwój napędzany przez Sztuczną Inteligencję" />
    <meta name="viewport" content="width=device-width" />
    <link rel="icon" type="image/png" href="/logo.png" />
    <meta name="generator" content={Astro.generator} />
    <title>{title} | EMPAT Solutions</title>
  </head>
  <body class="bg-slate-900 text-slate-300 font-sans antialiased selection:bg-cyan-500/30 selection:text-cyan-200 flex flex-col min-h-screen">
    <Header lang={lang} />
    <main class="flex-grow">
      <slot />
    </main>
  </body>
</html>

```

### Plik: `src/components/Header.astro`
```astro
---
const { lang = 'pl' } = Astro.props;

// Pobieramy aktualną ścieżkę z serwera
const pathname = Astro.url.pathname;
// Normalizujemy ścieżkę (usuwamy slash na końcu)
const currentPath = pathname.endsWith('/') && pathname.length > 1 ? pathname.slice(0, -1) : pathname;

// Słownik precyzyjnego routingu (Blog usunięty)
const pathTranslations: Record<string, string> = {
  '/pl': '/en/',
  '/en': '/pl/',
  '/pl/o-mnie': '/en/about',
  '/en/about': '/pl/o-mnie',
  '/pl/projekty': '/en/projects',
  '/en/projects': '/pl/projekty',
  '/pl/kontakt': '/en/contact',
  '/en/contact': '/pl/kontakt',
};

// Zaktualizowany Słownik Nawigacji (Blog usunięty)
const nav = {
  pl: [
    { title: "Home", url: "/pl/" },
    { title: "O mnie", url: "/pl/o-mnie" },
    { title: "Projekty", url: "/pl/projekty" },
    { title: "Kontakt", url: "/pl/kontakt" },
  ],
  en: [
    { title: "Home", url: "/en/" },
    { title: "About", url: "/en/about" },
    { title: "Projects", url: "/en/projects" },
    { title: "Contact", url: "/en/contact" },
  ]
};

const currentNav = nav[lang as keyof typeof nav];
const btnText = lang === 'pl' ? "Darmowa Konsultacja" : "Free Consultation";
const btnLink = lang === 'pl' ? "/pl/kontakt" : "/en/contact";

// Przełącznik języków
const switchLangUrl = pathTranslations[currentPath] || (lang === 'pl' ? "/en/" : "/pl/");
const switchLangText = lang === 'pl' ? "EN" : "PL";
---

<header class="fixed w-full top-0 z-50 bg-slate-900/95 backdrop-blur-sm border-b border-slate-800 transition-all">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-24">
      
      <div class="flex-shrink-0 flex items-center">
        <a href={lang === 'pl' ? "/pl/" : "/en/"} aria-label="EMPAT Solutions - Home" class="focus:outline-none focus:ring-2 focus:ring-cyan-400 rounded">
          <img src="/logo.png" alt="EMPAT Solutions Logo" class="h-16 md:h-20 w-auto object-contain rounded-sm" />
        </a>
      </div>

      <nav class="hidden md:flex space-x-8">
        {currentNav.map(item => (
          <a href={item.url} class="text-lg text-slate-300 hover:text-cyan-400 font-medium tracking-wide transition-colors duration-300">
            {item.title}
          </a>
        ))}
      </nav>

      <div class="hidden md:flex items-center space-x-4">
        <a href={switchLangUrl} class="text-slate-400 hover:text-white font-bold px-3 py-1 border border-slate-700 rounded-md transition-colors hover:border-cyan-500">
          {switchLangText}
        </a>
        
        <a href={btnLink} class="bg-cyan-500 hover:bg-cyan-400 text-slate-900 px-6 py-2 rounded-md font-bold transition-all duration-300 shadow-[0_0_15px_rgba(6,182,212,0.3)] hover:shadow-[0_0_25px_rgba(6,182,212,0.6)]">
          {btnText}
        </a>
      </div>

    </div>
  </div>
</header>
<div class="h-24"></div>

```

### Plik: `src/pages/pl/index.astro`
```astro
---
// Poprawiona ścieżka importu (cofamy się o dwa poziomy: pl -> pages -> src)
import Layout from '../../layouts/Layout.astro';
---

<Layout title="Strona Główna" lang="pl">
  <section class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-3xl mx-auto">
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight text-white mb-6">
          Rozwój napędzany przez <br /><span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">Sztuczną Inteligencję</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-300 mb-10">
          Optymalizujemy procesy, zwiększamy wydajność i wdrażamy bezpieczne rozwiązania AI dla Twojego biznesu. Przejdź na wyższy poziom operacyjny.
        </p>
        
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <a href="/pl/kontakt" class="bg-cyan-500 hover:bg-cyan-400 text-slate-900 px-8 py-3 rounded-md font-bold transition-all duration-300 shadow-[0_0_15px_rgba(6,182,212,0.3)] hover:shadow-[0_0_25px_rgba(6,182,212,0.6)]">
            Rozpocznij transformację
          </a>
          <a href="/pl/projekty" class="border border-slate-600 hover:border-cyan-400 text-white px-8 py-3 rounded-md font-bold transition-all duration-300">
            Zobacz nasze realizacje
          </a>
        </div>
      </div>
    </div>

    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-900/20 rounded-full blur-[120px] -z-10 pointer-events-none"></div>
  </section>
</Layout>

<section class="py-24 bg-slate-900/50 border-t border-slate-800 relative z-10 overflow-hidden">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-500/5 rounded-full blur-[80px] pointer-events-none"></div>

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <h2 class="text-sm font-bold tracking-widest text-cyan-500 uppercase mb-8">Zaufali nam</h2>

      <div id="testimonial-wrapper" class="relative min-h-[250px] md:min-h-[200px] flex items-center justify-center">

        <div class="testimonial-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100 translate-x-0 flex flex-col justify-center items-center">
          <svg class="w-12 h-12 text-cyan-500/20 mb-6 mx-auto" fill="currentColor" viewBox="0 0 32 32"><path d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.896 3.456-8.352 9.12-8.352 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z"/></svg>
          <p class="text-2xl md:text-3xl font-medium text-slate-200 italic mb-8 leading-relaxed max-w-3xl">
            "Szkolenie otworzyło mi oczy i pomogło zrozumieć możliwości, które daje sztuczna inteligencja."
          </p>
          <div>
            <div class="text-white font-bold text-lg">Wiktoria Papała</div>
            <div class="text-cyan-400">Właścicielka, Papaja Tatuaże</div>
          </div>
        </div>

        <div class="testimonial-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 translate-x-8 pointer-events-none flex flex-col justify-center items-center">
          <svg class="w-12 h-12 text-cyan-500/20 mb-6 mx-auto" fill="currentColor" viewBox="0 0 32 32"><path d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.896 3.456-8.352 9.12-8.352 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z"/></svg>
          <p class="text-2xl md:text-3xl font-medium text-slate-200 italic mb-8 leading-relaxed max-w-3xl">
            "Dzięki Emilowi znalazłam przyjaciela idealnego."
          </p>
          <div>
            <div class="text-white font-bold text-lg">Iza Dudzik</div>
            <div class="text-cyan-400">Ilustratorka / Praktykantka</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const slides = document.querySelectorAll('.testimonial-slide');
      let currentIdx = 0;

      if(slides.length > 1) {
        setInterval(() => {
          // Ukryj obecny (odjeżdża w lewo)
          slides[currentIdx].classList.remove('opacity-100', 'translate-x-0');
          slides[currentIdx].classList.add('opacity-0', '-translate-x-8', 'pointer-events-none');
          
          // Następny slajd
          currentIdx = (currentIdx + 1) % slides.length;
          
          // Reset pozycji przed wjazdem
          slides[currentIdx].classList.remove('-translate-x-8');
          slides[currentIdx].classList.add('translate-x-8');
          
          // Mikrosekunda przerwy na render i wjazd z prawej
          setTimeout(() => {
            slides[currentIdx].classList.remove('opacity-0', 'translate-x-8', 'pointer-events-none');
            slides[currentIdx].classList.add('opacity-100', 'translate-x-0');
          }, 50);

        }, 6000); 
      }
    });
  </script>

```

### Plik: `src/pages/pl/projekty.astro`
```astro
---
import Layout from '../../layouts/Layout.astro';
---

<Layout title="Projekty" lang="pl">
  <section class="pt-12 pb-20 lg:pt-16 lg:pb-28">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="mb-10">
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-4">
          Nasze <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">Realizacje</span>
        </h1>
        <div class="h-1 w-20 bg-cyan-500 rounded"></div>
        <p class="mt-6 text-xl text-slate-400 max-w-2xl">
          Zobacz, jak wdrożenia sztucznej inteligencji i nasze szkolenia transformują procesy w realnych biznesach.
        </p>
      </div>

      <div class="flex flex-col gap-8">
        
        <div class="bg-slate-800/40 border border-slate-700 rounded-2xl overflow-hidden shadow-2xl transition-all hover:border-cyan-500/50">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-0">
            
            <div class="p-8 lg:p-12 border-b lg:border-b-0 lg:border-r border-slate-700">
              <div class="flex items-center gap-3 mb-6">
                <span class="px-3 py-1 text-xs font-bold uppercase tracking-wider text-cyan-400 bg-cyan-400/10 rounded-full">Marketing AI</span>
                <span class="text-slate-500 text-sm font-medium">Poznań, 2025</span>
              </div>
              
              <h2 class="text-3xl font-bold text-white mb-4">AI w marketingu kreatywnym</h2>
              <div class="flex items-center gap-4 mb-6">
                <h3 class="text-xl text-slate-300 font-medium m-0">Klient: <span class="text-white">Papaja Tatuaże</span></h3>
                <div class="h-16 w-px bg-slate-700"></div>
                <img src="/papaja-logo.png" alt="Papaja Tatuaże Logo" class="h-32 w-auto object-contain grayscale hover:grayscale-0 transition-all duration-300" />
              </div>
              
              <p class="text-slate-400 mb-8 leading-relaxed">
                W ramach współpracy z kreatywną pracownią tatuażu pokazaliśmy, jak narzędzia oparte na sztucznej inteligencji mogą diametralnie wspierać działania marketingowe i zwiększać zasięgi w mediach społecznościowych.
              </p>

              <h4 class="text-white font-bold mb-4">Zakres Wdrożenia i Szkolenia:</h4>
              <ul class="space-y-3">
                <li class="flex items-start">
                  <svg class="w-6 h-6 shrink-0 text-cyan-400 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                  <span class="text-slate-300">Narzędzia AI do tworzenia scenariuszy filmów na TikToka i Reelsy.</span>
                </li>
                <li class="flex items-start">
                  <svg class="w-6 h-6 shrink-0 text-cyan-400 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                  <span class="text-slate-300">Inteligentne edytory do montażu wideo i pracy z dźwiękiem.</span>
                </li>
                <li class="flex items-start">
                  <svg class="w-6 h-6 shrink-0 text-cyan-400 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                  <span class="text-slate-300">Rozwiązania wspomagające pisanie treści promocyjnych i opisów.</span>
                </li>
              </ul>
            </div>

            <div class="p-8 lg:p-12 bg-slate-800/80 flex flex-col justify-center">
              <h4 class="text-xl font-bold text-white mb-4">Efekt Operacyjny</h4>
              <p class="text-slate-400 leading-relaxed">
                Dzięki szkoleniu, studio Papaja Tatuaże zyskało zupełnie nowe możliwości w tworzeniu angażujących treści. Zoptymalizowano czas potrzebny na produkcję materiałów promocyjnych, co bezpośrednio przełożyło się na zwiększenie zasięgów i interakcji z klientami.
              </p>
            </div>
            
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <div class="bg-slate-900/50 p-8 rounded-2xl border border-slate-700/50 flex flex-col justify-between hover:border-cyan-500/30 transition-colors">
            <div>
              <svg class="w-10 h-10 text-cyan-500/20 mb-4" fill="currentColor" viewBox="0 0 32 32" aria-hidden="true"><path d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.896 3.456-8.352 9.12-8.352 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z" /></svg>
              <p class="text-lg text-slate-300 italic mb-6">"Szkolenie otworzyło mi oczy i pomogło zrozumieć możliwości, które daje sztuczna inteligencja."</p>
            </div>
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 shrink-0 rounded-full bg-cyan-900 flex items-center justify-center text-cyan-400 font-bold border border-cyan-500/30">WP</div>
              <div>
                <div class="text-white font-bold">Wiktoria Papała</div>
                <div class="text-cyan-400 text-sm">Właścicielka, Papaja Tatuaże</div>
              </div>
            </div>
          </div>

          <div class="bg-slate-900/50 p-8 rounded-2xl border border-slate-700/50 flex flex-col justify-between hover:border-cyan-500/30 transition-colors">
            <div>
              <svg class="w-10 h-10 text-cyan-500/20 mb-4" fill="currentColor" viewBox="0 0 32 32" aria-hidden="true"><path d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.896 3.456-8.352 9.12-8.352 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z" /></svg>
              <p class="text-lg text-slate-300 italic mb-6">"Dzięki Emilowi znalazłam przyjaciela idealnego."</p>
            </div>
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 shrink-0 rounded-full bg-cyan-900 flex items-center justify-center text-cyan-400 font-bold border border-cyan-500/30">ID</div>
              <div>
                <div class="text-white font-bold">Iza Dudzik</div>
                <div class="text-cyan-400 text-sm">Ilustratorka / Praktykantka</div>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</Layout>

```
