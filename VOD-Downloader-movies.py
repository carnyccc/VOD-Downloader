# VideoOnDemand Downloader 0.1 beta
# 
# Author: Kilian Sommer
#
# Mit dem Video On Demand Downloader können Serien von 
# IPTV Anbietern einer M3U Datei heruntergeladen werden.

import os
import requests
from tqdm import tqdm

# Definieren Sie Ihren benutzerdefinierten User-Agent da IPTV Anbieter oft den User-Agent abfragen.
custom_user_agent = 'VLC/3.0.2.LibVLC/3.0.2'
m3u_file = 'download.m3u'

try:
    # Lesen Sie den Inhalt der download.m3u-Datei
    with open(m3u_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print('Die Datei "download.m3u" wurde nicht gefunden.')
    exit(1)

# Initialisieren Sie Variablen für den Hauptordner, den Unterordner und den Dateinamen
current_main_folder = ""
current_sub_folder = ""
current_filename = ""

try:
    # Durchlaufen Sie die Zeilen in der M3U-Datei
    for line in lines:
        if line.startswith('#EXTINF:'):
            # Extrahieren Sie den Ordner und den Dateinamen aus der Zeile
            folder_line = line.strip()
            folder_start = folder_line.find('tvg-name="') + len('tvg-name="')
            folder_end = folder_line.find('"', folder_start)
            folder = folder_line[folder_start:folder_end]

            name_start = folder_line.find('"', folder_end + 1) + 1
            name = folder_line[name_start:].strip()
            filename = name.split(',', 1)[1].strip().replace('/', '_') + '.mkv'

            print(f'Datei wird heruntergeladen: {filename}')

            # Extrahieren Sie den Hauptordner und den Unterordner aus dem Dateinamen
            # parts = filename.split('S0', 1)
            # if len(parts) > 1:
            #     main_folder = parts[0].strip()
            #     sub_folder = 'S0' + parts[1].split('E', 1)[0].strip()
            # else:
            #     main_folder = ""
            #     sub_folder = "" 

            # Wenn der Hauptordner sich geändert hat, erstellen Sie ihn, wenn er nicht existiert
            # if main_folder != current_main_folder:
            #     current_main_folder = main_folder
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                    print(f'Ordner erstellt: {folder}')
                except OSError as e:
                    print(f'Fehler beim Erstellen des Ordners "{folder}": {str(e)}')
                    exit(1)

            # Wenn der Unterordner sich geändert hat, erstellen Sie ihn, wenn er nicht existiert
            # if sub_folder != current_sub_folder:
            #     current_sub_folder = sub_folder
            #     if sub_folder:
            #         sub_folder_path = os.path.join(main_folder, sub_folder)
            #         if not os.path.exists(sub_folder_path):
            #             try:
            #                 os.makedirs(sub_folder_path)
            #                 print(f'Unterordner erstellt: {sub_folder}')
            #             except OSError as e:
            #                 print(f'Fehler beim Erstellen des Unterordners "{sub_folder}": {str(e)}')
            #                 exit(1)

            current_filename = filename
        elif line.startswith('http'):
            # Extrahieren Sie die Download-URL aus der Zeile
            url = line.strip()

            # Definieren Sie den Header mit dem benutzerdefinierten User-Agent
            headers = {'User-Agent': custom_user_agent}

            # Überprüfen Sie, ob die Datei neu heruntergeladen werden soll (wenn total_size nicht 0 ist oder wenn total_size und local_size unterschiedlich sind)
            download_path = os.path.join(folder, current_filename)
            if os.path.exists(download_path):
                local_size = os.path.getsize(download_path)
            else:
                local_size = 0

            response = requests.get(url, headers=headers, stream=True)
            total_size = int(response.headers.get('Content-length', 0))

            if total_size != 0 and total_size != local_size:
                # Herunterladen der Datei mit dem benutzerdefinierten User-Agent und Speichern mit dem richtigen Dateinamen im richtigen Ordner
                if response.status_code == 200 or response.status_code == 206:
                    try:
                        with open(download_path, 'wb') as output_file:
                            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

                            for data in response.iter_content(1024):
                                output_file.write(data)
                                progress_bar.update(len(data))

                            progress_bar.close()
                        print(f'Datei heruntergeladen: {current_filename}')
                    except OSError as e:
                        print(f'Fehler beim Speichern der Datei "{current_filename}": {str(e)}')
                        exit(1)
                else:
                    print(f'Fehler beim Herunterladen der Datei: {current_filename}')
            else:
                print(f'Datei bereits vollständig heruntergeladen und übersprungen: {current_filename}')

    print('Alle Dateien wurden heruntergeladen und umbenannt.')

except KeyboardInterrupt:
    print('Das Programm wurde vom Benutzer abgebrochen. Auf Wiedersehen!')
