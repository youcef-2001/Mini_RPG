# Mini_RPG


projet pour l' implementation de design patterns sur un RPG 




-   Tout les Enemies , Player et PNJ sont des personnages.
-   tout les personnages ont une liste d'objet appelr inventaire, pour le marchand ce sera sa liste d'objets a vendre.
-   pour le player ce sera l'inventaire pour stocker les objets 
-   pour le voleur en plus de son inventaire il pourra donc voler un objet du player qu'il attaquera.
-   pour les PNJ cette liste sera vide
-   pour le coffre cette liste sera ajouter afin de contenir des objets aussi
-   les player pourront avoir des objet equipement en arme et armures , certaine armes sont specifique a la classe guerrier par exemple et d'autres sont commune ce qui explique la classe CommuneEquipment.

-   la classe Environnement peux etre cree avec le Environement builder afin de la personnaliser et ajouter les caracteristique necessaire  types Cle pour la foret ou Boss pour le donjon

-   les Event seront ecraser a chaque nouvelle Event, ce dernier est utiliser comme variable dans un environnementn et qui sera changer a chaque nouvel evennement rencontre.
-   EventMarchand pour discuter et commercer avec le marchand
-   Dialogue pour ajouter une logique de quete et que le PNJ qui offre la cle puisse interagir avec l' utilisateur
-   Coffre afin de recupere un coffre retrouver dans le chemin de la quete.

-   Game Contexte devra etre mla classe qui implemente la sauvegarde et le chargement et elle contient l'essentiel des informations du jeu qui seront serialiser et sauvegarder.

-   la classe Event est utiliser similairement a la classe strategy

L'UML explique brievement les relations et classes etablie.








