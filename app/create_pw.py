import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# with open('credentials.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# print(config)
# config['credentials'] = {'usernames': {'cody': {'email': 'zhi.zhou.2023@mitb.smu.edu.sg', 'name': 'Cody, Zhi Zou', 'password': '123'}}
hashed_passwords = stauth.Hasher.hash_passwords(config['credentials'])
print(hashed_passwords)