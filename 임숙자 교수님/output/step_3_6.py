import streamlit as st
import pandas as pd
from pathlib import Path

OUT_DIR = Path(__file__).parent / "output"
file_stem = "step_3_5"  # CSV 생성한 파일 이름을 정확히 넣어야 해요
csv_path = OUT_DIR / f"{file_stem}.csv"

st.title("ECOS 데이터 CSV 보기")

if csv_path.exists():
    df = pd.read_csv(csv_path)
    st.dataframe(df)
else:
    st.write("CSV 파일이 존재하지 않습니다.")
