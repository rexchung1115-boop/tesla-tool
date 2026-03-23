import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tesla Sales Toolkit",
    page_icon="⚡",
    layout="wide",
)

# ====== 深色 Tesla 風格 ======
st.markdown("""
<style>
.stApp {
    background-color: #0b0c10;
    color: #e5e7eb;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

/* 卡片 */
.card {
    background: #111318;
    border: 1px solid #1f2937;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* 標題 */
.title {
    font-size: 2.2rem;
    font-weight: 800;
    color: white;
}

/* 副標 */
.subtitle {
    color: #9ca3af;
    margin-bottom: 10px;
}

/* 輸入框 */
input, textarea {
    background-color: #1a1d24 !important;
    color: white !important;
    border-radius: 12px !important;
}

/* select */
div[data-baseweb="select"] > div {
    background-color: #1a1d24 !important;
    border-radius: 12px !important;
}

/* 預覽 */
.preview {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 16px;
    white-space: pre-wrap;
    line-height: 1.7;
}

/* 按鈕 */
button[kind="primary"] {
    background: #e11d48 !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ====== 公版 ======
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
            "交車地點",
            "期望交期",
            "備註",
        ],
    },
    "TD Note": {
        "intro": "試駕紀錄如下：",
        "fields": [
            "目標 Model",
            "換購車動機",
            "考慮比較的競品",
            "疑慮",
            "購買時間",
            "決策者",
            "充電規劃",
            "使用情境",
            "目前車輛",
            "C/E/T/N",
            "Next Step",
        ],
    },
}

# ====== UI ======
st.markdown('<div class="title">⚡ Tesla Sales Toolkit</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">高效公版填寫 / 試駕推進工具</div>', unsafe_allow_html=True)

left, right = st.columns(2)

# ====== 左：輸入 ======
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    template_name = st.selectbox("選擇公版", list(TEMPLATES.keys()))
    template = TEMPLATES[template_name]

    inputs = {}

    for field in template["fields"]:
        inputs[field] = st.text_input(field)

    if st.button("🧹 清空"):
        st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ====== 右：輸出 ======
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    lines = [f"{k}：{v}" for k, v in inputs.items() if v]

    final_text = template["intro"] + "\n\n" + "\n".join(lines)

    st.markdown('<div class="preview">' + final_text + '</div>', unsafe_allow_html=True)

    st.text_area("可複製內容", final_text, height=200)

    safe_text = json.dumps(final_text)

    components.html(f"""
    <button onclick="copyText()" style="
        background:#e11d48;
        color:white;
        padding:10px 16px;
        border:none;
        border-radius:10px;
        margin-top:10px;
        cursor:pointer;
    ">📋 一鍵複製</button>

    <script>
    function copyText() {{
        navigator.clipboard.writeText({safe_text});
    }}
    </script>
    """, height=60)

    st.markdown('</div>', unsafe_allow_html=True)
