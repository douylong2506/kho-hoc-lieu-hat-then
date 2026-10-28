import streamlit as st

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(
    page_title="Kho học liệu Hát Then - Đàn Tính",
    page_icon="🌾",
    layout="wide"
)

# Tăng cỡ chữ cho dễ nhìn
st.markdown("""
    <style>
    html, body, [class*="st-"] { font-size: 18px !important; }
    button[data-baseweb="tab"] p { font-size: 18px !important; font-weight: bold !important; }

    /* Thêm 2 dòng này để chỉnh to tiêu đề và phụ đề */
    h1 { font-size: 38px !important; }
    p { font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. TIÊU ĐỀ CHÍNH
st.title("🌾 KHO HỌC LIỆU HÁT THEN - ĐÀN TÍNH")
st.caption("Sản phẩm Chuyển đổi số bảo tồn và phát huy giá trị di sản văn hóa dân tộc")
st.divider()

# 3. TẠO 4 HỘP (TABS) LỚN
tab1, tab2, tab3, tab_co = st.tabs([
    "🎵 1. Nghệ thuật Hát Then - Đàn Tính",
    "🎙️ 2. Trải nghiệm & Phỏng vấn",
    "🪈 3. Nhạc cụ bổ trợ",
    "📤 4. Dành riêng cho Cô giáo"
])

# LINK MẪU (Sau này thay link thật vào đây)
LINK_YOUTUBE_MAU = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
LINK_ANH_MAU = "https://via.placeholder.com/500x300.png?text=Hinh+Anh+Thuc+Te"

# ==============================================================================
# HỘP 1: NGHỆ THUẬT HÁT THEN - ĐÀN TÍNH
# ==============================================================================
with tab1:
    st.header("🎵 Nghệ thuật Hát Then - Đàn Tính")
    tab_anh_1, tab_tay_1 = st.tabs(["🇬🇧 Bản Anh - Việt (English)", "🌾 Bản Tày - Việt"])

    with tab_anh_1:
        st.subheader("🇬🇧 Nội dung Song ngữ Anh - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

    with tab_tay_1:
        st.subheader("🌾 Nội dung Tiếng Tày - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

# ==============================================================================
# HỘP 2: TRẢI NGHIỆM & PHỎNG VẤN
# ==============================================================================
with tab2:
    st.header("🎙️ Trải nghiệm & Phỏng vấn Thực tế")
    tab_anh_2, tab_tay_2 = st.tabs(["🇬🇧 Bản Anh - Việt (English)", "🌾 Bản Tày - Việt"])

    with tab_anh_2:
        st.subheader("🇬🇧 Nội dung Song ngữ Anh - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

    with tab_tay_2:
        st.subheader("🌾 Nội dung Tiếng Tày - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

# ==============================================================================
# HỘP 3: NHẠC CỤ BỔ TRỢ
# ==============================================================================
with tab3:
    st.header("🪈 Nhạc cụ bổ trợ cho Hát Then - Đàn Tính")
    tab_anh_3, tab_tay_3 = st.tabs(["🇬🇧 Bản Anh - Việt (English)", "🌾 Bản Tày - Việt"])

    with tab_anh_3:
        st.subheader("🇬🇧 Nội dung Song ngữ Anh - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

    with tab_tay_3:
        st.subheader("🌾 Nội dung Tiếng Tày - Việt")
        st.write("🎬 **5 Video:**")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

# ==============================================================================
# HỘP 4: GÓC DÀNH RIÊNG CHO CÔ GIÁO
# ==============================================================================
with tab_co:
    st.header("📤 Dành riêng cho Cô giáo bổ sung tư liệu")
    st.write("Cô giáo có thể dán trực tiếp link YouTube vào ô dưới đây để xem video trực tiếp trên ứng dụng:")

    link_co_nhap = st.text_input(
        "📌 Dán đường link YouTube vào đây:",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    if link_co_nhap:
        st.success("✅ Đã nhận link! Video hiển thị bên dưới:")
        st.video(link_co_nhap)
    else:
        st.info("👉 Hãy copy link YouTube rồi dán (Ctrl+V) vào ô trống phía trên.")