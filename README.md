# hakuchumu
WEBアプリケーションのテストコード自動生成ツール

## 使用用法
- chromedriverをダウンロード
- テスト対象のディレクトリを引数に起動<pre><code>python main.py hoge</code></pre>
- テスト対象にディレクトリにそのプロジェクトでアクセスしうるURLのリストを作成してください

## 出力(上から順番にミクロ)
- セッタリスト
- アクションリスト(入力クリックなどできればブラウザのonclickとかonchangeのようなイベント毎)
- テストコード

## のちにDBに出力結果をプールする予定だがいまは保留 