import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names=["Rahul.N","Rajagopal.P","Venkatsakthi.R","Abishek.R"]
usernames=["rahul","raj","venkat","abishek"]
passwords=["5048","5049","5070","5301"]

hashed_passwords=stauth.Hasher(passwords).generate()
file_path=Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)
