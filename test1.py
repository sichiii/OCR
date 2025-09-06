tesseract 123.jpg output
tesseract 111.jpg output -l chi_tra

from passporteye import read_mrz
from PIL import Image

# 開啟圖片
img = Image.open("photo2.jpg")
width, height = img.size

# 裁切底部 150 像素 (要依你的圖片大小調整)
mrz_area = img.crop((0, height-150, width, height))

# 轉成 RGB 再存檔
mrz_area.convert("RGB").save("mrz_only.jpg")

# 讀取 MRZ
mrz = read_mrz("mrz_only.jpg")

if mrz is None:
    print("無法讀取 MRZ")
else:
    print(mrz.to_dict())
