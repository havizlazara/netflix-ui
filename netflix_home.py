import streamlit as st

movies = {
    "Trending Now": ["The Witcher", "Stranger Things", "Money Heist", "Wednesday", "Squid Game"],
    "Popular on Netflix": ["You", "Lupin", "Dark", "Bridgerton", "Narcos"],
    "New Releases": ["Atlas", "Rebel Moon", "Heart of Stone", "Lift", "Beef"]
}

st.set_page_config(page_title="Netflix UI", layout="wide")
st.markdown("<h1 style='color: red; font-size: 50px;'>NETFLIX</h1>", unsafe_allow_html=True)
st.markdown("### Welcome back, user123 👋 What do you want to watch today?")

for category, titles in movies.items():
    st.markdown(f"### {category}")
    cols = st.columns(len(titles))
    for i, title in enumerate(titles):
        with cols[i]:
            st.image("https://via.placeholder.com/150x220?text=" + title.replace(" ", "+"), caption=title)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")