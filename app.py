from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import io
import base64

app = Flask(__name__)

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("pm25_data.csv")

# Train KMeans
kmeans = KMeans(n_clusters=6, random_state=0)
df["Cluster"] = kmeans.fit_predict(df[["pm25"]])

# -------------------------
# AQI Category Function
# -------------------------
def get_aqi_category(value):
    """Return AQI category name for given PM2.5 value."""
    if value <= 50:
        return "Good 😀"
    elif value <= 100:
        return "Moderate 🙂"
    elif value <= 150:
        return "Unhealthy (Sensitive Groups) 😐"
    elif value <= 200:
        return "Unhealthy 😷"
    elif value <= 300:
        return "Very Unhealthy 🤒"
    else:
        return "Hazardous ☠️"

# -------------------------
# Store user values
# -------------------------


# -------------------------
# Routes
# -------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    global user_value, user_cluster
    prediction = None
    category = None
    user_value = None
    user_cluster = None

    if request.method == "POST":
        try:
            user_value = float(request.form["pm_value"])
            user_cluster = kmeans.predict([[user_value]])[0] + 1  # shift 0–5 to 1–6
            category = get_aqi_category(user_value)  # use function
            prediction = f"Cluster C{user_cluster} - {category}"
        except:
            prediction = "Invalid input"
            category = None

    return render_template("index.html",
                           prediction=prediction,
                           user_value=user_value,
                           user_cluster=user_cluster,
                           category=category)

@app.route("/details")
def details():
    global user_value, user_cluster

    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot of clusters
    for cluster in df["Cluster"].unique():
        cluster_data = df[df["Cluster"] == cluster]
        ax.scatter(cluster_data["city"], cluster_data["pm25"],
                   label=f"C{cluster+1}", s=50)

    # Plot user input
    if user_value is not None:
        ax.scatter("Your City", user_value,
                   c="gold", s=200, marker="*", edgecolors="black",
                   label="Your Input")
        ax.annotate("PM2.5 in your city",
                    xy=("User Input", user_value+2),
                    xytext=(0,25), textcoords="data",
                    ha="center",va="bottom", fontsize=9, color="black", fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color="black"))

    ax.set_title("Air Quality Clusters")
    ax.set_xlabel("City")
    ax.set_ylabel("PM2.5 Level")
    plt.xticks(rotation=45, ha="right")
    ax.legend(loc="lower left",bbox_to_anchor=(1, 0.5), fontsize=9, frameon=True)

    # Save plot as base64 string
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode("utf8")
    plt.close()

    return render_template("details.html",
                           user_value=user_value,
                           user_cluster=user_cluster,
                           category=get_aqi_category(user_value) if user_value else "Unknown",
                           plot_url=plot_url)

# -------------------------

if __name__ == "__main__":
    app.run(debug=True)
