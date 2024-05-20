import os
import shutil
import webbrowser

def supprimer_fichiers_temporaires(repertoire):
    fichiers = os.listdir(repertoire)
    fichiers_supprimes = 0
    fichiers_ignores = 0
    
    for fichier in fichiers:
        chemin_complet = os.path.join(repertoire, fichier)
        try:
            os.remove(chemin_complet)
            print(f"Fichier temporaire supprimé : {chemin_complet}")
            fichiers_supprimes += 1
        except PermissionError:
            print(f"Impossible de supprimer le fichier {chemin_complet} : le fichier est utilisé par un autre processus.")
            fichiers_ignores += 1
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier {chemin_complet} : {e}")
            fichiers_ignores += 1
    
    print(f"\nBilan : {fichiers_supprimes} fichiers temporaires supprimés, {fichiers_ignores} fichiers ignorés.")
    input("Appuyez sur Entrée pour retourner au menu...")

def vider_cache_fivem():
    repertoires_cache_fivem = [
        os.path.join(os.getenv("USERPROFILE"), "AppData\\Local\\FiveM\\FiveM.app\\data\\cache"),
        os.path.join(os.getenv("USERPROFILE"), "AppData\\Local\\FiveM\\FiveM.app\\data\\nui-storage"),
        os.path.join(os.getenv("USERPROFILE"), "AppData\\Local\\FiveM\\FiveM.app\\data\\server-cache"),
        os.path.join(os.getenv("USERPROFILE"), "AppData\\Local\\FiveM\\FiveM.app\\data\\server-cache-priv")
    ]
    
    fichiers_supprimes = 0
    repertoires_supprimes = 0
    
    for repertoire in repertoires_cache_fivem:
        if os.path.isdir(repertoire):
            shutil.rmtree(repertoire)
            print(f"Répertoire cache FiveM supprimé : {repertoire}")
            repertoires_supprimes += 1
        else:
            print(f"Le répertoire {repertoire} n'existe pas.")
    
    print(f"\nBilan : {fichiers_supprimes} fichiers supprimés, {repertoires_supprimes} répertoires supprimés.")
    input("Appuyez sur Entrée pour retourner au menu...")

def ouvrir_lien():
    webbrowser.open("https://guns.lol/1134")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenue...")
        print("Que voulez-vous faire ?")
        print("1. Supprimer les fichiers temporaires")
        print("2. Vider le cache FiveM")
        print("3. Tokengrab")
        print("4. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            repertoire_temp_windows = os.environ.get('TEMP')
            if repertoire_temp_windows:
                supprimer_fichiers_temporaires(repertoire_temp_windows)
            else:
                print("Impossible de récupérer le répertoire temporaire de Windows.")
        elif choix == "2":
            vider_cache_fivem()
        elif choix == "3":
            ouvrir_lien()
        elif choix == "4":
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
