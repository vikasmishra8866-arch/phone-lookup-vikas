import streamlit as st
import requests
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Phone Lookup", page_icon="📱", layout="centered")

# --- CUSTOM CSS (Aapka Signature Style) ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1e213a 0%, #050505 100%);
        color: #ffffff;
    }
    .header-box {
        text-align: center; padding: 25px; border-radius: 20px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.4); margin-bottom: 30px;
    }
    .main-title {
        font-size: 35px; font-weight: 900; letter-spacing: 3px; color: #d4af37;
    }
    .rgb-container {
        padding: 12px; border-radius: 10px; margin-bottom: 15px;
        background: rgba(0, 0, 0, 0.8); border: 2px solid transparent;
        text-align: center; font-weight: bold; animation: rgb-border 4s linear infinite;
    }
    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; color: #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; color: #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
    }
    /* RED TEXT IN INPUT BOX */
    .stTextInput input {
        color: #FF0000 !important; font-size: 22px !important; font-weight: 900 !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid #FF0000 !important; text-align: center;
    }
    /* RESULT BOX */
    .result-card {
        background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px;
        border-left: 5px solid #d4af37; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-box">
        <p class="main-title">SATELLITE PHONE LOOKUP</p>
        <p style="color: #ffffff; font-size: 14px;">💎 Powered by API | Managed by: <span style="color: #d4af37;">VIKAS MISHRA</span></p>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN INTERFACE ---
st.markdown('<div class="rgb-container">📡 ENTER TARGET MOBILE NUMBER</div>', unsafe_allow_html=True)
phone_number = st.text_input("", placeholder="Enter 10 Digit No.", max_chars=10, label_visibility="collapsed")

if st.button("🚀 EXECUTE SEARCH ENGINE"):
    if len(phone_number) == 10 and phone_number.isdigit():
        with st.spinner("🛰️ Scanning Database via Satellite..."):
            try:
                # API Call
                API_URL = f"https://anishexploits.site/anish-exploits/api.php?key=demo-testing&num={phone_number}"
                response = requests.get(API_URL, timeout=30)
                data = response.json()

                if data.get("success") and data.get("result"):
                    res = data["result"][0]
                    st.balloons()
                    
                    st.markdown(f"""
                    <div class="result-card">
                        <h3 style="color:#d4af37;">✅ Information Found</h3>
                        <p>👤 <b>Name:</b> {res.get('name', 'N/A')}</p>
                        <p>👨‍🦳 <b>Father:</b> {res.get('father_name', 'N/A')}</p>
                        <p>🏠 <b>Address:</b> {res.get('address', 'N/A')}</p>
                        <p>📍 <b>Circle:</b> {res.get('circle', 'N/A')}</p>
                        <p>🆔 <b>ID Number:</b> {res.get('id_number', 'N/A')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ No Data Found for this number.")
            except Exception as e:
                st.error(f"📡 Connection Error: API is not responding.")
    else:
        st.warning("⚠️ Please enter a valid 10-digit number.")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
