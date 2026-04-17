import streamlit as st
from groq import Groq
import uuid
import re

# ---------------- CONFIG ----------------
st.set_page_config(page_title="NEXORA", page_icon="🤖", layout="centered")

# ---------------- VALIDACIÓN EMOJIS ----------------
def is_emoji_only(text):
    emoji_pattern = re.compile(
        "[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F1E0-\U0001F1FF]+"
    )
    return bool(emoji_pattern.fullmatch(text.strip()))

# ---------------- CLIENTE ----------------
@st.cache_resource
def get_client():
    return Groq(api_key=st.secrets["CLAVE_API"])

client = get_client()

MODEL = "llama-3.3-70b-versatile"

# ---------------- ESTADO ----------------
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_avatar" not in st.session_state:
    st.session_state.user_avatar = "✨"

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    cid = str(uuid.uuid4())
    st.session_state.current_chat = cid
    st.session_state.chats[cid] = {
        "title": "Nuevo chat",
        "messages": []
    }

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 800

if "editing_chat" not in st.session_state:
    st.session_state.editing_chat = None

# ---------------- HELPERS ----------------
def messages():
    return st.session_state.chats[st.session_state.current_chat]["messages"]

def save(role, content, avatar):
    messages().append({
        "role": role,
        "content": content,
        "avatar": avatar
    })

def build_messages():
    system = {
        "role": "system",
        "content": (
            "Respondé en español neutro. "
            f"El usuario se llama {st.session_state.user_name or 'usuario'}. "
            "Sé claro y natural."
        )
    }

    return [system] + [
        {"role": m["role"], "content": m["content"]}
        for m in messages()
    ]

def responder(msgs):
    return client.chat.completions.create(
        model=MODEL,
        messages=msgs,
        stream=True,
        temperature=st.session_state.temperature,
        max_tokens=st.session_state.max_tokens
    )

# ---------------- SIDEBAR: USUARIO ----------------
st.sidebar.title("👤 Perfil")

st.session_state.user_name = st.sidebar.text_input(
    "Tu nombre",
    value=st.session_state.user_name
)

emoji_input = st.sidebar.text_input(
    "Emoji de usuario (solo emojis)",
    value=st.session_state.user_avatar
)

if emoji_input:
    if is_emoji_only(emoji_input):
        st.session_state.user_avatar = emoji_input
    else:
        st.sidebar.warning("Solo podés usar emojis 🙂")

st.sidebar.markdown("---")

# ---------------- SIDEBAR: CHATS ----------------
st.sidebar.title("💬 Chats")

if st.sidebar.button("➕ Nuevo chat"):
    cid = str(uuid.uuid4())
    st.session_state.chats[cid] = {
        "title": "Nuevo chat",
        "messages": []
    }
    st.session_state.current_chat = cid
    st.rerun()

for cid, chat in st.session_state.chats.items():

    col1, col2 = st.sidebar.columns([4, 1])

    with col1:
        if st.button(chat["title"][:18], key=f"open_{cid}"):
            st.session_state.current_chat = cid
            st.rerun()

    with col2:
        if st.button("✏️", key=f"edit_{cid}"):
            st.session_state.editing_chat = cid

if st.session_state.editing_chat:
    cid = st.session_state.editing_chat

    new_name = st.sidebar.text_input(
        "Nuevo nombre del chat",
        value=st.session_state.chats[cid]["title"],
        key="rename_chat"
    )

    if st.sidebar.button("Guardar nombre"):
        st.session_state.chats[cid]["title"] = new_name
        st.session_state.editing_chat = None
        st.rerun()

st.sidebar.markdown("---")

st.sidebar.title("⚙️ Ajustes")

st.session_state.temperature = st.sidebar.slider(
    "Creatividad",
    0.0,
    1.5,
    value=float(st.session_state.temperature),
    step=0.1
)

st.session_state.max_tokens = st.sidebar.slider(
    "Longitud",
    128,
    1500,
    value=int(st.session_state.max_tokens),
    step=64
)

# ---------------- HEADER NEXORA ----------------
st.title("🤖 NEXORA")

st.markdown("### Hola soy **NEXORA**, tu asistente virtual 👋")

# ---------------- CHAT RENDER ----------------
for m in messages():
    with st.chat_message(m["role"], avatar=m.get("avatar")):
        st.markdown(m["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Escribí un mensaje...")

if user_input:

    avatar = st.session_state.user_avatar or "✨"

    save("user", user_input, avatar)

    with st.chat_message("user", avatar=avatar):
        st.markdown(user_input)

    msgs = build_messages()

    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        full = ""

        stream = responder(msgs)

        for chunk in stream:
            if chunk.choices[0].delta.content:
                full += chunk.choices[0].delta.content
                placeholder.markdown(full + "▌")

        placeholder.markdown(full)

    save("assistant", full, "🤖")