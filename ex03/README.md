# 第3回
## 迷えるこうかとん(ex03/maze.py)
## 注意：make_mazeも変更しています！！また、small_coin.pngをfigの中に入れてから実行してください。

### 画面に表示されているコインを制限時間内に全部取得してください!!
![image](https://user-images.githubusercontent.com/85730896/205853981-5063f8c4-b37c-4f09-b9e1-e4136ef783a0.PNG)

### ゲーム概要詳細
- ex03/maze.pyを実行すると，1500x900のcanvasに道とコインが設置されるのでコインを全部取れたらクリアのゲームです。
- 実行するたびに道とコインの位置が変わります
- 時間制限があり、上のバーがなくなると時間切れです
- Game Over, Game Clearした場合にメッセージボックスが出てきてokを押すとウィンドウが閉じます。

### 操作方法
- 矢印キーで上下左右に動くことができます

### 追加機能
- マップ上のランダムな位置にコインを追加(ランダムに選んだ位置が壁だった場合周辺の4マスを探索して空いてるマスに配置)
- コインが配置してあるマスに移動したときコインを削除する
- コインをすべて回収したらGame Clearとメッセージボックスを表示
- 時間制限バーの設定(時間に応じて長方形のサイズが変化していくように設定)
- 時間制限が来たら警告のメッセージボックスを表示
- 迷路サイズの変更(15x9マスから30x18マスに)

### ToDo
- [ ] 現在の取得コイン枚数の表示
- [ ] 難易度の選択画面
