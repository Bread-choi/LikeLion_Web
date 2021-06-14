from tkinter import *
import pandas as pd
import os
print(os. getcwd())
dat = pd.read_csv("./city.csv", engine='python',encoding='utf-8')


print(dat)
def click():   #제출버튼 클릭시 동작
  print("버튼이 클릭되었어요.")
  word = entry.get()
  output.delete(0.0, END)

  try:
     def_word = dat.loc[dat['용어명'] == word, '용어설명'].values[0]
  except:
     def_word = "단어를 뜻을 찾을 수 없어요."
  output. insert(END, def_word)


window = Tk()
window.title("city")

label = Label(window, text="단어 입력")
label.grid(row=0, column=0, sticky=W)

entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

btn = Button(window, text="제출", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

lable2 = Label(window, text="\n의미:")
lable2.grid(row=3, column=0, sticky=W)

lable2 = Label(window, text="\n의미:")
lable2. grid(row=3, column=1, sticky=W)

output = Text(window, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

window.mainloop()