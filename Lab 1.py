import time,sys, os
RED='\u001b[41m'
BLUE='\u001b[44m'
WHITE='\u001b[47m'
RESET='\u001b[0m'
ERASE='\x1B[2K'
BEGIN='\x1B[1G'

def flag():
    pixel='  '
    length=20
    height=20

    for i in range(height):
        if i<=height/5:
            print(RED + pixel*length + RESET)
        elif height/5 < i <= height*0.4:
            print(RED + pixel * int(length * 0.4) + WHITE + pixel * (length // 5) + RED + pixel * int(length * 0.4) + RESET)
        elif int(height * 0.4) < i <= height*0.6:
            print(RED + pixel * (length//5) + WHITE + pixel * int(length * 0.6) + RED + pixel * (length//5) + RESET)
        elif i<= height*0.8:
            print(RED + pixel * int(length * 0.4) + WHITE + pixel * (length//5) + RED + pixel * int(length * 0.4) + RESET)
        else:
            print(RED + pixel * length + RESET)

#flag()

def pattern():
    height=25
    width=41
    r=10
    x1 = 10
    y1 = 12
    x2 = 30
    y2 = 12
    colors=[13,26,47,55,69]
    while True:
        for color in colors:
            for y in range(height):
                line=''
                for x in range(width):
                    d1 = ((x - x1) / r) ** 2 + ((y - y1) / r) ** 2
                    d2 = ((x - x2) / r) ** 2 + ((y - y2) / r) ** 2
                    if abs(d1-1)<0.15 or abs(d2-1)<0.15:
                        line+=f'\033[48;5;{color}m   \033[0m'
                    else:
                        line+='   '
                print(line)
            time.sleep(1)
#pattern()

def animation():
    nomer=['Первый','Второй','Третий','Четвёртый','Пятый']
    frames=[
        '|',
        '/',
        '__',
        '/\\',
        ' __',
        ' /\\',
        '  __',
        '  /\\',
        '   __',
        '   /\\',
        '    __',
        '    /\\',
        '     __',
        '     /\\',
        '      __',
        '      /\\',
        '        \\',
        '         |',
    ]
    for x in range(5):
        for frame in frames:
            os.system('cls')
            print(f'{nomer[x]} червяк ползёт:', end='', flush=True)
            print(frame,end='', flush=True)
            time.sleep(0.3)
            print(f'\u001b[H',end="\r",flush=True)

# animation()

def sequence():
    file=open('sequence.txt','r')
    promejutok=[]
    brak=[]
    for line in file:
        if -3<int(float(line))<3:
            promejutok.append(float(line))
        else:
            brak.append(float(line))
    file.close()
    print(promejutok)
    print(len(promejutok),len(brak))
    print(f'{BLUE}{' ' * int(len(promejutok)/5)}{RESET}{len(promejutok)/(len(promejutok)+len(brak))*100}%')
    print(f'{RED}{' ' * int(len(brak) / 5)}{RESET}{len(brak) / (len(promejutok) + len(brak))*100}%')

# sequence()









    # for x in range(5):
    #     for frame in frames:
    #         print(f'{nomer[x]} червяк ползёт:', end='', flush=True)
    #         print(frame,end='', flush=True)
    #         time.sleep(0.3)
    #         print(f'\u001b[F\u001b[K',end="\r",flush=True)




















