import math
import collections as coll
import operator
import re
from nltk import PorterStemmer
import side_functions as sf


def square_rooted(x):
	return round(math.sqrt(sum([a*a for a in x])),3)

one_f=[]
two_f=[]
ind_doc=[]

f_here = "./title_ids.txt"
N = sf.get_len(f_here)

stop_words = sf.get_stopWords('../stoplist.txt')
s = open('./sec/secindex.txt')
red=s.readlines()

for line in red:
	line=line.split('|')
	one_f.append(line[0])
	two_f.append(line[2][:-1])
	ind_doc.append(line[1])

indtwo_len=len(one_f)


while(1):
	top=10
	try:
		ps = PorterStemmer()
		input_t=raw_input()
		line=input_t.split()
		rank={}
		final=[]
		map_dis=[]
		flag = "a"

		for j in range(len(line)):
			temp=[]
			if(len(line[j])>1 and line[j][1]==':'):
				temp.append(line[j][0])
				temp.append(line[j][2:])
				flag = line[j][0]
			else:
				temp.append(flag)
				temp.append(line[j])
			map_dis.append(temp)
		# print "what1"1"
		#print map_dis
		for j in range(len(map_dis)):
			map_dis[j][1]=ps.stem(map_dis[j][1]).lower()
		# print "bet"1"
		for j in range(len(map_dis)):
			try:
				stop_words[map_dis[j][1]]
			except:
				final.append(map_dis[j])
		# print "bet"2"
		map_dis=final
		#print map_dis
		qlist=[]
		# print "what1"2"
		for i in map_dis:
			qlist.append(i[1])
		counts = coll.Counter(qlist)
		#print counts
		max_freq=counts[list(counts)[0]]
		final_result={}
		query_vector=[]
		for j in range(len(map_dis)):
			data=sf.get_string(map_dis[j][1], indtwo_len, one_f, two_f, ind_doc)
			lists=data.split('|')
			temp=sf.score(lists, len(lists), N, map_dis[j][0])
			term_inv=temp['inv']
			query_vector.append((counts[map_dis[j][1]]/max_freq)*(term_inv))
			ver = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
			ver_k = coll.OrderedDict(ver)
			final_result[map_dis[j][1]]=ver_k
		list_o_keys=[]
		for term in final_result:
			count=0
			for j in final_result[term]:
				if j != 'inv':
					count+=1
					list_o_keys.append(j.lstrip())

					if count>=10:
						break
		list_o_keys=list(set(list_o_keys))
		#print list_o_keys
		doc_vecs={}
		for doc in list_o_keys:
			dummy=[]
			for i in final_result:
				if doc in final_result[i]:
					dummy.append(final_result[i][doc])
				else:
					dummy.append(0)
			doc_vecs[doc]=dummy
		final_dic = sf.find_cos(query_vector, doc_vecs)
		sort_l = sorted(final_dic.items(), key=operator.itemgetter(1), reverse=True)
		answer=coll.OrderedDict(sort_l)

		for i in answer:
			h=open("./title_ids.txt",'r')
			l=h.readlines()
			for j in l:
				line=j.split(' ')
			#	print line
				if line[len(line)-1][:-1]==i:
					print j[:-1]
					break
	except Exception as e:
		print "Error in dealing with the query. Error: " + str(e)
