## GIT

- Version control system
- = Versioning
- Existing (other) solutions : 
  - Subversion
  - Mercurial
- Partager du code
- Remonter le temps
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