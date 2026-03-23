import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tesla 公版填寫工具", page_icon="🚗")

st.title("🚗 Tesla 公版填寫工具")

TEMPLATES = {
    "Order": {
        "intro": """🦔
感謝您選擇Tesla，加入我們的使命，與我們一同加速全球轉向永續能源的發展。
以下關於您的訂單相關資訊，也再麻煩您一同協助確認，謝謝您！""",
        "fields": [
            "訂購人", "付款方式", "車輛登記人姓名", "車輛登記人地址",
            "充電座安裝", "充電座安裝地址", "安裝建物類型及名稱",
            "車輛號牌", "期望交付期間", "交車地點", "推薦碼", "備註"
        ],
    },

    "Lead/PDC": {
        "intro": "您好，這邊是 Tesla，為您整理聯繫資訊如下：",
        "fields": [
            "客戶姓名", "聯絡電話", "需求車型", "購車時間",
            "是否試駕", "追蹤時間", "備註"
        ],
    },

    "Trade-in": {
        "intro": "以下為舊換新資料確認：",
        "fields": [
            "車主姓名", "舊車品牌", "舊車車型",
            "年份", "里程", "是否貸款", "備註"
        ],
    },

    "TD Note": {
        "intro": "試駕紀錄如下：",
        "fields": [
            "客戶姓名", "試駕車型", "感受",
            "顧慮點", "下一步", "備註"
        ],
    },

    "PDC SMS": {
        "intro": "您好，提醒您交付資訊如下：",
        "fields": [
            "客戶姓名", "交車時間", "交車地點",
            "文件", "尾款", "備註"
        ],
    },

    "PDC 威脅 SMS": {
        "intro": "提醒您尚有資料未完成，請盡快處理：",
        "fields": [
            "客戶姓名", "未完成項目",
            "截止時間", "影響", "備註"
        ],
    },

    "貸款": {
        "intro": "貸款資料如下：",
        "fields": [
            "申請人", "銀行", "期數",
            "頭期款", "月付", "備註"
        ],
    },
}

template_name = st.selectbox("📌 選擇公版", list(TEMPLATES.keys()))
template = TEMPLATES[template_name]

inputs = {}
for field in template["fields"]:
    inputs[field] = st.text_input(field)

lines = [f"{k}：{v}" for k, v in inputs.items() if v]

final_text = template["intro"] + "\n\n" + "\n".join(lines)

st.text_area("📋 整理好的文字", final_text, height=300)

safe_text = json.dumps(final_text)

components.html(f"""
<button onclick="copyText()">📋 一鍵複製</button>
<span id="msg"></span>

<script>
function copyText() {{
navigator.clipboard.writeText({safe_text});
document.getElementById("msg").innerText = " 已複製";
}}
</script>
""", height=60)
