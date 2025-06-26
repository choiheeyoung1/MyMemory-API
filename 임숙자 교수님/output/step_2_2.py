from pathlib import Path
import streamlit as st
import pytesseract
from PIL import Image

from step_2_1 import (
    chat_message_llm,
    chat_message_user,
    init_session_state,
)

# 기타 상수 및 경로
WORK_DIR = Path(__file__).parent
OUT_2_2 = WORK_DIR / "step_2_2.xlsx"

# ✅ 여기에 read_text 함수 추가
def read_text(image_path):
    """이미지에서 텍스트를 추출합니다."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="kor+eng")
    return text

# Streamlit 앱 실행 부분
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("🤖 만들면서 배우는 챗봇")

    init_session_state(dict(gemma=[], llama=[]))
    gemma = st.session_state["gemma"]
    llama = st.session_state["llama"]

    for msg_gemma, msg_llama in zip(gemma, llama):
        if msg_gemma["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg_gemma["content"])
        else:
            col_gemma, col_llama = st.columns(2)
            with col_gemma:
                with st.chat_message("Gemma"):
                    st.markdown(msg_gemma["content"])
            with col_llama:
                with st.chat_message("Llama"):
                    st.markdown(msg_llama["content"])

    if prompt := st.chat_input("여기에 대화를 입력하세요!"):
        msg_user = chat_message_user(prompt)
        gemma.append(msg_user)
        llama.append(msg_user)

        col_gemma, col_llama = st.columns(2)
        with col_gemma:
            msg_gemma = chat_message_llm("Gemma", "gemma2:9b", gemma)
            gemma.append(msg_gemma)

        with col_llama:
            msg_llama = chat_message_llm("Llama", "llama3.1:8b", llama)
            llama.append(msg_llama)


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
