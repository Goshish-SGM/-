import tkinter as tk
import winsound
from string import ascii_uppercase
import random

def play():
    winsound.PlaySound('mc_music.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

def exit():
    window.destroy()

def generate_rl(x):
    return ''.join(random.choice(ascii_uppercase) for i in range(x))

def generate_key():
    let = l_entry.get()
    if len(let)!=6 or not let.isdigit():
        entry_output.delete(0, tk.END)
        entry_output.insert(0, 'ВВЕДИТЕ 6 ЦИФР!')
        return
    block1 = list(let[3:6])
    block2 = list(let[:3])
    block_let1 = list(generate_rl(2))
    block_let2 = list(generate_rl(2))
    r1=block1+block_let1
    random.shuffle(r1)
    Block1=''.join(r1)
    r2 = block2 + block_let2
    random.shuffle(r2)
    Block2 = ''.join(r2)
    sum=str(int(''.join(block1))+int(''.join(block2)))
    if len(sum)<4:
        while len(sum)<4:
            sum='0'+sum
    Block3=sum
    key=f'{Block1}-{Block2}-{Block3}'
    entry_output.delete(0, tk.END)
    entry_output.insert(0, key)
    return key

window = tk.Tk()
window.title('Generator 3000')
window.geometry('500x500')
window.configure(bg='white')
window.geometry('500x400')
window.resizable(width=False, height=False)
bg_img = tk.PhotoImage(file='minecraft.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

label1=tk.Label(window,
                text='Code Generator 3000',
                font=('Comic Sans MS', 20),
                bg='Orange',
                fg='White')
label1.place(x=105, y=20)

label_input = tk.Label(window,
                       text="Введите 6 цифр:",
                       font=('Comic Sans MS', 12),
                       bg='white')
label_input.place(x=180, y=80)

l_entry=tk.Entry(window, width=20, font=('Comic Sans MS','14'))
l_entry.insert(0, '')
l_entry.place(x=120, y=120)


label_output = tk.Label(window, text="Ваш ключ:", font=('Comic Sans MS', 12), bg='white')
label_output.place(x=200, y=160)

entry_output = tk.Entry(window, width=20, font=('Comic Sans MS', 14), justify='center')
entry_output.place(x=120, y=200)

btn=tk.Button(window,
              text='Generate',
              width=8,
              font=('Comic Sans MS',20),
              bg='orange',
              fg='white',
              command=generate_key)
btn.place(x=175,y=250)

btn=tk.Button(window,
              text='Music',
              width=4,
              font=('Comic Sans MS',10),
              bg='orange',
              fg='white',
              command=play)
btn.place(x=420,y=350)

btn=tk.Button(window,
              text='Exit',
              width=4,
              font=('Comic Sans MS',10),
              bg='orange',
              fg='white',
              command=exit)
btn.place(x=430,y=5)

window.mainloop()












