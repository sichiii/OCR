from passporteye import read_mrz
from PIL import Image

# ------------------------------
# MRZ 欄位清理函數
# ------------------------------
def clean_mrz_name(text: str) -> str:
    if text is None:
        return ""
    text = text.replace("K", "<").replace(" ", "")
    return text.split("<")[0]

def clean_mrz_personal_number(text: str) -> str:
    if text is None:
        return ""
    text = text.replace("K", "<").replace(" ", "")
    return text.split("<")[0]

# ------------------------------
# 讀取護照 MRZ
# ------------------------------
mrz = read_mrz("photo2.jpg", extra_cmdline_params="--psm 6")

if mrz is None:
    print("❌ 無法讀取 MRZ，請確認圖片清晰度")
else:
    data = mrz.to_dict()

    # ------------------------------
    # 後處理：清理護照類型、名字、個人號碼
    # ------------------------------
    data['type'] = data.get('type', '').split('<')[0]
    data['names'] = clean_mrz_name(data.get('names'))
    data['personal_number'] = clean_mrz_personal_number(data.get('personal_number'))

    # ------------------------------
    # 輸出結果
    # ------------------------------
    print("========== 護照 MRZ 解析結果 ==========")
    print(f"護照類型   : {data['mrz_type']} ({data['type']})")
    print(f"國籍代碼   : {data['country']} ({data['nationality']})")
    print(f"護照號碼   : {data['number']} (檢查碼 {data['check_number']}, 驗證 {data['valid_number']})")
    print(f"姓氏       : {data['surname']}")
    print(f"名字       : {data['names']}")
    print(f"出生日期   : {data['date_of_birth']} (檢查碼 {data['check_date_of_birth']}, 驗證 {data['valid_date_of_birth']})")
    print(f"性別       : {data['sex']}")
    print(f"到期日     : {data['expiration_date']} (檢查碼 {data['check_expiration_date']}, 驗證 {data['valid_expiration_date']})")
    print(f"個人號碼   : {data['personal_number']} (檢查碼 {data['check_personal_number']}, 驗證 {data['valid_personal_number']})")
    print(f"總體驗證   : {data['valid_composite']}")
    print(f"信心分數   : {data['valid_score']}%")
    print("=====================================")
