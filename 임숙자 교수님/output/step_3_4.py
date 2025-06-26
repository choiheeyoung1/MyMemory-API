from pathlib import Path
import pandas as pd
from datakart import Ecos
import streamlit as st

# 경로 설정
WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"
OUT_DIR.mkdir(exist_ok=True)

# ECOS API 키
ECOS_KEY = "WEBU7NTPBWO8YYQOV0TN"
ecos = Ecos(ECOS_KEY)

# ECOS 통계 조회
resp = ecos.stat_search(
    stat_code="722Y001",
    freq="M",
    item_code1="0101000",
    start="202301",
    end="202412",
)

# API 결과 출력 (디버그용)
st.write("API 응답 데이터:", resp)

# 응답 데이터 처리 및 데이터 존재 여부 확인
if "StatisticSearch" in resp and resp["StatisticSearch"].get("row"):
    data_list = resp["StatisticSearch"]["row"]
    st.write("조회된 데이터 수:", len(data_list))
    df_raw = pd.DataFrame(data_list)
else:
    st.error("API 데이터가 없습니다.")
    df_raw = pd.DataFrame()

# 엑셀 파일 경로 설정
file_stem = Path(__file__).stem
excel_path = OUT_DIR / "step_3_5.xlsx"

# 엑셀 저장
with pd.ExcelWriter(excel_path) as writer:
    df_raw.to_excel(writer, sheet_name="기준금리", index=False)

st.title("한국은행 기준금리 통계 (월별)")

if excel_path.exists():
    df = pd.read_excel(excel_path, sheet_name="기준금리")
    st.dataframe(df)

    if not df.empty:
        df_chart = df[["TIME", "DATA_VALUE"]].copy()
        df_chart["DATA_VALUE"] = pd.to_numeric(df_chart["DATA_VALUE"], errors="coerce")
        df_chart = df_chart.dropna()
        st.line_chart(df_chart.set_index("TIME"))
    else:
        st.warning("데이터프레임이 비어 있습니다.")
else:
    st.error(f"엑셀 파일이 존재하지 않습니다: {excel_path}")
