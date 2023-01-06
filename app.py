from multiapp import MultiApp
from apps import yeni_konu_ekle
import yaml
from streamlit_authenticator import Authenticate
from yaml import SafeLoader
from utility import *
st.set_page_config(
    page_title="SMART4ENV",
    page_icon="🧊",
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
#     st.error("Kullanıcı Adı/Şifre Yanlış!")
#
# if authentication_status == None:
#     st.warning("Lütfen Kullanıcı Adı ve Şifre Giriniz.")
app = MultiApp()

# Add all your application here
# app.add_app("ÖDEV İZLEME VE DEĞERLENDİRME", izleme.app)

app.add_app("RESEARCH STAFF INFORMATION", yeni_konu_ekle.app)

app.run()

