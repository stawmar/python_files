import easygui
pojemnosc=float(easygui.enterbox("Podaj pojemosc baku w litrach"))
poziom=float(easygui.enterbox("Podaj poziom paliwa w baku w procentach"))
spalanie=float(easygui.enterbox("Ile spalasz na 100 km?"))
rezerwa=pojemnosc-5
stacja=float(easygui.enterbox("Jak daleko jest do nastepnej stacji?"))
zasieg=pojemnosc*(poziom/float(100))*(100/float(spalanie))
if zasieg>stacja:
    easygui.msgbox("Poziom baku: "+str(rezerwa)+" Poziom paliwa: "+str(poziom)+"%"+
               " Spalasz "+str(spalanie)+" litrow na 100 km"+
               " Mozesz przejechac jeszcze "+str(zasieg)+" Kolejna stacja benzynowa jest za "+
               str(stacja)+" Mozesz jechac dalej")

else: easygui.msgbox("Poziom baku: "+str(rezerwa)+" Poziom paliwa: "+str(poziom)+"%"+
               " Spalasz "+str(spalanie)+" litrow na 100 km"+
               " Mozesz przejechac jeszcze "+str(zasieg)+" Kolejna stacja benzynowa jest za "+
               str(stacja)+" Musisz zatankowac na najblizszej stacji!!!")
