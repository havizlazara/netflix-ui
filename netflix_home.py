import streamlit as st

movies = {
    "Trending Now": ["The Witcher", "Stranger Things", "Money Heist", "Wednesday", "Squid Game"],
    "Popular on Netflix": ["You", "Lupin", "Dark", "Bridgerton", "Narcos"],
    "New Releases": ["Atlas", "Rebel Moon", "Heart of Stone", "Lift", "Beef"]
}
poster_urls = {
    "The Witcher": "https://raw.githubusercontent.com/havizlazara/netflix-ui/main/The%20Witcher_%20Storm%27s%20Embrace.png"
    "Squid Game": "https://raw.githubusercontent.com/havizlazara/netflix-ui/main/Squid%20Game%20Poster%20with%20Two%20Girls.png"
    }

st.set_page_config(page_title="Netflix UI", layout="wide")
st.markdown("<h1 style='color: red; font-size: 50px;'>NETFLIX</h1>", unsafe_allow_html=True)
st.markdown("### Welcome back, user123 👋 What do you want to watch today?")


for category, titles in movies.items():
    st.markdown(f"### {category}")
    cols = st.columns(len(titles))
    for i, title in enumerate(titles):
        with cols[i]:
            img_url = poster_urls.get(title, "https://via.placeholder.com/150x220")
            st.image(img_url, caption=title)
            

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")