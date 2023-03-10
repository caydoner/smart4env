from multiapp import MultiApp
from apps import yeni_konu_ekle
import yaml
from streamlit_authenticator import Authenticate
from yaml import SafeLoader
from utility import *
st.set_page_config(
    page_title="SMART4ENV",
    page_icon="????",
    layout="wide",
    initial_sidebar_state="expanded")

local_css('./style.css')


# --- USER AUTHENTICATION ---
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
#
# authenticator = Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )
#
# name, authentication_status, username = authenticator.login("Login", "main")
#
# if authentication_status == False:
#     st.error("Kullan覺c覺 Ad覺/??ifre Yanl覺??!")
#
# if authentication_status == None:
#     st.warning("L羹tfen Kullan覺c覺 Ad覺 ve ??ifre Giriniz.")
app = MultiApp()

# Add all your application here
# app.add_app("??DEV 襤ZLEME VE DE??ERLEND襤RME", izleme.app)

app.add_app("RESEARCH STAFF INFORMATION", yeni_konu_ekle.app)

app.run()

