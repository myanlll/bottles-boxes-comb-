# bottles-boxes-comb-
***I don't even know what this is. Just some boxes and bottles.***
# Kombinasyon Hesaplama Sistemi

## Açıklama
Betik, kullanıcı girişleriyle belirlenmiş hayali bir kapasite ve şişe çeşit durumlarını ele alarak, kutuyu hem boş tutmayacak hem de kapasiteyi aşmayacak şekilde şişeleri hangi kombinasyonlarda yerleştirebileceğimizi bulmamıza olanak sağlar. Kullanıcıdan girdi alır ve olası tüm kombinasyonları oluşturur. Sonrasında ise önce kutuda şişenin bulunmadığı (geçersiz) durumları, ardından da kutu hacminin aşıldığı (geçersiz) durumları saptar ve bu kombinasyonları kaldırır. Devamında ise toplam kombinasyon sayısını, kombinleme biçimlerini (örneğin, 1,0,3) sıraladıktan sonra okuma kolaylığı olması açısından tekrar toplam kombinasyon sayısını verir.

Fonksiyon, iki parametre alır: kapasite ve şişeler. Kapasite, kutunun alabileceği maksimum şişe sayısını temsil ederken, şişeler parametresi ise kullanılabilir şişe sayısını temsil eder. Kapasiteye sahip bir kutunun, belirli sayıda şişe ile kaç farklı şekilde doldurulabileceğini hesaplamak için kullanılan bu kod parçası, daha önce oluşturulan kombinasyonlar listesini kullanarak yeni kombinasyonlar oluşturur. Toplamları sıfır olan kombinasyonları filtreleyip ardından kutu kapasitesini aşan kombinasyon durumlarının olup olmadığını kontrol eder ve eğer varsa, onları da sonuç geçerli_kombinasyonlar’dan çıkartır. Sonrasında geçerli_kombinasyonlar setindeki her bir kombinasyonu yazdırmak için bir döngü başlatılır. Her bir kombinasyon, print fonksiyonu kullanılarak yazdırılır. Ardından, okuma kolaylığı açısından toplam set uzunluğunu (geçerli kombinasyonlar sayısını) alır ve çıktı olarak verir.

## Özellikler
- Kapasite Yönetimi: Kutu kapasitesine göre şişe kombinasyonları hesaplar.
- Şişe Türleri: Farklı şişe türleri için kombinasyonlar oluşturur.
- Geçerli Kombinasyonlar: Toplam kapasiteyi aşmayan geçerli kombinasyonları döndürür.

## Kurulum
Kodun çalıştırılabilmesi için Python'un sisteminizde kurulu olması gerekmektedir.

## Kullanım
Kodunuzu çalıştırmak için:
    ```bash
    python main.py
    ```


# Combination Calculation System

## Description
The script is designed to handle hypothetical scenarios of capacity and bottle types determined by user inputs, identifying which combinations of bottles can be placed in a box without leaving it empty or exceeding its capacity. It takes input from the user and generates all possible combinations. Then, it first identifies invalid combinations where the box is empty, and then where the box capacity is exceeded, and removes these combinations. Next, it lists the total number of combinations, the combination patterns (e.g., 1,0,3), and then again gives the total number of combinations for ease of reading.

The function takes two parameters: capacity and bottles. Capacity represents the maximum number of bottles that the box can hold, while the bottles parameter represents the number of available bottles. This code snippet, used to calculate how many different ways a box with a given capacity can be filled with a certain number of bottles, uses the previously created combination list to generate new combinations. It filters out combinations that total zero, then checks for any combinations that exceed the box capacity, and if there are any, it removes them from the valid_combinations set. Then, a loop is initiated to print each combination in the valid_combinations set. Each combination is printed using the print function. Finally, for ease of reading, it takes the total set length (the number of valid combinations) and outputs it.
## Features
- Capacity Management: Calculates bottle combinations based on box capacity.
- Bottle Types: Generates combinations for different bottle types.
- Valid Combinations: Returns valid combinations that do not exceed the total capacity.

## Installation
Make sure Python is installed on your system to run the code.

## Usage
To run the code:
    ```bash
    python main.py
    ```

## License
This project is officially licensed under "No One's Gonna Steal This, For sure" License.
