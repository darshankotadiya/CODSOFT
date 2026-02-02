import streamlit as st
import math
import time

# --- ADVANCED UI & NEON STYLING ---
st.set_page_config(page_title="Nexus-AI | Unbeatable", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    body { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        height: 100px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        font-size: 50px !important;
        color: #00d4ff;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        border: 1px solid #00d4ff;
        box-shadow: 0 0 20px #00d4ff;
        transform: translateY(-2px);
    }
    .main-title {
        font-size: 50px;
        font-weight: bold;
        background: -webkit-linear-gradient(#00d4ff, #0055ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MINIMAX CORE LOGIC ---
def check_winner(b):
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for p in win:
        if b[p[0]] == b[p[1]] == b[p[2]] != "": return b[p[0]]
    return "Draw" if "" not in b else None

def minimax(b, depth, is_max):
    res = check_winner(b)
    if res == "X": return 10 - depth
    if res == "O": return depth - 10
    if res == "Draw": return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "X"; score = minimax(b, depth + 1, False); b[i] = ""; best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "O"; score = minimax(b, depth + 1, True); b[i] = ""; best = min(score, best)
        return best

# --- SESSION STATE ---
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.winner = None

# --- UI HEADER ---
st.markdown("<p class='main-title'>⚡ NEXUS-AI TIC-TAC-TOE</p>", unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:gray;'>Developer: Darshan Kotadiya | MSc.IT Intern</p>", unsafe_allow_html=True)

# --- GAME GRID ---
cols = st.columns([1, 1, 1])
for i in range(9):
    with cols[i % 3]:
        val = st.session_state.board[i]
        if val == "" and st.session_state.winner is None:
            if st.button(" ", key=f"btn_{i}"):
                st.session_state.board[i] = "O"
                st.session_state.winner = check_winner(st.session_state.board)
                if st.session_state.winner is None:
                    # AI Move
                    best_s = -math.inf; move = -1
                    for j in range(9):
                        if st.session_state.board[j] == "":
                            st.session_state.board[j] = "X"; s = minimax(st.session_state.board, 0, False); st.session_state.board[j] = ""
                            if s > best_s: best_s = s; move = j
                    if move != -1: st.session_state.board[move] = "X"
                    st.session_state.winner = check_winner(st.session_state.board)
                st.rerun()
        else:
            # Styled X and O
            color = "#ff007f" if val == "X" else "#00d4ff"
            st.markdown(f"<button disabled style='width:100%; height:100px; border-radius:15px; border:1px solid {color}; background:none; color:{color}; font-size:40px; font-weight:bold;'>{val}</button>", unsafe_allow_html=True)

# --- WINNER CELEBRATION ---
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a Draw!")
    elif st.session_state.winner == "X":
        st.error("🤖 AI Wins! Hard luck, Darshan.")
    else:
        st.balloons()
        st.success("🎉 Incredible! You beat the AI!")
    
    if st.button("🔄 Play Again"):
        st.session_state.board = [""] * 9
        st.session_state.winner = None
        st.rerun()
