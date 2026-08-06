import streamlit as st
import pandas as pd
import plotly.express as px


# Test dashboard functionality using: streamlit run Overview.py
# Load synthetic dataset
df_gaming = pd.read_csv("synthetic_gaming_data.csv")


# Title
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0;">The Perfect Game</h1>
        <h1 style="font-style: italic; margin-top: 0;">Video Games Rating & Review Insights</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# Overview
st.write("""
This dashboard gives a broad overview of a large synthetic collection of video game data and highlights 
general patterns in how games are rated across different genres and play styles. You will get a quick sense 
of what tends to score well and how different types of games compare. From here, you can drill down into 
specific segments, apply filters, and explore the data more closely to see how different factors influence 
game ratings and overall trends.
""")


# Overview Visual (Emoji-Based Rating Summary)
st.subheader("How Players Rate Games")

st.write(
    "Player ratings tend to fall into a few recognizable tiers. Here's a quick, easy-to-read "
    "breakdown of how games are rated across the dataset."
)


# Create rating tiers
controller_icon = "https://cdn-icons-png.flaticon.com/128/808/808439.png"

def rating_to_tier(score):
    if score >= 90:
        return "High"
    elif score >= 75:
        return "Medium"
    else:
        return "Low"

df_gaming["rating_tier"] = df_gaming["rating_score"].apply(rating_to_tier)
tier_counts = df_gaming["rating_tier"].value_counts(normalize=True) * 100

tier_icon_count = {
    "High": 5,
    "Medium": 3,
    "Low": 1
}

st.subheader("How Players Rate Games")
st.write("Player ratings tend to fall into a few recognizable tiers:")

for tier, pct in tier_counts.items():
    count = tier_icon_count[tier]
    icons_html = "".join([f'<img src="{controller_icon}" width="26">' for _ in range(count)])

    st.markdown(
        f"""
        <div style="
            display:flex;
            align-items:center;
            justify-content:flex-start;
            gap:20px;
            width:100%;
        ">
            <div style="min-width:160px;">
                {icons_html}
            </div>
            <div>
                <strong>{tier}: {pct:.1f}% of games</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.caption("Most games fall into the low/medium tiers, reflecting consistent mid‑range ratings across the dataset.")


# Add image for background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://media.istockphoto.com/id/1061119906/photo/game-background.jpg?b=1&s=612x612&w=0&k=20&c=A8VH5IYC1M3r85YxVHZDqHEshJzJsASyU3vTAzvnq90=");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


