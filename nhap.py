import streamlit as st

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(
    page_title="Kho học liệu Hát Then - Đàn Tính",
    page_icon="🌾",
    layout="wide")

# 2. TIÊU ĐỀ CHÍNH CỦA ỨNG DỤNG
st.title("🌾 KHO HỌC LIỆU HÁT THEN - ĐÀN TÍNH")
st.caption("Sản phẩm Chuyển đổi số bảo tồn và phát huy giá trị di sản văn hóa dân tộc")
st.divider()

# 3. TẠO 3 "HỘP" NỘI DUNG NGHỆ THUẬT (TABS)
tab1, tab2, tab3 = st.tabs([
    "🎵 Nghệ thuật Hát Then - Đàn Tính",
    "🎙️ Trải nghiệm cùng Hát Then - Đàn Tính",
    "🪈 Nhạc cụ bổ trợ cho Hát Then - Đàn Tính"
])

# ==========================================
# HỘP 1: NGHỆ THUẬT HÁT THEN - ĐÀN TÍNH
# ==========================================
with tab1:
    st.header("🎵 Danh mục Video bài hát Then & Đàn Tính")
    st.write("Tổng hợp các video biểu diễn bài hát Then, gảy Đàn Tính do câu lạc bộ và nghệ nhân thể hiện.")

    # --- KHU VỰC VIDEO ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Bài hát Then mẫu 1")
        # 🟢 LỆNH CHÈN VIDEO YOUTUBE:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.caption("Trích đoạn biểu diễn Hát Then cổ")

    with col2:
        st.subheader("2. Bài hát Then mẫu 2")
        # 🟢 LỆNH CHÈN VIDEO YOUTUBE:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.caption("Tiết mục Đàn Tính hòa tấu")

# ==========================================
# HỘP 2: TRẢI NGHIỆM CÙNG HÁT THEN - ĐÀN TÍNH
# ==========================================
with tab2:
    st.header("🎙️ Video Giới thiệu & Phỏng vấn Thực tế")
    st.write("Mô tả: Ghi lại chuyến đi thực địa, phỏng vấn nghệ nhân và trải nghiệm của học sinh.")

    # --- KHU VỰC VIDEO PHỎNG VẤN ---
    st.subheader("🎬 Phỏng vấn Nghệ nhân")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    st.divider()

    # --- KHU VỰC BỘ CỦA ẢNH TRẢI NGHIỆM ---
    st.subheader("📸 Hình ảnh các chuyến đi thực địa")

    img_col1, img_col2, img_col3 = st.columns(3)

    with img_col1:
        # 🟢 LỆNH CHÈN ẢNH TỪ THƯ MỤC:
        # (Thay "images/anh1.jpg" thành tên file ảnh thật của em)
        st.image("https://via.placeholder.com/400x300.png?text=Anh+Thuc+Dia+1", caption="Buổi gặp gỡ nghệ nhân")

    with img_col2:
        st.image("https://via.placeholder.com/400x300.png?text=Anh+Thuc+Dia+2", caption="Tập gảy Đàn Tính")

    with img_col3:
        st.image("https://via.placeholder.com/400x300.png?text=Anh+Thuc+Dia+3", caption="Quá trình quay clip")

    # Nút bấm mở kho ảnh Google Drive (nếu có nhiều ảnh)
    st.info("💡 Xem thêm toàn bộ kho ảnh thực địa trên Google Drive:")
    st.link_button("👉 Bấm vào đây để xem toàn bộ Album Ảnh", "https://drive.google.com")

# ==========================================
# HỘP 3: NHẠC CỤ BỔ TRỢ
# ==========================================
with tab3:
    st.header("🪈 Nhạc cụ bổ trợ cho Hát Then - Đàn Tính")
    st.write("Mô tả: Các bài hòa tấu sáo trúc và nhạc cụ dân tộc bổ trợ cho điệu Then.")

    col_sao1, col_sao2 = st.columns(2)

    with col_sao1:
        st.subheader("1. Bài thổi sáo bổ trợ 1")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.caption("Giai điệu sáo trúc quê hương")

    with col_sao2:
        st.subheader("2. Bài thổi sáo bổ trợ 2")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.caption("Hòa tấu Sáo và Đàn Tính")