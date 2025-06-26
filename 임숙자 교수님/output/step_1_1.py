from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR = WORK_DIR / "input"
OUT_DIR = WORK_DIR / "output"   # ← 이 부분 추가

if __name__ == "__main__":
    IN_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)  # output 폴더도 생성
