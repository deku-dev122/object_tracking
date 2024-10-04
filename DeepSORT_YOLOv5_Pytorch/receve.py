import socket
import cv2
import numpy as np
import os

# 保存先のディレクトリを指定
SAVE_DIR = "uploaded_images"

# ディレクトリが存在しない場合は作成
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# フラグの初期値をFalseに設定（外部から変更されることを想定）
save_image_flag = False

def receive_image(server_socket):
    conn, addr = server_socket.accept()  # クライアントの接続を受け入れる
    print(f"Connected by {addr}")
    
    # 画像データの受信
    data = b""
    while True:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet

    conn.close()

    # 画像データをnumpy配列に変換
    img_array = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if img is None:
        print("Failed to decode image")
        return None

    # 画像を保存するかどうかのフラグに基づいて保存
    if save_image_flag:
        filename = os.path.join(SAVE_DIR, "uploaded_image.jpg")
        cv2.imwrite(filename, img)
        print(f"Image saved as {filename}")

    return img

def start_server(flag):
    global save_image_flag
    save_image_flag = flag  # 外部から渡されたフラグに応じて画像を保存するかどうか決定

    # ソケットサーバーのセットアップ
    HOST = '192.168.128.111'  # すべてのインターフェースで接続を待ち受ける
    PORT = 5000       # ポート番号

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        # 画像受信の処理
        img = receive_image(server_socket)
        
        return img  # ndarray形式で画像を返す

if __name__ == "__main__":
    # 例として、画像保存フラグをTrueに設定してサーバーを開始
    image = start_server(True)
    if image is not None:
        print("Image received and processed.")
