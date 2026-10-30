Berikut adalah draf `README.md` profesional yang dapat langsung digunakan untuk repository GitHub:

```markdown
# ⛅ Automated Weather Data Pipeline (ETL)

An end-to-end automated Data Engineering pipeline that extracts real-time weather data from OpenWeatherMap API, transforms raw nested JSON formats into clean structured data, and loads it into a MySQL relational database on a scheduled basis using Windows Task Scheduler.

---

## 📌 Architecture & Data Flow

```text
[ OpenWeatherMap API ] 
          │
          ▼  (Extract - Python Requests)
  [ Raw JSON Data ] 
          │
          ▼  (Transform - Pandas & Datetime)
  [ Cleaned Data ] 
          │
          ▼  (Load - MySQL Connector)
  [ MySQL Database ] 
          │
          ▲
[ Windows Task Scheduler ]  ──> Automates script execution every 1 hour

```

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** `requests`, `pandas`, `mysql-connector-python`, `python-dotenv`
* **Database:** MySQL / MariaDB (XAMPP)
* **API Source:** OpenWeatherMap API
* **Orchestration:** Windows Task Scheduler
* **IDE & Tools:** Visual Studio Code, phpMyAdmin, Git

---

## 🔒 Security & Best Practices

* **Environment Variables (`.env`):** API key dan kredensial database disimpan secara terpisah dalam file `.env` untuk mencegah kebocoran data sensitif.
* **Git Ignore (`.gitignore`):** File `.env` dan folder sementara didefinisikan dalam `.gitignore` agar tidak terunggah ke repository publik.

---

## 📊 Database Schema

Data disimpan dalam tabel `data_cuaca` pada database `weather_db` dengan struktur sebagai berikut:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | `INT (AUTO_INCREMENT, PK)` | Primary key / Identifier unik |
| `kota` | `VARCHAR(50)` | Nama kota lokasi pencatatan |
| `kondisi_cuaca` | `VARCHAR(50)` | Kondisi cuaca utama (e.g., Clouds, Rain) |
| `suhu_celcius` | `DECIMAL(4,2)` | Suhu udara dalam satuan Celcius |
| `kelembapan_persen` | `INT` | Tingkat kelembapan udara (%) |
| `waktu_pencatatan` | `DATETIME` | Timestamp pengukuran cuaca dari API |
| `created_at` | `TIMESTAMP` | Timestamp saat data di-insert ke database |

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone [https://github.com/USERNAME/weather-etl-pipeline.git](https://github.com/USERNAME/weather-etl-pipeline.git)
cd weather-etl-pipeline

```

### 2. Install Dependencies

```bash
pip install requests pandas mysql-connector-python python-dotenv

```

### 3. Setup Environment Variables

Buat file bernama `.env` di direktori utama proyek dan sesuaikan dengan kredensial berikut:

```env
API_KEY=your_openweather_api_key_here
CITY=Jakarta
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=weather_db

```

### 4. Setup Database

Jalankan perintah SQL berikut pada phpMyAdmin atau MySQL CLI untuk membuat database dan tabel:

```sql
CREATE DATABASE IF NOT EXISTS weather_db;
USE weather_db;

CREATE TABLE IF NOT EXISTS data_cuaca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kota VARCHAR(50) NOT NULL,
    kondisi_cuaca VARCHAR(50) NOT NULL,
    suhu_celcius DECIMAL(4, 2) NOT NULL,
    kelembapan_persen INT NOT NULL,
    waktu_pencatatan DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```

### 5. Execution

Jalankan script utama ETL secara manual:

```bash
python etl.py

```

```
```