import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Skryjeme Streamlit prvky, aby prezentace vynikla
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# HTML kód prezentace
html_code = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshop: Technologie Stack</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0f172a; /* Slate 900 */
            color: #f1f5f9;
            overflow: hidden;
            margin: 0;
        }

        /* Slide Container */
        .slide-container {
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }

        /* Individual Slide */
        .slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.6s ease;
            opacity: 0;
            pointer-events: none;
            visibility: hidden; /* Důležité: skryje element úplně */
        }

        /* Active Slide (Center) */
        .slide.active {
            transform: translateX(0) scale(1);
            opacity: 1;
            pointer-events: auto;
            visibility: visible;
            z-index: 10;
        }

        /* Previous Slide (Left) */
        .slide.prev {
            transform: translateX(-100%) scale(0.9);
            opacity: 0;
        }

        /* Next Slide (Right - default state handled in JS logic or CSS default) */
        .slide.next {
            transform: translateX(100%) scale(0.9);
            opacity: 0;
        }

        /* Content Card */
        .card {
            background-color: #1e293b; /* Slate 800 */
            border: 1px solid #334155;
            border-radius: 1.5rem;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 1200px;
            min-height: 600px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            position: relative;
            z-index: 20;
        }

        /* Header Strip */
        .card-header {
            padding: 2rem 3rem;
            border-bottom: 1px solid #334155;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Body Content */
        .card-body {
            padding: 3rem;
            flex-grow: 1;
            display: grid;
            grid-template-columns: 1fr 1.5fr; /* Left Icon/Title, Right Content */
            gap: 3rem;
            align-items: center;
        }

        /* Typography overrides */
        h1 { font-size: 3.5rem; font-weight: 700; letter-spacing: -0.02em; }
        h2 { font-size: 2.5rem; font-weight: 600; }
        h3 { font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem; color: #94a3b8; }
        p { font-size: 1.125rem; line-height: 1.6; color: #cbd5e1; }
        
        /* List Styles */
        ul.feature-list li {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
            position: relative;
        }
        ul.feature-list li::before {
            content: "•";
            position: absolute;
            left: 0;
            color: currentColor; 
            font-weight: bold;
        }

        /* Theme Colors */
        .theme-intro h1 { color: #38bdf8; }
        .theme-python { color: #60a5fa; } /* Blue */
        .theme-pandas { color: #c084fc; } /* Purple */
        .theme-altair { color: #fb923c; } /* Orange */
        .theme-streamlit { color: #f87171; } /* Red */

        .bg-python { background: rgba(96, 165, 250, 0.1); }
        .bg-pandas { background: rgba(192, 132, 252, 0.1); }
        .bg-altair { background: rgba(251, 146, 60, 0.1); }
        .bg-streamlit { background: rgba(248, 113, 113, 0.1); }

    </style>
</head>
<body>

    <div class="slide-container" id="presentation-container">

        <!-- SLIDE 1: INTRO -->
        <div class="slide active" id="slide-0">
            <div class="card theme-intro">
                <div class="card-body" style="grid-template-columns: 1fr; text-align: center;">
                    <div>
                        <div class="mb-6 inline-block px-4 py-1 rounded-full bg-slate-700 text-slate-300 text-sm font-semibold tracking-wide uppercase">
                            Workshop Overview
                        </div>
                        <h1 class="mb-6">Moderní Python Stack<br>pro Datovou Analýzu</h1>
                        <p class="max-w-3xl mx-auto text-xl text-slate-400 mb-10">
                            Dnešní workshop není jen o psaní kódu. Je o efektivitě. Vybrali jsme sadu nástrojů, které spolu perfektně hrají a tvoří standard v oboru Data Science.
                        </p>
                        
                        <!-- Tech Icons Grid -->
                        <div class="grid grid-cols-4 gap-8 max-w-4xl mx-auto mt-12">
                            <div class="flex flex-col items-center gap-3 opacity-80 hover:opacity-100 transition">
                                <i class="fab fa-python text-5xl text-blue-400"></i>
                                <span class="font-bold">Python</span>
                            </div>
                            <div class="flex flex-col items-center gap-3 opacity-80 hover:opacity-100 transition">
                                <i class="fas fa-table text-5xl text-purple-400"></i>
                                <span class="font-bold">Pandas</span>
                            </div>
                            <div class="flex flex-col items-center gap-3 opacity-80 hover:opacity-100 transition">
                                <i class="fas fa-chart-area text-5xl text-orange-400"></i>
                                <span class="font-bold">Altair</span>
                            </div>
                            <div class="flex flex-col items-center gap-3 opacity-80 hover:opacity-100 transition">
                                <i class="fas fa-crown text-5xl text-red-400"></i>
                                <span class="font-bold">Streamlit</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-footer p-6 border-t border-slate-700 flex justify-between text-slate-500 text-sm">
                    <span>Od dat k aplikaci</span>
                    <span>Stiskněte šipku doprava ➝</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 2: PYTHON -->
        <div class="slide next" id="slide-1">
            <div class="card theme-python">
                <div class="card-header">
                    <span class="text-xl font-bold tracking-tight text-blue-400">Jádro systému</span>
                    <i class="fab fa-python text-3xl text-blue-400"></i>
                </div>
                <div class="card-body">
                    <!-- Left Column -->
                    <div class="text-center p-8 rounded-2xl bg-python border border-blue-500/20">
                        <i class="fab fa-python text-9xl text-blue-400 mb-6 block"></i>
                        <h2 class="text-white mb-2">Python</h2>
                        <p class="text-blue-300">Univerzální jazyk dat</p>
                    </div>
                    <!-- Right Column -->
                    <div>
                        <h3>Proč Python?</h3>
                        <p class="mb-6">
                            Python se stal "lingua franca" datové vědy. Není to nejrychlejší jazyk na světě (na to máme C++), ale je nejrychlejší na <strong>vývoj</strong>.
                        </p>
                        <ul class="feature-list text-lg text-slate-300 space-y-4">
                            <li>
                                <strong class="text-white">Čitelnost:</strong> Syntaxe připomíná angličtinu. Kód se čte spíše jako recept než jako instrukce pro stroj.
                            </li>
                            <li>
                                <strong class="text-white">Ekosystém:</strong> Je to lepidlo. Python spojuje vysoce výkonné knihovny (napsané v C) s jednoduchým rozhraním.
                            </li>
                            <li>
                                <strong class="text-white">Kdo ho používá?</strong> NASA pro analýzu snímků z vesmíru, Netflix pro doporučovací algoritmy, Spotify pro analýzu zvuku.
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3: PANDAS -->
        <div class="slide next" id="slide-2">
            <div class="card theme-pandas">
                <div class="card-header">
                    <span class="text-xl font-bold tracking-tight text-purple-400">Zpracování dat</span>
                    <i class="fas fa-table text-3xl text-purple-400"></i>
                </div>
                <div class="card-body">
                    <!-- Left Column -->
                    <div class="text-center p-8 rounded-2xl bg-pandas border border-purple-500/20">
                        <i class="fas fa-boxes text-9xl text-purple-400 mb-6 block"></i>
                        <h2 class="text-white mb-2">Pandas</h2>
                        <p class="text-purple-300">Excel na steroidech</p>
                    </div>
                    <!-- Right Column -->
                    <div>
                        <h3>Co to umí?</h3>
                        <p class="mb-6">
                            Zatímco Excel začne při 100 000 řádcích lapat po dechu, Pandas se teprve zahřívá. Je to nástroj pro načtení, čištění a transformaci dat.
                        </p>
                        <ul class="feature-list text-lg text-slate-300 space-y-4">
                            <li>
                                <strong class="text-white">Datový vysavač:</strong> Načte cokoliv – CSV, Excel, SQL databáze, JSON API.
                            </li>
                            <li>
                                <strong class="text-white">DataFrame:</strong> Hlavní stavební kámen. Představte si programovatelnou tabulku v paměti RAM.
                            </li>
                            <li>
                                <strong class="text-white">Manipulace:</strong> Bleskurychlé filtrování ("ukaž mi prodeje nad 1000 Kč"), seskupování a pivot tabulky na jeden řádek kódu.
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4: ALTAIR -->
        <div class="slide next" id="slide-3">
            <div class="card theme-altair">
                <div class="card-header">
                    <span class="text-xl font-bold tracking-tight text-orange-400">Vizualizace</span>
                    <i class="fas fa-chart-line text-3xl text-orange-400"></i>
                </div>
                <div class="card-body">
                    <!-- Left Column -->
                    <div class="text-center p-8 rounded-2xl bg-altair border border-orange-500/20">
                        <i class="fas fa-chart-area text-9xl text-orange-400 mb-6 block"></i>
                        <h2 class="text-white mb-2">Altair</h2>
                        <p class="text-orange-300">Gramatika grafiky</p>
                    </div>
                    <!-- Right Column -->
                    <div>
                        <h3>Jiný přístup ke kreslení</h3>
                        <p class="mb-6">
                            Většina knihoven (jako Matplotlib) funguje imperativně ("nakresli čáru odtud tam"). Altair je <strong>deklarativní</strong>.
                        </p>
                        <ul class="feature-list text-lg text-slate-300 space-y-4">
                            <li>
                                <strong class="text-white">Co vs. Jak:</strong> Neříkáte programu, jak má kreslit pixely. Říkáte mu: "Osu X mapuj na čas, osu Y na cenu a barvu na kategorii."
                            </li>
                            <li>
                                <strong class="text-white">Web-Native:</strong> Grafy jsou ve skutečnosti JSON objekty. Díky tomu jsou lehké a perfektně se vkládají do webových stránek.
                            </li>
                            <li>
                                <strong class="text-white">Interaktivita zdarma:</strong> Zoomování, posouvání (pan) a tooltips (bubliny s hodnotami) často vyžadují jediný příkaz `.interactive()`.
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 5: STREAMLIT -->
        <div class="slide next" id="slide-4">
            <div class="card theme-streamlit">
                <div class="card-header">
                    <span class="text-xl font-bold tracking-tight text-red-400">Prezentace & App</span>
                    <i class="fas fa-crown text-3xl text-red-400"></i>
                </div>
                <div class="card-body">
                    <!-- Left Column -->
                    <div class="text-center p-8 rounded-2xl bg-streamlit border border-red-500/20">
                        <i class="fas fa-desktop text-9xl text-red-400 mb-6 block"></i>
                        <h2 class="text-white mb-2">Streamlit</h2>
                        <p class="text-red-300">Appka bez frontendisty</p>
                    </div>
                    <!-- Right Column -->
                    <div>
                        <h3>Game Changer</h3>
                        <p class="mb-6">
                            Dříve, když chtěl datový analytik sdílet svou práci, poslal PDF nebo musel poprosit programátora, aby mu vyrobil web. Streamlit tuto bariéru boří.
                        </p>
                        <ul class="feature-list text-lg text-slate-300 space-y-4">
                            <li>
                                <strong class="text-white">Python In, App Out:</strong> Píšete čistý Python skript. Streamlit ho čte shora dolů a generuje HTML/JS/CSS za vás.
                            </li>
                            <li>
                                <strong class="text-white">Widgety:</strong> Přidat posuvník, tlačítko nebo výběr data je otázka jednoho řádku kódu. Žádné složité "callbacky".
                            </li>
                            <li>
                                <strong class="text-white">Rychlé prototypování:</strong> Ideální pro dashboardy, kde klient potřebuje vidět data a hrát si s filtry v reálném čase.
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- CONTROLS -->
    <div class="fixed bottom-0 left-0 w-full p-6 flex justify-between items-center z-50 pointer-events-none">
        <div class="pointer-events-auto bg-slate-800/80 backdrop-blur px-4 py-2 rounded-full text-slate-400 font-mono text-sm border border-slate-700">
            <span id="slide-counter">1 / 5</span>
        </div>
        
        <div class="pointer-events-auto flex gap-4">
            <button onclick="toggleFullscreen()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none focus:ring-2 focus:ring-blue-500 cursor-pointer" title="Fullscreen">
                <i class="fas fa-expand"></i>
            </button>
            <button onclick="prevSlide()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none focus:ring-2 focus:ring-blue-500 cursor-pointer">
                <i class="fas fa-arrow-left"></i>
            </button>
            <button onclick="nextSlide()" class="w-12 h-12 rounded-full bg-blue-600 hover:bg-blue-500 text-white flex items-center justify-center transition shadow-lg shadow-blue-900/50 focus:outline-none focus:ring-2 focus:ring-blue-400 cursor-pointer">
                <i class="fas fa-arrow-right"></i>
            </button>
        </div>
    </div>

    <!-- Progress Bar -->
    <div class="fixed top-0 left-0 h-1 bg-slate-800 w-full z-50">
        <div id="progress-bar" class="h-full bg-blue-500 transition-all duration-300" style="width: 20%"></div>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        const progressBar = document.getElementById('progress-bar');
        const counter = document.getElementById('slide-counter');

        function updateSlide() {
            slides.forEach((slide, index) => {
                // Remove all state classes first
                slide.classList.remove('active', 'prev', 'next');
                
                // Add correct class based on position relative to currentSlide
                if (index === currentSlide) {
                    slide.classList.add('active');
                } else if (index < currentSlide) {
                    slide.classList.add('prev');
                } else {
                    slide.classList.add('next');
                }
            });

            // Update Progress bar and counter
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            progressBar.style.width = `${progress}%`;
            counter.innerText = `${currentSlide + 1} / ${totalSlides}`;
        }

        function nextSlide() {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlide();
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                updateSlide();
            }
        }
        
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    alert(`Error attempting to enable fullscreen: ${err.message}`);
                });
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        // Keyboard Navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                prevSlide();
            } else if (e.key === 'f') {
                toggleFullscreen();
            }
        });

        // Initialize proper states on load
        updateSlide();
    </script>
</body>
</html>
"""

# Vykreslení HTML komponenty
components.html(html_code, height=850, scrolling=False)
