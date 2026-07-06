// HTML elemanlarını JS'e çekiyoruz
const resultInput = document.getElementById('passwordResult');
const lengthInput = document.getElementById('passwordLength');
const lengthValue = document.getElementById('lengthValue');

const uppercaseCheck = document.getElementById('includeUppercase');
const lowercaseCheck = document.getElementById('includeLowercase');
const numbersCheck = document.getElementById('includeNumbers');
const symbolsCheck = document.getElementById('includeSymbols');

const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');

// 1. Slider (Kaydırıcı) hareket ettikçe ekrandaki sayıyı güncelleyelim
lengthInput.addEventListener('input', function () {
    lengthValue.textContent = lengthInput.value;
});

// 2. Şifre Üretme Fonksiyonu
function generatePassword() {
    const length = lengthInput.value;

    // Karakter havuzlarımız
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
    const numberChars = "0123456789";
    const symbolChars = "!@#$%^&*()_+~`|}{[]:;?><,./-=";

    let charPool = ""; // Kullanıcının seçimine göre dolacak ana havuz

    // Kullanıcı hangi kutuyu seçtiyse o havuzu ana havuza ekliyoruz
    if (uppercaseCheck.checked) charPool += uppercaseChars;
    if (lowercaseCheck.checked) charPool += lowercaseChars;
    if (numbersCheck.checked) charPool += numberChars;
    if (symbolsCheck.checked) charPool += symbolChars;

    // Eğer kullanıcı hiçbir kutuyu seçmediyse uyarı verelim
    if (charPool === "") {
        alert("Lütfen en az bir karakter tipi seçin!");
        return;
    }

    let generatedPassword = "";
    // İstenen uzunluk kadar döngü çalıştırıp havuzdan rastgele seçim yapıyoruz
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charPool.length);
        generatedPassword += charPool[randomIndex];
    }

    // Üretilen şifreyi ekrandaki kutuya yazdırıyoruz
    resultInput.value = generatedPassword;
}

// 3. Kopyalama Fonksiyonu
function copyPassword() {
    if (resultInput.value === "") return; // Şifre yoksa işlem yapma

    resultInput.select(); // Metni seç
    document.execCommand('copy'); // Panoya kopyala (En basit yöntem)
    alert('Şifre panoya kopyalandı!');
}

// Butonlara tıklanınca çalışacak tetikleyiciler
generateBtn.addEventListener('click', generatePassword);
copyBtn.addEventListener('click', copyPassword);

// Sayfa ilk açıldığında da otomatik bir şifre üretsin
generatePassword();