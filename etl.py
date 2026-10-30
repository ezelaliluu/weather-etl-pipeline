import os
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector
import requests

# Load variabel dari file .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


def run_etl():
  print("[1/3] Mengambil data dari OpenWeatherMap API...")
  response = requests.get(URL)
  raw_data = response.json()

  print("[2/3] Merapikan dan mentransformasi data...")
  kondisi_cuaca = raw_data["weather"][0]["main"]
  suhu = raw_data["main"]["temp"]
  kelembapan = raw_data["main"]["humidity"]
  unix_timestamp = raw_data["dt"]
  waktu_lokal = datetime.fromtimestamp(unix_timestamp)

  print("[3/3] Menyimpan data ke MySQL (XAMPP)...")
  try:
    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = db.cursor()

    query = """
        INSERT INTO data_cuaca (kota, kondisi_cuaca, suhu_celcius, kelembapan_persen, waktu_pencatatan)
        VALUES (%s, %s, %s, %s, %s)
        """
    val = (CITY, kondisi_cuaca, suhu, kelembapan, waktu_lokal)

    cursor.execute(query, val)
    db.commit()

    print(
        "BERHASIL! Pipeline ETL sukses dieksekusi dan data tersimpan di"
        " database."
    )

  except mysql.connector.Error as err:
    print(f"Error Database: {err}")
  finally:
    if "db" in locals() and db.is_connected():
      cursor.close()
      db.close()


if __name__ == "__main__":
  run_etl()