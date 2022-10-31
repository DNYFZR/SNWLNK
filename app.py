# Streamlit SNWLNK app 
import src.snwlnk as app

if __name__ == "__main__":
    # Configure
    app.LoadCSS(path="css/style.css")
    app.Celebrate(active=True)
    
    # Run
    app.App(
        profile = app.configureApp(),
        profile_pic = "config/profile.jpg")
