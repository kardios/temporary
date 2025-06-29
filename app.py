import streamlit as st
import telebot

# Set up Telegram Bot
recipient_user_id = os.environ['RECIPIENT_USER_ID']
bot_token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(bot_token)

st.write("**Readhacker** and **Sherwood Lab** have been decommissioned with effect from 30 June 2025.")
st.write("With widespread availability of AI and dynamic advancements in the AI space, it is timely to explore ways to better contextualise AI for our work. Please approach **Digital Accelerator Unit** on future capabilities.")

if st.button("Snowfall"): 
  bot.send_message(chat_id=recipient_user_id, text="Readhacker\nSnowfall")  
  st.snow()
if st.button("Balloons"): 
  bot.send_message(chat_id=recipient_user_id, text="Readhacker\nBalloons")  
  st.balloons()
