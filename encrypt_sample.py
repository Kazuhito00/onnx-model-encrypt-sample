import base64

import onnxruntime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(
    data,
    password_text,
    salt=b'salt',
    stretching_iterations=390000,
):
    # ソルト付与・ストレッチング実施用インスタンス生成
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=stretching_iterations,
    )

    # キー生成
    password = password_text.encode("utf-8")
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # Fernetオブジェクトを指定キーで生成
    fernet = Fernet(key)

    # 暗号化
    encrypt_data = fernet.encrypt(data)

    return encrypt_data


def main():
    # ONNXモデルをバイナリモードでロード
    model_path = 'resnet50-v1-12.onnx'
    with open(model_path, 'rb') as onnx_file:
        onnx_data = onnx_file.read()

    # ONNXモデル読み込み確認
    onnx_session = onnxruntime.InferenceSession(
        onnx_data,
        providers=['CPUExecutionProvider'],
    )
    print(onnx_session.get_inputs()[0])
    print(onnx_session.get_outputs()[0])

    # パスワード入力
    password_text = input('Password:')

    # 暗号化
    encrypt_data = encrypt(onnx_data, password_text)

    # 暗号化したデータをファイルに書き込む
    with open('resnet50-v1-12.dat', 'wb') as f:
        f.write(encrypt_data)


if __name__ == '__main__':
    main()
