import requests
from pathlib import Path
import pandas as pd
from datakart import Ecos

# 경로 설정
try:
    WORK_DIR = Path(__file__).parent
except NameError:
    WORK_DIR = Path.cwd()

OUT_DIR = WORK_DIR / "output"
OUT_DIR.mkdir(exist_ok=True)

# ECOS API 키 (공백 제거 완료)
ECOS_KEY = "WEBU7NTPBWO8YYQOV0TN"

ecos = Ecos(ECOS_KEY)

resp = ecos.stat_search(
    stat_code="722Y001",
    freq="M",
    item_code1="0101000",
    start="202301",
    end="202412",
)

# 데이터프레임 생성
if "StatisticSearch" in resp and resp["StatisticSearch"].get("row"):
    data_list = resp["StatisticSearch"]["row"]
    df_raw = pd.DataFrame(data_list)
else:
    df_raw = pd.DataFrame()

# CSV 저장
file_stem = Path(__file__).stem if "__file__" in globals() else "output"
csv_path = OUT_DIR / f"{file_stem}.csv"

df_raw.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
