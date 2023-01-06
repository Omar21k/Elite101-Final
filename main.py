import random

def guessing_game():
  
  shots=3
  guess=0
  while guess!=7:
    guess=int(input('guess my favorite number: '))
    shots=shots-1
    print(f'You have {shots} shots left')
    if shots==0 and guess!=7:
      print('you ran out of guesses')
      break
  if guess==7:
    print('BUT YOU GUESSED IT GOOD JOB YOU WON!!! ')
      


ran=random.choice(['Im kinda tired but yeah', 'I feel great', 'Im exausted', 'I feel okay today is just not it', 'Im alright'])

name=input('Hi there, my name is Mobi! What\'s your name? ')
#-------------------------sport---------------------------------------
sport=input(f'Nice to meet you {name}, what\'s your favorite sport')
if sport=='soccer':
  player=input(f'Omg that\'s my favorite sport too {name}!!, who\'s your favorite player?')
  if player=='Ronaldo' or player=='Cristiano Ronaldo' or player=='ronaldo' or player=='cr7':
    print('He is my favorite too, he\'s the goat')
  elif player=='Messi' or player=='messi':
    print('Yeah, he is a great player')
  else:
    print('Yeah but Messi and Ronaldo are definitely the best')
elif sport=='Basketball' or sport=='basketball':
  print('I like playing basketball but not really watch it')
elif sport=='Baseball' or sport=='baseball':
  print('I never truly undertood Baseball to be honest')
elif sport=='Football' or sport=='football':
  print('I find football boring but it\'s definitely entertaining to a lot of people')
else:
  print('Oh cool')

#-----------------------------Age-------------------------------------

  
age=int(input((f'Oh silly me I forgot to ask, how old are you {name}')))
if age<=3:
  print('OH REALLY, haha you\'re so funny')
elif 10>=age>=4:
  cartoon=input(f'Wow, you\'re so young what\'s your favorite cartoon show {name}')
  if cartoon=='We bare bears' or cartoon=='We Bare Bears':
    bear=input('OMG SAME, who\'s your favorite character?')
    if bear=='Ice Bear' or bear=='ice bear' or bear=='Ice bear':
      print('Yeah that\'s my favorite character too, he\'s so funny')
    elif bear=='Panda' or bear=='panda':
      print('Hahaha yeah Panda is so cool')
    elif bear=='Grizzly' or bear=='Grizz' or bear=='grizzly':
      print('I like how he is the oldest brother and enjoys mentiontiong it')
    else:
      print('My favorite is Ice Bear')
  elif cartoon=='Gumball' or cartoon=='gumball':
    print('I used to watch gumball when I was little, it\'s really good')
  elif cartoon== 'Arthur' or 'arthur':
    print('Ahhh how original')
  else:
    print('Cool')
elif 13>=age>=11:
  job=input('What do you want to be when you grow up')
  if job=='idk' or job=='I\'m not sure' or job=='I don\'t know':
    print('Although I\'m an intelligent chatbot, It took me time to figure out that that\'s what I want to do for living')
  elif job=='Doctor' or job=='Dentist' or job=='doctor' or job=='dentist':
    print(f'yeah {job}s make a lot of money but it\'s a difficult academic pathway, the outcome is definitely worth it though')
  else:
    print('hopefully you achieve that!')
elif 18>=age>=14:
  decision=input('Oh so you\'re probably go to high school by now, are planning on going to college?')
  if decision=='yes' or decision=='Yes' or decision=='yeah' or decision=='Yeah':
    college=input('What college do you want to go to')
    if college=='Stanford'or college=='stanford':
      print('It\'s one of, if not the best computer science college to go to, a lot of professors from Stanford have wona Noble prize')
    else:
      print(f'yeah {college} is pretty cool')
elif 25>=age>=19:
  employed=input('Are you employed')
  if employed=='yes' or employed=='Yes' or employed=='Yeah' or employed=='yeah':
    work=input('Oh cool what do you work?')
    print('cool')
  elif employed=='No' or employed=='no':
    print('The company I work for needs some salesmen soooo')
  else:
    print('oh cool')
else:
  quote=input('What\'s your favorite quote or piece of advice?')
  print('Mine is "Everybody wants to go to heaven but nobody wants to die"')


#------------------------------Reading--------------------------------
reading=input('Do like reading fiction or non-fiction more? ')
if reading =='fiction' or reading=='Fiction':
  print(f'Well I recommend reading a novel called "We were liars" it\'s one of the best to exist, the plot twist at the end is so unpredictable no matter how hard you try, you should read it {name}')
elif reading=='non fiction' or reading=='non-fiction' or reading=='Non fiction':
  print('Well you should ready a book called "Atomic habits" and also "How to win friends and influence people " these two are life changers to be honest, they will definitely change your perception of life')
#--------------------------------Food---------------------------------
food=input(f'What\'s your favorite food {name}')
egyptian=input('Have you ever tried egyptian food?')
if egyptian=='yes' or egyptian=='Yes' or egyptian=='Yeah' or egyptian=='yeah':
  wow=input(f'No way {name}, what did you try?')
  print('That\'s crazy!!')
elif egyptian=='No' or egyptian=='no':
  print('WELL you should try it it\'s different from anything you have ever tired before')
else:
  print('Oh cool')
#---------------------------Guessing Game-----------------------------
game=input(f'Do you want to play a little game {name}')
if game=='Yes' or game=='yes' or game=='sure' or game=='Sure':
  print('Great!, the game is called "Guess my favorite number", you will try to guess my favorite single digit number.\nyou will have 3 shots. Good luck\nLet\'s begin!!')
guessing_game()


print(f'Ahhh that was fun {name}')
fun=input(f'Did you have fun talking to me {name}?')
if fun=='Yes' or fun=='yes' or fun=='ofc' or fun=='yeah':
 print(f'I\'m so happy to hear that, you\'re such a wonderful person {name}, I wish you nothing bul the very best in life...\n-Mobi')
elif fun=='no' or fun=='No' or fun=='Not really' or fun=='not really':
  print('Sorry to hear that, I wish you nothing but the very best in life...\n-Mobi')
else:
  print('Well, I wish you nothing but the very best in life...\n-Mobi')
