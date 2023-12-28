import streamlit as st

st.set_page_config(page_title = "My Webpage", page_icon=":tada", layout="wide")


# -----  Header Section ----------

st.subheader("Hi, I am Muhammad :wave:")
st.title("A Gen-AI Specialist from Pakistan")
st.write("I am enthusiastic about exploring the Metaverse, harnessing Web 3.0, and leveraging generative AI to revolutionize digital interactions and innovations.")
st.write("[Learn More >](https://m-h-s-portfolio.vercel.app/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
                 On my YouTube channel and LinkedIn, I share overviews of my projects for those who:

                 - are fascinated by the practical applications of Gen-AI Applications.
                 - have a keen interest in the evolving landscape of Web 3.0, Metaverse and 3D modelling.
                 - are excited about the potential and advancements in generative AI.
                 - are looking for insights into real-world projects harnessing these cutting-edge technologies.
                 
                 If you're intrigued by these areas and want a glimpse into groundbreaking projects, consider subscribing and turning on notifications to get a firsthand look at my latest creations.
                 
                 """
                 )
st.write("[Youtube Channel >](https://www.youtube.com/channel/UC8Ep4wPR7PLvKuvqFRssgRw)")


