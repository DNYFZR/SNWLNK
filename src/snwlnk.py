import re, PIL, streamlit as st
from utils.tools import st_button, load_css


def LoadCSS(path: str ="css/style.css"):
    load_css(path)

def Celebrate(active: bool = True):
    if active:
        st.snow()

@st.cache
def configureApp():
    with open("config/profile.yml", "rb") as profiles:
        # Read in, decode & remove chars 
        profiles = profiles.read().decode()
        profiles = profiles.replace('"', '').replace('\r', '').split('\n')
        
        # Extract key-val pairs
        profiles = {i.split(':', maxsplit=1)[0] : i.split(':', maxsplit=1)[1].strip() for i in profiles if re.findall(':', i)}

    return profiles

def App(profile: dict = configureApp(), profile_pic: str = "config/profile.jpg"):
    # App logo
    st.markdown(f'''**❄ SNWLNK ❄**''')

    # App page
    _, col2, _ = st.columns(3)
    col2.image(PIL.Image.open(profile_pic))

    # Person Info
    st.header(f'''{profile['name']}''')

    if "bio" in profile.keys():
        with st.container():
            st.markdown(
                f'''<p style="font-size:100%;" align="center"><b>{profile['bio']}</b></p>''', 
                unsafe_allow_html=True)
            
    # Links
    for key in profile.keys():
        if key not in ['name', 'bio']:
            st_button(label=key, url=profile[key])

    # Footnotes
    st.markdown('---')
    st.markdown(
        f'''<p style="font-size:75%;" align="right"><b>SNWLNK by DNYFZR</b></p><br/>''', 
        unsafe_allow_html=True)
