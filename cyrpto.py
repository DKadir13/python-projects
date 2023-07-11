#request ve tkinter ı import ederiz ve as ile kısaltırız
import requests
import tkinter as tk

# Tkinter uygulamasını oluşturma ve başlığı ayarlama
app = tk.Tk()
app.title("Kripto Değişim Uygulaması")

# Binance API'si için sembolleri ayarlama. Bu sembolleri arttırabilirir
symbols = ["BTCUSDT", "ETHUSDT", "GMTUSDT", "LUNAUSDT"]
#Bir API KEY E sahip olmamız lazım bunun için ise alpha vantage sitesine girip üye olup bir api key alıyoruz
API_KEY = "1BPQQK72QV991YG8"

# Verileri çekmek için bir fonksiyon oluşturup  bu fonksiyona sembolü yazmak için bir parametre bölümü oluşturuyoruz. 
def get_crypto_data(symbol):
    #bu bölümde ise url yi oluşturuyoruz ve requests.get ile url yi çekiyoruz. Burada response json ile çektiğimiz verileri json formatına çeviriyoruz.
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    #Bu satırda ise json formatına çevirdiğimiz verileri data adlı oluşturduğumuz değişkene atıyoruz. 
    data = response.json()
    #bu satırda ise data değişkenindeki verilerin price kısmını float formatına çeviriyoruz ve price adlı değişkene atıyoruz
    price = float(data["price"])
    #bu fonksiyonun son satırında ise return price ile price değişkenini döndürüyoruz
    return price

# Bu fonksiyon ile verileri güncelleyeceğiz
def update_crypto_data():
    # Bu satırda crypto_prices adlı boş bir liste oluşturuyoruz
    crypto_prices = []
    #Sonrasında for döngüsüyle symbols adlı listemizdeki sembolleri çekiyoruz ve get_crypto_data fonksiyonuna gönderiyoruz.
    for symbol in symbols:
        #for döngüsü ile çektiğimiz symbols listesindeki sembolleri get_crypto_data fonksiyonuna gönderiyoruz ve price adlı değişkene atıyoruz
        price = get_crypto_data(symbol)
        #Bu satırda kripto paralarını ve fiyatlarını crypto_prices adlı listeye ekliyoruz
        crypto_prices.append((symbol, price))

    # Etiketleri güncelleyin ve yeni fiyatları yazdırın
    for i, (symbol, price) in enumerate(crypto_prices):
        # Bu satırda ise for döngüsü ile çektiğimiz sembolleri ve fiyatlarını tkinter ekranına yazdırıyoru
        label = tk.Label(app, text=f"{symbol}: {price:.8f} $", font=("Arial", 14))
        label.grid(row=i, column=0, padx=10, pady=5)

# Veriler güncellendikten sonra bu verileri tkinter ekranına yazdırmak için bir buton ve bu butona tıklandığında çalışacak bir fonksiyon oluşturuyoruz
button = tk.Button(app, text="Verileri Güncelle", command=update_crypto_data, font=("Arial", 16))
button.grid(row=0, column=1, padx=10, pady=5)

# Bu satır ile veriler ilk açıldığında en güncel halini veriyor ve verileri güncellemek için butona basmamız gerekiyor
update_crypto_data()

# Tkinter uygulamasını çalıştırın
app.mainloop()
