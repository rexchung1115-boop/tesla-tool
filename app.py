import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tesla Sales Toolkit",
    page_icon="⚡",
    layout="wide",
)

st.markdown("""
<style>

/* ===== 全域 ===== */
.stApp {
    background: linear-gradient(180deg, #07090d 0%, #0b0f17 100%);
    color: #f9fafb;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ===== 字體系統（最佳尺寸）===== */
html, body, [class*="css"] {
    font-size: 16.5px !important;
    color: #f3f4f6;
}

/* ===== 標題 ===== */
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.4rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: 1.1rem;
    color: #d1d5db;
    margin-bottom: 1.8rem;
}

/* ===== 卡片 ===== */
.card {
    background: linear-gradient(180deg, #10141d 0%, #0e131b 100%);
    border: 1px solid #202938;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.4);
}

/* ===== 區塊 ===== */
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.4rem;
}

.section-desc {
    font-size: 1rem;
    color: #cbd5e1;
    margin-bottom: 1.2rem;
    line-height: 1.6;
}

/* ===== Label ===== */
label, .stTextInput label, .stSelectbox label, .stTextArea label {
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: #f3f4f6 !important;
    margin-bottom: 4px !important;
}

/* ===== Input ===== */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    font-size: 1.05rem !important;
    padding: 10px 12px !important;
    background-color: #171c26 !important;
    color: #ffffff !important;
    border: 1px solid #313a4a !important;
    border-radius: 14px !important;
}

/* placeholder */
div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder {
    color: #94a3b8 !important;
}

/* focus */
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #ef4444 !important;
    box-shadow: 0 0 0 1px #ef4444 !important;
}

/* ===== Select ===== */
div[data-baseweb="select"] > div {
    background-color: #171c26 !important;
    border-radius: 14px !important;
    border: 1px solid #313a4a !important;
    font-size: 1.05rem !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
    font-size: 1.05rem !important;
}

/* ===== 預覽區 ===== */
.preview-box {
    background: linear-gradient(180deg, #0f1a2d 0%, #101826 100%);
    border: 1px solid #213250;
    border-radius: 18px;
    padding: 18px;
    white-space: pre-wrap;
    line-height: 1.8;
    color: #f8fafc;
    font-size: 1.05rem;
    min-height: 130px;
}

/* ===== 複製區 ===== */
textarea {
    font-size: 1.05rem !important;
    color: #ffffff !important;
}

/* ===== 按鈕 ===== */
.stButton > button {
    border-radius: 14px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    padding: 10px 16px !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #ef4444 0%, #e11d48 100%) !important;
    color: white !important;
}

.stButton > button:hover {
    filter: brightness(1.08);
}

/* ===== 小字 ===== */
.small-tip {
    font-size: 0.9rem;
    color: #cbd5e1;
    margin-bottom: 10px;
}

.footer-note {
    font-size: 0.9rem;
    color: #cbd5e1;
    margin-top: 12px;
}

</style>
""", unsafe_allow_html=True)

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
        "intro": """⚡
感謝您選擇 Tesla，與我們一起加速世界邁向永續能源。""",
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
    st.session_state.template_name = "Lead/PDC"

if "include_intro" not in st.session_state:
    st.session_state.include_intro = True

if "field_values" not in st.session_state:
    st.session_state.field_values = {}

st.markdown('<div class="hero-title">⚡ Tesla Sales Toolkit</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">高效公版填寫 / 試駕推進工具</div>', unsafe_allow_html=True)

left_col, right_col = st.columns([1.05, 0.95], gap="large")

with left_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">表單輸入區</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">先選擇公版，再填入對應欄位內容。</div>', unsafe_allow_html=True)

    selected_template = st.selectbox(
        "選擇公版",
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
        new_values[field] = st.text_input(
            field,
            value=old_value,
            key=f"field_{selected_template}_{field}"
        )

    st.session_state.field_values = new_values

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("🧹 清除重填", use_container_width=True):
            st.session_state.field_values = {}
            st.rerun()

    with col_b:
        st.button("✅ 已完成輸入", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">即時預覽</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-desc">這裡會顯示整理後可直接傳給客戶或內部使用的文字。</div>',
        unsafe_allow_html=True
    )

    preview_text = final_text if final_text.strip() else "請先在左側填入內容，這裡會自動生成。"
    st.markdown(f'<div class="preview-box">{preview_text}</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)
    st.text_area("可複製內容", final_text, height=250)

    safe_text = json.dumps(final_text)

    components.html(
        f"""
        <div style="margin-top: 8px; display:flex; align-items:center; gap:12px;">
            <button
                onclick="copyText()"
                style="
                    background: linear-gradient(135deg, #ef4444 0%, #e11d48 100%);
                    color: white;
                    padding: 11px 18px;
                    border: none;
                    border-radius: 14px;
                    cursor: pointer;
                    font-size: 15px;
                    font-weight: 700;
                    box-shadow: 0 10px 24px rgba(225, 29, 72, 0.35);
                "
            >
                📋 一鍵複製
            </button>
            <span id="msg" style="color:#86efac; font-size:14px;"></span>
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
        height=62,
    )

    st.markdown(
        f'<div class="footer-note">目前公版：<strong>{selected_template}</strong></div>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)
