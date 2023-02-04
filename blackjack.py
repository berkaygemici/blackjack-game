import random
import time
listemiz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
def p_randomla():
    sonuc = random.choice(listemiz)
    return int(sonuc)
def k_randomla():
    sonuc = random.choice(listemiz)
    return int(sonuc)
listemiz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
while True:
    veri = input('q ile çıkınız, basla ile oyuna başlayın')
    if veri == 'q':
        break
    if veri == 'basla':
        print('Oyuna hoş geldiniz,bakiye giriniz')
        bakiye = int(input('Bakiye:'))

        while (bakiye > 0):
            print('Güncel bakiyeniz:',bakiye)

            deger = int(input('Ne kadar para ile oynamak istiyorsunuz'))
            bizimel = 0
            if (deger > bakiye):
                print('Girdiğiniz değer bakiyenizden fazla olamaz, Bakiyeniz:',bakiye)
            elif (bakiye >= deger):
                dealer = random.choice(listemiz)
                print('Kurpiye Kartlarının değeri {} \nNOT:Tek kartın değeri budur,daha açılmamış bir kart bulunmaktadır.'.format(dealer))
                dealer += k_randomla()

                time.sleep(1)
                bizimel += p_randomla() + p_randomla()
                if p_randomla() == 11:
                    int(input('AS kartını çektiniz 1 mi olsun 11 mi'))
                print('Oyuncu el değeri: ', bizimel)
                time.sleep(1)
                while (bizimel <= 21):

                    time.sleep(1)
                    istek = input("Kart çekmek için 'cek', durmak icin 'dur' yazabilirsiniz.")
                    if istek == 'cek':
                        bizimel = bizimel + p_randomla()
                        print('Elinizin Güncel Değeri:', bizimel)
                    if istek == 'dur':
                        print('Elinizin Güncel Değeri:',bizimel)
                        time.sleep(1)
                        print('krupiyenin güncel el değeri:',dealer)
                        while dealer < 17:
                            dealer += k_randomla()
                            print('Krupiye kart çekiyor....')
                            time.sleep(2)
                            print('krupiyenin güncel el değeri:',dealer)

                        if (dealer > 21):
                            time.sleep(1)
                            print("Krupiye 21'i geçti. Kazandınız")
                            bakiye += deger
                            break
                        elif (dealer > bizimel):
                            time.sleep(1)
                            print('Maalesef krupiye kazandı!')
                            bakiye -= deger
                            break
                        elif (bizimel > dealer):
                            time.sleep(1)
                            print('Tebrikler! Kazandınız.')
                            bakiye += deger
                            break
                        elif (bizimel == dealer):
                            time.sleep(1)
                            print('Berabere')
                            break
                        elif(bizimel == 21):
                            time.sleep(1)
                            print('BLACKJACK!!! Tebrikler Kazandınız %20 blackjack bonusu eklendi.')
                            bakiye += (deger**120)/100

                else:
                    time.sleep(1)
                    print('Maalesef kaybettiniz!')
                    bakiye -= deger
#TODO ONLINE UYGULAMASINI YAP