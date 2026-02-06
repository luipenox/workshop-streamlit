import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# --- Konfigurace a Data ---
st.set_page_config(layout="wide")

# Funkce pro generování "špinavých" dat
@st.cache_data
def get_dirty_data():
    df = pd.read_csv('data/prodeje.csv')
    df['Datum'] = pd.to_datetime(df['Datum'])
    # Simulace chyb
    df.loc[2, 'Cena'] = np.nan          # Chybějící hodnota
    df.loc[5, 'Pobocka'] = 'brno'       # Nekonzistence
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True) # Duplikát
    return df

df = get_dirty_data()
# Aplikace čištění a transformace na pozadí
df['Cena'] = df['Cena'].fillna(0)
df = df.drop_duplicates()
df['Pobocka'] = df['Pobocka'].str.capitalize()
df['Celkem'] = df['Cena'] * df['Mnozstvi']
df_clean = df.copy()

# --- Hlavní nadpis ---
st.title("🐼 Pandas Masterclass")
st.caption("Od surových dat k čistým insightům během jedné hodiny.")

# --- Navigace ---
tab_intro, tab_load, tab_clean, tab_transform, tab_agg, tab_challenge = st.tabs([
    "🎬 PREZENTACE",
    "1. Načtení & Průzkum", 
    "2. Čištění dat", 
    "3. Transformace", 
    "4. Agregace (Pivot)", 
    "🚀 PŘÍPRAVA PRO GRAFY"
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
    <title>Pandas Power Demo</title>
    
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

        /* Individual Slide Logic - ROBUST FIX */
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
            
            /* Smooth Transition */
            transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
            
            /* Default Hidden State */
            opacity: 0;
            pointer-events: none;
            z-index: 0;
            transform: scale(0.95);
        }

        /* Active Slide */
        .slide.active {
            opacity: 1;
            pointer-events: auto;
            z-index: 20;
            transform: translateX(0) scale(1);
        }

        /* Previous Slide (Exit Left) */
        .slide.prev {
            opacity: 0;
            transform: translateX(-100%) scale(0.9);
            z-index: 10;
        }

        /* Next Slide (Waiting Right) */
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
            position: relative; /* Ensure z-index works inside */
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
                        <div class="inline-block px-3 py-1 bg-indigo-500/20 text-indigo-300 rounded-full text-sm font-mono mb-6 border border-indigo-500/30">
                            import pandas as pd
                        </div>
                        <h1>Síla Pandas 🐼<br><span class="text-indigo-400">Excel na steroidech</span></h1>
                        <p class="mt-6 text-xl">
                            Pandas je standard pro analýzu dat v Pythonu. Umožňuje načítat, čistit, transformovat a analyzovat miliony řádků dat během zlomku vteřiny.
                        </p>
                        <ul class="mt-8 space-y-4 text-slate-300">
                            <li class="flex items-center gap-3">
                                <i class="fas fa-bolt text-yellow-400"></i> 100x rychlejší než manuální práce
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-database text-blue-400"></i> Načte cokoliv (CSV, Excel, SQL)
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-code text-green-400"></i> Automatizovatelné skripty
                            </li>
                        </ul>
                    </div>
                    <div class="flex items-center justify-center">
                        <i class="fas fa-table text-[15rem] text-indigo-500/20 animate-pulse"></i>
                    </div>
                </div>
                <div class="card-footer p-6 border-t border-slate-700 bg-slate-800/50 flex justify-between text-slate-500 font-mono text-sm">
                    <span>pandas 2.0+</span>
                    <span>Použij šipky ➝</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 1: NAČÍTÁNÍ -->
        <div class="slide next" id="slide-1">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">1. Načtení dat</h3>
                    <i class="fas fa-file-import text-indigo-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-blue-500/20 text-blue-400"><i class="fas fa-file-csv"></i></div>
                        <h2>Vše začíná daty</h2>
                        <p>Zapomeňte na `Otevřít soubor > Importovat > Nastavit oddělovač`. Pandas automaticky detekuje formáty a načte data do struktury zvané <strong>DataFrame</strong>.</p>
                        <p>DataFrame je jako tabulka v Excelu, ale žije v paměti RAM a je připravena na programování.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                        </div>
                        <div class="code-content">
                            <span class="kwd">import</span> pandas <span class="kwd">as</span> pd<br><br>
                            <span class="comment"># Načtení z CSV</span><br>
                            df = pd.<span class="func">read_csv</span>(<span class="str">"prodeje_2024.csv"</span>)<br><br>
                            <span class="comment"># Načtení z Excelu</span><br>
                            df_xl = pd.<span class="func">read_excel</span>(<span class="str">"report.xlsx"</span>)<br><br>
                            <span class="comment"># Rychlý náhled prvních 5 řádků</span><br>
                            <span class="func">print</span>(df.<span class="func">head</span>())
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2: FILTROVÁNÍ -->
        <div class="slide next" id="slide-2">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">2. Průzkum a Filtrování</h3>
                    <i class="fas fa-filter text-indigo-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-green-500/20 text-green-400"><i class="fas fa-search"></i></div>
                        <h2>Žádné "For" cykly</h2>
                        <p>V Pythonu běžně používáme cykly. V Pandas <strong>NE</strong>. Používáme tzv. <em>vektorizované operace</em>.</p>
                        <p>Chcete vyfiltrovat data? Stačí napsat podmínku přímo do závorek. Je to čitelné (skoro jako angličtina) a extrémně rychlé.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                        </div>
                        <div class="code-content">
                            <span class="comment"># Zjistit základní statistiky (průměr, max, min)</span><br>
                            stats = df.<span class="func">describe</span>()<br><br>
                            <span class="comment"># FILTROVÁNÍ:</span><br>
                            <span class="comment"># Vyber objednávky nad 1000 Kč</span><br>
                            velke_objednavky = df[df[<span class="str">'cena'</span>] > <span class="num">1000</span>]<br><br>
                            <span class="comment"># Kombinace podmínek (Brno A nad 1000)</span><br>
                            brno_vip = df[(df[<span class="str">'mesto'</span>] == <span class="str">'Brno'</span>) & (df[<span class="str">'cena'</span>] > <span class="num">1000</span>)]
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3: AGREGACE -->
        <div class="slide next" id="slide-3">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">3. Agregace (GroupBy)</h3>
                    <i class="fas fa-layer-group text-indigo-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-purple-500/20 text-purple-400"><i class="fas fa-calculator"></i></div>
                        <h2>Pivot Table v kódu</h2>
                        <p>Metoda <code>.groupby()</code> je magie. Rozdělí data do skupin, aplikuje funkci (suma, průměr) a složí je zpět.</p>
                        <p>Odpovědi na otázky typu <em>"Kolik jsme prodali v každém městě?"</em> nebo <em>"Jaká je průměrná cena podle kategorie?"</em> získáte na jeden řádek.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                        </div>
                        <div class="code-content">
                            <span class="comment"># Celkové tržby podle města</span><br>
                            trzby_mesta = df.<span class="func">groupby</span>(<span class="str">'mesto'</span>)[<span class="str">'cena'</span>].<span class="func">sum</span>()<br><br>
                            <span class="comment"># Průměrný věk zákazníků podle pohlaví</span><br>
                            vek_demo = df.<span class="func">groupby</span>(<span class="str">'pohlavi'</span>)[<span class="str">'vek'</span>].<span class="func">mean</span>()<br><br>
                            <span class="comment"># Více agregací najednou</span><br>
                            report = df.<span class="func">groupby</span>(<span class="str">'kategorie'</span>).<span class="func">agg</span>({<br>
                            &nbsp;&nbsp;<span class="str">'cena'</span>: [<span class="str">'sum'</span>, <span class="str">'mean'</span>],<br>
                            &nbsp;&nbsp;<span class="str">'id'</span>: <span class="str">'count'</span><br>
                            })
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4: ČIŠTĚNÍ DAT -->
        <div class="slide next" id="slide-4">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-slate-200 font-bold">4. Čištění a Čas</h3>
                    <i class="fas fa-broom text-indigo-400"></i>
                </div>
                <div class="card-body">
                    <div>
                        <div class="feature-icon bg-orange-500/20 text-orange-400"><i class="far fa-calendar-alt"></i></div>
                        <h2>Realita není dokonalá</h2>
                        <p>Data často obsahují chyby nebo prázdná místa. Pandas má vestavěné nástroje na jejich opravu.</p>
                        <p>Navíc exceluje v práci s časem. Chcete sečíst tržby po měsících? Metoda <code>resample</code> to udělá okamžitě.</p>
                    </div>
                    <div class="code-window">
                        <div class="code-header">
                            <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                        </div>
                        <div class="code-content">
                            <span class="comment"># Vyhození řádků, kde chybí data</span><br>
                            df_clean = df.<span class="func">dropna</span>()<br><br>
                            <span class="comment"># Vyplnění chybějících hodnot nulou</span><br>
                            df_filled = df.<span class="func">fillna</span>(<span class="num">0</span>)<br><br>
                            <span class="comment"># --- TIME SERIES MAGIC ---</span><br>
                            <span class="comment"># Převod textu na datum</span><br>
                            df[<span class="str">'datum'</span>] = pd.<span class="func">to_datetime</span>(df[<span class="str">'datum'</span>])<br><br>
                            <span class="comment"># Sečíst prodeje po měsících (M = Month)</span><br>
                            mesicni_prodeje = df.<span class="func">resample</span>(<span class="str">'M'</span>, on=<span class="str">'datum'</span>).<span class="func">sum</span>()
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
            <button onclick="toggleFullscreen()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 cursor-pointer" title="Fullscreen">
                <i class="fas fa-expand"></i>
            </button>
            <button onclick="prevSlide()" class="w-12 h-12 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition border border-slate-600 focus:outline-none cursor-pointer">
                <i class="fas fa-arrow-left"></i>
            </button>
            <button onclick="nextSlide()" class="w-12 h-12 rounded-full bg-indigo-600 hover:bg-indigo-500 text-white flex items-center justify-center transition shadow-lg shadow-indigo-900/50 focus:outline-none cursor-pointer">
                <i class="fas fa-arrow-right"></i>
            </button>
        </div>
    </div>

    <!-- Progress Bar -->
    <div class="fixed top-0 left-0 h-1 bg-slate-800 w-full z-50">
        <div id="progress-bar" class="h-full bg-indigo-500 transition-all duration-300" style="width: 20%"></div>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        const progressBar = document.getElementById('progress-bar');
        const counter = document.getElementById('slide-counter');

        function updateSlide() {
            slides.forEach((slide, index) => {
                // Hard reset of classes to prevent sticking
                slide.className = 'slide';
                
                if (index === currentSlide) {
                    slide.classList.add('active');
                } else if (index < currentSlide) {
                    slide.classList.add('prev');
                } else {
                    slide.classList.add('next');
                }
            });

            // Update Progress
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

        // Init
        updateSlide();
    </script>
</body>
</html>
    """
    components.html(html_code, height=850, scrolling=False)

# ==========================================
# TAB 1: NAČTENÍ A PRŮZKUM
# ==========================================
with tab_load:
    st.header("🔍 Průzkum dat: Krok za krokem")
    st.markdown("Když dostanete nová data, chováte se jako detektiv. Musíte zjistit, s čím máte tu čest.")

    # --- KROK 1: Import a Načtení ---
    st.subheader("Krok 1: Import a Načtení")
    st.markdown("Nejdřív musíme knihovnu importovat a načíst soubor (CSV, Excel).")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
import pandas as pd

# Načtení CSV souboru do proměnné 'df' (DataFrame)
df = pd.read_csv('data/prodeje.csv')
        """, language="python")
    with col2:
        st.success("Data načtena do paměti RAM.")
        st.write("Proměnná `df` nyní obsahuje celou tabulku.")

    st.divider()

    # --- KROK 2: První pohled (Head/Tail) ---
    st.subheader("Krok 2: První pohled (`head`)")
    st.markdown("Nikdy nevypisujte celou tabulku (`print(df)`), pokud má milion řádků. Podívejte se jen na začátek.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.head() # Zobrazí prvních 5 řádků", language="python")
        st.caption("Existuje i `df.tail()`, která ukáže konec tabulky.")
    with col2:
        st.dataframe(df.head())

    st.divider()

    # --- KROK 3: Rozměry (Shape) ---
    st.subheader("Krok 3: Kolik toho je? (`shape`)")
    st.markdown("Základní otázka: Mám 10 řádků nebo 10 milionů?")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.shape", language="python")
        st.caption("Vrátí (počet_řádků, počet_sloupců)")
    with col2:
        shape = df.shape
        st.write(f"**Výsledek:** {shape}")
        st.info(f"Máme **{shape[0]}** záznamů a **{shape[1]}** sloupců.")

    st.divider()

    # --- KROK 4: Struktura a Typy (`info`) ---
    st.subheader("Krok 4: Technická kontrola (`info`)")
    st.markdown("Jsou čísla opravdu čísla? Je datum datum? A nechybí nám něco?")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.info()", language="python")
        st.markdown("""
        **Co hledat:**
        *   `Dtype`: Je 'Cena' `int/float`? (Pokud je `object`, je to špatně).
        *   `Non-Null Count`: Pokud je číslo menší než počet řádků, chybí data!
        """)
    with col2:
        import io
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

    st.divider()

    # --- KROK 5: Statistiky (`describe`) ---
    st.subheader("Krok 5: Matematický pohled (`describe`)")
    st.markdown("Rychlý přehled o číselných sloupcích. Odhalí extrémy a divné hodnoty.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.describe()", language="python")
        st.markdown("""
        **Vysvětlivky:**
        *   `mean`: Průměr
        *   `min/max`: Extrémy (nejsou tam záporné ceny?)
        *   `50%`: Medián (často lepší než průměr)
        """)
    with col2:
        st.dataframe(df.describe())

    st.divider()

    # --- KROK 6: Kategorická data (`value_counts`) ---
    st.subheader("Krok 6: Co je ve sloupcích? (`value_counts`)")
    st.markdown("Pro textové sloupce (Kategorie, Pobočka) nás zajímá, jaké hodnoty se tam opakují.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df['Kategorie'].value_counts()", language="python")
    with col2:
        st.write(df['Kategorie'].value_counts())

# ==========================================
# TAB 2: ČIŠTĚNÍ DAT
# ==========================================
with tab_clean:
    st.header("🧹 Čištění dat: Diagnóza a Léčba")
    st.markdown("Data jsou málokdy dokonalá. Ukážeme si postup: **Najít problém -> Opravit problém**.")

    # --- PROBLÉM 1: Chybějící hodnoty ---
    st.subheader("1. Chybějící hodnoty (NaN)")
    st.markdown("Někdy data prostě chybí. Pandas je označuje jako `NaN` (Not a Number).")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Kde to chybí?**")
        st.code("df.isnull().sum()", language="python")
        st.write("Výsledek:", df.isnull().sum())
        st.warning("Vidíme, že ve sloupci 'Cena' chybí 1 hodnota.")
    
    with col2:
        st.markdown("**💊 Léčba: Doplnit nebo smazat?**")
        st.markdown("Můžeme řádek smazat (`dropna`) nebo doplnit (`fillna`). Zde doplníme nulu.")
        st.code("df['Cena'] = df['Cena'].fillna(0)", language="python")
        
        # Aplikace opravy
        df['Cena'] = df['Cena'].fillna(0)
        st.success("Hotovo! Počet NaN nyní: " + str(df['Cena'].isnull().sum()))

    st.divider()

    # --- PROBLÉM 2: Duplicity ---
    st.subheader("2. Duplicity")
    st.markdown("Stejný řádek se v datech objeví dvakrát (např. chyba při exportu).")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Máme dvojčata?**")
        st.code("df.duplicated().sum()", language="python")
        dups = df.duplicated().sum()
        st.write(f"Počet duplicitních řádků: **{dups}**")
        if dups > 0:
            st.warning("Pozor, máme tam duplicity!")
    
    with col2:
        st.markdown("**💊 Léčba: Odstranit duplicity**")
        st.code("df = df.drop_duplicates()", language="python")
        
        # Aplikace opravy
        df = df.drop_duplicates()
        st.success(f"Hotovo! Počet duplicit nyní: {df.duplicated().sum()}")

    st.divider()

    # --- PROBLÉM 3: Nekonzistentní text ---
    st.subheader("3. Nekonzistentní text (Překlepy)")
    st.markdown("Počítač vidí 'Brno' a 'brno' jako dvě různé věci.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Co tam máme?**")
        st.code("df['Pobocka'].unique()", language="python")
        st.write("Unikátní hodnoty:", df['Pobocka'].unique())
        st.warning("Vidíte 'Brno' a 'brno'?")
    
    with col2:
        st.markdown("**💊 Léčba: Sjednotit velikost**")
        st.markdown("Převedeme vše na formát 'První velké'.")
        st.code("df['Pobocka'] = df['Pobocka'].str.capitalize()", language="python")
        
        # Aplikace opravy
        df['Pobocka'] = df['Pobocka'].str.capitalize()
        st.success("Hotovo! Hodnoty: " + str(df['Pobocka'].unique()))

# ==========================================
# TAB 3: TRANSFORMACE
# ==========================================
with tab_transform:
    st.header("🛠️ Feature Engineering: Tvorba nových dat")
    st.markdown("Surová data často nestačí. Musíme si 'vypočítat' to, co nás zajímá.")

    # --- 1. Matematické operace ---
    st.subheader("1. Matematické operace")
    st.markdown("Máme `Cenu` a `Množství`. Chceme vědět, kolik zákazník zaplatil celkem.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("df['Celkem'] = df['Cena'] * df['Mnozstvi']", language="python")
    with col2:
        df_clean['Celkem'] = df_clean['Cena'] * df_clean['Mnozstvi']
        st.dataframe(df_clean[['Produkt', 'Cena', 'Mnozstvi', 'Celkem']].head(3))

    st.divider()

    # --- 2. Práce s časem (Datetime) ---
    st.subheader("2. Práce s časem (Datetime)")
    st.markdown("Datum `2023-01-01` nám moc neřekne. Ale 'Leden' nebo 'Neděle' už ano!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Měsíc (slovně)
df['Mesic'] = df['Datum'].dt.month_name()

# Den v týdnu
df['Den'] = df['Datum'].dt.day_name()
        """, language="python")
    with col2:
        df_clean['Mesic'] = df_clean['Datum'].dt.month_name()
        df_clean['Den'] = df_clean['Datum'].dt.day_name()
        st.dataframe(df_clean[['Datum', 'Mesic', 'Den']].head(3))
        st.info("💡 Funguje jen, pokud je sloupec převeden na `datetime`!")

    st.divider()

    # --- 3. Kategorizace (Binning) ---
    st.subheader("3. Kategorizace (Binning)")
    st.markdown("Chceme rozdělit objednávky na 'Malé' a 'Velké'.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Funkce pro kategorizaci
def obarvit(cena):
    if cena > 10000:
        return 'Velká'
    else:
        return 'Malá'

df['Typ'] = df['Celkem'].apply(obarvit)
        """, language="python")
    with col2:
        df_clean['Typ'] = df_clean['Celkem'].apply(lambda x: 'Velká' if x > 10000 else 'Malá')
        st.dataframe(df_clean[['Celkem', 'Typ']].head(3))

    st.divider()

    # --- 4. Pokročilé filtrování ---
    st.subheader("4. Pokročilé filtrování")
    st.markdown("Jak vybrat přesně to, co hledáme?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Podmínka A ZÁROVEŇ (AND `&`)**")
        st.code("""
# Pobočka Praha A Velká objednávka
mask = (df['Pobocka'] == 'Praha') & (df['Typ'] == 'Velká')
df[mask]
        """, language="python")
    with col2:
        mask = (df_clean['Pobocka'] == 'Praha') & (df_clean['Typ'] == 'Velká')
        st.dataframe(df_clean[mask].head(3))

# ==========================================
# TAB 4: AGREGACE
# ==========================================
with tab_agg:
    st.header("📊 Agregace: Od detailu k přehledu")
    st.markdown("Manažera nezajímají jednotlivé účtenky. Zajímá ho: **'Kolik jsme vydělali v Praze?'**")

    # --- 1. GroupBy (Základ) ---
    st.subheader("1. GroupBy (Seskupování)")
    st.markdown("Princip: Rozděl data do skupinek -> Spočítej něco pro každou skupinku.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Příklad: Tržby podle Pobočky**")
        st.code("""
# Seskupit podle 'Pobocka' a sečíst 'Celkem'
df.groupby('Pobocka')['Celkem'].sum()
        """, language="python")
    with col2:
        res = df_clean.groupby('Pobocka')['Celkem'].sum()
        st.dataframe(res)

    st.divider()

    # --- 2. Více metrik najednou ---
    st.subheader("2. Více metrik najednou (.agg)")
    st.markdown("Co když chci součet, průměr i počet objednávek najednou?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
df.groupby('Kategorie')['Celkem'].agg(
    ['sum', 'mean', 'count']
)
        """, language="python")
    with col2:
        res_agg = df_clean.groupby('Kategorie')['Celkem'].agg(['sum', 'mean', 'count'])
        st.dataframe(res_agg)

    st.divider()

    # --- 3. Řazení výsledků ---
    st.subheader("3. Řazení výsledků (.sort_values)")
    st.markdown("Chceme vidět ty nejlepší nahoře.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Seřadit sestupně (ascending=False)
df.groupby('Pobocka')['Celkem'].sum().sort_values(ascending=False)
        """, language="python")
    with col2:
        res_sort = df_clean.groupby('Pobocka')['Celkem'].sum().sort_values(ascending=False)
        st.dataframe(res_sort)

    st.divider()

    # --- 4. Pivot Tables (Kontingenční tabulky) ---
    st.subheader("4. Pivot Tables (Matice)")
    st.markdown("Královská disciplína. Data ve dvou dimenzích (řádky vs. sloupce).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
df.pivot_table(
    values='Celkem',    # Co počítáme (čísla)
    index='Pobocka',    # Co je v řádcích
    columns='Kategorie',# Co je ve sloupcích
    aggfunc='sum',      # Funkce (sum, mean...)
    fill_value=0        # Co dát místo NaN
)
        """, language="python")
    with col2:
        pivot = df_clean.pivot_table(
            values='Celkem', 
            index='Pobocka', 
            columns='Kategorie', 
            aggfunc='sum',
            fill_value=0
        )
        st.dataframe(pivot)

# ==========================================
# TAB 5: PŘÍPRAVA PRO GRAFY (OBECNĚ)
# ==========================================
with tab_challenge:
    st.header("🚀 Příprava podkladů pro Dashboard")
    st.markdown("""
    Ať už analyzujete prodeje, počasí nebo sportovní výsledky, vždy budete potřebovat připravit data pro grafy.
    Zde je **5 univerzálních vzorů**, které využijete v 90 % případů.
    """)

    # 1. Časová řada
    st.subheader("1. Vzor: Vývoj v čase (Time Series)")
    st.info("Cíl: Připravit data pro **Line Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle časové jednotky (den, měsíc, rok) a sečíst hodnoty.
    *   **X osa:** Časový sloupec
    *   **Y osa:** Číselný sloupec (Suma/Průměr)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df.groupby('CASOVY_SLOUPEC')['CISELNY_SLOUPEC'].sum().reset_index()", language="python")

    st.divider()

    # 2. Kategorické srovnání
    st.subheader("2. Vzor: Žebříček (Ranking)")
    st.info("Cíl: Připravit data pro **Bar Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle kategorie a seřadit je, abychom viděli "Kdo je nejlepší".
    *   **X osa:** Kategorický sloupec (Kdo?)
    *   **Y osa:** Číselný sloupec (Kolik?)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("""
df.groupby('KATEGORICKY_SLOUPEC')['CISELNY_SLOUPEC'].sum()
  .sort_values(ascending=False)
  .reset_index()
        """, language="python")

    st.divider()

    # 3. Detailní rozpad
    st.subheader("3. Vzor: Rozpad (Drill-down)")
    st.info("Cíl: Připravit data pro **Stacked Bar Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle DVOU kategorií najednou.
    *   **X osa:** Hlavní kategorie (např. Pobočka)
    *   **Barva:** Podkategorie (např. Typ produktu)
    *   **Y osa:** Číselný sloupec
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df.groupby(['HLAVNI_KAT', 'POD_KAT'])['CISELNY_SLOUPEC'].sum().reset_index()", language="python")

    st.divider()

    # 4. Korelace
    st.subheader("4. Vzor: Vztahy (Correlation)")
    st.info("Cíl: Připravit data pro **Scatter Plot**.")
    st.markdown("""
    **Princip:** Zde většinou neagregujeme. Hledáme vztah mezi dvěma čísly na úrovni detailu.
    *   **X osa:** Číselný sloupec A (např. Cena)
    *   **Y osa:** Číselný sloupec B (např. Množství)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df[['CISELNY_SLOUPEC_A', 'CISELNY_SLOUPEC_B', 'KATEGORIE']]", language="python")

    st.divider()

    # 5. KPI Metriky
    st.subheader("5. Vzor: Jedno číslo (KPI)")
    st.info("Cíl: Připravit data pro **Big Number**.")
    st.markdown("""
    **Princip:** Jednoduchá agregace celého sloupce. Žádné seskupování.
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("total = df['CISELNY_SLOUPEC'].sum()", language="python")
