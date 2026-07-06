// HTML'deki formu JavaScript'e tanıtıyoruz
const loginForm = document.getElementById('loginForm');

// Form gönderildiğinde (Butona basıldığında) çalışacak fonksiyon
loginForm.addEventListener('submit', function (event) {
    // Sayfanın kendi kendine yenilenmesini engelliyoruz
    event.preventDefault();

    // Kullanıcının kutulara yazdığı değerleri alıyoruz
    const usernameInput = document.getElementById('username').value;
    const passwordInput = document.getElementById('password').value;

    // ÖRNEK GİRİŞ BİLGİLERİ (İleride bunu değiştirebilirsin)
    const dogruKullaniciAdi = "admin";
    const dogruSifre = "1234";

    // Kontrol yapıyoruz
    if (usernameInput === dogruKullaniciAdi && passwordInput === dogruSifre) {
        alert("Giriş Başarılı! Yönlendiriliyorsunuz...");

        // Giriş başarılı olunca gitmesini istediğin sayfa (Örn: ana_sayfa.html veya herhangi bir link)
        window.location.href = "https://www.google.com";
    } else {
        alert("Hatalı kullanıcı adı veya şifre! Lütfen tekrar deneyin.");
    }
});