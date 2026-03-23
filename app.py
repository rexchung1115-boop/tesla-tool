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

/* focus（Tesla紅） */
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
