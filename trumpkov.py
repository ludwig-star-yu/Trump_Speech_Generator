import numpy as np
inputs=""

for i in range(1,20):

    isTrumpSpeech=False
    with open('./trump_speech/trump'+str(i)+'.txt','r',encoding='UTF-8') as f:

        for line in f.readlines():
            if isTrumpSpeech:
                inputs+=line.replace('\n','')
                isTrumpSpeech=False
            elif line.startswith("Donald Trump:") \
                    or line.startswith("President Donald Trump:") \
                    or line.startswith("President Trump:")\
                    or line.startswith('President Donald J. Trump'):
                isTrumpSpeech = True;
                continue

words = inputs.split(" ")
while "" in words:
    words.remove("")
print("words:",words[:10])
#print(words)

model ={}
for i in range(0,len(words)-2):
    state1 = words[i]
    state2= words[i+1]
    state3= words[i+2]
    
    if (state1,state2) not in model.keys():
        model[(state1,state2)]=[]
    model[(state1,state2)].append(state3)

states = list(model.keys())[np.random.randint(len(model.keys()))]
#output=model[states][0]
output=""
for i in range(50):
    #print('states:',states)
    if states not in model.keys():
        break
    sam_list = model[states];
    #print(sam_list)
    s1 = np.random.choice(a=sam_list,size=1)[0]
    output += " " + s1
    states = (list(states)[1],s1)

print('keys count:',len(model.keys()))
print(list(model.keys())[1])
print('__________________________output________________________')
print(output)