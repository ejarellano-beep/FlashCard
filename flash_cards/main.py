import streamlit as st
from deck import Deck



if 'flashcard_deck' not in st.session_state:
    st.session_state.flashcard_deck = Deck('flashcards.csv')
    st.session_state.is_flipped = False

deck=st.session_state.flashcard_deck

st.title('⚡️Flashcard Forge')
card=deck.current_card()
if st.session_state.is_flipped:
    st.info(f'**Answer:**{card.answer}')
else:
    st.warning(f'**Question:**{card.question}')

col1, col2, col3 = st.columns(3)
if col1.button('Shuffle'):
    deck.shuffle()
    st.rerun()

if col2.button('Next'):
    deck.next_card()
    st.session_state.is_flipped = False
    st.rerun()

if col3.button('Flip'):
    st.session_state.is_flipped = not st.session_state.is_flipped
    st.rerun()