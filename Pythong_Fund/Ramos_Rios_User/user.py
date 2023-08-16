class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #default values
        self.is_rewards_member = False
        self.gold_card_points = 0

    #display info self method
    def display_info(self):
        print(f"{self.first_name} \n {self.last_name} \n {self.email} \n {self.age} \n {self.is_rewards_member} \n {self.gold_card_points}")

    #enroll self method
    def enroll(self, is_rewards_member):
        if is_rewards_member == True:
            self.gold_card_points = 200

    #spend points
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

    #re-enroll
    def re_enroll(self):
        if is_rewards_member == True:
            print("You're already a member")
        else:
            self.enroll()


user1 = user("Jesus", "Ramos", "email", 25)
user2 = user("Jose", "Ramos", "jose.email@email.com", 29)

user1.display_info()

user1.enroll(True)
user1.display_info()
#spending 50 points first user
user1.spend_points(50)
user1.display_info()
#enroll second user
user2.enroll(True)
#spen 80points second user
user2.spend_points(80)
user2.display_info()

