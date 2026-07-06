// HTML elemanlarını JS'e çekiyoruz
const strengthText = document.getElementById('strengthText');
const resultInput = document.getElementById('passwordResult');
const lengthInput = document.getElementById('passwordLength');
const lengthValue = document.getElementById('lengthValue');

const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');

// Seçenekleri ve karşılık gelen karakter havuzlarını bir nesne dizisinde tutuyoruz
const charSets = [
    { el: document.getElementById('includeUppercase'), chars: "ABCDEFGHIJKLMNOPQRSTUVWXYZ" },
    { el: document.getElementById('includeLowercase'), chars: "abcdefghijklmnopqrstuvwxyz" },
    { el: document.getElementById('includeNumbers'), chars: "0123456789" },
    { el: document.getElementById('includeSymbols'), chars: "!@#$%^&*()_+~`|}{[]:;?><,./-=" }
];

// 1. Slider hareket ettikçe ekrandaki sayıyı güncelle
lengthInput.addEventListener('input', () => {
    lengthValue.textContent = lengthInput.value;
});

// 2. Şifre Üretme Fonksiyonu
function generatePassword() {
    const length = Number(lengthInput.value);
    let charPool = ""; 

    // İşaretli olan kutucukların karakterlerini ana havuza ekle
    charSets.forEach(set => {
        if (set.el.checked) charPool += set.chars;
    });

    if (charPool === "") {
        resultInput.value = "Karakter tipi seçin!";
        strengthText.textContent = "-";
        strengthText.className = "";
        return;
    }

    let generatedPassword = "";
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charPool.length);
        generatedPassword += charPool[randomIndex];
    }

    resultInput.value = generatedPassword;

    // ŞİFRE GÜCÜ KONTROLÜ
    if (length < 10) {
        strengthText.textContent = "Zayıf";
        strengthText.className = "weak";  
    } else if (length < 16) {
        strengthText.textContent = "Orta";
        strengthText.className = "medium"; // CSS'e .medium (sarı/turuncu) sınıfı ekleyebilirsin
    } else {
        strengthText.textContent = "Güçlü";
        strengthText.className = "strong"; 
    }
}

// 3. Modern Kopyalama Fonksiyonu
function copyPassword() {
    const pwd = resultInput.value;
    if (!pwd || pwd === "Karakter tipi seçin!") return; 

    // Modern pano (clipboard) API'si kullanımı
    navigator.clipboard.writeText(pwd).then(() => {
        const originalText = copyBtn.textContent;
        copyBtn.textContent = "Kopyalandı! ✅";
        copyBtn.style.backgroundColor = "#28a745"; // Geçici yeşil renk
        
        // 2 saniye sonra butonu eski haline döndür
        setTimeout(() => {
            copyBtn.textContent = originalText;
            copyBtn.style.backgroundColor = ""; 
        }, 2000);
    }).catch(err => {
        console.error('Kopyalama başarısız oldu: ', err);
    });
}

// Olay Dinleyicileri (Event Listeners)
generateBtn.addEventListener('click', generatePassword);
copyBtn.addEventListener('click', copyPassword);

// Sayfa ilk açıldığında çalıştır
generatePassword();