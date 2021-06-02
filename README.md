# Device_Management

## Comment Fonctionne le code ?

J'ai decidé de créer une classe pour chaque element du sujet soit :
  * Device
  * Firmware
  * Patient

Afin de garde en mémoires les objets j'ai definit une liste de patients et une liste de devices.

Ensuite pour rendre plus facile l'utilisation du code j'ai crée un menu qui permet différentes fonctionnalités soit :
  * 1 - Declarer (permet de créer un objet device)
  * 2 - Associer (permet d'associer un objet device avec un objet patient -> il faut créer un objet patient avant)
  * 3 - Dissocier (permet de dissocier un objet device d'un objet patient)
  * 4 - Mettre à jour le firmware (permet de mettre a jour le firmware)
  * 5 - Afficher les devices (affiche la liste de tous les devices)
  * 6 - Afficher Firmware (affiche la liste de tous les firmware)
  * 7 - Afficher Patient (affiche la liste tous les patients)
  * 8 - Nouveau Patient (permet de créer un nouveau patient)
  
Pour le firmware j'ai décidé d'en créer un seul qui serait commun à tous les devices comme "un sytème d'exploitation" 
ainsi quand on le met à jour tous les devices sont mis à jours en même temps.

On a différentes verifications pour certaines opérations afin respecter les contraintes du sujet.

Si une opération s'est bien passé on affiche alors 'OK' sinon on affiche 'KO'.

Le code est assez simpliste et pas très optimisé notamment à cause des nombreux if.
