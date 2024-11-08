# HASH
Bu programlar hash algoritmasında en çok kullanılan **(md5,sha1,sha256)** şifrelemeleri kırmak veya şifrelemek için kullanılır. Şifrelemek için **_"encode.py"_**, kırmak için **_"decode.py"_**.

---
### Programı İndirme
* `git clone https://github.com/wolkann/cryptography`
* `cd cryptography`

---

### "encode.py" Kullanımı
* `python3 encode.py` Yazarak programı çalıştırıyoruz.
* Algoritma listesinde şifrelemek istediğimiz algoritmayı seçiyoruz.
* Şifrelemek istediğimiz kelimeyi yazıyoruz.
* Ve belirlediğimiz kelimenin hash algoritması oluşuyor.

#### Program içi görüntü:
<img src="https://github.com/wolk4n/malware-analyzer/blob/main/imgs/cli.jpg">

---

### "decode.py" Kullanımı
* `python3 decode.py` Yazarak programı çalıştırıyoruz.
* Şifresini kırmak istediğimiz algoritmayı seçiyoruz.
* Wordlist dosyamızın dosya yolunu yazıyoruz.
* Kırmak istediğimiz hash'i yazıyoruz.

#### Program içi görüntü:
<img src="https://github.com/wolkann/cryptography/blob/main/img/decode.png ">

---

### Wordlists
Wordlist, içerisinde birçok farklı sözcük ve şifre kombinasyonu barındıran kelime listesidir. Bu kelime listeler şifre kırmaya yönelik saldırıların olmazsa olmaz işlemidir. Wordlist’in içerisindeki kelime şifre ile eşleşmesi durumda saldırı sonuçlanır. Eğer Wordlist şifreyi içermiyorsa tamamen kullanışsız olur bu sebepten dolayı daha geniş Wordlist ile yapılan saldırıların başarı oranı çok daha yüksektir.

* Eğer bir wordlist dosyanız yoksa projenin içindeki halihazırda gelen "_wordlist.txt_" dosyasını kullanabilirsiniz.

* Daha geniş bir wordliste ihtiyacınız varsa "_rockyou.txt_" dosyasını kullanın!

Rockyou.txt dosyası için:https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

