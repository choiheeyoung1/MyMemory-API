from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈에서 경로 불러오기
from step_2_2 import read_text       # OCR 결과 읽기 함수 불러오기

OUT_X = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75  # 인식률 기준값


def read_text_and_draw_line(path: Path):
    parsed = read_text(path)  # 문자 인식 결과
    img = Image.open(path)    # 이미지 열기
    draw = ImageDraw.Draw(img, "RGBA")  # RGBA 모드로 드로잉 객체 생성
    font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=50)

    for row in parsed:
        bbox, text, prob = row  # 좌표, 텍스트, 인식률 분리
        box = [(x, y) for x, y in bbox]  # 리스트 그대로 튜플 리스트로 변환

        # 폴리곤(영역) 그리기, 인식률에 따라 색 변경
        draw.polygon(
            box,
            outline=(255, 0, 0) if prob >= PROB else (0, 255, 0),
            width=10,
        )

        start_x, start_y = box[0]  # 텍스트 시작 좌표

        # 텍스트 바운딩 박스 크기 계산
        left, top, right, bottom = font.getbbox(text)
        text_width = right
        text_height = bottom

        pad = 10  # 여백 설정
        bg_width = pad + text_width + pad
        bg_height = pad + text_height + pad

        # 배경 사각형 그리기 (불투명 검정)
        draw.rectangle(
            xy=(
                start_x,
                start_y,
                start_x + bg_width,
                start_y + bg_height,
            ),
            fill=(0, 0, 0, 200),
        )

        # 텍스트 그리기 (흰색)
        draw.text(
            xy=(start_x + pad, start_y + pad),
            text=text,
            fill=(255, 255, 255),
            font=font,
        )

    img.save(OUT_X)
    print(f"Saved annotated image to: {OUT_X}")


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_draw_line(path)
