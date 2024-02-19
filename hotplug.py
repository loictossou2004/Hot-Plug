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

token = 'YOUR_TOKEN'
dropbox_folder_path = '/CHEMIN_VERS_LE_DOSSIER_DROPBOX'
chemin_dossier_local = "CHEMIN_VERS_LE_DOSSIER_LOCAL"

# list_folder_contents(token, folder_path)
upload_file(token, dropbox_folder_path, chemin_dossier_local)
