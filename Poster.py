print("       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒     ▒▒▒▒  ▒▒▒     ▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒                           ")
print("              ▒▒          ▒▒▒      ▒▒▒  ▒▒▒▒▒   ▒▒▒  ▒▒                                    ")
print("              ▒▒          ▒▒▒      ▒▒▒  ▒▒▒ ▒▒  ▒▒▒  ▒▒                                    ")
print("              ▒▒          ▒▒▒      ▒▒▒  ▒▒▒   ▒▒▒▒▒  ▒▒                                    ")
print("              ▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒    ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒                           ")
print("                                                       ▒                                   ")
print("    ▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒         ")
print("    ▒▒     ▒▒   ▒▒▒    ▒▒▒    ▒▒                  ▒▒         ▒▒▒          ▒▒     ▒▒        ")
print("    ▒▒▒▒▒▒▒     ▒▒▒    ▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒         ▒▒         ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒          ")
print("    ▒▒          ▒▒▒    ▒▒▒            ▒▒▒         ▒▒         ▒▒▒          ▒▒     ▒▒        ")
print("    ▒▒          ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒         ▒▒         ▒▒▒▒▒▒▒▒▒▒   ▒▒     ▒▒        ")



import pyautogui , sys
import keyboard
import time
print("Ekran boyutunuz algılanıyor")
print(pyautogui.size())
print("Belli bir yerden devam etmek için lütfen sayı giriniz 0 dan başlamak için lütfen 0 giriniz")
i =int(input("Lütfen değer giriniz; "))
print("--------------------------------------------------------------------------------------------")
print("Etiketleyeceğiniz kişinin adını ve soy adını arada 1 boşluk bırakarak giriniz")
kısı =input("isim soyisim : ")
print("--------------------------------------------------------------------------------------------")
print("program kaça kadar devam edecek ?")
m = int(input())
print("facebook post açma yerine mousenizi getirip entere basınız")

def fare():
    while True:
        x, y = pyautogui.position() 
        if keyboard.is_pressed('insert'):
            x1=x
            y1=y
            print(x1,y1)
            return x1,y1
        else:
            time.sleep(0.01)
print("--------------------------------------------------------------------------------------------")
print("program hazır lütfen facebook yerini geri açınız ve programı başlatmak için entere basınız")
print("DİKKAT PROGRAM ÇALIŞIRKEN BİLGİSAYARI KULLANMAYINIZ")
if keyboard.is_pressed('enter'):
    pydirectinput.move(x1,y1)
    pyautogui.click(button='left', clicks=1, interval=0.25)




        

            



    