import streamlit as st
from utils import threat_identification,threat_classification,threat_notifications
import json
import time
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()
if st.session_state.get('authentication_status'):
    authenticator.logout()
    # Create a title for the web app
    st.title('BankGuard API Demo')

    # Form
    with st.form(key='my_form'):
        hist_ave_spending_per_month = st.number_input('Historical Avg Spending per Month (SGD)')
        hist_avg_txn = st.number_input('Historical Avg Per Txn Amt (SGD) ')
        txn_amt = st.number_input('Txn Amount (SGD) ')
        timestamp = st.time_input('Txn Timestamp')
        oversea_payment = st.toggle('Overseas Payment?')
        ip_address = st.text_input('Label IP Address',value='192.168.1.254')
        ip_country = st.text_input('IP Address Country')
        outdated = st.toggle('Browser/ OS Outdated?')

        submit_button = st.form_submit_button(label='Submit')            

    # When the form is submitted
    if submit_button:
        time.sleep(3)
        form_data = {'Historical Avg Spending per Month (SGD)':hist_ave_spending_per_month,
        'Historical Avg Per Txn Amt (SGD) ':hist_avg_txn,
        'Txn Amount (SGD) ':txn_amt,
        'Txn Timestamp':timestamp.strftime('%H%M'),
        'Overseas Payment?':oversea_payment,
        'Label IP Address':ip_address,
        'IP Address Country':ip_country,
        'Browser/ OS Outdated?':outdated}
        # f'Data {form_data}')

        form_data = json.dumps(form_data)
        print(form_data)

        is_threat = threat_identification(form_data)
        if is_threat:
            threat_cate, threat_level = threat_classification(form_data,is_threat)
        else:
            threat_cate = threat_level = None
        st.write(f'is_threat: {is_threat}')
        st.write(f'threat_cate: {threat_cate}')
        st.write(f'threat_level: {threat_level}')

elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')

