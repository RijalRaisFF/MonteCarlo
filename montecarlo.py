#MONTECARLO#
#Nama : Rijal Rais Fani Fadilah
#NRP : 152018104
#Kelas : C
#-----------------------------------------#
import random
def inputdata():
    while True:
        entry1 = input('Pemesanan = ')
        entry2 = input('Minggu-Ke =  ')
        if (entry1 == '') and (entry2 == ''):
                break
        try:
            datainput.append((int(entry1),int(entry2)))
        except:
            print("Tidak Valid!")

def prob():
    ftot = 0
    out = []
    for a in range(len(datainput)):
        ftot += datainput[a][1]
    for a in range(len(datainput)):
        n = datainput[a][1] / ftot
        out.append(n)
    return out

def probkum(inprob):
    out = []
    out.append(inprob[0])
    panjang = len(inprob) - 1
    for a in range(panjang):
        n = out[a] + inprob[a+1]
        out.append(round(n,1))
    return out

def interval(inprobkum):
    atas = []
    bawah = []
    bawah.append(0)
    for a in range((len(inprobkum))-1):
        n = inprobkum[a] + 0.001
        bawah.append(n)
    for a in range((len(inprobkum))):
        n = inprobkum[a]
        atas.append(n)
    return bawah, atas

def predict(jumlah , down, up, harga):
    total1 = 0
    total2 = 0
    data = []
    out = []
    for a in range(jumlah):
        data.append(random.random())
    for a in range(jumlah):
        if (data[a] >= down[0]) and (data[a] <= up[0]):
            n=0
        elif (data[a] >= down[1]) and (data[a] <= up[1]):
            n=1
        elif (data[a] >= down[2]) and (data[a] <= up[2]):
            n=2
        elif (data[a] >= down[3]) and (data[a] <= up[3]):
            n=3
        elif (data[a] >= down[4]) and (data[a] <= up[4]):
            n=4
        elif (data[a] >= down[5]) and (data[a] <= up[5]) :
            n=5
        out.append(n)
    data = []
    for a in  range(len(out)):
        total1 += out[a]
        n = out[a] * harga
        total2 += n
    print('Prediksi Permintaan Banyaknya Barang = ', total1, 'barang')
    print('Prediksi Pengeluaran Yang Harus Di Bayar = Rp.',total2)

datainput = []
inputdata()
alpha = prob()
beta = probkum(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Masukkan banyak prediksi: '))
price = int(input('Tentukan modal barang: '))
print('== Prediksi Dengan MonteCarlo ==')
predict(npredict, bo, ab, price)
