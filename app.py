import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Pro Lookup", page_icon="🔑", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1e213a 0%, #050505 100%); color: #ffffff; }
    .header-box { text-align: center; padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.4); margin-bottom: 30px; }
    .main-title { font-size: 35px; font-weight: 900; letter-spacing: 3px; color: #d4af37; }
    .rgb-container { padding: 12px; border-radius: 10px; margin-bottom: 15px; background: rgba(0, 0, 0, 0.8); border: 2px solid transparent; text-align: center; font-weight: bold; animation: rgb-border 4s linear infinite; }
    @keyframes rgb-border { 0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; } 33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; } 66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; } 100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; } }
    
    /* INPUT BOX RED STYLE */
    .stTextInput input { color: #FF0000 !important; font-size: 24px !important; font-weight: 900 !important; background-color: rgba(255, 255, 255, 0.1) !important; border: 2px solid #FF0000 !important; text-align: center; }
    
    .result-card { background: rgba(0, 255, 0, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #00FF00; margin-top: 20px; }
    
    /* ADMIN SECTION STYLE */
    .admin-box { background: rgba(212, 175, 55, 0.1); padding: 10px; border-radius: 10px; border: 1px dashed #d4af37; margin-bottom: 20px; }

    /* 🔥 PINK BUTTON STYLE 🔥 */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #FF1493 0%, #FF69B4 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 20px !important;
        border-radius: 12px !important;
        padding: 10px 0 !important;
        width: 100% !important;
        box-shadow: 0 0 15px rgba(255, 20, 147, 0.6) !important;
        text-transform: uppercase;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 25px rgba(255, 20, 147, 0.9) !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header-box"><p class="main-title">ULTRA LOOKUP PRO</p><p style="color: #ffffff; font-size: 14px;">Managed by: <span style="color: #d4af37; font-weight:bold;">VIKAS MISHRA</span></p></div>', unsafe_allow_html=True)

# --- ADMIN SETTINGS (EXPAND LIMIT) ---
with st.expander("🛠️ ADMIN: EXPAND SEARCH LIMIT"):
    st.markdown('<div class="admin-box">Yahan apni Premium API Key daalein</div>', unsafe_allow_html=True)
    custom_key = st.text_input("ENTER API KEY:", value="demo-testing", type="password")

# --- UI ---
st.markdown('<div class="rgb-container">⚙️ SCANNING MODE</div>', unsafe_allow_html=True)
mode = st.radio("", ["Standard Lookup", "Advanced API Debug"], horizontal=True, label_visibility="collapsed")

st.markdown('<div class="rgb-container">📱 TARGET MOBILE NUMBER</div>', unsafe_allow_html=True)
phone_number = st.text_input("", placeholder="Enter 10 Digit No.", max_chars=10, key="phone_input", label_visibility="collapsed").strip()

if st.button("🚀 EXECUTE SEARCH ENGINE"):
    if len(phone_number) == 10 and phone_number.isdigit():
        with st.spinner("🛰️ Scanning Database..."):
            try:
                # Using Custom Key from Admin Box
                API_URL = f"https://anishexploits.site/anish-exploits/api.php?key={custom_key}&num={phone_number}"
                response = requests.get(API_URL, timeout=20)
                data = response.json()

                # CHECK LIMIT ERROR
                if data.get("error") == "daily_limit_exceeded":
                    st.error("🚫 API LIMIT REACHED: Aapki 'demo-testing' key ki limit khatam ho gayi hai. Kripya Admin panel mein Premium Key daalein.")
                
                elif data.get("status") == "Success" and data.get("results"):
                    res = data.get("results").get("0")
                    st.balloons()
                    st.markdown(f"""
                    <div class="result-card">
                        <h3 style="color:#00FF00;">✅ DATA FOUND</h3>
                        <p>👤 <b>Name:</b> {res.get('name', 'N/A')}</p>
                        <p>👨‍🦳 <b>Father:</b> {res.get('fname', 'N/A')}</p>
                        <p>🏠 <b>Address:</b> {res.get('address', 'N/A')}</p>
                        <p>📍 <b>Circle:</b> {res.get('circle', 'N/A')}</p>
                        <p>🆔 <b>ID:</b> {res.get('id', 'N/A')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ No Information Found.")

                if mode == "Advanced API Debug":
                    st.info("🔍 Technical Debug Info:")
                    st.json(data)

            except Exception as e:
                st.error(f"📡 API Error: {e}")
    else:
        st.warning("⚠️ Enter a valid 10-digit number.")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
