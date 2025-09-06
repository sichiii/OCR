import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

# 設定 Tesseract 的安裝路徑
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"

# 讀取圖片
image = Image.open("photo2.jpg")

# ------------------
# 影像預處理
# ------------------

# 1. 提高對比度
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2.5)  # 可以調整 1.5 ~ 3.0

# 2. 提高亮度（可選）
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1.2)

# 3. 灰階
gray = image.convert("L")

# 4. 轉成 numpy array 做二值化
img_array = np.array(gray)
_, binary = cv2.threshold(img_array, 150, 255, cv2.THRESH_BINARY)  # 門檻值 150 可調整

# 5. 降噪
binary = cv2.medianBlur(binary, 3)  # 3x3 中值濾波

# 6. 轉回 PIL Image
processed_image = Image.fromarray(binary)

# ------------------
# OCR 辨識
# ------------------
text = pytesseract.image_to_string(processed_image, lang="chi_tra", config="--psm 7")

print("辨識結果：")
print(text)

# ------------------
# 可選：顯示處理後圖片
# ------------------
processed_image.show()
