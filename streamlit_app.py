import streamlit as st
import random
import time

# Set page configuration
st.set_page_config(
    page_title="Rock Paper Scissors Game",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4287f5;
        text-align: center;
    }
    .game-area {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .result-win {
        color: #28a745;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .result-lose {
        color: #dc3545;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .result-draw {
        color: #ffc107;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .score-display {
        font-size: 1.2rem;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

def users_selection(keyword):
    if keyword.lower() == "rock":
        return "Rock"
    elif keyword.lower() == "scissor" or keyword.lower() == "scissors":
        return "Scissor"
    elif keyword.lower() == "paper":
        return "Paper"
    else:
        return None

def game_condition(user_choose, name, user_score, bot_score):
    words = ["Rock", "Paper", "Scissor"]
    bot_choose = random.choice(words)
    
    result_text = ""
    result_class = ""
    
    if user_choose.lower() == "rock" and bot_choose.lower() == "scissor" or \
       user_choose.lower() == "paper" and bot_choose.lower() == "rock" or \
       user_choose.lower() == "scissor" and bot_choose.lower() == "paper":
        result_text = "You Win 🏆"
        result_class = "result-win"
        user_score += 1
    elif user_choose.lower() == bot_choose.lower():
        result_text = "It's a DRAW 😄"
        result_class = "result-draw"
    else:
        result_text = "You Lose 🤓"
        result_class = "result-lose"
        bot_score += 1
    
    return bot_choose, result_text, result_class, bot_score, user_score

def main():
    # Display header
    st.markdown("<h1 class='main-header'>Rock (🥌), Paper(📄), Scissor(✂) Game 🎯</h1>", unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
    if 'bot_score' not in st.session_state:
        st.session_state.bot_score = 0
    if 'game_count' not in st.session_state:
        st.session_state.game_count = 0
    if 'total_games' not in st.session_state:
        st.session_state.total_games = 0
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'game_history' not in st.session_state:
        st.session_state.game_history = []
    
    # Game setup section
    if not st.session_state.game_started:
        with st.container():
            st.subheader("Game Setup")
            user_name = st.text_input("Enter your name:", key="name_input")
            rounds = st.number_input("Number of rounds (each round has 3 games):", min_value=1, max_value=10, value=1, step=1)
            
            if st.button("Start Game"):
                if user_name:
                    st.session_state.user_name = user_name
                    st.session_state.total_games = rounds * 3
                    st.session_state.game_started = True
                    st.session_state.user_score = 0
                    st.session_state.bot_score = 0
                    st.session_state.game_count = 0
                    st.session_state.game_history = []
                    st.rerun()
                else:
                    st.error("Please enter your name to start the game.")
    
    # Game play section
    else:
        # Display game progress
        games_left = st.session_state.total_games - st.session_state.game_count
        current_round = (st.session_state.game_count // 3) + 1
        current_game = (st.session_state.game_count % 3) + 1
        
        st.subheader(f"Round {current_round}, Game {current_game}")
        st.progress(st.session_state.game_count / st.session_state.total_games)
        st.write(f"Games left: {games_left}")
        
        # Game area
        with st.container():
            st.markdown("<div class='game-area'>", unsafe_allow_html=True)
            st.subheader("Select your weapon:")
            
            # Create a row of buttons for weapon selection
            col1, col2, col3 = st.columns(3)
            
            with col1:
                rock_btn = st.button("Rock 🥌", use_container_width=True)
            with col2:
                paper_btn = st.button("Paper 📄", use_container_width=True)
            with col3:
                scissor_btn = st.button("Scissor ✂️", use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Process the game when a weapon is selected
            if rock_btn or paper_btn or scissor_btn:
                user_choice = "Rock" if rock_btn else "Paper" if paper_btn else "Scissor"
                
                # Show user's selection
                st.write(f"You selected: {user_choice}")
                
                # Get game result
                bot_choice, result_text, result_class, new_bot_score, new_user_score = game_condition(
                    user_choice, 
                    st.session_state.user_name, 
                    st.session_state.user_score, 
                    st.session_state.bot_score
                )
                
                # Update scores
                st.session_state.bot_score = new_bot_score
                st.session_state.user_score = new_user_score
                st.session_state.game_count += 1
                
                # Display result
                st.markdown(f"<div class='{result_class}'>{result_text}</div>", unsafe_allow_html=True)
                st.write(f"Bot chose: {bot_choice}")
                
                # Add to game history
                st.session_state.game_history.append({
                    "round": current_round,
                    "game": current_game,
                    "user_choice": user_choice,
                    "bot_choice": bot_choice,
                    "result": result_text
                })
                
                # Check if game is over
                if st.session_state.game_count >= st.session_state.total_games:
                    st.balloons()
                
                # Force a rerun to update the UI
                time.sleep(1)
                st.rerun()
        
        # Display current scores
        st.markdown("<div class='score-display'>", unsafe_allow_html=True)
        st.subheader("Current Score:")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=f"{st.session_state.user_name}", value=st.session_state.user_score)
        with col2:
            st.metric(label="CyberCoder", value=st.session_state.bot_score)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Game history
        with st.expander("Game History"):
            for i, game in enumerate(st.session_state.game_history):
                st.write(f"Round {game['round']}, Game {game['game']}: " +
                         f"You chose {game['user_choice']}, Bot chose {game['bot_choice']} - {game['result']}")
        
        # Final results when all games are played
        if st.session_state.game_count >= st.session_state.total_games:
            st.markdown("<h2>🎮 FINAL RESULTS 🎮</h2>", unsafe_allow_html=True)
            
            if st.session_state.user_score > st.session_state.bot_score:
                st.markdown(f"<div class='result-win'>{st.session_state.user_name} Won 🎉 with a score of {st.session_state.user_score} to {st.session_state.bot_score}</div>", unsafe_allow_html=True)
            elif st.session_state.bot_score > st.session_state.user_score:
                st.markdown(f"<div class='result-lose'>Cyber Coder Won 🎉 with a score of {st.session_state.bot_score} to {st.session_state.user_score}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='result-draw'>It's a tie! Both players scored {st.session_state.user_score} points</div>", unsafe_allow_html=True)
            
            if st.button("Play Again"):
                st.session_state.game_started = False
                st.rerun()

if __name__ == "__main__":
    main()