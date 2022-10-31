import re, PIL, sys, streamlit as st
sys.path.append('../')
from ..utils.tools import st_button, load_css

# Load CSS style
load_css(path="../css/style.css")

# Celebrate   
st.snow()


# Bring in data from profiles.yml
with open("../config/profile.yml", "rb") as profiles:
    # Read in, decode & remove chars 
    profiles = profiles.read().decode()
    profiles = profiles.replace('"', '').replace('\r', '').split('\n')
    
    # Extract key-val pairs
    profiles = {i.split(':', maxsplit=1)[0] : i.split(':', maxsplit=1)[1].strip() for i in profiles if re.findall(':', i)}

# App logo
st.markdown(f'''**❄ SNWLNK ❄**''')

# App page
col1, col2, col3 = st.columns(3)
col2.image(PIL.Image.open("../config/profile.jpg"))

# Person Info
st.header(f'''{profiles['name']}''')

if "info" in profiles.keys():
    with st.container():
        st.markdown(f'''<p align="center"><b>{profiles['info']}</b></p>''', unsafe_allow_html=True)
        
# Links
for key in profiles.keys():
    if key not in ['name', 'info']:
        print(key, profiles[key])
        st_button(label=key, url=profiles[key])

st.markdown('---')