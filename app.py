import streamlit as st
import streamlit.components.v1 as components
import json

st.title("🚗 Tesla 公版填寫工具")

default_message = """🦔
感謝您選擇Tesla，加入我們的使命，與我們一同加速全球轉向永續能源的發展。
以下關於您的訂單相關資訊，也再麻煩您一同協助確認，謝謝您！
"""

template_type = st.selectbox("📌 選擇公版", ["Order"])

customer_name = st.text_input("訂購人")
payment_method = st.text_input("付款方式")
owner_name = st.text_input("車輛登記人姓名")
owner_address = st.text_input("車輛登記人地址")
charger_install = st.text_input("充電座安裝")
charger_address = st.text_input("充電座安裝地址")
install_type = st.text_input("安裝建物類型及名稱")
license_plate = st.text_input("車輛號牌")
delivery_period = st.text_input("期望交付期間")
delivery_location = st.text_input("交車地點")
referral_code = st.text_input("推薦碼")
note = st.text_input("備註")

fields = {
    "訂購人": customer_name,
    "付款方式": payment_method,
    "車輛登記人姓名": owner_name,
    "車輛登記人地址": owner_address,
    "充電座安裝": charger_install,
    "充電座安裝地址": charger_address,
    "安裝建物類型及名稱": install_type,
    "車輛號牌": license_plate,
    "期望交付期間": delivery_period,
    "交車地點": delivery_location,
    "推薦碼": referral_code,
    "備註": note,
}

formatted_lines = [
    f"{label}：{value.strip()}"
    for label, value in fields.items()
    if value.strip()
]

formatted_text = "\n".join(formatted_lines)

final_text = default_message
if formatted_text:
    final_text += f"\n\n{formatted_text}"

st.markdown("### 📋 最終文字（開場＋表單內容）")
st.text_area("可直接複製貼上", final_text, height=400)

# 一鍵複製功能
safe_text = json.dumps(final_text)

components.html(
    f"""
    <button onclick="copyText()" style="background:#1677ff;color:white;padding:10px 16px;border:none;border-radius:8px;">
        📋 一鍵複製
    </button>
    <span id="msg" style="margin-left:10px;color:green;"></span>

    <script>
    function copyText() {{
        navigator.clipboard.writeText({safe_text});
        document.getElementById("msg").innerText = "已複製";
    }}
    </script>
    """,
    height=60
)
