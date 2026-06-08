import streamlit as st

# Cấu hình giao diện ứng dụng chuyên nghiệp
st.set_page_config(page_title="Tool Hướng Dẫn Photoshop", page_icon="🖥️", layout="centered")

st.title("🖥️ HỆ THỐNG ĐIỀU PHỐI QUY TRÌNH PHOTOSHOP")
st.markdown("#### *Cẩm nang xử lý Stencil, Alignment & Căn theo đường gióng Margin dành cho Newbie*")
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
    product_size_type = st.selectbox("Kích thước sản phẩm (Product Size):", [
        "Normal (Cho phép co kéo ảnh)",
        "Keep original product size (GIỮ NGUYÊN CỠ SẢN PHẨM - KHÔNG CO KÉO ẢNH)"
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
    
    if product_size_type == "Keep original product size (GIỮ NGUYÊN CỠ SẢN PHẨM - KHÔNG CO KÉO ẢNH)":
        st.error("🚨 LƯU Ý ĐẶC BIỆT: Hệ thống yêu cầu 'Keep original product size' ➡️ TUYỆT ĐỐI KHÔNG DÙNG CTRL+T TRÊN LỚP ẢNH SẢN PHẨM. Giữ nguyên kích cỡ ban đầu của ảnh gốc!")
    else:
        st.success("QUY TẮC: Giữ sản phẩm đứng yên để không lệch bóng đổ. Bắt Stencil di chuyển theo sản phẩm!")
        
    st.write("1. **Khóa liên kết sản phẩm:** Nhấn giữ `Ctrl` chọn đồng thời 3 layer: **Product**, **Retouch BG**, và **Shadow** (nếu có) $\rightarrow$ Click chuột phải chọn **Link Layers** (đảm bảo khối này đứng im, đồng bộ cùng nhau).")
    st.write("2. **Gặp vùng chọn của Sản phẩm làm gốc:** Nhấn giữ phím `Ctrl` + click chuột trái vào ô ảnh thu nhỏ (**Thumbnail**) của layer **Product** để tạo đường kiến bò bao quanh sản phẩm gốc.")

    # Bước 3: Căn Stencil chạy theo Sản phẩm
    st.markdown("#### 🟦 BƯỚC 3: CĂN LAYER STENCIL THEO VÙNG CHỌN SẢN PHẨM")
    st.write("- Kích chọn vào layer **Stencil**. Dùng công cụ Move Tool (V) và nhìn lên thanh tùy chọn công cụ (Align) phía trên cùng của Photoshop:")
    
    if "Center" in alignment:
        st.info("➡️ Bấm nút **Align Horizontal Centers** và **Align Vertical Centers** để bắt layer STENCIL tự động nhảy vào CHÍNH GIỮA sản phẩm gốc.")
    elif "Vertical" in alignment:
        st.info("➡️ Bấm nút **Align Vertical Centers** để layer STENCIL tự động căn giữa theo CHIỀU DỌC của sản phẩm.")
    elif "Horizontal" in alignment:
        st.info("➡️ Bấm nút **Align Horizontal Centers** để layer STENCIL tự động căn giữa theo CHIỀU NGANG của sản phẩm.")

    # Bước 4: Luật co kéo ảnh theo đường gióng Guides (Margin)
    st.markdown("#### 🟨 BƯỚC 4: LUẬT CO KÉO SẢN PHẨM THEO ĐƯỜNG GIÓNG (MARGIN)")
    
    st.warning("⚠️ QUY TẮC PHẢI THUỘC LÒNG: Khi dùng lệnh `Ctrl + T` để co kéo, phải kéo ở 4 góc góc ảnh để giữ nguyên tỷ lệ, TUYỆT ĐỐI KHÔNG làm bóp méo, hư hình dáng sản phẩm!")
    
    st.success("💡 MẸO CAO THỦ GIÚP CĂN ĐÚNG LỀ 100%: Khi bấm `Ctrl + T`, hãy bật và di chuyển cái nút tâm định vị (Reference Point) đặt vào vị trí cạnh đã chuẩn lề/chuẩn biên trước. Sau đó, nhấn giữ phím **Alt** kết hợp kéo góc ảnh đối diện. Ảnh sẽ phóng to/thu nhỏ dồn về phía tâm đó, giúp cạnh còn lại chạm khít vào đường lề (Margin) bên kia cực kỳ chính xác!")

    # Nếu có yêu cầu làm lề thì nhắc mở Guides
    if "Margin not set" not in margin_type:
        st.write(f"- 💡 **MỞ ĐƯỜNG GIÓNG MARGIN:** Vào menu **View > New Guide Layout** (hoặc tạo Guides thủ công) để mở các thước gióng chắn cạnh theo đúng thông số yêu cầu: **{margin_type}**.")

    # Kiểm tra xem có bị khóa kích thước sản phẩm không
    if product_size_type == "Keep original product size (GIỮ NGUYÊN CỠ SẢN PHẨM - KHÔNG CO KÉO ẢNH)":
        st.error("🛑 ĐANG BẬT CHẾ ĐỘ 'KEEP ORIGINAL PRODUCT SIZE':\n\n- **TUYỆT ĐỐI KHÔNG CO KÉO SẢN PHẨM.**\n\n- **Hành động:** Bạn chỉ được phép bấm chọn duy nhất layer **Stencil**, dùng lệnh `Ctrl + T` co kéo gá miếng Stencil này sao cho vừa khít theo phom sản phẩm/hoặc đụng các đường Guides, giữ khối ảnh sản phẩm nguyên vẹn hoàn toàn.")
    else:
        # Nếu được co kéo ảnh bình thường, áp dụng logic thế ảnh cắt cạnh
        if image_status == "Ảnh nguyên vẹn (Không bị cắt)":
            if "Margin not set" in margin_type:
                st.write("- **Cách làm:** Co kéo toàn bộ khối ảnh sao cho nằm gọn gàng trong khung Stencil đã căn giữa.")
            else:
                st.write("- **Cách làm:** Nhấn `Ctrl + T` điều chỉnh khối sản phẩm (giữ đúng tỷ lệ ảnh) sao cho **TẤT CẢ CÁC CẠNH đều đụng vừa khít vào các đường Guides (Margin)** vừa mở.")
                
        elif image_status == "Ảnh bị CẮT 1 CẠNH":
            st.error("🚨 THẾ ẢNH: BỊ CẮT MẤT 1 CẠNH")
            st.write("- ➡️ **Cạnh bị cắt cụt:** Dùng `Ctrl + T` kéo lớn ảnh đồng tỷ lệ cho cạnh cụt này **tràn hẳn ra ngoài mép biên Canvas** (Mép ngoài cùng của file ảnh).")
            st.write("- ➡️ **Các cạnh KHÔNG bị cắt:** Áp dụng mẹo ghim tâm định vị, giữ `Alt` kéo cho cạnh không bị cắt **đụng vừa khít vào đường Guides (Margin)** quy định.")

        elif image_status == "Ảnh bị CẮT 2 CẠNH LIỀN KỀ":
            st.error("🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH LIỀN KỀ")
            st.write("- ➡️ **2 cạnh bị cắt cụt:** Kéo **tràn hẳn ra ngoài mép biên ngoài cùng của Canvas**.")
            st.write("- ➡️ **Các cạnh KHÔNG bị cắt còn lại:** Dùng mẹo giữ `Alt` điều chỉnh sao cho **đụng vừa khít vào đường Guides (Margin)** để bảo đảm thẩm mỹ.")

        elif image_status == "Ảnh bị CẮT 2 CẠNH ĐỐI DIỆN":
            st.error("🚨 THẾ ẢNH: BỊ CẮT 2 CẠNH ĐỐI DIỆN")
            st.write("- ➡️ **2 cạnh bị cắt đối diện:** TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM LỀ Ơ CHỖ CỤT. Nhấn `Ctrl + T` kéo lớn ảnh, bắt **cả 2 cạnh bị cắt cụt này phải TRÀN RA và CHẠM VỪA KHÍT vào mép biên Canvas**.")
            st.write("- ➡️ **Các cạnh còn lại (Không bị cắt):** Nếu hệ thống yêu cầu, điều chỉnh ghim tâm giữ `Alt` cho chúng **đụng sát vào đường Guides (Margin)**.")

        elif image_status == "Ảnh bị CẮT 3 CẠNH":
            st.error("🚨 THẾ ẢNH: BỊ CẮT 3 CẠNH")
            st.write("- ➡️ **3 cạnh bị cắt cụt:** Kéo cho **tràn hết ra ngoài rìa biên Canvas** để giấu vết nấc cụt.")
            st.write("- ➡️ **Duy nhất 1 cạnh KHÔNG bị cắt:** Nhấn `Ctrl + T` ghim tâm định vị ở biên Canvas, giữ `Alt` kéo góc ảnh sao cho cạnh nguyên vẹn này **đụng sát vào đường Guides (Margin)**.")

        elif image_status == "Ảnh bị CẮT 4 CẠNH":
            st.error("🚨 THẾ ẢNH: BỊ CẮT CẢ 4 CẠNH")
            st.write("- **Cách làm:** Bỏ qua thước gióng Margin. Dùng công cụ Crop (C) cắt lẹm thẳng vào trong sản phẩm, bắt cả 4 cạnh tràn biên Canvas và tập trung giữ khu vực trung tâm nổi bật nhất.")

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
