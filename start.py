import os
import json
import subprocess
import sys

def uruchom_backend():
    sciezka_config = "config.json"
    
    # 1. Wczytujemy zmienne z pliku konfiguracyjnego (jeśli istnieje)
    if not os.path.exists(sciezka_config):
        print(f"[INFO] Brak pliku {sciezka_config} - uruchamiam z domyślnymi zmiennymi środowiskowymi (localhost).")
        env_vars = os.environ.copy()
    else:
        with open(sciezka_config, "r", encoding="utf-8") as f:
            dane_bazy = json.load(f)
        
        env_vars = os.environ.copy()
        env_vars["DB_URL"] = dane_bazy.get("DB_URL", "")
        env_vars["DB_USER"] = dane_bazy.get("DB_USER", "")
        env_vars["DB_PASS"] = dane_bazy.get("DB_PASS", "")
        print(f"[OK] Wczytano dane dostępowe bazy z pliku {sciezka_config}.")


    sciezka_jar = "target/demo-0.0.1-SNAPSHOT.jar"
    if not os.path.exists(sciezka_jar):
        print(f"[BŁĄD] Nie znaleziono pliku {sciezka_jar}!")
        print("Najpierw zbuduj aplikację poleceniem: ./mvnw clean package -DskipTests")
        sys.exit(1)

    try:
        subprocess.run(["java", "-jar", sciezka_jar], env=env_vars)
    except KeyboardInterrupt:
        print("\n[STOP] Zatrzymano serwer backendu.")

if __name__ == "__main__":
    uruchom_backend()