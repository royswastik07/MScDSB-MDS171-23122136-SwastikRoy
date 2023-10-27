import random
class petStore:
    def __init__(self):
        self.pets={
            "dog":[],
            "cat":[],
            "rabbit":[],
            "parrot":[]
        }
        self.main()
    def genID(self):
        ID=""
        for i in range(0,5):
            ID+=str(random.randint(i,10))
        return ID
    def collectpet(self):
        pet_type = input("Enter pet type: ").lower()
        breed=input("Enter the Breed: ")
        age=int(input("Enter age of the pet(in months): "))
        price=int(input("Enter the Price: "))
        if pet_type in self.pets:
            ID=self.genID()
            self.pets[pet_type].append({
                "ID":ID,
                "Breed": breed.upper(),
                "Age": age,
                "Price": price,
                "Avability": True          
            })
            
    def searchPet(self):
        search_pet_type=input("Enter the Pet type you want to search[DOG/CAT/RABBIT/PARROT]: ").lower()
        search_breed=input("Enter the Breed you want to search: ").upper()
        search_id=input("Enter the pet ID: ")
        if search_pet_type in self.pets:
            for item in self.pets[search_pet_type]:
                if search_breed == item['Breed']:
                    if search_id in item["ID"]:
                        print(item)
                    # else:
                    #     print("ID not exist")
                else:
                    print("Breed is not exist")               
        else:
            print("Pet type not exist")
            
    
    def sellPet(self):
        search_pet_type=input("Enter the Pet type you want to search[DOG/CAT/RABBIT/PARROT]: ").lower()
        search_breed=input("Enter the Breed you want to search: ").upper()
        search_id=input("Enter the pet ID: ")
        if search_pet_type in self.pets:
            for item in self.pets[search_pet_type]:
                if search_breed == item['Breed']:
                    if search_id in item["ID"]:
                        item["Avability"] = False
                    # else:
                    #     print("ID not exist")
                else:
                    print("Breed is not exist")               
        else:
            print("Pet type not exist")
    
    def showAllpets(self):
        for item,value in self.pets.items():
            print(item,value)
    
    def main(self):
        while True:
            print("Wellcome to Christ Pet Store")
            print("Options")
            print("------------------")
            print("1.Store pet details")
            print("2.Search for a pet")
            print("3.Sell a pet")
            print("4.List all pets")
            print("5.Exit")
            choice=int(input("Enter Your Choice: "))
            if choice == 1:
                self.collectpet()
            elif choice == 2:
                self.searchPet()
            elif choice == 3:
                self.sellPet()
            elif choice == 4:
                self.showAllpets()
            elif choice == 5:
                print("Exiting....")
                break
            else:
                print("Invalid Input!!!!!")