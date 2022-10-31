# Streamlit SNWLNK app 
import src.snwlnk as app

if __name__ == "__main__":
    # Configure
    app.LoadCSS(path="css/style.css")
    app.Celebrate(active=False)
    
    # Run
    app.Run(
        profile = app.configureApp(sourcefile = "config/profile.yml"), 
        profile_pic = "config/profile.jpg")
