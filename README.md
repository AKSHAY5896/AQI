# 🌫️ PM2.5 Air Quality Predictor — Flask Web App

A Flask-based web application that takes a user-entered **PM2.5 value**, clusters it against 50 Indian cities using **K-Means (K=6)**, assigns an **AQI health category**, and displays an interactive **cluster scatter plot** comparing the user's input to real city data.

---

## 🖥️ App Demo

| Page | Description |
|---|---|
| `/` | Enter a PM2.5 value → get predicted cluster & AQI category |
| `/details` | View your result alongside a full city cluster scatter plot |

### Flow

```
User enters PM2.5 value
        │
        ▼
  KMeans Prediction (K=6)
        │
        ├─► Cluster label (C1 – C6)
        └─► AQI Category (Good → Hazardous)
                │
                ▼
        /details — Scatter plot of all 50 cities
        with user's value highlighted ⭐
```

---

## 📊 Dataset

| Property | Details |
|---|---|
| **File** | `pm25_data.csv` |
| **Records** | 50 Indian cities |
| **Columns** | `city`, `pm25` |
| **PM2.5 Range** | 3.25 — 308.89 µg/m³ |
| **Mean PM2.5** | ~167.49 µg/m³ |

---

## 🤖 ML Details

### Algorithm
**K-Means Clustering** with `n_clusters=6`, `random_state=0`

Trained on the `pm25` column of all 50 cities. When a user submits a value, `kmeans.predict()` assigns it to the nearest cluster centroid in real time.

### AQI Categories

| PM2.5 (µg/m³) | Category |
|---|---|
| ≤ 50 | 😀 Good |
| 51 – 100 | 🙂 Moderate |
| 101 – 150 | 😐 Unhealthy (Sensitive Groups) |
| 151 – 200 | 😷 Unhealthy |
| 201 – 300 | 🤒 Very Unhealthy |
| > 300 | ☠️ Hazardous |

---

## 📂 Project Structure

```
pm25-predictor/
│
├── templates/
│   ├── index.html          # Home page — input form & prediction result
│   └── details.html        # Details page — cluster plot & full breakdown
│
├── pm25_data.csv           # Dataset (50 Indian cities)
├── app.py                  # Flask app — ML model, routes, plot generation
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pm25-predictor.git
cd pm25-predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
flask
pandas
matplotlib
scikit-learn
```

---

## 🚀 Running the App

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000/
```

---

## 🗺️ Routes

### `GET / POST /`
- **GET** — renders the input form
- **POST** — accepts a PM2.5 float value, runs `kmeans.predict()`, returns the cluster (C1–C6) and AQI category

### `GET /details`
- Generates a Matplotlib scatter plot of all 50 cities coloured by cluster
- Overlays the user's input as a gold star ⭐ marker
- Encodes the plot as a base64 PNG and embeds it directly in the HTML — no file I/O needed

---

## 🔑 Key Implementation Notes

- **`matplotlib.use('Agg')`** is set at startup so Matplotlib runs without a display (required for server-side rendering in Flask)
- The cluster plot is generated in-memory using `io.BytesIO()` and served as a base64-encoded image — no static files created
- Cluster indices from KMeans (0–5) are shifted to **C1–C6** for user-facing display
- AQI colour coding in `details.html` uses CSS classes (`good`, `moderate`, `sensitive`, `unhealthy`, `veryunhealthy`, `hazardous`)

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| **Flask** | Web framework & routing |
| **Pandas** | CSV loading & DataFrame operations |
| **Scikit-learn** | KMeans clustering & real-time prediction |
| **Matplotlib** | Server-side cluster scatter plot |
| **HTML / CSS** | Frontend templates (Jinja2) |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub: [@AKSHAY5896](https://github.com/AKSHAY5896)

