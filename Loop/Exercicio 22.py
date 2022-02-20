#Orgulhoso desse codigo, mesmo que 80% foi copiado eu entendi o codigo todo!
scores=[]
while True:
    score=input("Students score: ")
    #asks for an input
    if score in ("","q","quit","e","end","exit"):
        #if the input was any of these strings, stop asking for input.
        break
    elif score.isdigit():
        #if the input was a number, add it to the list.
        scores.append(int(score))
    else:
        #the user typed in nonsense, probably a typo, ask them to try again
        print("invalid score, please try again or press enter to end list")
#you now have an array scores to process as you see fit.
n = len(scores)

soma = 0
media = 0

for num in scores[0:n]:
    soma = soma + num

media = soma / n

print(media)
