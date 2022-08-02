# tem1
hoge



(1)WinHTTPに関するプロキシ設定

・プロキシ情報の設定削除
　　netsh winhttp reset proxy

・プロキシ情報の設定実施
　　netsh winhttp set proxy proxy-server="proxy.****.go.jp:3128"

・設定したプロキシ情報を表示
　　netsh winhttp show proxy
　　※プロキシサーバーがproxy.****.go.jp: 3128 になっていることをご確認ください。
