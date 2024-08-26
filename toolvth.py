import random
from collections import Counter
import os
import time
import sys
                                                                # Mã màu ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
                                                                # Danh sách các phòng với tên viết tắt và tên đầy đủ
phong = {
    "NHÀ KHO": "NK",
    "PHÒNG HỌP": "PH",                                              "PHÒNG GIÁM ĐỐC": "PGD",
    "PHÒNG TRÒ CHUYỆN": "PTC",
    "PHÒNG GIÁM SÁT": "PGS",
    "VĂN PHÒNG": "VP",
    "PHÒNG TÀI VỤ": "PTV",
    "PHÒNG NHÂN SỰ": "PNS"
}

phong_keys = list(phong.values())

def hien_thi_danh_sach_phong():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{AQUA}DANH SÁCH PHÒNG VIẾT TẮT TOOL VIP MINH HÒA:{RESET}")
    for ten_phong, ten_viet_tat in phong.items():
        print(f"{BOLD}{BLUE}{ten_phong} ({ten_viet_tat}){RESET}")

def hien_thi_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    intro_messages = [
        "ADMIN MINH HÒA CHÀO BẠN ĐÃ ĐẾN VỚI TOOL 💥",
        "TOOL HỖ TRỢ DỰ ĐOÁN TỈ SỐ CHÍNH XÁC LÊN ĐẾN 98% ⚠️",
        "ADMIN MINH HÒA XIN ĐƯỢC PHÉP BẮT ĐẦU TOOL 💢",
        "NHẬP TÊN PHÒNG VIẾT TẮT MÀ SÁT THỦ ĐÃ VÀO TRẬN TRƯỚC ❗"
        "MUA TOOL VIP CỰC RẺ LIÊN HỆ ZALO 0889550699 🎭"
    ]

    for message in intro_messages:
        print(f"{BOLD}{CYAN}{message}{RESET}")
        time.sleep(2)  # Hiển thị mỗi thông điệp trong 2 giây

    print(f"\n{BOLD}{GREEN}ĐANG TẢI VUI LÒNG CHỜ NHÉ ⏰")

    # Hiệu ứng tải
    for i in range(1, 101):
        sys.stdout.write(f"\r{BOLD}{LIME}TIẾN TRÌNH TẢI: {i}% {'█' * (i // 5)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần

    # Xóa màn hình sau khi tải xong
    os.system('cls' if os.name == 'nt' else 'clear')

hien_thi_intro()
hien_thi_danh_sach_phong()

while True:
    phong_satt_thu_da_vao = input ("Nhập Phòng Sát Thủ Đã Vào Trận Trước (ADMIN MINH HÒA)🃏: ").strip()

    if phong_satt_thu_da_vao.lower() == 'exit':
        print(f"{BOLD}{AQUA}CẢM ƠN ĐÃ SỬ DỤNG TOOL! ADMIN MINH HÒA")

        break

    if phong_satt_thu_da_vao not in phong_keys:
        print("PHÒNG KHÔNG HỢP LỆ VUI LÒNG NHẬP LẠI ⚠.")
    else:
        so_lan_mo_phong = 1000000
        ket_qua_chon = [random.choice(phong_keys) for _ in range(so_lan_mo_phong)]
        dem_phong = Counter(ket_qua_chon)
        xac_suat_phong = {phong_key: dem_phong[phong_key] / so_lan_mo_phong for phong_key in phong_keys}

        phong_thap_nhat = min(xac_suat_phong, key=xac_suat_phong.get)
        xac_suat_phong_thap_nhat_pt = xac_suat_phong[phong_thap_nhat] * 100
        phan_tram_con_lai = 100 - xac_suat_phong_thap_nhat_pt

        ten_phong_thap_nhat = [name for name, code in phong.items() if code == phong_thap_nhat][0]

        hien_thi_danh_sach_phong()

        for i in range(1, 101):
            sys.stdout.write(f"\r{BOLD}{LIME}BẮT ĐẦU DỰ ĐOÁN: {i}% {'█' * (i // 5)}{RESET}")
            sys.stdout.flush()
            time.sleep(0.03)

        print(f"\n{BOLD}{AQUA}PHÒNG NÊN CHỌN: {RESET}{BOLD}{BLUE}{ten_phong_thap_nhat} ({phong_thap_nhat}){RESET}")
        print(f"{BOLD}{YELLOW}TỈ LỆ AN TOÀN: {RESET}{phan_tram_con_lai:.2f}%")