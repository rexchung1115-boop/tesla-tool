import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tesla 公版填寫工具",
    page_icon="🚗",
    layout="centered",
)

st.title("🚗 Tesla 公版填寫工具")

TEMPLATES = {
    "Order": {
        "intro": """🦔
感謝您選擇Tesla，加入我們的使命，與我們一同加速全球轉向永續能源的發展。
以下關於您的訂單相關資訊，也再麻煩您一同協助確認，謝謝您！""",
        "fields": [
            "訂購人",
            "付款方式",
            "車輛登記人姓名",
            "車輛登記人地址",
            "充電座安裝",
            "充電座安裝地址",
            "安裝建物類型及名稱",
            "車輛號牌",
            "期望交付期間",
            "交車地點",
            "推薦碼",
            "備註",
        ],
    },
    "Lead/PDC": {
        "intro": "您好，這邊是 Tesla，為您整理聯繫資訊如下：",
        "fields": [
            "客戶姓名",
            "聯絡電話",
            "需求車型",
            "購車時間",
            "是否試駕",
            "追蹤時間",
            "備註",
        ],
    },
    "Trade-in": {
        "intro": "以下為舊換新資料確認：",
        "fields": [
            "車主姓名",
            "舊車品牌",
            "舊車車型",
            "年份",
            "里程",
            "是否貸款",
            "備註",
        ],
    },
    "TD Note": {
        "intro": "試駕紀錄如下：",
        "fields": [
            "目標 Model",
            "換購車動機",
            "考慮比較的競品",
            "疑慮（不購車的原因）",
            "購買時間",
            "決策者 / 使用人",
            "充電規劃",
            "平常用車的用途",
            "目前使用車輛",
            "是否 Trade in",
            "備註",
            "C/E/T/N",
            "Next Step",
        ],
    },
    "PDC SMS": {
        "intro": "您好，提醒您交付資訊如下：",
        "fields": [
            "客戶姓名",
            "交車時間",
            "交車地點",
            "文件",
            "尾款",
            "備註",
        ],
    },
    "PDC 威脅 SMS": {
        "intro": "提醒您尚有資料未完成，請盡快處理：",
        "fields": [
            "客戶姓名",
            "未完成項目",
            "截止時間",
            "影響",
            "備註",
        ],
    },
    "貸款": {
        "intro": "貸款資料如下：",
        "fields": [
            "申請人",
            "銀行",
            "期數",
            "頭期款",
            "月付",
            "備註",
        ],
    },
}

template_name = st.selectbox("📌 選擇公版", list(TEMPLATES.keys()))
template = TEMPLATES[template_name]

field_values = {}
for field in template["fields"]:
    field_values[field] = st.text_input(field)

include_intro = st.checkbox("包含開場文字", value=True)

formatted_lines = [
    f"{label}：{value.strip()}"
    for label, value in field_values.items()
    if value.strip()
]

final_parts = []
if include_intro and template["intro"].strip():
    final_parts.append(template["intro"].strip())
if formatted_lines:
    final_parts.append("\n".join(formatted_lines))

final_text = "\n\n".join(final_parts)

st.markdown("### 📋 整理好的文字")
st.text_area("可直接複製貼上", final_text, height=320)

safe_text = json.dumps(final_text)

components.html(
    f"""
    <div style="margin-top: 8px;">
        <button
            onclick="copyText()"
            style="
                background:#1677ff;
                color:white;
                padding:10px 16px;
                border:none;
                border-radius:8px;
                cursor:pointer;
                font-size:15px;
            "
        >
            📋 一鍵複製
        </button>
        <span id="msg" style="margin-left:10px;color:green;"></span>
    </div>

    <script>
    async function copyText() {{
        try {{
            await navigator.clipboard.writeText({safe_text});
            document.getElementById("msg").innerText = "已複製";
        }} catch (e) {{
            document.getElementById("msg").innerText = "複製失敗，請手動複製";
        }}
    }}
    </script>
    """,
    height=60,
)
