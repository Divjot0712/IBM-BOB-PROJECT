import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="MindBridge AI", page_icon="🌿", layout="centered")

st.markdown("""
<style>
.main {background: linear-gradient(180deg, #f5fbfa 0%, #ffffff 70%);}
.hero {padding: 1.2rem 1.4rem; border-radius: 18px; background: #17324d; color: white; margin-bottom: 1rem;}
.hero h1 {color: white; margin-bottom: .2rem;}
.hero p {color: #dcecf0; margin-bottom: 0;}
div.stButton > button {border-radius: 12px; min-height: 2.7rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🌿 MindBridge AI</h1><p>A safe first step toward everyday mental wellness</p></div>', unsafe_allow_html=True)
st.info("This educational prototype offers general wellbeing support. It is not a therapist, diagnostic tool, or emergency service. Please avoid entering identifying or highly sensitive information.")

with st.expander("What this tool can and cannot do"):
    st.write("It can help you reflect, try a simple coping exercise, and consider a next step.")
    st.write("It cannot diagnose a condition, provide treatment, or replace qualified professional care.")

st.subheader("1. Quick check-in")
mood = st.slider("How are you feeling right now?", min_value=1, max_value=5, value=3,
                 help="1 = very difficult, 5 = feeling good")
emotion = st.selectbox("Which word best describes your mood? (optional)",
                       ["Prefer not to say", "Stressed", "Anxious", "Sad", "Lonely", "Overwhelmed", "Calm", "Hopeful", "Okay"])
if st.button("Reflect on my check-in", use_container_width=True):
    if mood <= 2:
        st.warning("Thank you for checking in. You do not have to solve everything at once. Try choosing one small, manageable next step below, and consider reaching out to someone you trust.")
    elif mood == 3:
        st.info("It is okay to have mixed feelings. A short pause may help you notice what you need right now.")
    else:
        st.success("Glad you are feeling relatively okay. You might take a moment to notice what has been helping you today.")
    if emotion not in ["Prefer not to say", "Okay", "Calm", "Hopeful"]:
        st.write(f"You selected **{emotion.lower()}**. That feeling is worth acknowledging without judging yourself.")

st.divider()
st.subheader("2. What is on your mind?")
st.caption("Share only what you are comfortable sharing. This prototype does not save your message.")
message = st.text_area("Optional message", placeholder="For example: I feel overwhelmed by upcoming exams.", max_chars=1000)

def safety_match(text):
    patterns = [
        r"\bkill myself\b", r"\bsuicid(?:e|al)\b", r"\bend my life\b",
        r"\bhurt myself\b", r"\bself[- ]harm\b", r"\bwant to die\b",
        r"\bcan't stay safe\b", r"\bcannot stay safe\b"
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)

def response_for(text):
    t = text.lower()
    if any(w in t for w in ["exam", "assignment", "deadline", "study", "college", "workload"]):
        return ("That sounds like a lot to carry. Try shrinking the task: write down everything on your mind, choose one task that takes 10 minutes, and begin only that. A short break and a realistic plan can help.")
    if any(w in t for w in ["anxious", "anxiety", "panic", "worry", "worried", "nervous"]):
        return ("Feeling anxious can be uncomfortable. If it feels okay, place both feet on the floor and slowly breathe out a little longer than you breathe in. Then name five things you can see. You can stop if this does not feel helpful.")
    if any(w in t for w in ["sad", "lonely", "alone", "empty", "down"]):
        return ("I'm sorry this feels difficult. You deserve support, and you do not have to handle everything alone. Consider sending a simple message to someone you trust, such as: “I'm having a hard day—could we talk for a few minutes?”")
    if any(w in t for w in ["angry", "frustrated", "irritated"]):
        return ("It may help to pause before responding to anything stressful. Step away briefly if you can, relax your shoulders, and write what you wish the other person understood. You can decide what to do after you feel steadier.")
    if any(w in t for w in ["tired", "burnout", "exhausted", "sleep"]):
        return ("Your body may be asking for a pause. If possible, drink some water, take a short screen break, and choose one basic need to support—food, rest, movement, or asking for help.")
    return ("Thank you for sharing. You do not need to figure everything out immediately. Try naming the feeling, noticing what you need in this moment, and choosing one small action that feels manageable. If this keeps affecting daily life, consider speaking with a qualified professional.")

if st.button("Get a supportive next step", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("You can type a little about what's on your mind, or skip to the coping tools below.")
    elif safety_match(message):
        st.error("Your safety matters. This tool cannot provide crisis care. If you may act on thoughts of harming yourself or cannot stay safe, contact local emergency services now or go to the nearest emergency department. If possible, tell a trusted person who can stay with you and help you get support. In India, you can call 112 for emergency assistance. Do not stay alone if you are in immediate danger.")
    else:
        st.markdown("**A possible next step**")
        st.write(response_for(message))
        st.caption("This is general wellbeing guidance, not medical advice. If distress is intense, persistent, or affecting daily life, please seek qualified support.")

st.divider()
st.subheader("3. Try a coping exercise")
tab1, tab2, tab3 = st.tabs(["Breathing", "Grounding", "Journaling"])
with tab1:
    st.write("Try a gentle breathing pause. Do not force your breath; stop if you feel uncomfortable.")
    st.markdown("1. Sit comfortably and relax your shoulders.\n2. Breathe in gently for about 4 seconds.\n3. Breathe out slowly for about 6 seconds.\n4. Repeat for up to one minute, at your own pace.")
with tab2:
    st.write("The 5–4–3–2–1 grounding exercise can bring attention back to the present.")
    st.markdown("• Notice **5** things you can see.\n• Notice **4** things you can feel.\n• Notice **3** things you can hear.\n• Notice **2** things you can smell.\n• Notice **1** thing you can taste, or one slow breath.")
with tab3:
    st.write("Complete one prompt privately in your own notes:")
    st.markdown("• Right now I feel…\n• One thing I can influence today is…\n• One small step I can take in the next 10 minutes is…\n• One person or service I could reach out to is…")

st.divider()
st.subheader("4. When to seek human support")
st.write("If feelings are intense, continue for a long time, or interfere with sleep, study, work, or relationships, consider speaking with a qualified mental-health professional or campus counsellor.")
st.write("If you may be in immediate danger, contact local emergency services now and reach out to a trusted person who can stay with you. In India, emergency assistance is available at **112**.")
st.caption("Prototype note: responses are rule-based and may miss context. This app does not store chat history, use a clinical model, or make a diagnosis.")
