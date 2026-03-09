import streamlit as st
from textblob import TextBlob

st.title("AI Sentiment Analyzer")
st.write("Enter a sentence and the AI will analyze whether the sentiment is positive, negative, or neutral.")
text = st.text_input("Enter a sentence")

if text:
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    st.write("### Sentiment Score:", score)

    if score > 0:
        st.success("Positive Sentiment 😊")
        st.write("The sentence expresses a positive feeling.")
        
    elif score < 0:
        st.error("Negative Sentiment 😞")
        st.write("The sentence expresses a negative feeling.")
        
    else:
        st.info("Neutral Sentiment 😐")
        st.write("The sentence has a neutral tone.")