from experta import *
import pyautogui as gui

universes=['Actors','Cartoons','Fictional','Marvel']
def chooseYourUniverse():
    return gui.confirm(text='Choose your domain',title='test-your-character',buttons=universes)

def printAndHalt(kb,message):
    gui.alert(text=message,title='test-your-character',button="Nice")
    kb.halt()

def getInput(message):
    response=gui.confirm(text=message,title='test-your-character',buttons=['Yes','No'])
    if response=='Yes':
        return 'y'
    elif response=='No':
        return 'n'
    
class Actors(KnowledgeEngine):
    @Rule(NOT(Fact(action=W())))
    def isAction(self):
        self.declare(Fact(action=getInput("Is most his/here rols are action?")))
    
    @Rule(Fact(action="y"),NOT(Fact(comedy=W())))
    def isComedy(self):
        self.declare(Fact(comedy=getInput("Does he/she act some comedian roles?")))
    
    @Rule(Fact(comedy="y"),NOT(Fact(bold=W())))
    def isBold(self):
        self.declare(Fact(bold=getInput("Is he/she bold?")))

    @Rule(Fact(bold="y"),NOT(Fact(muscles=W())))
    def isMuscular(self):
        self.declare(Fact(muscles=getInput("Is he/she muscular?")))
    
    @Rule(Fact(muscles="y"))
    def isRock(self):
        printAndHalt(self,"He's Dwayne Johnson aka The Rock")

    @Rule(Fact(muscles="n"))
    def isStatham(self):
        printAndHalt(self,"He's Jason Statham")

    @Rule(Fact(bold="n"),NOT(Fact(asian=W())))
    def isAsian(self):
        self.declare(Fact(asian=getInput("Is he/she asian?")))

    @Rule(Fact(asian="y"))
    def isChan(self):
        printAndHalt(self,"He's Jackie Chan")

    @Rule(Fact(asian="n"))
    def isNiro(self):
        printAndHalt(self,"He's Robert De Niro")
    
    @Rule(Fact(comedy="n"),NOT(Fact(muscles2=W())))
    def isMuscular2(self):
        self.declare(Fact(muscles2=getInput("Is he/she muscular?")))

    @Rule(Fact(muscles2="y"),NOT(Fact(WWE=W())))
    def isWWE(self):
        self.declare(Fact(WWE=getInput("Did he/she performe in WWE?")))

    @Rule(Fact(WWE="y"))
    def isCena(self):
        printAndHalt(self,"He's John Cena")
    
    @Rule(Fact(WWE="n"))
    def isStallone(self):
        printAndHalt(self,"He's Sylvester Stallone")
    
    @Rule(Fact(muscles2="n"),NOT(Fact(short=W())))
    def isShort(self):
        self.declare(Fact(short=getInput("Is he/she short?")))

    @Rule(Fact(short="y"))
    def isPescie(self):
        printAndHalt(self,"He's Joe Pesci")
    
    @Rule(Fact(short="n"))
    def isPacino(self):
        printAndHalt(self,"He's Alfredo Pacino")
    
    @Rule(Fact(action="n"),NOT(Fact(arabic=W())))
    def isArabic(self):
        self.declare(Fact(arabic=getInput("Is he/she arabic or has arabic origins?")))
    
    @Rule(Fact(arabic="y"),NOT(Fact(egypt=W())))
    def isEgypt(self):
        self.declare(Fact(egypt=getInput("Is he/she egyptian?")))
    
    @Rule(Fact(egypt="y"),NOT(Fact(bold2=W())))
    def isBold2(self):
        self.declare(Fact(bold2=getInput("Is he/she bold?")))    
    
    @Rule(Fact(bold2="y"))
    def isHenedi(self):
        printAndHalt(self,"He's Mohamed Henedi")
    
    @Rule(Fact(bold2="n"))
    def isHelmy(self):
        printAndHalt(self,"He's Ahmed Helmy")
    
    @Rule(Fact(egypt="n"),NOT(Fact(wig=W())))
    def isWig(self):
        self.declare(Fact(wig=getInput("Does he/she wear wig?")))    
    
    @Rule(Fact(wig="y"))
    def isAzmeh(self):
        printAndHalt(self,"He's Yasser Al-Azmeh")
    
    @Rule(Fact(wig="n"))
    def isLahham(self):
        printAndHalt(self,"He's Duraid Lahham")
    
    @Rule(Fact(arabic="n"),NOT(Fact(director=W())))
    def isDirector(self):
        self.declare(Fact(director=getInput("Did he/she directe any movies?")))
    
    @Rule(Fact(director="y"),NOT(Fact(comedy2=W())))
    def isComedy2(self):
        self.declare(Fact(comedy2=getInput("Does he/she act some comedian roles?")))
    
    @Rule(Fact(comedy2="y"))
    def isBurnham(self):
        printAndHalt(self,"He's Robert Pickering (Bo) Burnham")
    
    @Rule(Fact(comedy2="n"))
    def isHarrison(self):
        printAndHalt(self,"He's Edward Harrison")
    

    @Rule(Fact(director="n"),NOT(Fact(drama=W())))
    def isDrama(self):
        self.declare(Fact(drama=getInput("Does he/she act some drama roles?")))
    
    @Rule(Fact(drama="y"))
    def isDepp(self):
        printAndHalt(self,"He's John Christopher Depp")
    
    @Rule(Fact(drama="n"))
    def isCarrey(self):
        printAndHalt(self,"He's Jim Carrey")

class Cartoons(KnowledgeEngine):
    @Rule(NOT(Fact(nickelodeon=W())))
    def isNickelodeon(self):
        self.declare(Fact(nickelodeon=getInput("Is your character from nickelodeon universe?")))
    
    @Rule(Fact(nickelodeon="y"),NOT(Fact(TMNT=W())))
    def isTMNT(self):
        self.declare(Fact(TMNT=getInput("Is your character from TMNT?")))
    
    @Rule(Fact(TMNT="y"),NOT(Fact(turtle=W())))
    def isTurtle(self):
        self.declare(Fact(turtle=getInput("Is your character a turtle?")))
    
    @Rule(Fact(turtle="y"),NOT(Fact(redish=W())))
    def eyePatchColor(self):
        self.declare(Fact(redish=getInput("Does your character wear redish eye patch?")))
    
    @Rule(Fact(redish="y"),NOT(Fact(serious=W())))
    def isSerious(self):
        self.declare(Fact(serious=getInput("Is your character serious?")))

    @Rule(Fact(serious="y"))
    def isRaphael(self):
        printAndHalt(self,"It's Raphael")

    @Rule(Fact(serious="n"))
    def isMichelangelo(self):
        printAndHalt(self,"It's Michelangelo")

    @Rule(Fact(redish="n"),NOT(Fact(swords=W())))
    def isSwords(self):
        self.declare(Fact(swords=getInput("Does your character fight using two swords?")))

    @Rule(Fact(swords="y"))
    def isLeonardo(self):
        printAndHalt(self,"It's Leonardo")

    @Rule(Fact(swords="n"))
    def isDonatello(self):
        printAndHalt(self,"It's Donatello")

    @Rule(Fact(turtle="n"),NOT(Fact(gray=W())))
    def grayCharacter(self):
        self.declare(Fact(gray=getInput("Does your character were gray armor or has gray skin?")))
        
    @Rule(Fact(gray="y"),NOT(Fact(evil=W())))
    def isEvil(self):
        self.declare(Fact(evil=getInput("Is your character evil?")))

    @Rule(Fact(evil="y"))
    def isShredder(self):
        printAndHalt(self,"It's Shredder")

    @Rule(Fact(evil="n"))
    def isSplinter(self):
        printAndHalt(self,"It's Master Splinter")

    @Rule(AND(OR(Fact(lion="n"),Fact(gray="n"),Fact(mouse="y")),NOT(Fact(girl=W()))))
    def isGirl(self):
        self.declare(Fact(girl=getInput("Is your character a girl?")))

    @Rule(Fact(girl="y"),Fact(gray="n"))
    def isApril(self):
        printAndHalt(self,"It's April O'Neil")

    @Rule(Fact(girl="n"),Fact(gray="n"))
    def isCasey(self):
        printAndHalt(self,"It's Casey Jones")

    @Rule(Fact(TMNT="n"),NOT(Fact(sponge=W())))
    def isSponge(self):
        self.declare(Fact(turtle=getInput("Is your character from SpongeBob SquarePant?")))
    
    @Rule(Fact(sponge="y"),NOT(Fact(restaurant=W())))
    def fromRestaurant(self):
        self.declare(Fact(restaurant=getInput("Does your character work in a restaurant?")))
    
    @Rule(AND(OR(Fact(restaurant="y"),Fact(bird="y")),NOT(Fact(yellow=W()))))
    def isYellow(self):
        self.declare(Fact(yellow=getInput("Is your character yellow?")))

    @Rule(Fact(yellow="y"),Fact(restaurant="y"))
    def isSpongeBob(self):
        printAndHalt(self,"It's SpongeBob SquarePants")

    @Rule(Fact(yellow="n"),Fact(restaurant="y"))
    def isSquidward(self):
        printAndHalt(self,"It's Squidward")

    @Rule(Fact(restaurant="n"),NOT(Fact(greedy=W())))
    def isGreedy(self):
        self.declare(Fact(greedy=getInput("Is your character famous for being greedy?")))

    @Rule(Fact(greedy="y"))
    def isKrabs(self):
        printAndHalt(self,"It's Mr. Krabs")

    @Rule(Fact(greedy="n"))
    def isPatrick(self):
        printAndHalt(self,"It's Patrick Star")

    @Rule(Fact(sponge="n"),NOT(Fact(tall=W())))
    def isTall(self):
        self.declare(Fact(tall=getInput("Is your character tall?")))
        
    @Rule(Fact(tall="y"),NOT(Fact(clever=W())))
    def isClever(self):
        self.declare(Fact(clever=getInput("Is your character clever?")))

    @Rule(Fact(clever="y"))
    def isKowalski(self):
        printAndHalt(self,"It's Kowalski")

    @Rule(Fact(clever="n"))
    def isRico(self):
        printAndHalt(self,"It's Rico")

    @Rule(Fact(tall="n"),NOT(Fact(leader=W())))
    def isLeader(self):
        self.declare(Fact(leader=getInput("Is your character the leader of the group he's/she's in?")))

    @Rule(Fact(leader="y"))
    def isSkipper(self):
        printAndHalt(self,"It's Skipper")

    @Rule(Fact(leader="n"))
    def isPrivate(self):
        printAndHalt(self,"It's Private")

    @Rule(Fact(nickelodeon="n"),NOT(Fact(disney=W())))
    def isDisney(self):
        self.declare(Fact(disney=getInput("Is your character from Disney?")))

    @Rule(Fact(disney="y"),NOT(Fact(mouseUni=W())))
    def isMouseUni(self):
        self.declare(Fact(mouseUni=getInput("Is your character from Mickey Mouse?")))
    
    @Rule(AND(OR(Fact(mouseUni="y"),Fact(cat="n")),NOT(Fact(mouse=W()))))
    def isMouse(self):
        self.declare(Fact(mouse=getInput("Is your character a mouse?")))
    
    # isGirl Rule
    
    @Rule(Fact(girl="y"),Fact(mouse="y"))
    def isMinnie(self):
        printAndHalt(self,"It's Minnie Mouse")

    @Rule(Fact(girl="n"),Fact(mouse="y"))
    def isMickey(self):
        printAndHalt(self,"It's Mickey Mouse")

    @Rule(Fact(mouse="n"),NOT(Fact(duck=W())))
    def isDuck(self):
        self.declare(Fact(duck=getInput("Is your character a duck?")))

    @Rule(Fact(duck="y"))
    def isDonald(self):
        printAndHalt(self,"It's Donald Duck")

    @Rule(Fact(duck="n"))
    def isGoofy(self):
        printAndHalt(self,"It's Goofy")

    @Rule(Fact(mouseUni="n"),NOT(Fact(lion=W())))
    def isLion(self):
        self.declare(Fact(lion=getInput("Is your character a lion?")))
        
    @Rule(Fact(lion="y"),NOT(Fact(evil=W())))
    def isEvil(self):
        self.declare(Fact(evil=getInput("Is your character evil?")))

    @Rule(Fact(evil="y"))
    def isScar(self):
        printAndHalt(self,"It's Scar")

    @Rule(Fact(evil="n"))
    def isSimba(self):
        printAndHalt(self,"It's Simba")

    # isGirl Rule

    @Rule(Fact(girl="y"),Fact(lion="n"))
    def isDory(self):
        printAndHalt(self,"It's Dory")

    @Rule(Fact(girl="n"),Fact(lion="n"))
    def isNemo(self):
        printAndHalt(self,"It's Nemo")

    @Rule(Fact(disney="n"),NOT(Fact(tomUni=W())))
    def isTomUni(self):
        self.declare(Fact(tomUni=getInput("Is your character from Tom and Jerry universe?")))
    
    @Rule(Fact(tomUni="y"),NOT(Fact(cat=W())))
    def isCat(self):
        self.declare(Fact(cat=getInput("Is your character a cat?")))
    
    @Rule(Fact(cat="y"),NOT(Fact(blue=W())))
    def isBlue(self):
        self.declare(Fact(blue=getInput("Is your character blue?")))

    @Rule(Fact(blue="y"))
    def isTom(self):
        printAndHalt(self,"It's Tom")

    @Rule(Fact(blue="n"))
    def isButch(self):
        printAndHalt(self,"It's Butch")

    # isMouse Rule

    @Rule(Fact(mouse="y"),Fact(cat="n"))
    def isJerry(self):
        printAndHalt(self,"It's Jerry")

    @Rule(Fact(mouse="n"),Fact(cat="n"))
    def isSpike(self):
        printAndHalt(self,"It's Spike")

    @Rule(Fact(tomUni="n"),NOT(Fact(bird=W())))
    def isBird(self):
        self.declare(Fact(bird=getInput("Is your character a bird?")))
        
    # isYellow Rule

    @Rule(Fact(yellow="y"),Fact(bird="y"))
    def isTweety(self):
        printAndHalt(self,"It's Tweety")

    @Rule(Fact(yellow="n"),Fact(bird="y"))
    def isDaffy(self):
        printAndHalt(self,"It's Daffy Duck")

    @Rule(Fact(bird="n"),NOT(Fact(human=W())))
    def isHuman(self):
        self.declare(Fact(human=getInput("Is your character a human?")))

    @Rule(Fact(human="y"))
    def isGranny(self):
        printAndHalt(self,"It's Granny")

    @Rule(Fact(human="n"))
    def isBugs(self):
        printAndHalt(self,"It's Bugs Bunny")




class Fictional(KnowledgeEngine):
    @Rule(NOT(Fact(black=W())))
    def isBlack(self):
        self.declare(Fact(black=getInput("Does your character has a black hair?")))
    
    @Rule(AND(OR(Fact(black="y"),Fact(starUni="n")),NOT(Fact(harryUni=W()))))
    def fromHarryUni(self):
        self.declare(Fact(harryUni=getInput("Is your character from Harry Potter univres?")))
    
    @Rule(AND(OR(AND(Fact(harryUni="y"),OR(Fact(black="y"),Fact(starUni="n"))),Fact(brown="n")),NOT(Fact(evil=W()))))
    def isEvil(self):
        self.declare(Fact(evil=getInput("Is your character evil?")))
    
    @Rule(Fact(evil="y"),Fact(harryUni="y"),Fact(black="y"),NOT(Fact(resurrected=W())))
    def isResurrected(self):
        self.declare(Fact(evil=getInput("Does your character resurrect?")))
        
    @Rule(Fact(resurrected="y"))
    def isRiddle (self):
        printAndHalt(self,"He's Tom Riddle")

    @Rule(Fact(resurrected="n"))
    def isSnape(self):
        printAndHalt(self,"He's Professor Severus Snape")

    @Rule(Fact(evil="n"),Fact(harryUni="y"),Fact(black="y"),NOT(Fact(beard=W())))
    def isBeard(self):
        self.declare(Fact(beard=getInput("Does your character have thick beard?")))
        
    @Rule(Fact(beard="y"))
    def isHagrid (self):
        printAndHalt(self,"He's Rubeus Hagrid")

    @Rule(Fact(beard="n"))
    def isPotter(self):
        printAndHalt(self,"He's Harry Potter")

    @Rule(Fact(harryUni="n"),Fact(black="y"),NOT(Fact(human=W())))
    def isHuman(self):
        self.declare(Fact(human=getInput("Is your character a human?")))
    
    @Rule(Fact(human="y"),NOT(Fact(girl=W())))
    def isGirl(self):
        self.declare(Fact(girl=getInput("Is your character a girl?")))
        
    @Rule(Fact(girl="y"))
    def isAlice(self):
        printAndHalt(self,"She's Alice from Alice's Adventures in Wonderland ")

    @Rule(Fact(girl="n"))
    def isHolmes(self):
        printAndHalt(self,"He's Sherlock Holmes")

    @Rule(AND(OR(Fact(human="n"),AND(Fact(harryUni="n"),Fact(starUni="n"))),NOT(Fact(cyborg=W()))))
    def isCyborg(self):
        self.declare(Fact(beard=getInput("Is your character a cyborg?")))
        
    @Rule(Fact(human="n"),Fact(cyborg="y"))
    def isTerminator(self):
        printAndHalt(self,"He's The Terminator")

    @Rule(Fact(human="n"),Fact(cyborg="n"))
    def isSpock(self):
        printAndHalt(self,"He's Spock from Star Trek series")

    @Rule(Fact(black="n"),NOT(Fact(starUni=W())))
    def isStarWarsUni(self):
        self.declare(Fact(starUni=getInput("Is your character from Star Wars univres?")))
    
    @Rule(Fact(starUni="y"),NOT(Fact(brown=W())))
    def isBrown(self):
        self.declare(Fact(brown=getInput("Does your character have brown hair?")))
    
    @Rule(Fact(brown="y"),NOT(Fact(fliped=W())))
    def isFliped(self):
        self.declare(Fact(fliped=getInput("Does your character turn from good to evil?")))
    
    @Rule(Fact(fliped="y"))
    def isSkywalker(self):
        printAndHalt(self,"He's Anakin Skywalker")
        
    @Rule(Fact(fliped="n"))
    def isKenobi(self):
        printAndHalt(self,"He's Obi-Wan Kenobi")

    # isEvil Rule
    
    @Rule(Fact(evil="y"),Fact(brown="n"))
    def isVader(self):
        printAndHalt(self,"He's Darth Vader")

    @Rule(Fact(evil="n"),Fact(brown="n"))
    def isYoda(self):
        printAndHalt(self,"He's Yoda")

    # fromHarryUni Rule
    
    # isEvil Rule
    
    @Rule(Fact(evil="y"),Fact(harryUni="y"),Fact(starUni="n"))
    def isVoldemort(self):
        printAndHalt(self,"He's Lord Voldemort")

    @Rule(Fact(evil="n"),Fact(harryUni="y"),Fact(starUni="n"))
    def isDumbledore(self):
        printAndHalt(self,"He's Professor Albus Dumbledore")

    # isCyborg Rule
        
    @Rule(Fact(harryUni="n"),Fact(starUni="n"),Fact(cyborg="y"))
    def isRobocob(self):
        printAndHalt(self,"He's Robocob")

    @Rule(Fact(harryUni="n"),Fact(starUni="n"),Fact(cyborg="n"))
    def isRobin(self):
        printAndHalt(self,"He's Robin Hood")

class Marvel(KnowledgeEngine):
    @Rule(NOT(Fact(black=W())))
    def isBlack(self):
        self.declare(Fact(black=getInput("Does your character has a black hair?")))
 
    @Rule(Fact(black="y"),NOT(Fact(suit=W())))
    def isSuit(self):
        self.declare(Fact(suit=getInput("Does your character wear black suit?")))
    
    @Rule(AND(OR(Fact(suit="y"),Fact(girl="n")),NOT(Fact(evil=W()))))
    def isEvil(self):
        self.declare(Fact(evil=getInput("Is your character evil?")))

    @Rule(AND(OR(AND(Fact(evil="y"),Fact(suit="y")),Fact(redSuit="y"),Fact(red="n")),NOT(Fact(fly=W()))))
    def canFly(self):
        self.declare(Fact(fly=getInput("Can your character fly?")))

    @Rule(Fact(fly="y"),Fact(evil="y"))
    def isLoki(self):
        printAndHalt(self,"He's Loki")
    
    @Rule(Fact(fly="n"),Fact(evil="y"))
    def isVenom(self):
        printAndHalt(self,"He's Venom")
    
    @Rule(Fact(evil="n"),Fact(suit="y"),NOT(Fact(wakanda=W())))
    def fromWakanda(self):
        self.declare(Fact(fly=getInput("Is your character from Wakanda?")))

    @Rule(Fact(wakanda="y"))
    def isPanther(self):
        printAndHalt(self,"He's Black Panther")
    
    @Rule(Fact(wakanda="n"))
    def isAnt(self):
        printAndHalt(self,"He's Ant Man")

    @Rule(Fact(suit="n"),NOT(Fact(redSuit=W())))
    def isRedSuit(self):
        self.declare(Fact(redSuit=getInput("Does your character wear red suit?")))
    
    # canFly Rule
    
    @Rule(Fact(fly="y"),Fact(redSuit="y"))
    def isIron(self):
        printAndHalt(self,"He's Iron Man")
    
    @Rule(Fact(fly="n"),Fact(redSuit="y"))
    def isSpider(self):
        printAndHalt(self,"He's Spider Man")
    
    @Rule(AND(OR(Fact(redSuit="n"),Fact(girl="y"),Fact(red="y")),NOT(Fact(xMen=W()))))
    def fromXMen(self):
        self.declare(Fact(xMen=getInput("Is your character from X-Men?")))

    @Rule(Fact(xMen="y"),Fact(redSuit="n"))
    def isWolverine(self):
        printAndHalt(self,"He's Wolverine")
    
    @Rule(Fact(xMen="n"),Fact(redSuit="n"))
    def isSheHulk(self):
        printAndHalt(self,"She's She-Hulk")

    @Rule(Fact(black="n"),NOT(Fact(blue=W())))
    def isBlue(self):
        self.declare(Fact(blue=getInput("Is your character blue or wear blue suit?")))
    
    @Rule(Fact(blue="y"),NOT(Fact(girl=W())))
    def isGirl(self):
        self.declare(Fact(girl=getInput("Is your character a girl?")))

    # fromXMen Rule

    @Rule(Fact(xMen="y"),Fact(girl="y"))
    def isStorm(self):
        printAndHalt(self,"She's Storm")
    
    @Rule(Fact(xMen="n"),Fact(girl="y"))
    def isMarvel(self):
        printAndHalt(self,"She's Captian Marvel")
    
    # isEvil Rule

    @Rule(Fact(evil="y"),Fact(girl="n"))
    def isThanos(self):
        printAndHalt(self,"He's Thanos")
    
    @Rule(Fact(evil="n"),Fact(girl="n"))
    def isAmerica(self):
        printAndHalt(self,"He's Captain America")

    @Rule(Fact(blue="n"),NOT(Fact(red=W())))
    def isRed(self):
        self.declare(Fact(red=getInput("Does your character has red hair?")))
    
    # fromXMen Rule

    @Rule(Fact(xMen="y"),Fact(red="y"))
    def isCyclops(self):
        printAndHalt(self,"He's Cyclops")
    
    @Rule(Fact(xMen="n"),Fact(red="y"))
    def isWidow(self):
        printAndHalt(self,"She's Black Widow")
    
    # canFly Rule
    
    @Rule(Fact(fly="y"),Fact(red="n"))
    def isThor(self):
        printAndHalt(self,"He's Thor")
    
    @Rule(Fact(fly="n"),Fact(red="n"))
    def isDead(self):
        printAndHalt(self,"He's Deadpool")


universe=chooseYourUniverse()

if universe==universes[0]:
    KBS=Actors()
elif universe==universes[1]:
    KBS=Cartoons()
elif universe==universes[2]:
    KBS = Fictional()
elif universe==universes[3]:
    KBS = Marvel()


KBS.reset()
KBS.run()