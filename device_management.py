class Device:

    id = 0

    def __init__(self, name, firmware):

        self.name = name
        self.firmware = firmware
        self.patient = None
    
    def associer(self, patient):

        self.patient = patient
    
    def dissocier(self):

            self.patient = None

    def __str__(self):

        return f'(name : {self.name} | firmware : {self.firmware} | patient : {self.patient})'


class Firmware:

    id = 0

    def __init__(self):
        self.name = f'FW_{self.id}'
    
    def update(self):

        self.id = self.id + 1
        self.name = f'FW_{self.id}'

    def __str__(self):
        return f'{self.name}'

class Patient:

    id = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

   
def choisir_element_list(list):
    """
    Permet de choisir un element dans une liste en permettant à l'utilisateur d'entrer un nombre correspondant à son choix
    """
    for id, element in enumerate(list):
        print(f'{id} : {element.name}')
    
    choix = int(input())
    return list[choix]

def afficher_state(state):
    """
    Affiche l'etat de l'operation. OK => succès | KO => echec
    """
    if state:
        print("OK")
    else :
        print("KO")


if __name__ == '__main__':
    nb = 0

    #liste stockant les différents devices créées
    list_devices = []
    #liste stockant les différents patients créées
    list_patients = []
    #On cree le firmware
    firmware = Firmware()

    while nb != 9:
        print('----- MENU ------')
        print('1 - Declarer')
        print('2 - Associer')
        print('3 - Dissocier')
        print('4 - Mettre à jour le firmware')
        print('5 - Afficher les devices')
        print('6 - Afficher Firmware')
        print('7 - Afficher Patient')
        print('8 - Nouveau Patient')
        print('9 - Quitter')

        nb = int(input("Entrer votre choix : "))

        
        state = True

        if nb == 1 :

            name = input("Entrer le nom du nouveau device : ")

            #On verifie que le device n'existe pas déjà
            for existing_dev in list_devices:
                if existing_dev.name == name:
                    state = False

            if state :
                #On crée le device et on l'ajoute a la liste des devices
                new_device = Device(name, firmware)
                list_devices.append(new_device)

        if nb == 2 :
            
            print('Choisir un device : ')
            dev = choisir_element_list(list_devices)

            print('Choisir un patient : ')
            patient = choisir_element_list(list_patients)

            #On verifie que le patient n'est pas déjà associé
            for existing_dev in list_devices:
                if existing_dev.patient == patient:
                    state = False
            
            #On verifie qu'un patient n'est pas déjà associé au device
            if dev.patient != None:
                state = False

            if state :
                #On associé le patient au device
                dev.associer(patient)

        if nb == 3 :

            print('Choisir un device : ')
            dev = choisir_element_list(list_devices)

            #On verifie qu'un patient est déjà associé
            if dev.patient == None:
                state = False
            
            if state:
                #On dissocie le patient du device
                dev.dissocier()

        if nb == 4 :

            firmware.update()
            print('Le firmware a été mis à jour !')

        if nb == 5 : 
            print('-- LISTE DES DEVICES --')
            for existing_dev in list_devices:
                print(existing_dev)

        if nb == 6 :
            print(f'Version du firmware : {firmware}')

        if nb == 7 :
            print('-- LISTE DES PATIENTS --')
            for patient in list_patients:
                print(patient)

        if nb == 8 :

            name = input("Entrer le nom du nouveau Patient : ")

            #On verifie que les patient n'existe pas déjà
            for patient in list_patients:
                if patient.name == name:
                    state = False

            if state :
                #On créer le nouveau patient et on l'ajoute a la liste de tous les patients
                new_patient = Patient(name)
                list_patients.append(new_patient)

        afficher_state(state)


