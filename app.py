import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tesla 公版填寫工具",
    page_icon="🚗",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f6f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .hero-card {
        background: linear-gradient(135deg, #ffffff 0%, #f3f5fb 100%);
        border: 1px solid #e7eaf3;
        border-radius: 22px;
        padding: 28px 30px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #18233a;
        margin: 0 0 8px 0;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #5b6475;
        margin: 0;
        line-height: 1.7;
    }

    .section-card {
        background: #ffffff;
        border: 1px solid #e8ecf4;
        border-radius: 22px;
        padding: 22px 22px 18px 22px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        height: 100%;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1b2740;
        margin-bottom: 6px;
    }

    .section-desc {
        font-size: 0.92rem;
        color: #6b7280;
        margin-bottom: 14px;
    }

    .preview-box {
        background: #f8faff;
        border: 1px solid #dce6ff;
        border-radius: 16px;
        padding: 16px;
        min-height: 120px;
        white-space: pre-wrap;
        line-height: 1.75;
        color: #1f2937;
        font-size: 0.98rem;
    }

    .small-tip {
        color: #6b7280;
        font-size: 0.88rem;
        margin-top: 4px;
        margin-bottom: 10px;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] > div,
    div[data-testid="stSelectbox"] div[role="combobox"] {
        border-radius: 14px !important;
    }

    .footer-note {
        margin-top: 14px;
        font-size: 0.85rem;
        color: #7b8190;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

TEMPLATES = {
    "Lead/PDC": {
        "intro": "Lead / PDC 紀錄如下：",
        "fields": [
            "選擇人名",
            "Model",
            "現有車款",
            "用車習慣",
            "充電規劃",
            "比較車款",
            "吸引反在乎之處",
            "疑慮",
            "C/E/T/N",
            "備註",
        ],
    },
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
}

if "template_name" not in st.session_state:
    st.session_state.template_name = "Order"

if "include_intro" not in st.session_state:
    st.session_state.include_intro = True

if "field_values" not in st.session_state:
    st.session_state.field_values = {}

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">🚗 Tesla 公版填寫工具</div>
        <p class="hero-subtitle">
            快速整理 Lead、Order 與 TD Note 內容，右側即時預覽，完成後可一鍵複製貼上。
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1.05, 0.95], gap="large")

with left_col:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">表單輸入區</div>
            <div class="section-desc">先選擇公版，再填入對應欄位內容。</div>
        """,
        unsafe_allow_html=True,
    )

    selected_template = st.selectbox(
        "📌 選擇公版",
        list(TEMPLATES.keys()),
        index=list(TEMPLATES.keys()).index(st.session_state.template_name),
    )
    st.session_state.template_name = selected_template
    template = TEMPLATES[selected_template]

    st.session_state.include_intro = st.checkbox(
        "包含開場文字",
        value=st.session_state.include_intro,
    )

    st.markdown('<div class="small-tip">未填寫的欄位不會出現在右側輸出。</div>', unsafe_allow_html=True)

    current_fields = template["fields"]
    new_values = {}

    for field in current_fields:
        old_value = st.session_state.field_values.get(field, "")
        new_values[field] = st.text_input(field, value=old_value, key=f"field_{selected_template}_{field}")

    st.session_state.field_values = new_values

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("🧹 清除重填", use_container_width=True):
            st.session_state.field_values = {}
            st.rerun()

    with col_b:
        st.button("✅ 已完成輸入", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

formatted_lines = [
    f"{label}：{value.strip()}"
    for label, value in st.session_state.field_values.items()
    if value.strip()
]

final_parts = []
if st.session_state.include_intro and template["intro"].strip():
    final_parts.append(template["intro"].strip())
if formatted_lines:
    final_parts.append("\n".join(formatted_lines))

final_text = "\n\n".join(final_parts)

with right_col:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">即時預覽</div>
            <div class="section-desc">這裡會顯示整理後可直接傳給客戶或內部使用的文字。</div>
        """,
        unsafe_allow_html=True,
    )

    preview_html = final_text if final_text.strip() else "請先在左側填入內容，這裡會自動生成。"
    st.markdown(f'<div class="preview-box">{preview_html}</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
    st.text_area("📋 可直接複製貼上", final_text, height=260)

    safe_text = json.dumps(final_text)

    components.html(
        f"""
        <div style="margin-top: 4px; display:flex; align-items:center; gap:12px;">
            <button
                onclick="copyText()"
                style="
                    background:#1677ff;
                    color:white;
                    padding:10px 18px;
                    border:none;
                    border-radius:12px;
                    cursor:pointer;
                    font-size:15px;
                    font-weight:600;
                    box-shadow: 0 8px 18px rgba(22,119,255,0.25);
                "
            >
                📋 一鍵複製
            </button>
            <span id="msg" style="color:#16a34a; font-size:14px;"></span>
        </div>

        <script>
        async function copyText() {{
            try {{
                await navigator.clipboard.writeText({safe_text});
                document.getElementById("msg").innerText = "已複製到剪貼簿";
            }} catch (e) {{
                document.getElementById("msg").innerText = "複製失敗，請手動複製";
            }}
        }}
        </script>
        """,
        height=60,
    )

    st.markdown(
        f"""
        <div class="footer-note">
            目前公版：<strong>{selected_template}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)
