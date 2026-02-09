import streamlit as st
import requests
import random

# --- CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Pro Engine", page_icon="⚡", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1e213a 0%, #050505 100%); color: #ffffff; }
    .header-box { text-align: center; padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); border: 1px solid #d4af37; margin-bottom: 30px; }
    .main-title { font-size: 35px; font-weight: 900; color: #d4af37; }
    .rgb-container { padding: 12px; border-radius: 10px; margin-bottom: 15px; background: rgba(0, 0, 0, 0.8); border: 2px solid transparent; text-align: center; animation: rgb-border 3s linear infinite; }
    @keyframes rgb-border { 0% { border-color: red; } 50% { border-color: green; } 100% { border-color: red; } }
    .stTextInput input { color: #FF0000 !important; font-size: 24px !important; font-weight: 900 !important; text-align: center; }
    .result-card { background: rgba(0, 255, 0, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="main-title">ULTRA ENGINE PRO</p><p>Managed by: VIKAS MISHRA</p></div>', unsafe_allow_html=True)

# --- KEY ROTATION LOGIC ---
# Agar aapke paas aur keys hain toh is list mein 'key1', 'key2' karke badha sakte hain
KEYS_POOL = ["demo-testing", "anish-special", "trial-access"] 

st.markdown('<div class="rgb-container">📱 ENTER TARGET NUMBER</div>', unsafe_allow_html=True)
phone_number = st.text_input("", placeholder="10 Digit No.", max_chars=10, label_visibility="collapsed").strip()

if st.button("🚀 EXECUTE MULTI-ROUTE SEARCH"):
    if len(phone_number) == 10:
        found = False
        with st.spinner("🛰️ Routing through multiple Satellite Gateways..."):
            for current_key in KEYS_POOL:
                try:
                    url = f"https://anishexploits.site/anish-exploits/api.php?key={current_key}&num={phone_number}"
                    res = requests.get(url, timeout=15).json()
                    
                    # Agar limit exceeded nahi hai aur data mil gaya
                    if res.get("status") == "Success":
                        data = res.get("results").get("0")
                        st.balloons()
                        st.markdown(f"""
                        <div class="result-card">
                            <h3 style="color:#00FF00;">✅ DATA RESTORED (Key: {current_key})</h3>
                            <p>👤 <b>Name:</b> {data.get('name')}</p>
                            <p>👨‍🦳 <b>Father:</b> {data.get('fname')}</p>
                            <p>🏠 <b>Address:</b> {data.get('address')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        found = True
                        break # Data milte hi loop band
                    
                    elif res.get("error") == "daily_limit_exceeded":
                        st.warning(f"⚠️ Gateway {current_key} is Full. Switching...")
                        continue # Agli key try karein
                        
                except:
                    continue
            
            if not found:
                st.error("🚫 ALL GATEWAYS BUSY: Aaj ki saari trial limits khatam ho gayi hain. Kripya 24 ghante baad ya Premium Key ke saath try karein.")
    else:
        st.warning("⚠️ Sahi number daalein.")

st.markdown("<br><center>© 2026 VIKAS MISHRA PRIVATE SUITE</center>", unsafe_allow_html=True)
