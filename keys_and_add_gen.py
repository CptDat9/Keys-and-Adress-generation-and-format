import bitcoin  # Thư viện 'bitcoin' được import để sử dụng các hàm và công cụ liên quan đến Bitcoin.

# Tạo khóa riêng tư ngẫu nhiên
valid_private_key = False  # Khởi tạo biến để kiểm tra tính hợp lệ của khóa riêng tư.
while not valid_private_key:  # Vòng lặp kiểm tra tính hợp lệ của khóa riêng tư.
    private_key = bitcoin.random_key()  # Tạo khóa riêng tư ngẫu nhiên dưới dạng chuỗi hexa.
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')  # Giải mã khóa riêng tư từ định dạng hex thành số thập phân.
    valid_private_key = 0 < decoded_private_key < bitcoin.N 
    # Kiểm tra xem khóa riêng tư có hợp lệ không (phải nằm trong khoảng từ 1 đến N của Bitcoin).

# In khóa riêng tư dưới dạng hex và decimal (hệ 10 và hệ 16)
print("Private Key (hex) is: ", private_key)  # In khóa riêng tư ở định dạng hex (mã hexa gồm 64 kí (gồm 32 byte, 1 byte = 8 bit))
print("Private Key (decimal) is: ", decoded_private_key)  # In khóa riêng tư ở dạng số thập phân.

# Chuyển đổi khóa riêng tư sang định dạng WIF (Wallet Import Format)
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')  
# Mã hóa khóa riêng tư ở định dạng WIF để dễ dàng lưu trữ và sử dụng trong ví Bitcoin.
print("Private Key (WIF) is: ", wif_encoded_private_key)  # In khóa riêng tư dưới định dạng WIF.

# Thêm hậu tố "01" để chỉ thị khóa riêng tư nén
compressed_private_key = private_key + '01'  
# Khóa riêng tư nén được tạo bằng cách thêm chuỗi "01" vào cuối khóa riêng tư ban đầu.
print("Private Key Compressed (hex) is: ", compressed_private_key)  # In khóa riêng tư nén dưới dạng hex.

# Tạo định dạng WIF từ khóa riêng tư nén (WIF-compressed)
wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')  
# Chuyển đổi khóa riêng tư nén sang định dạng WIF nén.
print("Private Key (WIF-Compressed) is: ", wif_compressed_private_key)  # In khóa riêng tư nén dưới định dạng WIF nén.

# Nhân điểm sinh G của đường cong Elliptic (EC) với khóa riêng tư để tạo ra điểm khóa công khai
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)  
# Khóa công khai được tạo ra từ phép nhân giữa khóa riêng tư và điểm sinh của đường cong Elliptic.
print("Public Key (x,y) coordinates is:", public_key)  # In tọa độ x, y của khóa công khai.

# Mã hóa khóa công khai dưới dạng hex, thêm tiền tố 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')  
# Mã hóa khóa công khai dưới định dạng hex với tiền tố "04".
print("Public Key (hex) is:", hex_encoded_public_key)  # In khóa công khai dưới dạng hex.

# Nén khóa công khai, thêm tiền tố phụ thuộc vào việc y là số chẵn hay lẻ
(public_key_x, public_key_y) = public_key  # Tách khóa công khai thành hai thành phần x và y.
if (public_key_y % 2) == 0:  # Nếu y là số chẵn, sử dụng tiền tố "02".
    compressed_prefix = '02'
else:  # Nếu y là số lẻ, sử dụng tiền tố "03".
    compressed_prefix = '03'

hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)  
# Mã hóa khóa công khai nén dưới định dạng hex, thêm tiền tố tương ứng.
print("Compressed Public Key (hex) is:", hex_compressed_public_key)  # In khóa công khai nén dưới dạng hex.

# Tạo địa chỉ Bitcoin từ khóa công khai
print("Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(public_key))  
# Chuyển khóa công khai thành địa chỉ Bitcoin thông qua mã hóa Base58.

# Tạo địa chỉ Bitcoin nén từ khóa công khai nén
print("Compressed Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(hex_compressed_public_key))  
# Tạo địa chỉ Bitcoin từ khóa công khai nén và in ra địa chỉ đã nén.
