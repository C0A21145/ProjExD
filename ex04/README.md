# 第四回
## 逃げろこうかとん(ex04/dodge_bomb.py)
![概要](https://user-images.githubusercontent.com/85730896/207261444-2b8da8ba-020d-4256-a47e-2f31e3ac4e81.PNG)
## 必要モジュール
- math
- random
- time
- pygame
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると、1600x900のスクリーンに草原が描画され、こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する

### 操作方法
- 矢印キーでこうかとんを上下左右に移動する

### 追加機能
- 爆弾に触れた際にゲームオーバー画面を表示する
- ゲームオーバーになった際スペースキーを押すと再チャレンジすることができる
- アイテムとしてマップ上に盾が生成される。爆弾の衝突を一度無効化してくれる。
- 右上の残り時間が0になったらゲームクリア画面に遷移する。
- 爆弾の大きさを大きくした。

### ToDo
- [ ] 爆弾が爆発したエフェクトを付ける
- [ ] 盾が壊れるエフェクトを付ける
- [ ] 爆弾の挙動をカスタマイズする。