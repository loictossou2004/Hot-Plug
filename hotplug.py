import os
import dropbox
from dropbox.exceptions import AuthError

def upload_file(token, dropbox_folder_path, chemin_dossier_local):
    try:
        dbx = dropbox.Dropbox(token)

        for dossier_racine, dossiers, fichiers in os.walk(chemin_dossier_local):
            drop_folder = dropbox_folder_path + '/' + dossier_racine
            dbx.files_create_folder(drop_folder)
            
            for nom_fichier in fichiers:
                chemin_fichier = os.path.join(dossier_racine, nom_fichier)
                file_path = chemin_fichier.split('/')[-1]
                
                with open(chemin_fichier, 'rb') as file:
                    path_online = f"{drop_folder}/{file_path}"
                    try:
                        dbx.files_upload(file.read(), path_online)
                        print(f"File '{file_path}' uploaded successfully to '{drop_folder}'.✅")
                    except:
                        print(f"File '{file_path}' uploaded error.❌")
                # print("Nom du fichier dropbox: %s" % file_path)
                # print("Nom du fichier local: %s" % chemin_fichier)
                # print("Nom du fichier à uploader: %s" % path_online)
            print()
    except AuthError as e:
        print(f"Error: {e.error}")

def list_folder_contents(token, folder_path):
    try:
        dbx = dropbox.Dropbox(token)
        result = dbx.files_list_folder(folder_path)
        for entry in result.entries:
            print(entry.name)
    except AuthError as e:
        print(f"Error: {e.error}")

token = 'sl.Bv4-BCCkA02rkDjbEt1U46yM1kXdgGfsCwEQDNBtpwDL6iyiEy7H9QOqcd9u5PV_TuTkEl5LO-bnIW9x5bqKevoq8_2gJPDtcsLFR7eQj6wg1iqKO_F-hs60qv84QsoMDGXn8-emTu-B1HoHQTXdZWk'
dropbox_folder_path = '/testATK'
chemin_dossier_local = "Downloads"

# list_folder_contents(token, folder_path)
upload_file(token, dropbox_folder_path, chemin_dossier_local)
