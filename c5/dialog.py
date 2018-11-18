# coding: utf-8
# version 3.7.1
# ダイアログを表示する為に必要なモジュール
import tkinter.messagebox as mb

# ダイアログを表示
ans = mb.askyesno("質問","ラーメンは好きですか？")

if ans == True:
    # OKボタンがあるだけのダイアログ
    mb.showinfo("同意","僕も好きです")
else:
    mb.showinfo("本当？","まさかラーメンが嫌いだなんて！")

