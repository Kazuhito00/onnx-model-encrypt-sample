import base64

import onnxruntime
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def decrypt(
    encryp_data,
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

    # 復号化
    decrypt_data = None
    try:
        decrypt_data = fernet.decrypt(encryp_data)
    except InvalidToken:
        print('Invalid Password')

    return decrypt_data


def main():
    # 暗号化したデータの読み込み
    with open('resnet50-v1-12.dat', 'rb') as f:
        encryp_data = f.read()

    # パスワード入力
    password_text = input('Password:')

    # 復号化
    decrypt_data = decrypt(encryp_data, password_text)

    # 復号化したONNXモデルの読み込み確認
    if decrypt_data is not None:
        onnx_session = onnxruntime.InferenceSession(
            decrypt_data,
            providers=['CPUExecutionProvider'],
        )
        print(onnx_session.get_inputs()[0])
        print(onnx_session.get_outputs()[0])


if __name__ == '__main__':
    main()
