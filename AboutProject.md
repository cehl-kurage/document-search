# 妄想ディレクトリ構成
- src/: メインのアルゴリズムはここに実装
    - examples/: 運用のヒントになるような仮実装を配置
    - scripts/: 直接実行するpythonファイルを配置する
    - models/: アルゴリズムを実行するためのモデル・パイプラインが定義される場所
    - main.py: アルゴリズムのエントリポイントになるファイル
- tests/
    - scripts/: 
    - models/: 
- configs/: hydraによってこのディレクトリ以下の設定が読み込まれます。
    - config.yaml
        検索に使用するモデルや`gradio`の設定を指定します。
    - models/: 各検索モデルの設定を指定します。
        - OpenAI_searcher.yaml
        ...
