# step_3_5.py

import streamlit as st
import pandas as pd
from pathlib import Path
from datakart import Ecos

from step_1_1 import OUT_DIR

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"


def ecos_to_xlsx():
    ECOS_KEY = "WEBU7NTPBWO8YYQOV0TN"
    CODE_LIST = [
        ["기준금리", "722Y001", "D", "0101000", 1000],
        ["국고채", "817Y002", "D", "010200000", 1000],
        ["회사채", "817Y002", "D", "010300000", 1000],
        ["코스피지수", "802Y001", "D", "0001000", 1000],
        ["원달러환율", "731Y001", "D", "0000001", 1000],
    ]

    with pd.ExcelWriter(OUT_2_2) as writer:
        ecos = Ecos(ECOS_KEY)
        for name, stat_code, freq, item_code1, limit in CODE_LIST:
            resp = ecos.stat_search(
                stat_code=stat_code,
                freq=freq,
                item_code1=item_code1,
                limit=limit,
            )
            df_raw = pd.DataFrame(resp)
            df_raw.to_excel(writer, sheet_name=name, index=False)


# Streamlit UI 코드 아래에 작성
st.title("ECOS 데이터 엑셀 저장 및 보기")

if st.button("엑셀 파일 생성"):
    ecos_to_xlsx()
    st.success(f"엑셀 파일이 생성되었습니다: {OUT_2_2}")

if OUT_2_2.exists():
    df = pd.read_excel(OUT_2_2, sheet_name=None)
    st.write("저장된 엑셀 데이터:")
    for sheet_name, sheet_df in df.items():
        st.subheader(sheet_name)
        st.dataframe(sheet_df)
else:
    st.write("엑셀 파일이 존재하지 않습니다.")
