""" 
Starshipladdev-
(21/10/19)
This is a highschool python project I created back in 2015.
It is a simple text-based dungeon explorer.
Horrible commenting will be left as is.


 """
#colours-snow,honeydew,midnight blue,firebrick,light blue,
#IntVar(),StringVar(),Label, font= ("font,size"), Var.set(set),textvariable,randrange()
#import n
#needed moduels
from Tkinter import *
from random import *
class PlayerClass:                  #defines the player class and all his attributes.- Will be called apoun during combat equation, buying stuff, and health.
   
   def __init__(self,health,attack,gold,haskey):
      self.health=health
      self.attack=attack
      self.gold=gold
class Enemy:                        #defines the enemy class- used to construct random enemies
   def __init__(self,name,health,attack,givegold):
      self.name=name
      self.health=health
      self.attack=attack
      self.givegold=givegold
nullvalue=0
player=PlayerClass(10,2,0,False)#Before anything else, creates a global playerclass
player_inventory=[]#Creates a list of inventory items. By using "name" in palyer_inventory, can call apoun any needed item
objects=["Sword Dealer","Health Potion","Key","Door"]#A list of objects that coudl be encountered- defines what type of non-hostiel encounter occurs
class MainProcess:#At the current moment, I cannot think of any reason I woudl need multile
                              #classes on screen. Due to this, at the moment ,I will keep all information here
   def __init__(self,parent,):#set up the widgits to be used(see brief for layout of nessasary widgits.)
       self.playername=StringVar()#This will be set at the name type section
       self.eventnumber=IntVar()#Ghostcode,could be sued o nfurther additions, dosn't affect program
       self.player_health=StringVar()#Not acctualy player.health,just the Strign value to dispaly under player's avatar. Is changed whenever the player.health is affected
       self.player_health.set("Health:"+str(player.health))
       self.eventnumber.set(0)#Ghost code
       self.face1=PhotoImage(file="face1.GIF")
       self.face2=PhotoImage(file="face2.GIF")#These sections simply load the in file images for later use
       self.face3=PhotoImage(file="face3.GIF")
       self.face4=PhotoImage(file="face4.GIF")
       self.maintext=Label(parent,text="Welcome to Adventure Simulator 2015. You need to locate a key, take the magical door out of here, and stay alive. Good luck",wraplength=350,bg="olive drab",)
       #^is probably the most important component. This is the text that the User will get-
       #-information about what is occurring from.
       #also note:ued wraplength instead of two labels for intro text
       self.maintext.grid(row=0,column=0,columnspan=3)
       self.avatar=Label(parent,image="")#Avatar is given a grid location, but no display
       self.avatar.grid(row=0,column=4)
       self.healthlabel=Label(parent,textvariable=self.player_health)#same goes for dispalyign the palyer's health
       #BUTTONS:The below __init__'s set up the four buttons that will be manipulated depending on what event is occurring.
       #they are by default set to send the player to character creation
       self.option1=Button(parent,text="Continue to Character Creation",command=self.setavatarpic,width=35)
       self.option1.grid(row=1,column=0)
       self.option2=Button(parent,text="Continue to Character Creation",command=self.setavatarpic,width=35)
       self.option2.grid(row=1,column=2)       
       self.option3=Button(parent,text="Continue to Character Creation",command=self.setavatarpic,width=35)
       self.option3.grid(row=2,column=0)                              
       self.option4=Button(parent,text="Continue to Character Creation",command=self.setavatarpic,width=35)
       self.option4.grid(row=2,column=2)
       #NAME SELECTION:Another two widgits that will be created for character creation, then removed after storign variables
       self.nametype=Entry(parent,)
       self.confirmname=Button(parent,text="confirm",command=self.confirmnamefunc)
       #FIRST FUNC:This will be the first function the palyer will be taken to, and allows them to select one of the pre-loaded images as a character avatar
       #it also sets the four options to have the corrosponding face
       #also temporarily sets buttosn width as 100, as images have diffrent measurmetns from
       #text
       #I found I could use the lambda command to stop option 4 automaticly beign called
       
   def setavatarpic(self):
      
      self.maintext.configure(text="Please select your character's avatar")
      self.option4.configure(width=100,text="",image=self.face4,command=lambda:self.setavatar1("d"))
      self.option1.configure(width=100,text="",image=self.face1,command=lambda:self.setavatar1("a"))
      self.option2.configure(width=100,text="",image=self.face2,command=lambda:self.setavatar1("b"))
      self.option3.configure(width=100,text="",image=self.face3,command=lambda:self.setavatar1("c"))

      #SET THE AVATAR LABEL WITH SELECTED IMAGE:
      #As noted in the log, I realised after I ahd set up these four diffrent functions I could have created one function and jsut set a diffrent image based on arguments given, but
      #I found there were mroe important issues to deal with, and its a working system.
	  #REREUPDATE-The setavatar function is now 1 function using 4 diffrent variables, not 4 diffrent functions.
#THESE CLASSES BELOW EACH SET THE AVATAR IAMGE AND DISPAY DYNAMIC HEALTH
   def setavatar1(self,x):
      if x=="a":
         self.avatar.configure(image=self.face1)
      elif x=="b":
         self.avatar.configure(image=self.face2)
      elif x=="c":
         self.avatar.configure(image=self.face3)
      elif x=="d":
         self.avatar.configure(image=self.face4)
      else:
         print("Error")
         
      self.setname()
      self.healthlabel.grid(row=1,column=4)      
         
#BELOW IS THE OLD SET IMAGE BUTTONS
# def setavatar1(self):
#      self.avatar.configure(image=self.face1)
#      self.setname()
 #     self.healthlabel.grid(row=1,column=4)
#   def setavatar2(self):
#      self.avatar.configure(image=self.face2)
#      self.setname()
#    def setavatar3(self):
#       self.avatar.configure(image=self.face3)
#       self.setname()
 #      self.healthlabel.grid(row=1,column=4)
#    def setavatar4(self):
 #      self.avatar.configure(image=self.face4)
  #     self.setname()
  #     self.healthlabel.grid(row=1,column=4)"""
  
  
#Set default Character Name as hero  
#SET THE PLAYERS NAME, STORE IT IN A CLASS SPECIFIC VARIABLE:
#The following function changes the U.I to a name input section(No char limit due to word wrap) and a continue button
#after this a random event will constantly be called
#FUTUREDEV:More character creation options: a stats modifying system woudl be easy enough to implement with buttons
   def setname(self):
      self.maintext.configure(text="Please chose your characters name")
      self.option1.grid_forget()
      self.option2.grid_forget()
      self.option3.grid_forget()
      self.option4.grid_forget()
      self.nametype.grid(row=1,column=0,columnspan=2)
      self.nametype.insert(END,"Hero")
      self.confirmname.grid(row=1,column=4)
   def confirmnamefunc(self,):
      self.b=self.nametype.get()
      self.playername.set(self.b)
      if "\"" in self.b:
         self.maintext.configure(text="You can't use quotation marks in your name sorry")
      elif len(self.b)>15:
         self.maintext.configure(text="Name is too long, please keep it under 15 characters")
      elif self.b=="":
         self.maintext.configure(text="Please input a name")
#ERROR CONTROL ^^^.
#Checks if the user has inputed any writing into the name entry. Othwerwise asks them to type somthing
#Checks if the user name has quotation marks. Sicne quotation amrks are used to talk to the character Later, The program tells the user to remove them
#confirm button remaisn unchanged throughout so they can still continue
#It also calls the user out if they try and use punctuation used i ngame, liek quotation marks.
         #Below sets a StringVar as the confirmed,uncourupted strign value.
         #It then resets the buttosn to 35 from now on.
      else:  
         self.name=self.playername.get()
         self.nametype.grid_forget()
         self.confirmname.grid_forget()
         self.maintext.configure(text=("your character's name is " +self.name))
         self.option1.grid(row=1,column=0,)
         self.option2.grid(row=1,column=2,)
         self.option3.grid(row=2,column=0,)
         self.option4.grid(row=2,column=2,)
         self.option1.configure(width=35,image="",text="Begin Your Quest",command=self.randomevent)
         self.option2.configure(width=35,image="",text="Begin Your Quest",command=self.randomevent)
         self.option3.configure(width=35,image="",text="Begin Your Quest",command=self.randomevent)
         self.option4.configure(width=35,image="",text="Begin Your Quest",command=self.randomevent)



#ONE OF THE MOST PRIMARY FUCNTIONS:FACE THE PALYER WITH A NEW RANDOM EVENT, POSITIVE OR NEGATIVE
#This function is what is called when one problem has been resolved and the player wishes to continue
#It creates a random number from a range each time its called, with a 50% cahnce of spawning a random monster(decided randomly in a similar manner)
#an a 50%chance of spawning a encoutner with an object. The object is called by retreiving a random index from the 'objects' list, and giving an appropriate
#change to the options available based on what strign value was used as an argument.
#I really like this as it gives a larger content selection
#NOTE:I try to input a 'quit' option wherever available for good user usability. this closes the application entierly
#FUTUREDEV:Create diffrent chances of event(E.G-morel iekly to encounter a sword dealer than a key)
#FUTUREDEVREVISE:The previosu statment was doen for a mosnter. there is a 3/5 chance to encoutner a ratman, the weakest enemy, comapred to
#other types of foe
   def randomevent(self,):
      type_of_event=randrange(0,3)     
      #moNSter shows up-Crete introduction text, change option buttosn to suitable options, create a isntacne of enemy fro ma selection
     #of prefab monster stats.
      if type_of_event==1:
         self.monster_type= randrange(0,5)
         if self.monster_type==1:
            self.monster=Enemy("Goblin",6,3,30)
         elif self.monster_type==2:
               self.monster=Enemy("Orc",8,4,50)
               
         elif self.monster_type==3 or self.monster_type==4:
            Enemy("Ratman",4,2,10)
         else:self.monster=Enemy("KALEB THE BIG FUCKIGN FAGGOT",20,16,50000000000000)
         self.maintext.configure(text="You see a "+self.monster.name +" appear in front of you")
         self.option1.configure(image="",text="attack it",command=self.attack)
         self.option2.configure(image="",text="run away",command=self.flee)
         self.option3.configure(image="",text="check it's stats",command=self.statcheck)
         self.option4.configure(image="",text="Quit",command=root.destroy)
      if type_of_event==2:
         self.f=randrange(0,len(objects))
         self.objectinstance=objects[self.f]
         #depending on what object is called, configure the option buttons to realevant options, with assosiated function called
         self.maintext.configure(text="You stumble across a " +self.objectinstance)
         if self.objectinstance=="Sword Dealer":
            self.option1.configure(text="Upgrade Sword(50G)",command=self.swordbuy)
            self.option3.configure(text="Check your purse",command=self.moneycheck)
            self.option2.configure(text="Continue on Your Quest",command=self.flee)
            self.option4.configure(text=" Quit",command=root.destroy)

         elif self.objectinstance=="Health Potion":
            self.option1.configure(text="Drink it up",command=self.drink)
            self.option2.configure(text="Listen to him-Drink it",command=self.drink)
            self.option3.configure(text="Say no to Peer Pressure and leave",command=self.flee)
            self.option4.configure(text="Quit ",command=root.destroy)
         elif self.objectinstance=="Key":
            self.option1.configure(text="Pick upthe key",command=self.getkey)
            self.option2.configure(text="Fight it",command=self.fightkey)
            self.option3.configure(text="Continue on Your Quest",command=self.flee)
            self.option4.configure(text=" Quit",command=root.destroy)
         elif self.objectinstance=="Door":
            self.doorbusted=randrange(0,11)
            if self.doorbusted>1:
               self.maintext.configure(text="You come across a Magic door. It's broke yo")
               self.option1.configure(text="Continue on your Quest",command=self.randomevent)
               self.option2.configure(text=" ",command=self.null)
               self.option3.configure(text=" ",command=self.null)
               self.option4.configure(text=" ",command=self.null)
            else:
               self.option1.configure(text="Open the door",command=self.dooropen)
               self.option2.configure(text="Fight it",command=self.fightkey)
               self.option3.configure(text="Continue on Your Quest",command=self.flee)
               self.option4.configure(text=" Quit",command=root.destroy)
         else:#Error correction in case the random event calls an event I havn't made. Used to make sure newevent fucntion is calling correctly
            self.maintext.configure(text="The Dev gone done messed up, Plz inform him")
#DRINK POTION OPTION
#Made a seperate fucntio nfor when palyer drinsk the potion, configures the global player health variable and adds 2. Then dispalys new health
   def drink(self):
      self.maintext.configure(text="You gulp down the magic potion. +2 health")
      player.health=(player.health+2)
      self.player_health.set("Health:"+str(player.health))
      self.option1.configure(text="Continue",command=self.randomevent)
      self.nullify()
#CHECK MONEY AMMOUNT
#I thought it woudl be more interactive to manually have to check yoour money rather than having it always rpesent like health
#Changes Maintext to the ammount of gold you have, but leaves word buying options there, so you can still buy items after knowign how much you have      
   def moneycheck(self):
      self.maintext.configure(text="You have "+str(player.gold)+" Gold coins in your purse")
#FIGHT INNANIAMTEOBJECT
#Dispaly humourous text when a palyer selects to fight a key or door. Leaves other options open to interact with the said object
   def fightkey(self):
      self.maintext.configure(text="It's an inanimate object. Why? What did you hope to acheive?")
#adds a key string value to the palyer inventory list. This will alter be used as an arugment when trying to open a door
#FUTUREDEV:More items that can be given to inventory list
#FUTUREDEV:Make it so palyer can only pick up key once
#FUTUREDEVREVISED:Key now replaced in objects string after being picked up.
#Program still knows player has a key, but the event will never unessacierily show up again.
#it also means sword dealer will appear more, fufiling my previous wish
   def getkey(self):
      self.maintext.configure(text="You pick up the key. This will come in handy later")
      player_inventory.append("Key")
      self.option1.configure(text="Continue",command=self.randomevent)
      self.nullify()
      objects[2]="Sword Dealer"
#This function then allows the palyer to continue or quit
#could call another random event where this function is used, but this leads to a more natural transitio nto a new event.
   def flee(self):
      self.maintext.configure(text="You decide you could do without it")
      self.option1.configure(text="Continue on Your Quest",command=self.randomevent)
      self.nullify()
#OPEN DOOR THAT ISNT BROKEN WITH KEY
#This fucntion sees if the palyer_invintory list includes the "key" item. If so it opens the door, otherwise it lets the palyer continue on the game

   def dooropen(self):
      if "Key" in player_inventory:
         self.maintext.configure(text="You open the door and step into a new world. Congratulations ,you win")
         self.option2.configure(text=" ",command=self.null)
         self.option3.configure(text=" ",command=self.null)
         self.option4.configure(text=" ",command=self.null)  
         self.option1.configure(text="Finish",command=root.destroy)
      elif "Key" not in player_inventory:      
         self.maintext.configure("You need a key")
         self.option1.configure(text="Continue",command=self.randomevent)
         self.nullify()
#ATTACK ENEMY CREATURE, PROCESS COMBAT SYSTEM, DISPALY LOSER TEXT IF HEALTH<0, DISPALY WIN TEXT AND GIVE GOLD IF
#ENEMY CREATURE DESTROYED
#The turn time is based on how quickly the player can kill the monster.
#since the monsters health varies based on which monster spawned, and the player attack varies based on how many sword upgrades the brought
#the turn time is modified by getting these two values each time this function is called.
#so that the player can't get to strong to even let the monster get an attack, if turn time=0 or less, it is automatically set to 1 to give the monster a chance to attack
#for every 1 in the turn time value, the monster deals a random number damage(subtraction from player.health) between 0 and its max attack
#every time thsi happens, the program checks if the palyers health value is 0 or less. If so the program allows the user to exit after being defeated
#otherwise it says that the monster has been killed, adds the monsters gold value to the palyer total gold, and allows the player to continue.
 #Throughout this the player health is displayed every time it is altered, for visual feedback for the user     
   def attack(self):
      self.turntime=(self.monster.health-player.attack)
      if self.turntime<=0:
         self.turntime=1
      for x in range(0,self.turntime):
         player.health=(player.health-(randrange(0,(self.monster.attack+1))))
         if player.health<=0:
            self.player_health.set("Health:0")
            self.maintext.configure(text="You are slain by the "+self.monster.name+". Your quest has ended")            
            self.option1.configure(text="Finish",command=root.destroy)
            self.nullify()
            break
         else:
            self.player_health.set("Health:"+str(player.health))
            self.maintext.configure(text="You slay the "+self.monster.name)
            self.option1.configure(text="Continue on your Quest",command=self.randomevent)
            player.gold=(player.gold+self.monster.givegold)


#A useless function that buttons not currently in use are assigned to. Its more aesthetically appealing to have useless buttons temporarily then have them
#randomly disappear
   def null(self):
      self.nullvalue=nullvalue
      self.nullvalue=(self.nullvalue+1)
#SHOW MOSNTERS STATS
#this function gets the statistics of the current instance of mosnter, and dispalys them to user.
#This allows the user to make and informed decision wether to ru nor fight, and those options remain unchanged
#since they were called in the previous action
   def statcheck(self):
      self.maintext.configure(text="The "+self.monster.name+" has the following stats: "+str(self.monster.health)+" health, does up to "+str(self.monster.attack)+" attack and drops "+str(self.monster.givegold)+" gold")
#Checks if the player has at least 50 gold.
#if so, adds 2 t othe total palyer.attack value, and gives the option to continue on, check total money, or do the same function.
#otherwise, the maintext dispalys a text that tells the user they do not have enough gold, and allows them to continue or call the check purse function
   def swordbuy(self):
      if player.gold>=50:
         player.gold=(player.gold-50)
         self.maintext.configure(text="He improves your sword by 2 damage, and takes your 50 gold. You now have "+str(player.attack)+" attack")
         player.attack=(player.attack+2)
         self.option1.configure(text="Upgrade further",command=self.swordbuy)
         self.option2.configure(text="Check your purse",command=self.moneycheck)
         self.option3.configure(text=" Continue on your quest",command=self.randomevent)
         self.option4.configure(text="Quit",command=root.destroy)
      else:
         self.maintext.configure(text="He shakes his head,and says \""+self.playername.get()+" You'll need more money for that\"")
         self.option1.configure(text="Continue on Your Quest",command=self.randomevent)
         self.option2.configure(text="Check your purse",command=self.moneycheck)
         self.option3.configure(text=" ",command=self.null)
         self.option4.configure(text="Quit",command=root.destroy)        
   def nullify(self):
      self.option2.configure(image="",text="  ",command=self.null)
      self.option3.configure(image="",text="  ",command=self.null)
      self.option4.configure(text="Quit",command=root.destroy)
	

#run the main system
root = Tk()
root.title("Adventure Simulator 2015")#Name of program
root.geometry("750x150+100+100")#Set geometry of program in pixles
show_label=MainProcess(root)
root.mainloop()#run the system in a loop

#To sum-
#MainProcess-
#attack function to resolve fights
#confirm name fucntion, put input value as StringValue of players name
#drink fucntion, add health to palyer classs health, change the health dispaly
#Sword buy, check if palyer has 50 gold. remove if so and add value to palyer.attack. offer to do it again or continue
#Open door, check if key string is anywhere in inventory list, if so end game after flavour text, if not allows player to continue
#flee- add flavour text the nallow player to encounter new rando mencounter
#random encoutner- give the palyer an encounter drawn fro ma rando mrange of int values, each with a corrospondign event
#enemy- spawn an enemy class with stats based on its object constructed, whcih si based on a rando mrange. Changes optiosn to a global selection.

#changenotes!!!!!!!!!!
#I made setavatar one fucntion, isntead of 4 difrrent ones
#I swapped repeditive code to nullify 3 buttons into 1 function to call that did the sme thing (self.nullify)

