import re, PIL, streamlit as st
from utils.tools import st_button, load_css


def LoadCSS(path: str):
    load_css(path)

def Celebrate(active: bool = True):
    if active:
        st.snow()

def configureApp(sourcefile: str):
    with open(sourcefile, "rb") as profiles:
        # Read in bytes object  
        profiles = profiles.read().decode()
        
        # Decode & clean / remove chars
        profiles = profiles.replace('"', '').replace('\r', '').split('\n')
        
        # Extract key-val pairs
        profiles = {i.split(':', maxsplit=1)[0] : i.split(':', maxsplit=1)[1].strip() for i in profiles if re.findall(':', i)}

    return profiles

def Run(profile: dict, profile_pic: str = None):
    
    # App Pic
    if profile_pic == None:
        st.image(PIL.Image.open("utils/images/default.jfif"), width=200)
    else:
        st.image(PIL.Image.open(profile_pic), width=200)

    # Person Info
    st.header(f'''{profile['name']}''')

    if "bio" in profile.keys():
        with st.container():
            st.markdown(
                f'''<p style="font-size:120%;" align="center"><b>{profile['bio']}</b></p>''', 
                unsafe_allow_html=True)
            
    # Links
    for key in profile.keys():
        if key not in ['name', 'bio']:
            st_button(label=key, url=profile[key])

    # Footnotes
    st.markdown('---')
    st.markdown(
        f'''<p style="font-size:75%;" align="right"><b>❄ SNWLNK by DNYFZR</b></p><br/>''', 
        unsafe_allow_html=True)
