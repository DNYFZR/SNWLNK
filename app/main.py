# SNWLNK App Class 
import re, PIL, streamlit as st

class SNWLNK:
    '''App Class...'''
    def __init__(self, profile_path: str =  "config/profile.yml", picture_path: str | None = "config/profile.jpg"):
        self.picture = picture_path

        with open(profile_path, "rb") as profile:
            # Read in bytes object  
            self.profile = profile.read().decode()
            
            # Decode & clean / remove chars
            self.profile = self.profile.replace('"', '').replace('\r', '').split('\n')
            
            # Extract key-val pairs
            self.profile = {i.split(':', maxsplit=1)[0] : i.split(':', maxsplit=1)[1].strip() for i in self.profile if re.findall(':', i)}

    def load_css(self, path: str):
        with open(path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

        return self

    def run(self):
        # App Pic
        if self.picture == None:
            st.image(PIL.Image.open("images/default.jfif"), width=200)
        else:
            st.image(PIL.Image.open(self.picture), width=200)

        # Person Info
        st.header(f'''{self.profile['name']}''')

        if "bio" in self.profile.keys():
            with st.container():
                st.markdown(
                    f'''<p style="font-size:120%;" align="center"><b>{self.profile['bio']}</b></p>''', 
                    unsafe_allow_html=True)
                
        # Links
        for key in self.profile.keys():
            if key not in ['name', 'bio']:
                st.markdown(f'<a href={self.profile[key]}><button class="button-43" role= "button"><b>{key}</b></button></a>', unsafe_allow_html=True)
                
        # Footnotes
        st.markdown(
            f'''<p style="font-size:75%;" align="right"><b>❄ SNWLNK by DNYFZR</b></p><br/>''', 
            unsafe_allow_html=True)

        return self

if __name__ == "__main__":
    app = SNWLNK(picture_path="config/profile.jpg", profile_path="config/profile.yml")
    app.load_css(path="app/css/style.css").run()
