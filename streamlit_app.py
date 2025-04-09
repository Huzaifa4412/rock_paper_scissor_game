import streamlit as st
import random

# Function to check game result
def game_condition(user_choose, bot_choose):
    if user_choose == bot_choose:
        return "Draw"
    elif (user_choose == "Rock" and bot_choose == "Scissor") or \
         (user_choose == "Paper" and bot_choose == "Rock") or \
         (user_choose == "Scissor" and bot_choose == "Paper"):
        return "User"
    else:
        return "Bot"

# Streamlit GUI
st.title("🎯 Rock 🥌, Paper 📄, Scissor ✂ Game")
st.markdown("Welcome to the Rock, Paper, Scissors game with **CyberCoder**!")

# Initialize session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.bot_score = 0
    st.session_state.round = 1
    st.session_state.game = 1
    st.session_state.total_games = 0
    st.session_state.name = ""
    st.session_state.started = False

# Input: Name and Rounds
if not st.session_state.started:
    st.session_state.name = st.text_input("📛 Enter your name:")
    rounds = st.number_input("🔁 How many rounds? (Each round has 3 games)", min_value=1, step=1)

    if st.button("Start Game"):
        st.session_state.total_games = rounds * 3
        st.session_state.started = True
        st.success(f"Nice to meet you {st.session_state.name}! Let's play {rounds} rounds!")
# Game interface
if st.session_state.started and st.session_state.total_games > 0:
    st.markdown(f"### Round {st.session_state.round} - Game {st.session_state.game}")
    st.markdown("#### Select your weapon:")
    col1, col2, col3 = st.columns(3)
    user_choice = None

    with col1:
        if st.button("🥌 Rock"):
            user_choice = "Rock"
    with col2:
        if st.button("📄 Paper"):
            user_choice = "Paper"
    with col3:
        if st.button("✂ Scissor"):
            user_choice = "Scissor"

    if user_choice:
        bot_choice = random.choice(["Rock", "Paper", "Scissor"])
        result = game_condition(user_choice, bot_choice)

        st.info(f"You selected: **{user_choice}**")
        st.info(f"CyberCoder selected: **{bot_choice}**")

        if result == "User":
            st.success("🏆 You win this game!")
            st.session_state.user_score += 1
        elif result == "Bot":
            st.error("🤖 CyberCoder wins this game!")
            st.session_state.bot_score += 1
        else:
            st.warning("😄 It's a draw!")

        st.session_state.total_games -= 1
        if st.session_state.game == 3:
            st.session_state.round += 1
            st.session_state.game = 1
        else:
            st.session_state.game += 1

        st.markdown(f"**Scores**: {st.session_state.name} - {st.session_state.user_score} | CyberCoder - {st.session_state.bot_score}")
        st.markdown(f"🎮 Games Left: {st.session_state.total_games}")
# FInal Results
if st.session_state.total_games == 0 and st.session_state.started:
    st.markdown("---")
    st.subheader("🎊 Final Results 🎊")
    if st.session_state.user_score > st.session_state.bot_score:
        st.success(f"{st.session_state.name} won with score {st.session_state.user_score} to {st.session_state.bot_score}")
    elif st.session_state.bot_score > st.session_state.user_score:
        st.error(f"CyberCoder won with score {st.session_state.bot_score} to {st.session_state.user_score}")
    else:
        st.warning(f"It's a tie! Both scored {st.session_state.user_score}")

    if st.button("🔁 Play Again"):
        for key in st.session_state.keys():
            del st.session_state[key]
