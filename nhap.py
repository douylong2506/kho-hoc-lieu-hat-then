import streamlit as st

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(
    page_title="Kho học liệu hát then đàn tính",
    page_icon="🌾",
    layout="wide"
)

# Tăng cỡ chữ tiêu đề và phụ đề cho trang web
st.markdown("""
    <style>
    /* 1. Tiêu đề chính (st.title) to rõ nhất */
    h1 {
        font-size: 38px !important;
        font-weight: bold !important;
    }

    /* 2. Phần mô tả/phụ đề (st.caption) nhỏ hơn tiêu đề một chút cho cân đối */
    [data-testid="stCaptionContainer"] p {
        font-size: 18px !important;
        color: #b0b0b0 !important;
    }

    /* 3. Cỡ chữ trong các tab và nội dung bình thường */
    button[data-baseweb="tab"] p { 
        font-size: 16px !important; 
        font-weight: bold !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TIÊU ĐỀ CHÍNH
st.title("🌾 Không gian văn hóa số: hát then, đàn tính")
st.caption("Sản phẩm Chuyển đổi số bảo tồn và phát huy giá trị di sản văn hóa dân tộc")
st.divider()

# 3. TẠO 4 HỘP (TABS) LỚN
tab1, tab2, tab3, tab_co, tab4 = st.tabs([
    "🎵 Nghệ thuật Hát Then - Đàn Tính",
    "🎙️ Trải nghiệm & Phỏng vấn",
    "🪈 Nhạc cụ bổ trợ",
    "📤 Dành riêng cho Cô giáo",
    "Bản dịch Việt - Anh những bài hát then"
])

# LINK MẪU (Sau này thay link thật vào đây)
LINK_YOUTUBE_MAU = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
LINK_ANH_MAU = "https://via.placeholder.com/500x300.png?text=Hinh+Anh+Thuc+Te"

# ==============================================================================
# HỘP 1: NGHỆ THUẬT HÁT THEN - ĐÀN TÍNH
# ==============================================================================
with tab1:
    st.header("🎵 Giới thiệu")
    tab_anh_1, tab_tay_1 = st.tabs(["Anh(English) - Việt", "Tày - Việt"])

    with tab_anh_1:
        st.subheader("Nội dung Song ngữ Anh - Việt")
        v1, v2 = st.columns(1)
        with v1:
            st.video("https://youtu.be/EUIonaSRYoQ")
            st.video("https://youtu.be/PSyExFe-dEU")
            st.video("https://youtu.be/0D8OQoj4IEM")
        st.write("📸 **5 Hình ảnh:**")
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c:
                st.image(f"ng{i}.jpg", caption=f"Ảnh {i}", use_container_width=True)

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
    tab_anh_2, tab_tay_2 = st.tabs(["Anh(English) - Việt", "🌾 Tày - Việt"])

    with tab_anh_2:
        st.subheader("Nội dung Song ngữ Anh - Việt")
        v1 = st.columns(2)
        with v1:
            st.video("https://youtu.be/lUofhKpwe3w")
            st.video("https://youtu.be/5a7uMVPboKs")
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
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
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

# ==============================================================================
# HỘP 3: NHẠC CỤ BỔ TRỢ
# ==============================================================================
with tab3:
    st.header("🪈 Nhạc cụ bổ trợ cho Hát Then - Đàn Tính")
    tab_anh_3, tab_tay_3 = st.tabs(["Bản Anh(English) - Việt", "Bản Tày - Việt"])

    with tab_anh_3:
        st.subheader("Nội dung Song ngữ Anh - Việt")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        cols = st.columns(5)
        for i, c in enumerate(cols, 1):
            with c: st.image(LINK_ANH_MAU, caption=f"Ảnh {i}")

    with tab_tay_3:
        st.subheader("🌾 Nội dung Tiếng Tày - Việt")
        v1, v2 = st.columns(2)
        with v1:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
        with v2:
            st.video(LINK_YOUTUBE_MAU)
            st.video(LINK_YOUTUBE_MAU)
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

with tab4:
  st.header("Trang nội dung Tab 4")

  # 1. Bốn khung văn bản (chia thành các đoạn hoặc dùng st.info/st.markdown để tạo khung)
  st.markdown("### 📝 Các phần nội dung chính")

  st.info(
      "Giới thiệu; https://vi.wikipedia.org/wiki/T%C3%ADnh_t%E1%BA%A9u."
          "Tính tẩu (hay tinh tẩu) (còn gọi là đàn Tính hay đàn Tẩu) (Hán-Việt: thiên cầm) là nhạc cụ của người Choang ở Trung Quốc , người Tày, người Nùng, người Thái ở Việt Nam và vài vùng thuộc Lào, Thái Lan người ta nhận thấy cũng có nhạc cụ này. Trong tiếng Tày, tính đọc chệch từ chữ thiên (天, tiān) có nghĩa là trời nhưng người Tày cố dịch từ đó là đàn, còn tẩu là bầu (quả bầu), dịch ra tiếng Việt, tính tẩu có nghĩa là đàn then. Để khỏi nhầm lẫn với loại đàn bầu của người miền xuôi, nhiều "
          "người gọi tính tẩu là đàn tính nhưng nếu dịch ra đàn bầu thì sai. Do đó chỉ cần hiểu đàn tính là cách gọi tắt của đàn tính tẩu."
          "Đối với dân tộc Choang ở Trung Quốc hay người Tày ở Việt Nam thì đàn tính là nhạc cụ chính dùng để độc tấu, đệm hát và chơi giai điệu múa. Khi đệm hát, đàn tính  thường chơi giai điệu của lời ca. Trong nhạc múa thiên cầm của dân tộc Choang có những bài bản riêng.")

  st.success(
      "Truyền thuyết:   Trong truyền thuyết lưu truyền của dân tộc Tày, sự tích kể về nguồn gốc ra đời cây đàn tính rằng, xưa kia có một chàng trai nghèo không lấy được vợ, thời gian trôi qua, bỗng một hôm ra suối chàng nhìn xuống nước thấy khuôn mặt mình đã trở nên già nua. Buồn phiền với thân phận của mình, chàng ao ước có được một cây đàn để tâm giao những lúc cô đơn. Sau đó, chàng lên trời xin ban cho hạt quả bầu, cho giống cây dâu để nuôi tằm. Khi đã có quả bầu nậm, có tơ tằm, chàng trai đã chế tác ra cây đàn tính. Cây đàn này có 12 dây nhưng mỗi khi chàng gẩy đàn thì những tâm sự u buồn của chàng đã hóa vào âm thanh của tiếng đàn. Sự u buồn khiến cho người và vật nghe thấy mà nao lòng chẳng buồn ăn. Cỏ cây nghe tiếng đàn cũng buồn mà héo úa. Bụt thấy thế vô cùng lo lắng nếu như chàng trai cứ đàn như vậy thì vạn vật sẽ chết hết. Bởi thế, Bụt bắt người chế tác ra cây đàn này phải bỏ bớt đi 9 dây, chỉ còn 3 dây như cây đàn tính bây giờ nên những âm thanh sầu não cũng không còn nữa mà chỉ còn những âm rộn ràng, tươi vui, trầm bổng.(https://baocaobang.vn/Truyen-thuyet-ve-dan-tinh-tau-17867.html)")

  st.warning(
      "Cấu tạo: https://vi.wikipedia.org/wiki/T%C3%ADnh_t%E1%BA%A9u·    Bầu vang (bộ phận tăng âm): làm bằng nửa quả bầu khô (cắt ngang). Kích cỡ bầu vang có thể thay đổi tùy theo quả bầu lớn nhỏ, song đường kính thường tư 15 đến 25 cm. Để có độ vang, âm sắc chuẩn người ta thường chọn quả bầu tròn và dày đều để làm bầu vang. Mặt đàn thường làm bằng gỗ cây ngô đồng xẻ mỏng khoảng 3mm. Trên mặt đàn có khoét 2 lỗ hình hoa thị để thoát âm (trước kia 2 lỗ hoa thị được khoét ở phía sau bầu đàn). Ngựa đàn tương đối nhỏ nằm trên mặt đàn. Cần đàn: bằng gỗ, thường là gỗ dâu hay gỗ thừng mục, nhẹ và thẳng. Cần đàn dài khoảng 9 nắm tay của người chơi đàn. Theo kinh nghiệm dân gian, số đo cỡ nào thì hợp với cỡ giọng hát của người có số đo ấy. Phần dưới của cần đàn xuyên qua bầu vang, còn phần trên cùng là đầu đàn uốn cong hình lưỡi liềm hoặc đầu rồng, đầu phượng … Mặt cần đàn trơn, không có phím như đàn tam. Hốc luồn dây có 2 hoặc 3 trục dây.")

  # 2. Thêm âm thanh (Audio) từ máy tính


  # 3. Hiển thị 3 ảnh (có thể dùng st.columns để xếp ngang 3 ảnh cho đẹp)
  st.markdown("### 🖼️ Hình ảnh minh họa sản phẩm/hoạt động")
  col1, col2, col3 = st.columns(3)

  # Thay tên file ảnh 'anh1.jpg', 'anh2.jpg', 'anh3.jpg' bằng ảnh thực tế của em
  with col1:
      st.image(
          "https://via.placeholder.com/500x300.png?text=Anh+1",
          caption="Ảnh minh họa 1",
          use_container_width=True,
      )
  with col2:
      st.image(
          "https://via.placeholder.com/500x300.png?text=Anh+1",
          caption="Ảnh minh họa 2",
          use_container_width=True,
      )
  with col3:
      st.image(
          "https://via.placeholder.com/500x300.png?text=Anh+1",
          caption="Ảnh minh họa 3",
          use_container_width=True,
      )