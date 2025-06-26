import sys

sys.path.append(r"C:\Users\user21\Desktop\임숙자 교수님\output")

from pathlib import Path

import streamlit as st

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_3 import read_text_and_draw_line, read_text_from_image
from liv_helper import translate_libre

st.title("✌ 인식률 체크 문자 인식 웹 앱")  # 웹 앱 제목

uploaded = st.file_uploader("인식할 이미지를 선택하세요.")
if uploaded is not None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    tmp_path = OUT_DIR / f"{Path(uploaded.name).stem}.jpg"  # 확장자 jpg로 저장
    tmp_path.write_bytes(uploaded.getvalue())

    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("원본 이미지")
        st.image(tmp_path.as_posix())

    with col_right:
        st.subheader("문자 인식 결과")
        with st.spinner(text="문자를 인식하는 중입니다..."):
            result_img_path = read_text_and_draw_line(tmp_path)
        st.image(result_img_path.as_posix())
  # 결과 이미지 출력

    st.subheader("📝 인식된 텍스트 및 번역 결과")
    with st.spinner("텍스트를 번역하는 중입니다..."):
        texts = read_text_from_image(tmp_path)
        if texts:
            full_text = " ".join(texts)  # 모든 인식된 텍스트를 공백으로 합침
            translated = translate_libre(full_text, source="en", target="ko")
            st.markdown(f"🔹 {full_text}<br/>➡️ {translated}", unsafe_allow_html=True)
        else:
            st.info("문자를 인식하지 못했습니다.")

            import sys
sys.path.append(r"C:\Users\user21\Desktop\임숙자 교수님\output")

