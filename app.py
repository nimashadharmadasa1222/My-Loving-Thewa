import streamlit as st

# Set up the page title and configuration
st.set_page_config(page_title="A Special Question For You", page_icon="❤️", layout="centered")

# 1. BACKGROUND MUSIC (Plays automatically in the background)
# Using a copyright-free romantic lo-fi track URL
music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.markdown(f"""
    <iframe src="{music_url}" allow="autoplay" style="display:none" id="iframeAudio"></iframe>
    <audio autoplay loop volume="0.5">
        <source src="{music_url}" type="audio/mp3">
    </audio>
""", unsafe_allow_html=True)

# 2. CUSTOM COLORS & STYLING (Pastel Pink & Rose Gold Theme)
st.markdown("""
    <style>
    /* Background color of the whole page */
    .stApp {
        background-color: #FFF0F5; /* Lavender Blush / Pastel Pink */
    }

    /* Main Question Text */
    .title-text {
        font-size: 42px;
        font-weight: 700;
        color: #B03060; /* Deep Rose */
        text-align: center;
        margin-bottom: 35px;
        font-family: 'Georgia', serif;
    }

    /* The Romantic Letter Box */
    .message-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #FFB6C1; /* Light Pink Border */
        box-shadow: 0px 4px 15px rgba(255, 182, 193, 0.4);
        font-size: 18px;
        color: #4A4A4A;
        line-height: 1.6;
        font-family: 'Georgia', serif;
    }

    /* Customizing the buttons to look prettier */
    div.stButton > button {
        background-color: #FFB6C1 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #FF69B4 !important; /* Hot Pink on hover */
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session states
if 'clicked_no' not in st.session_state:
    st.session_state.clicked_no = False
if 'clicked_yes' not in st.session_state:
    st.session_state.clicked_yes = False

# Main Header
st.markdown("<div class='title-text'>Do you love me? ❤️</div>", unsafe_allow_html=True)

# Layout columns for Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 💖", use_container_width=True):
        st.session_state.clicked_yes = True
        st.session_state.clicked_no = False

with col2:
    if st.button("No 💔", use_container_width=True):
        st.session_state.clicked_no = True

# If he clicks "No"
if st.session_state.clicked_no and not st.session_state.clicked_yes:
    st.error("❌ Your answer is incorrect. Access denied! Please try again 😉")

# If he clicks "Yes"
if st.session_state.clicked_yes:
    st.balloons()  # Throws balloons on screen

    # 50/50 split layout for Flowers and Letter
    display_col1, display_col2 = st.columns([1, 1.2])

    with display_col1:
        # Giant bouquet emoji arrangement
        st.markdown("<h1 style='text-align: center; font-size: 110px; margin-top: 20px;'>💐✨🌹</h1>",
                    unsafe_allow_html=True)
        st.success("Correct answer! 🥰")

    with display_col2:
        # 3. EDIT YOUR MESSAGE HERE 👇
        st.markdown("""
        <div class='message-box'>
            <b style='color: #B03060; font-size: 22px;'>ආදරණීය Thewa වෙත,</b><br><br>
            මම දන්නවා ඔයා හරි Answer එක තමයි දෙන්න‍ෙ කියලා ❤️ <br>
            ඉතින් මග‍ෙ රත්තරන් මම මේක ලියන්නේ ගොඩක් පාළුවෙන්.
            මගෙ හිතට ගොඩාක් දේවල් දැනෙනවා. දේවල් මේ වෙලාවේ ඔයාට කියන්න
            පුළුවන් උනා නම්... ඒත් ඔයා වැඩ නේ. මට ඉතින් කරදර කරන්න බෑනෙ.
            මගෙ හිතට හරි බයයි. මට ඔයාව ඕනි. ලගට දුවගෙන ඇවිත් බදාගෙන තුරුලු කරන් අඩන්න හිතෙනවා.
            Mn dnnw oy mt godak adarei kiyala. Math ehemai. Mn hamadama api denna inn lassana
            future ekkata heena mawanawa. මැරෙනකල් ඔයත් එක්ක ආදරෙන් ඉන්න ❤️
            ඔයාව මගෙ﻿ ජීවිතේට ගොඩාක් වටිනවා 
            ඔයා වෙනුවෙන්මයි මම මේක හැදුවේ
            I love you. 🌙❤️✨
                                 01/07/2026
        </div>
        """, unsafe_allow_html=True)
