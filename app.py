import streamlit as st

# Cấu hình giao diện ứng dụng chuyên nghiệp
st.set_page_config(page_title="Tool Hướng Dẫn Photoshop", page_icon="🖥️", layout="centered")

st.title("🖥️ HỆ THỐNG ĐIỀU PHỐI QUY TRÌNH PHOTOSHOP")
st.markdown("#### *Cẩm nang xử lý Stencil, Alignment & Lấy Sản phẩm làm gốc dành cho Newbie*")
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

    # Bước 2: Khóa sản phẩm làm gốc cố định
    st.markdown("#### 🎯 BƯỚC 2: CỐ ĐỊNH KHỐI SẢN PHẨM & GỌI VÙNG CHỌN GỐC")
    st.success("QUY TẮC: Giữ sản phẩm đứng yên để không lệch bóng đổ. Bắt Stencil di chuyển theo sản phẩm!")
    st.write("1. **Khóa liên kết sản phẩm:** Nhấn giữ `Ctrl` chọn đồng thời 3 layer: **Product**, **Retouch BG**, và **Shadow** (nếu có) $\rightarrow$ Click chuột phải chọn **Link Layers** (đảm bảo khối này đứng im, đồng bộ cùng nhau).")
    st.write("2. **Gọi vùng chọn của Sản phẩm làm gốc:** Nhấn giữ phím `Ctrl` + click chuột trái vào ô ảnh thu nhỏ (**Thumbnail**) của layer **Product** để tạo đường kiến bò bao quanh sản phẩm gốc.")

    # Bước 3: Căn Stencil chạy theo Sản phẩm
    st.markdown("#### 🟦 BƯỚC 3: CĂN LAYER STENCIL THEO VÙNG CHỌN SẢN PHẨM")
    st.write("- Kích chọn vào layer **Stencil**. Dùng công cụ Move Tool (V) và nhìn lên thanh tùy chọn công cụ (Align) phía trên cùng của Photoshop:")
    
    if "Center" in alignment:
        st.info("➡️ Bấm nút **Align Horizontal Centers** và **Align Vertical Centers** để bắt layer STENCIL tự động nhảy vào CHÍNH GIỮA sản phẩm gốc.")
    elif "Vertical" in alignment:
        st.info("➡️ Bấm nút **Align Vertical Centers** để layer STENCIL tự động căn giữa theo CHIỀU DỌC của sản phẩm.")
    elif "Horizontal" in alignment:
        st.info("➡️ Bấm nút **Align Horizontal Centers** để layer STENCIL tự động căn giữa theo CHIỀU NGANG của sản phẩm.")

    # Bước 4: Luật co kéo Canvas/Lề sau khi đã căn khớp
    st.markdown("#### 🟨 BƯỚC 4: LUẬT XỬ LÝ CẠNH CẮT & LỀ (MARGINS)")
    st.write("- Sau khi Stencil đã căn giữa theo sản phẩm thành công, tiến hành xử lý lề dựa trên thế ảnh gốc:")
    
    if image_status == "Ảnh nguyên vẹn (Không bị cắt)":
        if "Margin not set" in margin_type:
            st.write("- **Quy tắc:** Co kéo toàn bộ Canvas nằm gọn trong khung Stencil đã căn và đưa vào giữa.")
        else:
            st.write(f"- **Quy tắc:** Thiết lập lề chuẩn xác theo thông số yêu cầu: **{margin_type}**.")
            
    elif image_status == "Ảnh bị CẮT 1 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 1 CẠNH (Ví dụ cụt đuôi bên phải)")
        st.write("- **Quy tắc:** KHÔNG làm lề cho cạnh bị cắt.")
        st.write("- **Cách làm tay:** Dùng `Ctrl + T` co kéo Canvas/Khung hình sao cho **cạnh bị cắt chạm vừa khít/bo sát vào biên của Canvas**. Cạnh đối diện không bị cắt thì lùi vào trong tự nhiên.")

    elif image_status == "Ảnh bị CẮT 2 CẠNH LIỀN KỀ":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH LIỀN KỀ")
        st.write("- **Quy tắc:** Chỉ làm lề cho **1 trong 2 cạnh còn nguyên vẹn** (cạnh không bị cắt). Kéo sát các cạnh bị cắt ra biên Canvas.")

    elif image_status == "Ảnh bị CẮT 2 CẠNH ĐỐI DIỆN":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH ĐỐI DIỆN")
        st.write("- **Quy tắc:** KHÔNG làm lề cho cả 2 cạnh còn lại.")

    elif image_status == "Ảnh bị CẮT 3 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT 3 CẠNH")
        st.write("- **Quy tắc:** KHÔNG làm lề cho duy nhất cạnh còn lại. Ưu tiên giữ viền cạnh không bị cắt.")

    elif image_status == "Ảnh bị CẮT 4 CẠNH":
        st.markdown("##### 🚨 THẾ ẢNH: BỊ CẮT CẢ 4 CẠNH")
        st.write("- **Quy tắc:** Dùng công cụ Crop (C) cắt lẹm bớt vào trong sản phẩm, tập trung giữ lại khu vực nổi bật có nhiều chi tiết nhất.")

    # Bước 5: Chỉ định Action bổ trợ hở trắng
    st.markdown("#### 🟥 BƯỚC 5: KIỂM TRA NỀN & BẬT ACTION HỖ TRỢ")
    if "Yes" in bg_check or image_status != "Ảnh nguyên vẹn (Không bị cắt)":
        st.error("⚠️ PHÁT HIỆN NỀN BỊ THIẾU HOẶC HỞ TRẮNG DO CẠNH CẮT CỦA SẢN PHẨM GỐC!")
        st.success("➡️ **HÀNH ĐỘNG BẮT BUỘC:** Chạy ngay **'Action chống hở trắng cạnh cắt'** để lấp đầy và xử lý mượt mà phần rìa biên!")
    else:
        st.write("- Kiểm tra lại bằng mắt, nếu phông nền đã khít và đủ thì không cần chạy Action hỗ trợ.")

    # Bước 6: Cấu trúc layer chuẩn trước khi lưu
    st.markdown("#### 🗂️ BƯỚC 6: ĐỒNG BỘ CẤU TRÚC LAYER")
    st.write("- Kiểm tra bảng điều khiển Layers trong Photoshop, đảm bảo đặt đúng tên và phân nhóm theo đúng quy định:")
    st.code("Variant (Thư mục chính)\n  └── Item / Color (Thư mục con)\n        ├── Stencil (Layer vùng chọn)\n        ├── Retouch / Retouch BG (Layer nền)\n        └── Product (Layer sản phẩm tách biệt)")
    
    st.write("---")
    st.success("✔️ Mọi thứ hoàn hảo! Tiến hành lưu file PSD và hoàn thành nhiệm vụ.")
