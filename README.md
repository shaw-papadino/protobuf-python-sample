# 概要

PythonでProtocol Buffer を扱うためのチュートリアルをやった時のレポジトリ

# 実行環境

- protobuf: stable 3.17.3
- pipenv(python=3.9)

# 試し方


1. `.proto`ファイルをコンパイルするためにProtocol Bufferのコンパイラとなる `protoc`コマンドをインストール
   1. [リリースページ](https://github.com/protocolbuffers/protobuf/releases/tag/v3.17.3)
   2. HomeBrewでinstall
   ```bash
   brew install protobuf
   ```
2. `addressbook.proto` をコンパイル
   ```bash
   protoc --python_out=./proto ./addressbook.proto
   ```
3. pipenvで環境を構築
   ```bash
   pipenv install
   ```
4. オブジェクトをシリアライズ → シリアライズされたbinaryをデシリアライズするだけのプログラム実行
   ```bash
   pipenv run python main.py
   ```

# 参考
[Protocol Buffer Basics: Python](https://developers.google.com/protocol-buffers/docs/pythontutorial)