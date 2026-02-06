import streamlit as st
import streamlit.components.v1 as components

# --- Konfigurace ---
st.set_page_config(layout="wide")

# --- Hlavní nadpis ---
st.title("🚀 Deployment Masterclass")
st.caption("Dostaňte svou aplikaci z localhostu do světa.")

# --- Navigace ---
tab_intro, tab_req, tab_git, tab_cloud, tab_secrets = st.tabs([
    "🎬 PREZENTACE",
    "1. Requirements.txt", 
    "2. GitHub", 
    "3. Streamlit Cloud", 
    "4. Secrets (Tajné)"
])

# ==========================================
# TAB 0: PREZENTACE
# ==========================================
with tab_intro:
    html_code = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deployment Masterclass</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

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
            transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
            opacity: 0;
            pointer-events: none;
            z-index: 0;
            transform: scale(0.95);
        }

        .slide.active {
            opacity: 1;
            pointer-events: auto;
            z-index: 20;
            transform: translateX(0) scale(1);
        }

        .slide.prev {
            opacity: 0;
            transform: translateX(-100%) scale(0.9);
            z-index: 10;
        }

        .slide.next {
            opacity: 0;
            transform: translateX(100%) scale(0.9);
            z-index: 10;
        }

        /* Content Card */
        .card {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 1.5rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            width: 100%;
            max-width: 1280px;
            min-height: 650px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            position: relative;
        }

        .card-header {
            padding: 2rem 3rem;
            border-bottom: 1px solid #334155;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(30, 41, 59, 0.95);
        }

        .card-body {
            padding: 3rem;
            flex-grow: 1;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        /* Code Window Styling */
        .code-window {
            background: #0d1117;
            border-radius: 0.75rem;
            border: 1px solid #30363d;
            overflow: hidden;
            font-family: 'JetBrains Mono', monospace;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        }

        .code-header {
            background: #161b22;
            padding: 0.75rem 1rem;
            display: flex;
            gap: 0.5rem;
            border-bottom: 1px solid #30363d;
        }

        .dot { width: 0.75rem; height: 0.75rem; border-radius: 50%; }
        .dot-red { background: #ff5f56; }
        .dot-yellow { background: #ffbd2e; }
        .dot-green { background: #27c93f; }

        .code-content {
            padding: 1.5rem;
            color: #c9d1d9;
            font-size: 1rem;
            line-height: 1.6;
        }

        /* Syntax Highlighting */
        .kwd { color: #ff7b72; } 
        .str { color: #a5d6ff; } 
        .func { color: #d2a8ff; } 
        .var { color: #79c0ff; } 
        .comment { color: #8b949e; font-style: italic; } 
        .num { color: #79c0ff; } 

        /* Typography */
        h1 { font-size: 3rem; font-weight: 800; color: #fff; line-height: 1.1; }
        h2 { font-size: 2.25rem; font-weight: 700; color: #fff; margin-bottom: 1rem; }
        p { color: #94a3b8; font-size: 1.125rem; line-height: 1.6; margin-bottom: 1.5rem; }
        
        .feature-icon {
            width: 3rem;
            height: 3rem;
            border-radius: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
        }
    </style>
</head>
<body>

    <div class="slide-container">

        <!-- SLIDE 0: INTRO -->
        <div class="slide active" id="slide-0">
            <div class="card">
                <div class="card-body" style="grid-template-columns: 1.2fr 0.8fr;">
                    <div>
                        <div class="inline-block px-3 py-1 bg-green-500/20 text-green-300 rounded-full text-sm font-mono mb-6 border border-green-500/30">
                            git push origin main
                        </div>
                        <h1>Deployment 🚀<br><span class="text-green-400">Jdeme Online</span></h1>
                        <p class="mt-6 text-xl">
                            Aplikace na vašem počítači (localhost) je fajn, ale nikdo ji nevidí. Pojďme ji dostat na internet, aby ji viděl celý svět.
                        </p>
                        <ul class="mt-8 space-y-4 text-slate-300">
                            <li class="flex items-center gap-3">
                                <i class="fab fa-github text-yellow-400"></i> GitHub jako skladiště kódu
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-cloud text-blue-400"></i> Streamlit Cloud jako server
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-sync text-green-400"></i> Automatické aktualizace
                            </li>
                        </ul>
                    </div>
                    <div class="flex items-center justify-center">
                        <i class="fas fa-rocket text-[15rem] text-green-500/20 animate-pulse"></i>
                    </div>
                </div>
                <div class="card-footer p-6 border-t border-slate-700 bg-slate-800/50 flex justify-between text-slate-500 font-mono text-sm">
                    <span>share.streamlit.io</span>
                    <span>Použij šipky ➝</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 1: ARCHITEKTURA -->
        <div class="slide next" id="slide-1">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">1. Jak to funguje?</h3>
                    <i class="fas fa-network-wired text-green-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-green-500/20 text-green-400"><i class="fas fa-server"></i></div>
                        <h2>Tři hráči</h2>
                        <p>Proces nasazení zahrnuje tři kroky:</p>
                        <ol class="list-decimal list-inside space-y-4 text-slate-300 ml-2">
                            <li><strong>Váš PC:</strong> Tady píšete kód.</li>
                            <li><strong>GitHub:</strong> Sem kód nahrajete (záloha + sdílení).</li>
                            <li><strong>Streamlit Cloud:</strong> Tento server si kód stáhne z GitHubu a spustí ho.</li>
                        </ol>
                    </div>
                    <div class="flex items-center justify-center gap-4">
                        <div class="text-center">
                            <i class="fas fa-laptop text-4xl text-slate-400 mb-2"></i>
                            <div class="text-sm">PC</div>
                        </div>
                        <i class="fas fa-arrow-right text-slate-600"></i>
                        <div class="text-center">
                            <i class="fab fa-github text-4xl text-white mb-2"></i>
                            <div class="text-sm">GitHub</div>
                        </div>
                        <i class="fas fa-arrow-right text-slate-600"></i>
                        <div class="text-center">
                            <i class="fas fa-cloud text-4xl text-red-400 mb-2"></i>
                            <div class="text-sm">Cloud</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2: REQUIREMENTS -->
        <div class="slide next" id="slide-2">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">2. Requirements.txt</h3>
                    <i class="fas fa-list-ul text-green-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-blue-500/20 text-blue-400"><i class="fas fa-shopping-basket"></i></div>
                        <h2>Nákupní seznam pro server</h2>
                        <p>Váš počítač ví, že máte nainstalovaný Pandas. Server to neví.</p>
                        <p>Soubor <code>requirements.txt</code> je seznam ingrediencí, které server musí nainstalovat, aby vaše aplikace fungovala.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                            <span class="text-xs text-slate-500 ml-2">requirements.txt</span>
                        </div>
                        <div class="code-content">
                            streamlit<br>
                            pandas<br>
                            altair<br>
                            openpyxl<br>
                            numpy
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3: CI/CD -->
        <div class="slide next" id="slide-3">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">3. Magie CI/CD</h3>
                    <i class="fas fa-sync text-green-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-purple-500/20 text-purple-400"><i class="fas fa-magic"></i></div>
                        <h2>Automatická aktualizace</h2>
                        <p>Nejlepší na tom je, že propojení nastavíte jen jednou.</p>
                        <p>Kdykoliv v budoucnu upravíte kód a pošlete ho na GitHub (<code>git push</code>), Streamlit Cloud si změny <strong>sám stáhne a aplikaci restartuje</strong>.</p>
                    </div>
                    <div class="flex flex-col items-center gap-4">
                        <div class="w-full p-4 bg-slate-800 border border-slate-600 rounded flex justify-between items-center">
                            <span>1. Změna kódu</span>
                            <i class="fas fa-check text-green-500"></i>
                        </div>
                        <i class="fas fa-arrow-down text-slate-500"></i>
                        <div class="w-full p-4 bg-slate-800 border border-slate-600 rounded flex justify-between items-center">
                            <span>2. Git Push</span>
                            <i class="fas fa-check text-green-500"></i>
                        </div>
                        <i class="fas fa-arrow-down text-slate-500"></i>
                        <div class="w-full p-4 bg-green-900/30 border border-green-500 text-green-300 rounded flex justify-between items-center font-bold">
                            <span>3. Auto Deploy</span>
                            <i class="fas fa-rocket animate-bounce"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4: SECRETS -->
        <div class="slide next" id="slide-4">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">4. Bezpečnost (Secrets)</h3>
                    <i class="fas fa-user-secret text-green-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-red-500/20 text-red-400"><i class="fas fa-key"></i></div>
                        <h2>Hesla na GitHub nepatří!</h2>
                        <p>Pokud vaše aplikace potřebuje heslo k databázi nebo API klíč, <strong>nikdy</strong> ho nepište do kódu.</p>
                        <p>Použijte <code>st.secrets</code>. Na lokále jsou v souboru, na cloudu v bezpečném nastavení.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                        </div>
                        <div class="code-content">
                            <span class="comment"># ŠPATNĚ (Vidí to všichni)</span><br>
                            <span class="comment"># heslo = "moje_tajne_heslo_123"</span><br><br>
                            <span class="comment"># SPRÁVNĚ (Bezpečné)</span><br>
                            heslo = st.secrets[<span class="str">"db_password"</span>]
                        </div>
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
            <button onclick="toggleFullscreen()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none focus:ring-2 focus:ring-green-500 cursor-pointer" title="Fullscreen">
                <i class="fas fa-expand"></i>
            </button>
            <button onclick="prevSlide()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none cursor-pointer">
                <i class="fas fa-arrow-left"></i>
            </button>
            <button onclick="nextSlide()" class="w-12 h-12 rounded-full bg-green-600 hover:bg-green-500 text-white flex items-center justify-center transition shadow-lg shadow-green-900/50 focus:outline-none cursor-pointer">
                <i class="fas fa-arrow-right"></i>
            </button>
        </div>
    </div>

    <!-- Progress Bar -->
    <div class="fixed top-0 left-0 h-1 bg-slate-800 w-full z-50">
        <div id="progress-bar" class="h-full bg-green-500 transition-all duration-300" style="width: 20%"></div>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        const progressBar = document.getElementById('progress-bar');
        const counter = document.getElementById('slide-counter');

        function updateSlide() {
            slides.forEach((slide, index) => {
                slide.className = 'slide';
                if (index === currentSlide) {
                    slide.classList.add('active');
                } else if (index < currentSlide) {
                    slide.classList.add('prev');
                } else {
                    slide.classList.add('next');
                }
            });

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

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
            if (e.key === 'f') toggleFullscreen();
        });

        updateSlide();
    </script>
</body>
</html>
    """
    components.html(html_code, height=850, scrolling=False)

# ==========================================
# TAB 1: REQUIREMENTS
# ==========================================
with tab_req:
    st.header("📦 Krok 1: Seznam ingrediencí")
    st.markdown("""
    Když vaříte podle receptu, potřebujete seznam surovin. 
    Server (Streamlit Cloud) to má stejně. Potřebuje vědět, jaké knihovny nainstalovat.
    To mu řekneme souborem `requirements.txt`.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Jak má vypadat?")
        st.code("""
streamlit
pandas
altair
openpyxl
        """, language="text")
        st.info("Každá knihovna na nový řádek. Žádné čárky.")

    with col2:
        st.subheader("Kde má být?")
        st.warning("Musí být v **hlavní složce** (root) vašeho projektu! Vedle `app.py` nebo `dashboard.py`.")
        st.markdown("📂 `muj-projekt/`")
        st.markdown("├── 📄 `dashboard.py`")
        st.markdown("└── 📄 `requirements.txt` ✅")

# ==========================================
# TAB 2: GITHUB
# ==========================================
with tab_git:
    st.header("🐙 Krok 2: GitHub")
    st.markdown("""
    Streamlit Cloud neumí číst soubory z vašeho počítače. Musíte je nahrát na GitHub.
    """)

    st.subheader("Postup (přes webový prohlížeč)")
    
    steps = [
        "Jděte na **[github.com/new](https://github.com/new)**.",
        "Pojmenujte repozitář (např. `muj-dashboard`).",
        "Zaškrtněte **Add a README file** (doporučeno).",
        "Klikněte **Create repository**.",
        "Klikněte na **Add file** -> **Upload files**.",
        "Přetáhněte tam své soubory (`dashboard.py`, `requirements.txt`, složku `data`).",
        "Dole klikněte na zelené **Commit changes**."
    ]
    
    for i, step in enumerate(steps, 1):
        st.markdown(f"**{i}.** {step}")

    st.success("🎉 Teď máte kód v cloudu!")

# ==========================================
# TAB 3: STREAMLIT CLOUD
# ==========================================
with tab_cloud:
    st.header("☁️ Krok 3: Streamlit Cloud")
    st.markdown("Teď propojíme GitHub se Streamlitem.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Postup")
        st.markdown("""
        1.  Jděte na **[share.streamlit.io](https://share.streamlit.io)**.
        2.  Přihlaste se přes GitHub.
        3.  Klikněte na **New app**.
        4.  Vyberte svůj repozitář (`muj-dashboard`).
        5.  **Main file path:** Změňte na `src/dashboard.py` (pokud ho máte ve složce src).
        6.  Klikněte **Deploy**! 🚀
        """)
    
    with col2:
        st.subheader("Co se děje na pozadí?")
        st.info("""
        1.  Streamlit si stáhne váš kód.
        2.  Přečte `requirements.txt`.
        3.  Nainstaluje knihovny (Pandas, Altair...).
        4.  Spustí `streamlit run dashboard.py`.
        """)

    st.divider()
    st.subheader("🚑 Řešení problémů (Troubleshooting)")
    with st.expander("Aplikace spadla (Error)"):
        st.write("**1. ModuleNotFoundError:** Zapomněli jste knihovnu v `requirements.txt`.")
        st.write("**2. FileNotFoundError:** Máte špatně cestu k datům. Na Linuxu (Cloud) záleží na velkých/malých písmenech!")
        st.write("**3. Chyba v cestě:** Zkuste `data/prodeje.csv` místo `../data/prodeje.csv` (záleží, odkud se skript spouští).")

# ==========================================
# TAB 4: SECRETS
# ==========================================
with tab_secrets:
    st.header("🔐 Secrets (Tajné údaje)")
    st.markdown("""
    **Nikdy** nedávejte hesla (API klíče, hesla k databázi) přímo do kódu na GitHub!
    Každý by je viděl. Použijte **Streamlit Secrets**.
    """)

    st.subheader("Jak na to?")
    st.markdown("1. V nastavení aplikace na Streamlit Cloud klikněte na **Settings** -> **Secrets**.")
    st.markdown("2. Zadejte hesla ve formátu TOML:")
    
    st.code("""
db_username = "admin"
db_password = "moje_tajne_heslo"
    """, language="toml")

    st.markdown("3. V kódu je pak načtete takto:")
    st.code("""
import streamlit as st

user = st.secrets["db_username"]
heslo = st.secrets["db_password"]
    """, language="python")
