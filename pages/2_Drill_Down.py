import streamlit as st
import pandas as pd
import plotly.express as px


# Read in the synthetic gaming dataset
df_gaming = pd.read_csv("synthetic_gaming_data.csv")

st.title("Focus Up: Drill Down into Video Game Ratings")


# Create a refresh button to reload the dataset
if st.button("Refresh Data"):
    df_gaming = pd.read_csv("synthetic_gaming_data.csv")
    st.success("Data refreshed!")


# Create sidebar filters
st.sidebar.header("Filters")

genre_filter = st.sidebar.selectbox(
    "Genre",
    options=["All"] + sorted(df_gaming["game_genre"].dropna().unique().tolist())
)

mode_filter = st.sidebar.selectbox(
    "Game Mode",
    options=["All"] + sorted(df_gaming["game_mode"].dropna().unique().tolist())
)

perspective_filter = st.sidebar.selectbox(
    "Player Perspective",
    options=["All"] + sorted(df_gaming["player_perspective"].dropna().unique().tolist())
)

year_filter = st.sidebar.slider(
    "Release Year",
    int(df_gaming["release_year"].min()),
    int(df_gaming["release_year"].max()),
    (int(df_gaming["release_year"].min()), int(df_gaming["release_year"].max()))
)


# Apply filters
filtered_df = df_gaming.copy()

if genre_filter != "All":
    filtered_df = filtered_df[filtered_df["game_genre"] == genre_filter]

if mode_filter != "All":
    filtered_df = filtered_df[filtered_df["game_mode"] == mode_filter]

if perspective_filter != "All":
    filtered_df = filtered_df[filtered_df["player_perspective"] == perspective_filter]

filtered_df = filtered_df[
    (filtered_df["release_year"] >= year_filter[0]) &
    (filtered_df["release_year"] <= year_filter[1])
]


# KPI cards
avg_rating = filtered_df["rating_score"].mean()
avg_rating_count = filtered_df["rating_count"].mean()

kpi1, kpi2 = st.columns(2)

with kpi1:
    st.metric("Average Rating Score", f"{avg_rating:.1f}")

with kpi2:
    st.metric("Average Rating Count", f"{avg_rating_count:.1f}")


# Side-by-side visualizations
left, right = st.columns(2)

with left:
    st.subheader("Rating Distribution")
    fig_rating = px.histogram(filtered_df, x="rating_score", nbins=20)
    st.plotly_chart(fig_rating, use_container_width=True)

with right:
    st.subheader("Average Rating by Genre")
    fig_genre = px.bar(
        filtered_df.groupby("game_genre")["rating_score"].mean().reset_index(),
        x="game_genre",
        y="rating_score",
        color="game_genre"
    )
    st.plotly_chart(fig_genre, use_container_width=True)


# Table for top (filered)
st.subheader("Top 10 Games by Rating")

relevant_cols = [
    "game_genre",
    "game_theme",
    "player_perspective",
    "game_mode",
    "age_rating",
    "supported_platforms",
    "release_year",
    "rating_score",
    "rating_count"
]

top10 = (
    filtered_df
    .sort_values("rating_score", ascending=False)
    .head(10)[relevant_cols]
)

st.dataframe(top10, hide_index=True, use_container_width=True)