import streamlit as st

st.set_page_config(page_title="Kho học liệu Hát Then - Đàn Tính", layout="wide")

# Link mẫu để test giao diện
LINK_YOUTUBE_MAU = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
LINK_ANH_MAU = "https://via.placeholder.com/500x300.png?text=Hinh+Anh"

st.title("🌾 KHO HỌC LIỆU HÁT THEN - ĐÀN TÍNH")
st.divider()

# Tạo 4 mục lớn ở ngoài
tab1, tab2, tab3, tab_co = st.tabs([
    "🎵 1. Nghệ thuật Hát Then - Đàn Tính",
    "🎙️ 2. Trải nghiệm & Phỏng vấn",
    "🪈 3. Nhạc cụ bổ trợ",
    "📤 4. Dành riêng cho Cô giáo"
])

# ==============================================================================
# MỤC 1: CÓ 2 MỤC CON (ANH - VIỆT VÀ TÀY - VIỆT)
# ==============================================================================
with tab1:
    st.header("🎵 Nghệ thuật Hát Then - Đàn Tính")

    # Tạo 2 tab con bên trong Mục 1
    tab_anh_viet, tab_tay_viet = st.tabs(["🇬🇧 Bản Anh - Việt (English)", "🌾 Bản Tày - Việt"])

    # --- TAB CON 1: ANH - VIỆT ---
    with tab_anh_viet:
        st.subheader("🇬🇧 Nội dung Song ngữ Anh - Việt")
        st.info("Explore traditional Then singing and Dan Tinh musical heritage.")

        # 5 Video cho phần Anh - Việt
        st.write("🎬 **5 Video (Bản Anh - Việt):**")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.write("Video 1 (English Sub)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 2 (English Sub)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 3 (English Sub)")
            st.video(LINK_YOUTUBE_MAU)
        with v_col2:
            st.write("Video 4 (English Sub)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 5 (English Sub)")
            st.video(LINK_YOUTUBE_MAU)

        st.divider()

        # 5 Hình ảnh cho phần Anh - Việt
        st.write("📸 **5 Hình ảnh (Bản Anh - Việt):**")
        img_cols_1 = st.columns(5)
        for i, col in enumerate(img_cols_1, start=1):
            with col:
                st.image(LINK_ANH_MAU, caption=f"Ảnh Anh-Việt {i}")

    # --- TAB CON 2: TÀY - VIỆT ---
    with tab_tay_viet:
        st.subheader("🌾 Nội dung Tiếng Tày - Việt")
        st.success("Lập Then - Tỉnh Tẩu / Tham khảo tiếng đồng bào dân tộc Tày.")

        # 5 Video cho phần Tày - Việt
        st.write("🎬 **5 Video (Bản Tày - Việt):**")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.write("Video 1 (Tiếng Tày)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 2 (Tiếng Tày)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 3 (Tiếng Tày)")
            st.video(LINK_YOUTUBE_MAU)
        with t_col2:
            st.write("Video 4 (Tiếng Tày)")
            st.video(LINK_YOUTUBE_MAU)
            st.write("Video 5 (Tiếng Tày)")
            st.video(LINK_YOUTUBE_MAU)

        st.divider()

        # 5 Hình ảnh cho phần Tày - Việt
        st.write("📸 **5 Hình ảnh (Bản Tày - Việt):**")
        img_cols_2 = st.columns(5)
        for i, col in enumerate(img_cols_2, start=1):
            with col:
                st.image(LINK_ANH_MAU, caption=f"Ảnh Tày-Việt {i}")

# ==============================================================================
# CÁC MỤC KHÁC (GIỮ NGUYÊN HOẶC TÙY CH