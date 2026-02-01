import pandas as pd
import altair as alt

# 1. Načtení dat
df = pd.read_csv('../data/prodeje.csv')
df['Datum'] = pd.to_datetime(df['Datum'])
df['Celkem'] = df['Cena'] * df['Mnozstvi']

# 2. Rychlý průzkum
print(df.head())
print(df.info())

# 3. Vizualizace (Altair)

# Bar chart
chart_bar = alt.Chart(df).mark_bar().encode(
    x='Kategorie',
    y='sum(Celkem)',
    color='Pobocka'
)
# V Jupyter Notebooku stačí napsat název proměnné pro zobrazení:
# chart_bar

# Line chart
chart_line = alt.Chart(df).mark_line().encode(
    x='Datum',
    y='sum(Celkem)'
)
# chart_line

# Scatter plot
chart_scatter = alt.Chart(df).mark_circle().encode(
    x='Mnozstvi',
    y='Cena',
    color='Kategorie'
)
# chart_scatter
