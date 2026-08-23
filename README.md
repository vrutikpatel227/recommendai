# 🎬 RecommendAI

Your personal cinematic universe — discover, save, and explore movies you’ll love.  
RecommendAI is a **Streamlit‑based movie recommendation system** that combines content‑based filtering, collaborative suggestions, and hybrid recommendations with a polished Netflix‑style UI.

---
# 🎬 RecommendAI

A Streamlit-based movie recommendation system using OMDb API.

## 🚀 Live Demo
You can try the app here: [RecommendAI Live](https://recommend-ai.streamlit.app/)


## 🚀 Features

- **Movie Grid Cards**
  - Posters with title, IMDb rating, Rotten Tomatoes score, director, runtime, and plot snippet.
  - Save favorites and watch trailers directly.

- **Favorites System**
  - Save movies to your favorites list.
  - Clear favorites with one click.
  - Export favorites as **CSV** or **PDF** (styled with red header + table layout).

- **Recommendation Engines**
  - Content‑based (genre similarity).
  - Collaborative (similar users’ choices).
  - Hybrid (combined approach).
  - Smart cosine similarity recommendations.

- **Search Functionality**
  - Autocomplete search bar with live OMDb suggestions.
  - Rich metadata display for search results.

- **Export Options**
  - Download recommendations as **PDF** or **CSV**.
  - PDF exports include styled tables and branding footer.

- **Premium UI**
  - Netflix‑style red accents, hover effects, centered buttons, hero banner, collapsible sidebar.

---

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Backend/Data**: Python, Pandas, scikit‑learn (TF‑IDF, cosine similarity)  
- **API**: [OMDb API](https://www.omdbapi.com/) for posters, ratings, metadata  
- **PDF Export**: FPDF  
- **Styling**: Custom CSS for Netflix‑style UI

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recommendai.git
   cd recommendai


2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Add your OMDb API key to Streamlit secrets:

. Create a file .streamlit/secrets.toml in the project root:

[omdb]
api_key = "YOUR_OMDB_API_KEY"


▶️ Usage
Run the app locally:

streamlit run main.py

Open http://localhost:8501 (localhost in Bing) in your browser.


📥 Exports
. Favorites: Download as CSV or styled PDF.

. Recommendations: Download as CSV or PDF with tables.


📸 Screenshots
. Hero banner with tagline.

. Movie grid cards with posters, ratings, director, runtime, plot.

. Sidebar favorites section with export buttons.

. Tabbed recommendations (Content‑based, Collaborative, Hybrid).


🌐 Deployment
You can deploy RecommendAI on:

Streamlit Cloud (recommended for simplicity).

Heroku / Render / Vercel with Python backend.

Docker for containerized deployment.

👨‍💻 Author
Built by Vrutik — Engineering student passionate about automation, dashboards, and movie recommendation systems.


---

### 🎯 Status Recap
- ✅ Code is stable and consistent (grid cards now show full metadata).  
- ✅ UI polished with Netflix‑style design.  
- ✅ Favorites and exports working.  
- ✅ README.md is now production‑ready.  

👉 Next step: I recommend adding a **requirements.txt** file so anyone can install dependencies easily. Do you want me to generate that file for you now?
