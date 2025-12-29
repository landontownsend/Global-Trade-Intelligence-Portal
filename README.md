# 🌐 Global Trade Intelligence Portal

### [🚀 View Live Dashboard](https://global-trade-intelligence-app-lruyubmberdnzwxztzvcoe.streamlit.app/)

A full-stack data analytics application that visualizes over 30 years of global trade flow data (1988–2021). This tool allows researchers and analysts to interactively filter millions of trade records to identify economic trends, top trading partners, and commodity anomalies.

## 🛠️ Tech Stack & Key Skills
* **Core:** Python 3.10+, Streamlit
* **Data Engineering:** Pandas, PyArrow (Parquet conversion for 70% storage optimization)
* **Visualization:** Plotly Express (Interactive Choropleth & Bar Charts)
* **Deployment:** Streamlit Community Cloud (CI/CD via GitHub)

## ⚡ Key Features
* **High-Performance Data Layer:** Migrated legacy CSV datasets to **Parquet format**, reducing load times and memory usage by ~70%.
* **Smart Caching:** Implemented `@st.cache_data` to ensure sub-second response times during filtering.
* **Interactive Analytics:** Users can drill down by specific years (1988-2021) and filter by reporting countries to view bilateral trade volumes.

## 📦 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/landontownsend/Global-Trade-Intelligence-Portal.git](https://github.com/landontownsend/Global-Trade-Intelligence-Portal.git)
