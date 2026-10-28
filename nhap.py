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
    button[data-baseweb="tab"] p { font-size: 20px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. TIÊU ĐỀ CHÍNH
st.title("🌾 KHO HỌC LIỆU HÁT THEN - ĐÀN TÍNH")
st.caption("Sản phẩm Chuyển đổi số bảo tồn và phát huy giá trị di sản văn hóa dân tộc")
st.divider()

# 3. TẠO 4 HỘP (TABS)
tab1, tab2, tab3, tab_co = st.tabs([
    "🎵 1. Nghệ thuật Hát Then - Đàn Tính",
    "🎙️ 2. Trải nghiệm & Phỏng vấn",
    "🪈 3. Nhạc cụ bổ trợ",
    "📤 4. Mục trống"
])

# LINK VIDEO VÀ ẢNH MẪU (Em chỉ cần thay các đường link dưới này khi có dữ liệu thật)
LINK_YOUTUBE_MAU = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
LINK_ANH_MAU = "https://via.placeholder.com/500x300.png?text=Hinh+Anh+Thuc+Te"

# ==============================================================================
# HỘP 1: NGHỆ THUẬT HÁT THEN - ĐÀN TÍNH
# ==============================================================================
with tab1:
    st.header("🎵 Nghệ thuật Hát Then - Đàn Tính")

    # CHIA 2 CỘT SONG NGỮ
    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        st.info("🇻🇳 **Tiếng Việt / English:** Khám phá điệu Then cổ truyền / *Explore traditional Then singing*")
    with col_lang2:
        st.success("🌾 **Tiếng Tày / Tiếng Việt:** Lập Then - Tỉnh Tẩu / *Hát Then - Đàn Tính*")

    st.divider()

    # --- 5 VIDEO ---
    st.subheader("🎬 Danh sách 5 Video bài hát Then")

    v1, v2 = st.columns(2)
    with v1:
        st.write("**1. Bài hát Then mẫu 1**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**2. Bài hát Then mẫu 2**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**3. Bài hát Then mẫu 3**")
        st.video(LINK_YOUTUBE_MAU)

    with v2:
        st.write("**4. Bài hát Then mẫu 4**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**5. Bài hát Then mẫu 5**")
        st.video(LINK_YOUTUBE_MAU)

    st.divider()

    # --- 5 HÌNH ẢNH ---
    st.subheader("📸 Bộ sưu tập 5 Hình ảnh")
    img_cols = st.columns(5)
    for idx, col in enumerate(img_cols, start=1):
        with col:
            st.image(LINK_ANH_MAU, caption=f"Ảnh {idx}")

# ==============================================================================
# HỘP 2: TRẢI NGHIỆM CÙNG HÁT THEN - ĐÀN TÍNH
# ==============================================================================
with tab2:
    st.header("🎙️ Trải nghiệm & Phỏng vấn Thực tế")

    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        st.info("🇻🇳 **Tiếng Việt / English:** Nhật ký thực địa & Phỏng vấn / *Fieldwork & Interviews*")
    with col_lang2:
        st.success("🌾 **Tiếng Tày / Tiếng Việt:** Bjoóc Then / *Hình ảnh trải nghiệm thực tế*")

    st.divider()

    # --- 5 VIDEO ---
    st.subheader("🎬 Danh sách 5 Video Phỏng vấn & Trải nghiệm")
    v1, v2 = st.columns(2)
    with v1:
        st.write("**1. Video phỏng vấn nghệ nhân 1**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**2. Video phỏng vấn nghệ nhân 2**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**3. Video nhật ký thực địa 1**")
        st.video(LINK_YOUTUBE_MAU)

    with v2:
        st.write("**4. Video nhật ký thực địa 2**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**5. Video cảm nhận của học sinh**")
        st.video(LINK_YOUTUBE_MAU)

    st.divider()

    # --- 5 HÌNH ẢNH ---
    st.subheader("📸 5 Hình ảnh phỏng vấn thực tế")
    img_cols = st.columns(5)
    for idx, col in enumerate(img_cols, start=1):
        with col:
            st.image(LINK_ANH_MAU, caption=f"Trải nghiệm {idx}")

# ==============================================================================
# HỘP 3: NHẠC CỤ BỔ TRỢ
# ==============================================================================
with tab3:
    st.header("🪈 Nhạc cụ bổ trợ cho Hát Then - Đàn Tính")

    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        st.info("🇻🇳 **Tiếng Việt / English:** Âm nhạc dân tộc phối hợp / *Accompanying instruments*")
    with col_lang2:
        st.success("🌾 **Tiếng Tày / Tiếng Việt:** Pí Lè, Pí Thỉu / *Sáo trúc và nhạc cụ dân tộc*")

    st.divider()

    # --- 5 VIDEO ---
    st.subheader("🎬 Danh sách 5 Video thổi sáo & hòa tấu")
    v1, v2 = st.columns(2)
    with v1:
        st.write("**1. Bài hòa tấu sáo trúc 1**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**2. Bài hòa tấu sáo trúc 2**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**3. Đàn Tính hòa tấu Sáo 1**")
        st.video(LINK_YOUTUBE_MAU)

    with v2:
        st.write("**4. Đàn Tính hòa tấu Sáo 2**")
        st.video(LINK_YOUTUBE_MAU)
        st.write("**5. Hướng dẫn thổi sáo điệu Then**")
        st.video(LINK_YOUTUBE_MAU)

    st.divider()

    # --- 5 HÌNH ẢNH ---
    st.subheader("📸 5 Hình ảnh nhạc cụ bổ trợ")
    img_cols = st.columns(5)
    for idx, col in enumerate(img_cols, start=1):
        with col:
            st.image(LINK_ANH_MAU, caption=f"Nhạc cụ {idx}")

# ==============================================================================
# HỘP 4: GÓC DÀNH RIÊNG CHO CÔ GIÁO (TỰ THÊM VIDEO MỚI)
# ==============================================================================
with tab_co:
    st.header("📤 Dành riêng cho Cô giáo bổ sung tư liệu")
    st.write(
        "Cô giáo hoặc giám khảo có thể dán trực tiếp link video YouTube vào đây để xem phát ngay lập tức trên ứng dụng!")

    # Ô cho cô gõ/dán link YouTube
    link_co_nhap = st.text_input(
        "📌 Cô hãy dán đường link video YouTube vào ô dưới đây:",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    # Nếu cô có dán link thì hiện video ngay
    if link_co_nhap:
        st.success("✅ Đã phát hiện link video! Video hiển thị bên dưới:")
        st.video(link_co_nhap)
    else:
        st.info("👉 Hướng dẫn: Cô copy link video YouTube rồi dán (Ctrl+V) vào ô trống ở trên để xem trực tiếp.")