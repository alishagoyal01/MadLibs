import random
#word1=input("Please enter a verb\n")
#word2=input("Please enter an animal name\n")

#print('A lion was once' +' '+word1+' ' +'in the jungle when a' + ' '+ word2+' ' + "started running up and down his body just for fun. This disturbed the lion’s sleep, and he woke up quite angry. He was about to eat the" +' '+word2 +' '+'when the mouse desperately requested the lion to set him free. \“I promise you, I will be of great help to you someday if you save me.” The lion laughed at the' +' '+word2+"'s"+" " +'confidence and let him go. \n "One day, a few hunters came into the forest and took the lion with them. They tied him up against a tree. The lion was struggling to get out and started to whimper. Soon, the mouse walked past and noticed the lion in trouble. Quickly, he ran and gnawed on the ropes to set the lion free. Both of them sped off into the jungle.')
f= open("madlibs.txt","r")
if f.mode=='r':
    f1=f.read()
    word1=(list(map(str,f1.split())))
    word2=(list(map(str,f1.split())))

    #print(random.choice(word1))
    #print(random.choice(word1))
    f.close()

story='A lion was once _____ in the jungle when a _____ started running up and down his body just for fun. This disturbed the lion’s sleep, and he woke up quite angry. He was about to eat the mouse when the _____ desperately requested the lion to set him free. “I promise you, I will be of great help to you someday if you save me.” The lion laughed at the _____’s confidence and let him go.\n One day, a few hunters came into the forest and took the lion with them. They tied him up against a tree. The lion was struggling to get out and started to whimper. Soon, the _____ walked past and noticed the lion in trouble. Quickly, he ran and gnawed on the ropes to set the lion free. Both of them sped off into the jungle.'

print(story.replace("_____",random.choice(word1)))