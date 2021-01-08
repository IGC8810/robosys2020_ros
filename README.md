# robosys2020_ros

## 概要
ロボットシステム学の課題．ROSでパッケージの作成を行った．<br>
publish.pyは，1[Hz]周期で文字列(Hello World!!)を投げる．
subscribe.pyは，Wordという名前のトピックを購読し，ターミナルに表示する．

## 動作環境
* OS : ubuntu20.04
* ROSdistro : noetic

## 実行コマンド

```
$ roscore
```
```
$ rosrun robosys2020_ros publish.py
```
```
$ rosrun robosys2020_ros subscribe.py
```
## 動画
* [Youtube]()

## 参考
* [ロボットシステム学 第10回](https://www.youtube.com/watch?v=PL85Pw_zQH0)
