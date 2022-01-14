import hangman_art 
import hangman_words
import random
print(hangman_art.logo)
print("WELCOME TO THE HANGMA GAMES")
chosen_word=random.choice(hangman_words.word_list)
end_of_game=False
score=7
blank=[]
for i in range(0,len(chosen_word)):
  blank+="_"
print(blank)
list_chosen_word=list(chosen_word)
while end_of_game==False:
  guess=input("guess a letter?\n")
  for i in range(0,len(chosen_word)):
    character=list_chosen_word[i]
    if guess==character:
      blank[i]=character
      print(blank)
  if "_"not in blank:
    end_of_game=True
    print("you have won a game")
  if guess not in list_chosen_word:
    score-=1
    print(hangman_art.stages[score])
  if score==0:
    end_of_game=True
    print("you have lost the game")
    print(f"your word was{chosen_word}")    


