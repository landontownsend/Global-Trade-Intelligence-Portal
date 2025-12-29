import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration (The "Aesthetic" part)
st.set_page_config(page_title="Global Trade Intel", layout="wide")
st.title("🌐 Global Trade Intelligence Portal")
st.markdown("Analysis of trade flows from 1988 to 2021 | Built with Python & Streamlit")

# 2. Load and Cache Data (Efficiency)
@st.cache_data
def load_data():
    df = pd.read_csv('/Users/landon/Trade Data Py/trade_1988_2021.csv')
    # Basic cleaning
    df = df.dropna(subset=['TradeValue in 1000 USD'])
    df['TradeValue_Billion'] = df['TradeValue in 1000 USD'] / 1000000
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Data")
year_list = sorted(df['Year'].unique(), reverse=True)
selected_year = st.sidebar.selectbox("Select Year", year_list)

country_list = sorted(df['ReporterName'].unique())
selected_country = st.sidebar.multiselect("Select Countries", country_list, default=["United States", "France", "Saudi Arabia"])

# Filter the dataframe
filtered_df = df[(df['Year'] == selected_year) & (df['ReporterName'].isin(selected_country))]

# 4. Top Level KPIs (Scorecards)
col1, col2, col3 = st.columns(3)
total_val = filtered_df['TradeValue_Billion'].sum()
avg_val = filtered_df['TradeValue_Billion'].mean()

col1.metric("Total Trade (Billions USD)", f"${total_val:,.2f}B")
col2.metric("Active Partners", filtered_df['PartnerName'].nunique())
col3.metric("Avg Transaction", f"${avg_val:,.2f}B")

# 5. Interactive Charts (Plotly)
st.divider()
left_col, right_col = st.columns(2)

with left_col:
    st.subheader(f"Top 10 Trading Partners in {selected_year}")
    top_partners = filtered_df.groupby('PartnerName')['TradeValue_Billion'].sum().nlargest(10).reset_index()
    fig_bar = px.bar(top_partners, x='TradeValue_Billion', y='PartnerName', 
                     orientation='h', template="plotly_dark", color='TradeValue_Billion')
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.subheader("Trade Value Distribution")
    fig_pie = px.pie(top_partners, values='TradeValue_Billion', names='PartnerName', hole=0.4, template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. Global Trend Chart
st.subheader("Historical Trade Evolution")
trend_df = df[df['ReporterName'].isin(selected_country)].groupby(['Year', 'ReporterName'])['TradeValue_Billion'].sum().reset_index()
fig_line = px.line(trend_df, x='Year', y='TradeValue_Billion', color='ReporterName', template="plotly_dark")
st.plotly_chart(fig_line, use_container_width=True)