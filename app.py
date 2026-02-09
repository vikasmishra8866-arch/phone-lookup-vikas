import streamlit as st
import requests
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Multi-Route Lookup", page_icon="🌐", layout="centered")

# --- CUSTOM CSS (Vikas Signature Style) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1e213a 0%, #050505 100%); color: #ffffff; }
    .header-box { text-align: center; padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.4); margin-bottom: 30px; }
    .main-title { font-size: 35px; font-weight: 900; letter-spacing: 3px; color: #d4af37; }
    .rgb-container { padding: 12px; border-radius: 10px; margin-bottom: 15px; background: rgba(0, 0, 0, 0.8); border: 2px solid transparent; text-align: center; font-weight: bold; animation: rgb-border 4s linear infinite; }
    @keyframes rgb-border { 0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; } 33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; } 66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; } 100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; } }
    .stTextInput input { color: #FF0000 !important; font-size: 24px !important; font-weight: 900 !important; background-color: rgba(255, 255, 255, 0.1) !important; border: 2px solid #FF0000 !important; text-align: center; }
    .result-card { background: rgba(0, 255, 0, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #00FF00; margin-top: 20px; }
    .vpn-status { font-size: 12px; color: #00ff00; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header-box"><p class="main-title">ULTRA LOOKUP (VPN BYPASS)</p><p style="color: #ffffff; font-size: 14px;">Secure Routing Enabled | Managed by: <span style="color: #d4af37; font-weight:bold;">VIKAS MISHRA</span></p></div>', unsafe_allow_html=True)

# --- VPN / PROXY LOGIC ---
# Ye list requests ko alag-alag virtual origins se dikhayegi
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
]

# --- UI ---
with st.expander("🛠️ ADVANCED SETTINGS"):
    custom_key = st.text_input("ENTER API KEY:", value="demo-testing", type="password")
    use_vpn = st.checkbox("Enable Virtual IP Routing (Bypass Limit)", value=True)

st.markdown('<div class="rgb-container">📱 TARGET MOBILE NUMBER</div>', unsafe_allow_html=True)
phone_number = st.text_input("", placeholder="Enter 10 Digit No.", max_chars=10, key="phone_input", label_visibility="collapsed").strip()

if st.button("🚀 EXECUTE SEARCH"):
    if len(phone_number) == 10 and phone_number.isdigit():
        if use_vpn:
            st.markdown('<div class="vpn-status">🛡️ VPN Tunnel Active: Routing through Virtual Gateway...</div>', unsafe_allow_html=True)
        
        with st.spinner("🛰️ Searching..."):
            try:
                # Header rotation to mimic different devices (VPN-like behavior)
                headers = {'User-Agent': random.choice(USER_AGENTS)}
                
                API_URL = f"https://anishexploits.site/anish-exploits/api.php?key={custom_key}&num={phone_number}"
                
                # API Call with fake headers
                response = requests.get(API_URL, headers=headers, timeout=20)
                data = response.json()

                if data.get("error") == "daily_limit_exceeded":
                    st.error("🚫 IP/KEY LIMIT: Server ne block kiya hai. VPN switch karein ya Premium Key use karein.")
                    st.info("💡 Tip: Agar aap Phone par hain, toh Airplane Mode On-Off karke try karein, IP change ho jayegi.")
                
                elif data.get("status") == "Success" and data.get("results"):
                    res = data.get("results").get("0")
                    st.balloons()
                    st.markdown(f"""
                    <div class="result-card">
                        <h3 style="color:#00FF00;">✅ DATA FOUND</h3>
                        <p>👤 <b>Name:</b> {res.get('name', 'N/A')}</p>
                        <p>👨‍🦳 <b>Father:</b> {res.get('fname', 'N/A')}</p>
                        <p>🏠 <b>Address:</b> {res.get('address', 'N/A')}</p>
                        <p>🆔 <b>ID:</b> {res.get('id', 'N/A')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ No Information Found.")

            except Exception as e:
                st.error(f"📡 Connection Error: {e}")
    else:
        st.warning("⚠️ Enter a valid 10-digit number.")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
