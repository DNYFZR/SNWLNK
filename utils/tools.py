import streamlit as st

def load_css(path: str):
    with open(path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


def st_button(label, url):
    
    if url == None:
        button_code = f'''
    <p>
        <a class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="false"><b>{label}</b></a>
    </p>'''
    
    else:
        button_code = f'''
        <p>
           <a 
                href={url} 
                class="btn btn-outline-primary btn-lg btn-block" 
                type="button" 
                width=50%
                aria-pressed="true">
                <b>{label}</b>
            </a></p>'''
    
    return st.markdown(button_code, unsafe_allow_html=True)