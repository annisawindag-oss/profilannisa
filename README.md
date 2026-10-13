# Website Profil: Annisa Winda Gustina

Website satu halaman memakai HTML, CSS, dan JavaScript biasa. Tidak perlu `npm install`, tidak perlu Vite atau Node.js.

## Isi folder

```
profil-annisa/
├── index.html          halaman utama (isi teks diubah di sini)
├── css/style.css       tampilan dan warna
├── js/main.js          tahun otomatis dan penanda menu
├── assets/favicon.svg  ikon tab browser
├── .gitignore          daftar file yang tidak ikut ke GitHub
└── README.md           panduan ini
```

## 1. Buka di VS Code

1. Ekstrak file zip. Hasilnya folder `profil-annisa`.
2. Di VS Code: **File → Open Folder**, pilih `profil-annisa`.
3. Pasang ekstensi **Live Server** (Ritwick Dey) lewat menu Extensions.
4. Klik kanan `index.html`, lalu pilih **Open with Live Server**. Halaman terbuka di browser dan otomatis menyegar setiap kali kamu menyimpan file.

Tanpa ekstensi pun bisa: klik dua kali `index.html` di File Explorer.

Folder ini proyek terpisah. Jangan digabung dengan folder `C:\kelolakeuangan`.

## 2. Mengubah isi

| Yang ingin diubah | File | Cari |
|---|---|---|
| Nama, status, pendidikan, domisili | `index.html` | bagian `<dl class="spec">` |
| Keahlian | `index.html` | bagian `<ul class="skills">`, tambah baris `<li>` |
| Warna | `css/style.css` | blok `:root` paling atas |

## 3. Menambah kontak

Tempel blok ini di `index.html`, tepat di atas `</main>`, lalu ganti isinya dengan datamu:

```html
<section class="section" id="kontak" aria-labelledby="judul-kontak">
  <div class="wrap split">
    <div>
      <h2 id="judul-kontak">Kontak</h2>
      <p class="muted">Cara menghubungi saya.</p>
    </div>
    <dl class="spec">
      <div class="row">
        <dt>Email</dt>
        <dd><a href="mailto:emailkamu@contoh.com">emailkamu@contoh.com</a></dd>
      </div>
      <div class="row">
        <dt>Instagram</dt>
        <dd><a href="https://instagram.com/usernamekamu">@usernamekamu</a></dd>
      </div>
    </dl>
  </div>
</section>
```

Kalau mau menu "Kontak" di bagian atas, tambahkan satu baris ini di dalam `<ul class="nav-links">`:

```html
<li><a href="#kontak">Kontak</a></li>
```

## 4. Unggah ke GitHub

Buat repository **baru dan kosong** di GitHub (jangan centang README atau .gitignore), misalnya `profil-annisa`. Salin URL HTTPS-nya dari tombol hijau **Code**.

Lalu di terminal VS Code, dari dalam folder `profil-annisa`:

```powershell
git init
git add .
git commit -m "Website profil pertama"
git branch -M main
git remote add origin https://github.com/USERNAME/profil-annisa.git
git push -u origin main
```

Ganti `USERNAME` dan nama repo dengan milikmu yang asli. Sebelum `git commit`, pastikan identitas Git sudah berisi nama dan email aslimu:

```powershell
git config --global user.name "Nama asli"
git config --global user.email "email-akun-github@contoh.com"
```

Setiap kali mengubah isi website, kirim perubahannya begini:

```powershell
git add .
git commit -m "Jelaskan perubahan di sini"
git push
```

## 5. Deploy ke Vercel

1. Buka vercel.com dan login dengan **Continue with GitHub**.
2. Klik **Add New → Project**, lalu **Import** repository `profil-annisa`.
3. Atur seperti ini:
   - **Application Preset**: `Other`
   - **Root Directory**: `./`
   - **Build Command** dan **Output Directory**: biarkan kosong
4. Klik **Deploy**. Setelah selesai, Vercel memberi alamat berakhiran `.vercel.app`.

Setelah itu, setiap `git push` ke branch `main` otomatis memperbarui website.

## Jika deploy gagal

- Error "repository does not contain the requested branch": kode belum di-push. Selesaikan bagian 4 dulu.
- Halaman tampil tanpa gaya: cek huruf besar dan kecil pada nama file dan folder (`css/style.css`). Server Vercel membedakannya.
