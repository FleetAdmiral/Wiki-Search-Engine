import math
import re
def get_len(file):
    curr = open("./title_ids.txt")
    temp = curr.readlines()
    leng = len(temp)
    curr.close()
    return leng

def get_stopWords(file):
    fi=open(file)
    stop_words={}
    for all in fi:
    	if all!='\n':
            all=all[:-1]
            stop_words[all]=1
    fi.close()
    return stop_words

def get_string(word, indtwo_len, one_f, two_f, ind_doc):
	for i in range(indtwo_len):
		if one_f[i]<=word and two_f[i]>=word:
		#	print 'hey'
			f=open("./sec/"+str(int(ind_doc[i])-1)+".txt")
			r=f.readlines()
			for j in r:
				j=j.split(":")
				if j[0] == word:
					return j[1].lstrip()
					break
def find_cos(q_v, d_v):
    final_dic={}
    y=q_v
    for i in d_v:
    	x=d_v[i]
    	final_dic[i]=cosine_similarity(x,y)
    return final_dic

def cosine_similarity(v1,v2):
	#print x,y

    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
	denom = math.sqrt(sumxx*sumyy)

	if denom!=0:
		return sumxy/denom

	else:
		return 1

def score(postinglist, n, N, flag):
	result={}
	inv = N/n
	result['inv']=math.log(N/n)
	for i in postinglist:
		#y=i.split('-')
		y_id=i.split('-')[0]
		re_fam = re.findall(r"([a-z])([0-9]+)", i.split('-')[1] , re.I)
		if flag=='a':
			count=0
			for j in re_fam:
				if j[0] == 't':
					count+= int(j[1])*20

				elif j[0] == 'b':
					count+= int(j[1])*4
				elif j[0] == 'r':
					count+= int(j[1])*10
				elif j[0] == 'e':
					count+= int(j[1])*10
				elif j[0] == 'c':
					count+= int(j[1])*10
                elif j[0] == 'i':
					count+= int(j[1])*7
		else:
			count=0
			#print re_fam, y_id
			for j in re_fam:
				if j[0] == flag:
					count+=int(j[1])
					break
		if count !=0:
			result[y_id]=(math.log(inv))+(math.log(count))
	return result

def get_path():
    return 'index.txt'
