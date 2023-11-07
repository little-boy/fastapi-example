## GIT

- Version control system
- = Versioning
- Existing (other) solutions : 
  - Subversion
  - Mercurial
- Partager du code
- Remonter le temps

- git checkout {commit hash}
    - ca permet de dire que on se met à une version antérieure du code (repo..)
    - hash : genere une chaine avec plus ou moins d'entropie, peu sécurisé pour le md5 / sha1
        - lorsqu'on hash une chaine, on ne peut revenir en arriere à partir de la chaine générée
        - souvent utilisé pour le stockage des mots de passe
        - ex: md5 / sha1 / sha256...
    - chiffrage : 
        - genere une chaine "chiffrée" que l'on peut "déchiffrer" = on peut revenir en arrière en connaissant l'algorithme.
 
- git checkout {branch}
    - changer de branche


Voir l'état courant des modifications : 
- git status

Pousser les modifications sur le repository : 
- git push
- git push origin HEAD

Créer une branche, enregistrer des modifs, et la pousser sur Github : 
- git checkout -b {branch name}
- git add 
- git commit (sauvegarder mes modifications sur la branche courante)
- git push origin HEAD

Supprimer (nettoyer) une branche mergée 
- git branch -d {branch name}

Lister les branches : 
- git branch

Lister les commits passés :
- git log 
- (sortir de git log : appuyer sur la touche "q")

Ajouter un fichier dans les fichiers évalués par Git : 
- git add {path to file}

Ajouter tous les nouveaux fichiers : 
- git add .

Commiter tous les fichiers courants : 
- git commit -m "description du commit"
- git commit -am "description du commit"

### instructions 
1 - créer un dossier avec des fichiers (n'importe lesquels)
    -> ex : copier les fichiers fastapi-example à l'exception du dossier .git
2 - créer un repository
3 - initialiser le repository : 
    - git init
    - git add . 
    - git commit -m "first commit"
    - git branch -M main
    - git remote add origin https://github.com/{votre pseudo}/git-exercise.git
    - git push -u origin main
4 - créer une branche
5 - créer des fichiers avec ce que vous voulez dedans
6 - commit / push 
7 - merger la branche


/!\ changer de branche : 
- git checkout {nom de ma branche}
ex: 
- je suis sur la branche "main"
- je crée une branche : git checkout -b feature/unit-tests
- je souhaite retourner sur la branche main : git checkout main
- je souhaite aller sur la branche "feature/unit-tests" : git checkout feature/unit-tests

Attention, si vous avez des modifications en cours sur la branche courante, git va refuser le changement de branche.
Vous devez d'abord soit : 
- commiter vos changements sur la branche courante,
- annuler vos changement
    - soit ils sont inutiles, vous les supprimez : `git checkout .`
    - soit ils sont utiles : `git stash` pour les "mettre de côté", `git stash pop` qu'ils soient de retour dans votre projet.