import streamlit as st

# Cấu hình giao diện ứng dụng chuyên nghiệp
st.set_page_config(page_title="Tool Hướng Dẫn Photoshop", page_icon="🖥️", layout="centered")

st.title("🖥️ HỆ THỐNG ĐIỀU PHỐI QUY TRÌNH PHOTOSHOP")
st.markdown("#### *Cẩm nang xử lý Stencil, Alignment & Chống lệch bóng dành cho Newbie*")
st.write("---")

# 1. PHẦN NHẬP DỮ LIỆU ĐẦU VÀO
st.markdown("### 📥 1. NHẬP THÔNG SỐ TỪ HỆ THỐNG")

col1, col2 = st.columns(2)

with col1:
    width = st.number_input("Chiều rộng (Width px):", min_value=1, value=2429, step=100)
    height = st.number_input("Chiều cao (Height px):", min_value=1, value=2931, step=100)
    alignment = st.selectbox("Kiểu căn chỉnh (Alignment):", [
        "Center (Căn giữa toàn bộ)", 
        "Vertical Alignment (Căn theo chiều dọc)", 
        "Horizontal Alignment (Căn theo chiều ngang)"
    ])

with col2:
    margin_type = st.selectbox("Yêu cầu về Lề (Margins):", [
        "Margin not set (Không thiết lập lề)", 
        "Margins in Pixels (Lề bằng Pixel)", 
        "Margins in Percent (Lề bằng %)"
    ])
    
    bg_check = st.selectbox("Yêu cầu Nền (Background Check):", [
        "Transparent / Filled Color (Nền trong suốt / Có màu cố định)", 
        "Background Check (Yes) - Thiếu hụt nền sau khi căn", 
        "Background Check (No) - Nền đầy đủ, phù hợp"
    ])

# Thêm phần chọn thế ảnh trực quan để bốc thuốc
image_status = st.selectbox("⚠️ QUAN TRỌNG: Nhìn ảnh gốc xem bị CẮT CẠNH thế nào?", [
    "Ảnh nguyên vẹn (Không bị cắt)",
    "Ảnh bị CẮT 1 CẠNH",
    "Ảnh bị CẮT 2 CẠNH LIỀN KỀ",
    "Ảnh bị CẮT 2 CẠNH ĐỐI DIỆN",
    "Ảnh bị CẮT 3 CẠNH",
    "Ảnh bị CẮT 4 CẠNH"
])

st.write("---")

# 2. PHẦN XUẤT KẾT QUẢ HƯỚNG DẪN
if st.button("🚀 XUẤT HƯỚNG DẪN CÁCH LÀM (BẤM VÀO ĐÂY)", type="primary"):
    
    st.markdown("### 📋 2. BẢN HƯỚNG DẪN THAO TÁC CHI TIẾT")
    st.warning("Yêu cầu nhân viên đọc kỹ từng bước dưới đây và làm theo, tuyệt đối không làm mò!")

    # Bước 1: Kích thước
    st.markdown("#### 🟩 BƯỚC 1: CÀI ĐẶT CANVAS (KÍCH THƯỚC KHUNG)")
    st.info(f"Vào menu **Image > Canvas Size** chỉnh kích thước chuẩn xác: **{width} x {height} pixel**. Đảm bảo hệ màu là **RGB Color / 8 bit**.")

    # Bước 2: CĂN CHỈNH NÂNG CAO - CHỐNG LỆCH BÓNG (Mục mới cập nhật)
    st.markdown("#### 🎯 BƯỚC 2: CĂN KHỚP STENCIL & SẢN PHẨM (CHỐNG LỆCH BÓNG)")
    st.success("Để sản phẩm không bị lệch so với bóng đổ (Shadow) và lớp nền (Retouch BG), nhân viên BẮT BUỘC thực hiện kỹ thuật sau:")
    st.write("1. **Liên kết các Layer:** Nhấn giữ phím `Ctrl` và bấm chọn đồng thời cả 3 layer: **Product**, **Retouch BG**, và cả layer **Shadow** (nếu có).")
    st.write("2. **Liên kết tạm thời (Link Layers):** Click chuột phải $\rightarrow$ Chọn **Link Layers** (hoặc bấm biểu tượng mắt xích dưới đáy bảng Layer) để khóa chặt 3 lớp này đi liền với nhau.")
    st.write("3. **Căn dựa theo Stencil:** Nhấn giữ `Ctrl` + click vào ảnh thu nhỏ (Thumbnail) của layer **Stencil** để gọi vùng chọn bao quanh Stencil.")
    st.write("4. **Thực hiện di chuyển:** Dùng công cụ Move Tool (V) di chuyển nhóm layer đã link sao cho khớp chuẩn xác hoàn toàn vào khung Stencil, đảm bảo phần bóng và sản phẩm dịch chuyển đồng bộ, không bị tách rời nhau làm lệch bóng.")

    # Bước 3: Căn chỉnh vị trí tổng thể
    st.markdown("#### 🟦 BƯỚC 3: CĂN CHỈNH VỊ TRÍ TỔNG THỂ (ALIGNMENT)")
    if "Center" in alignment:
        st.write("- Sau khi đã link các layer ở Bước 2, bấm nút **Align Center** trên thanh công cụ để đưa toàn bộ khối đối tượng vào chính giữa khung hình theo cả 2 trục dọc và ngang.")
    elif "Vertical" in alignment:
        st.write("- Chỉ sử dụng tính năng căn chỉnh đối tượng theo **chiều dọc** (trên / dưới).")
    elif "Horizontal" in alignment:
        st.write("- Chỉ sử dụng tính năng căn chỉnh đối tượng theo **chiều ngang** (trái / phải).")

    # Bước 4: Luật co kéo ảnh bị cắt cạnh
    st.markdown("#### 🟨 BƯỚC 4: LUẬT XỬ LÝ CẠNH CẮT & LỀ (MARGINS)")
    
    if image_status == "Ảnh nguyên vẹn (Không bị cắt)":
        if "Margin not set" in margin_type:
            st.write("- **Quy tắc:** Co kéo toàn bộ Canvas nằm gọn trong khung Stencil và canh giữa.")
        else:
            st.write(f"- **Quy tắc:** Tạo khoảng cách lề an toàn chuẩn xác theo thông số yêu cầu: **{margin_type}**.")
            
    elif image_status == "Ảnh bị CẮT 1 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 1 CẠNH (Ví dụ cụt đuôi bên phải)")
        st.write("- **Quy tắc cốt lõi:** KHÔNG làm lề cho cạnh bị cắt.")
        st.write("- **Cách làm tay:** Nhấn `Ctrl + T` phóng to khối sản phẩm đã liên kết lên sao cho **cạnh bị cắt chạm vừa khít/bo sát vào biên tương ứng của Canvas**. Cạnh đối diện không bị cắt thì lùi vào trong tự nhiên.")
        if "Margin not set" in margin_type:
            st.write("- *Lưu ý nâng cao:* Ưu tiên căn theo sản phẩm, co kéo toàn bộ Canva nằm trong khung Stencil.")

    elif image_status == "Ảnh bị CẮT 2 CẠNH LIỀN KỀ":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH LIỀN KỀ")
        st.write("- **Quy tắc cốt lõi:** Chỉ làm lề cho **1 trong 2 cạnh còn nguyên vẹn** (cạnh không bị cắt).")
        st.write("- **Cách làm tay:** Đẩy 2 cạnh bị cắt ra chạm sát biên Canvas.")

    elif image_status == "Ảnh bị CẮT 2 CẠNH ĐỐI DIỆN":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH ĐỐI DIỆN")
        st.write("- **Quy tắc cốt lõi:** KHÔNG làm lề cho cả 2 cạnh còn lại.")

    elif image_status == "Ảnh bị CẮT 3 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 3 CẠNH")
        st.write("- **Quy tắc cốt lõi:** KHÔNG làm lề cho duy nhất cạnh còn lại.")
        st.write("- **Cách làm tay:** Ưu tiên lấy diện tích sản phẩm nhiều nhất và giữ phần viền của cạnh không bị cắt.")

    elif image_status == "Ảnh bị CẮT 4 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT CẢ 4 CẠNH")
        st.write("- **Quy tắc cốt lõi:** Sử dụng công cụ Crop (C) cắt lẹm bớt vào trong sản phẩm.")
        st.write("- **Cách làm tay:** Tập trung giữ lại khu vực nổi bật nhất và có nhiều chi tiết đắt giá của sản phẩm.")

    # Bước 5: Chỉ định Action bổ trợ hở trắng
    st.markdown("#### 🟥 BƯỚC 5: KIỂM TRA NỀN & BẬT ACTION HỖ TRỢ")
    if "Yes" in bg_check or image_status != "Ảnh nguyên vẹn (Không bị cắt)":
        st.error("⚠️ PHÁT HIỆN NỀN BỊ THIẾU HOẶC HỞ TRẮNG DO CO KÉO CẠNH CẮT!")
        st.success("➡️ **HÀNH ĐỘNG BẮT BUỘC:** Sau khi co kéo xong, nhân viên phải chạy ngay **'Action chống hở trắng cạnh cắt'** để xử lý mượt mà phần rìa biên!")
    else:
        st.write("- Kiểm tra lại bằng mắt, nếu phông nền đã khít và đủ thì không cần chạy Action hỗ trợ.")

    # Bước 6: Cấu trúc layer chuẩn trước khi lưu
    st.markdown("#### 🗂️ BƯỚC 6: ĐỒNG BỘ CẤU TRÚC LAYER")
    st.write("- Kiểm tra bảng điều khiển Layers trong Photoshop, đảm bảo đặt đúng tên và phân nhóm theo đúng quy định:")
    st.code("Variant (Thư mục chính)\n  └── Item / Color (Thư mục con)\n        ├── Stencil (Layer vùng chọn)\n        ├── Retouch / Retouch BG (Layer nền)\n        └── Product (Layer sản phẩm tách biệt)")
    
    st.write("---")
    st.success("✔️ Mọi thứ hoàn hảo! Tiến hành lưu file PSD và hoàn thành nhiệm vụ.")
