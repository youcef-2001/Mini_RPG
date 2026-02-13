





from Model.GameContext import GameContext
from Model.Environnement import EnvironnementBuilder
from Model.personnage_factory import Guerrier, Mage, Voleur


if __name__ == "__main__":

    print("Debut du jeu!")
    print("Donjon Quest!")


    #initialisation des environnement
    builder = EnvironnementBuilder()
    village= builder.reset().SetTitle("Village").AddEventlist(5).AddQuest().GetEnv()
    foret= builder.reset().SetTitle("Foret").AddEventlist(10).insertKey().GetEnv()
    donjon= builder.reset().SetTitle("Donjon").AddEventlist(20).setBoss().GetEnv()
    #Setup du joueur


    choices= ["Guerrier,Mage,Voleur"]
    player_reply= input(f"Choisissez le type de joueur de depart: {choices}")
    joueur = None
    match(player_reply):
        case "Guerrier" : joueur = Guerrier()
        case "Mage" : joueur= Mage()
        case "Voleur": joueur= Voleur()



    gamecontext= GameContext(village,foret,donjon,joueur)
    gamecontext.launch()


