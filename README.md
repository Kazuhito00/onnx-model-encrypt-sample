# onnx-model-encrypt-sample
ONNXモデルを[pyca/cryptography](https://github.com/pyca/cryptography)を用いて暗号化/復号化するサンプルです。<br>
※Pythonスクリプトで実施する都合上、気休め程度です。<br>　セキュリティを考慮した運用を考える場合、復号化するプログラムはC++等で実行ファイルを作成することをおすすめします。

# Requirement 
* cryptography 36.0.2 or later
* onnxruntime 1.10.0 or later

# Usage
サンプルの実行方法は以下です。<br>
各プログラムを実行後に任意のパスワードを入力してください。<br>
暗号化実施時には「resnet50-v1-12.dat」(ONNXモデルを暗号化したもの)を出力し<br>
復号化実施時には「resnet50-v1-12.dat」を読み込みます。
```bash
python encrypt_sample.py 
Password:
```
```bash
python decrypt_sample.py
Password:
```

# Reference
* [pyca/cryptography](https://github.com/pyca/cryptography)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
onnx-model-encrypt-sample is under [Apache-2.0 License](LICENSE).

