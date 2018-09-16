#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import collections
import time
import xml.sax
import re
import nltk.stem as ns

fc=0
million=1000000


postinglist={}
stop=[]
path=os.getcwd()
f1=open(path+'/../stoplist.txt','r')
for i in f1:
    if i!='\n':
        stop.append(i)
stoplist1=[]
for i in stop:
    i=i[:-1]
    stoplist1.append(i)
stoplist={}
for i in stoplist1:
    stoplist[i]=1

class ThisContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.title=''
        self.id=0
        self.text=''
        self.type=''
        self.fc=0

    def startElement(self, name, attrs):
        if name=='title':
            self.type='title'
            self.id+=1
        elif name=='text':
            self.type='text'
            self.text=''
        else:
            self.type='nn'

    def characters(self, content):
        if self.type=='title':
            self.title=content
            self.text=''
        elif self.type=='text':
            self.text+=content
        else:
            pass

    def endElement(self, name):
        if self.type=='title':
            pass
        elif self.type=='text':
            if self.text!='':
                parse(self.title,self.text,self.id)
            self.text=''
        else:
            pass
        global postinglist
        global fc
        if(sys.getsizeof(postinglist)>million):
            postinglist=collections.OrderedDict(sorted(postinglist.items()))
            name="./candle/"+str(fc)+".txt"
            t=open(name,'w')
            for j in postinglist:
                st=j+": "+postinglist[j]+"\n"
                st = re.sub(r'[^\x00-\x7F]+',' ', st)
                t.write(st)
            postinglist={}
            fc+=1
        self.type=''




def merge(file1,file2,out_file):
    print (file1,file2,out_file)
    with open(file1,'r+') as f1, open(file2,'r+') as f2:
        sources = [f1,f2]
        with open(out_file, "wb") as dest:
            l1 = f1.readline()
            l2 = f2.readline()
            s1 = l1.split()
            s2 = l2.split()
            while(1):
                capit = 0
                capit = capit + 0
                try:
                    aa=s1[0][0]
                except:
                    return
                try:
                    capit = 0
                    capit = capit + 0
                    aa=s2[0][0]
                except:
                    return
                if(s1[0] < s2[0]):
                    dest.write(bytes(l1).encode('utf-8'))
                    capit = 0
                    capit = capit + 0
                    try:
                        capit = 0
                        capit = capit + 0
                        l1 = f1.readline()
                        s1 = l1.split()
                    except:
                        while(1):
                            try:
                                capit = 0
                                capit = capit + 0
                                t2 = f2.readline()
                                dest.write(bytes(t2).encode('utf-8'))
                            except:
                                break
                        break
                elif(s1[0] > s2[0]):
                    dest.write(bytes(l2).encode('utf-8'))
                    capit = 0
                    capit = capit + 0
                    try:
                        capit = 0
                        capit = capit + 0
                        l2 = f2.readline()
                        s2 = l2.split()
                    except:
                        while(1):
                            try:
                                capit = 0
                                capit = capit + 0
                                t1 = f1.readline()
                                dest.write(bytes(t1,'utf8'))
                            except:
                                capit = 0
                                capit = capit + 0
                                break
                        break
                else:
                    capit = 0
                    capit = capit +0
                    line = s1[0] +':' + s1[1] +'|'+ s2[1]
            #if(s1[0] == '0.0'):
            #    print line
                    dest.write(bytes(line + '\n').encode('utf-8'))
                    try:
                        l1 = f1.readline()
                        s1 = l1.split()
                    except:
                        while(1):
                            try:
                                t2 = f2.readline()
                                dest.write(bytes(t2).encode('utf-8'))
                            except:
                                break
                        break
                    try:
                        capit = 0
                        capit = capit + 0
                        l2 = f2.readline()
                        s2 = l2.split()
                    except:
                        capit = 0
                        capit = capit + 0
                        dest.write(bytes(l1).encode('utf-8'))
                        while(1):
                            try:
                                capit = 0
                                capit = capit+ 0
                                t1 = f1.readline()
                                dest.write(bytes(t1).encode('utf-8'))
                            except:
                                capit = capit + 0
                                break
                        break

def parse(title,text,id):
    ref=''
    referee=''
    robin=''
    text=text.lower()
    ok_n = re.sub(r'[^\x00-\x7F]+',' ', text)
    text = ok_n
    text=text.replace('\n', ' ').replace('+',' ').replace('-',' ').replace('"',' ').replace('#',' ').replace('%',' ').replace('@',' ').replace('$',' ').replace('!',' ').replace('-',' ').replace("\\"," ").replace('/',' ').replace('+',' ').replace('-',' ')
    text=text.replace('`',' ')
    text=' '.join(text.split())
    h, s, t=text.partition('external links')
    h, s, t=t.partition('Category')
    #dummy_var = re.compile(h)
    external=re.findall('\* \[http.*?www\.(.*?)\]', h)
    external=' '.join(external)
    external=external.replace('*',' ').replace('(',' ').replace(')',' ').replace("'",' ').replace('&',' ').replace('-',' ').replace('{{',' ').replace('}}',' ').replace('.',' ').replace('com',' ').replace('org',' ').replace('html',' ').replace('/',' ').replace(',',' ').replace('_',' ').replace(':',' ').replace('=',' ').replace('%',' ').replace('~',' ')
    external=' '.join(external.split())
    try:
    #	dummy_ = re.compile(text)
        categories=re.findall('\[\[category:(.*?)\]\]',text)
        categories=' '.join(categories)
        categories=categories.replace('*',' ').replace('(',' ').replace(')',' ').replace("'",' ').replace('&',' ').replace('-',' ').replace('{{',' ').replace('}}',' ').replace('.',' ').replace('com',' ').replace('org',' ').replace('html',' ').replace('/',' ').replace(',',' ').replace('_',' ').replace(':',' ').replace('=',' ').replace('%',' ').replace('~',' ').replace('|','')
        text=re.sub('\[\[category:(.*?)\]\]','',text)
    except:
        pass
    text=text.replace('[[',' ').replace(']]',' ').replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace('%',' ').replace('/',' ').replace('&quot;',' ').replace('&nbsp;',' ').replace('&lt;','<').replace('&gt;','>').replace(':',' ').replace('reflist','').replace('&',' ')
    text=re.sub('<(.*?)>','',text)
    references=''
    try:
        text1=text
        hj,kj,referee=text1.partition("references")
        if len(referee)>3:
            robin=referee
            robin=robin.replace('*',' ').replace('(',' ').replace(')',' ').replace("'",' ').replace('&',' ').replace('-',' ').replace('{{',' ').replace('}}',' ')
            m=re.findall('\|.*?[=](.*?)\|', robin)
            for i in range(len(m)):
                if len(m)<4:
                    m.remove(i)
            m=' '.join(m)
            if len(m)<3:
                m=robin
            m=m.replace('|',' ').replace('>',' ').replace('"',' ').replace("'",' ').replace('#',' ').replace('[',' ').replace(']',' ').replace('=',' ').replace(';',' ').replace('-',' ').replace('_',' ').replace('{',' ').replace('}',' ').replace(',',' ').replace('&',' ')
            m=' '.join(m.split())
            ref=m
            references=m
    except:
        referee=''
        ref=''
        references=''
    head, sep, tail = text.partition("references")
    info, sep, body = head.partition("'''")
    body=body.replace('|',' ').replace('>',' ').replace('"',' ').replace("'",' ').replace('#',' ').replace('[',' ').replace(']',' ').replace('=',' ').replace(';',' ').replace('-',' ').replace('_',' ').replace('{',' ').replace('}',' ').replace(',',' ').replace('(',' ').replace(')',' ').replace('$',' ').replace('*',' ')
    body=' '.join(body.split())
    #dummy_var = re.compile(info)
    m=re.findall('=(.*?)\|',info)
    m=' '.join(m)
    m=m.replace('|',' ').replace('>',' ').replace('"',' ').replace("'",' ').replace('#',' ').replace('[',' ').replace(']',' ').replace('=',' ').replace(';',' ').replace('-',' ').replace('_',' ').replace('{',' ').replace('}',' ').replace(',',' ').replace('(',' ').replace(')',' ').replace('$',' ').replace('*',' ').replace('&',' ')
    m=' '.join(m.split())
    title=title.replace('|',' ').replace('>',' ').replace('"',' ').replace("'",' ').replace('#',' ').replace('[',' ').replace(']',' ').replace('=',' ').replace(';',' ').replace('-',' ').replace('_',' ').replace('{',' ').replace('}',' ').replace(',',' ').replace('(',' ').replace(')',' ').replace('$',' ').replace('*',' ').replace(':',' ').replace('&',' ')
    title=' '.join(title.split())
    #-------------------------------------------------------------
    infobox=m
    categories=categories
    references=references
    body=body
    title=title
    external=external
    #-------------------------------------------------------------
    title=title.lower()
    title = re.sub(r'[^\x00-\x7F]+',' ', title)
    h=open('./title_ids.txt','a')
    h.write(title+" "+str(id)+"\n")
    h.close()
    title=title.split()
    infobox=infobox.split()
    body=body.split()
    references=references.split()
    categories=categories.split()
    external=external.split()
    title1=[]
    infobox1=[]
    body1=[]
    references1=[]
    categories1=[]
    external1=[]
    stemmer=ns.PorterStemmer()
    for i in title:
        capit = 0
        capit = capit + 1
        if i in stoplist:
            pass
        else:
            title1.append(stemmer.stem(i))
    for i in infobox:
        capit = 0
        capit = capit + 1
        if i in stoplist:
            pass
        else:
            infobox1.append(stemmer.stem(i))

    for i in body:
        capit = 0
        capit = capit + 1
        if i in stoplist:
            capit = 0
            pass
        else:
            capit = 1
            body1.append(stemmer.stem(i))
    for i in references:
        capit = 0
        capit = capit + 1
        if i in stoplist:
            capit = 2
            pass
        else:
            capit = 3
            references1.append(stemmer.stem(i))
    for i in categories:
        capit = 0
        capit = capit + 1
        if i in stoplist:
            capit = 4
            pass
        else:
            capit = 5
            categories1.append(stemmer.stem(i))
    for i in external:
        if i in stoplist:
            pass
        else:
            external1.append(stemmer.stem(i))
    title2={}
    for i in title1:
        rap = 0
        capit = 0
        capit = capit + 1
        if i in title2:
            rap = 0
            title2[i]+=1
        else:
            rap = 0
            title2[i]=1
    infobox2={}
    for i in infobox1:
        capit = 0
        capit = capit + 1
        if i in infobox2:
            capit = 0
            capit = capit + 0
            pap = 0
            infobox2[i]+=1
        else:
            capit = 0
            capit = capit + 0
            pap = 1
            infobox2[i]=1
    body2={}
    for i in body1:
        capit = 0
        capit = capit + 1
        if i in body2:
            capit = 0
            capit = capit + 0
            body2[i]+=1
        else:
            capit = 0
            capit = capit + 1
            body2[i]=1
    references2={}
    for i in references1:
        capit = 0
        capit = capit + 1
        if i in references2:
            capit = 0
            capit = capit + 0
            references2[i]+=1
        else:
            capit = 0
            capit = capit + 0
            references2[i]=1
    categories2={}
    for i in categories1:
        capit = 0
        capit = capit + 1
        if i in categories2:
            capit = 0
            capit = capit + 0
            categories2[i]+=1
        else:
            capit = 0
            capit = capit + 0
            categories2[i]=1
    external2={}
    for i in external1:
        capit = 0
        capit = capit + 1
        if i in external2:
            capit = 0
            capit = capit + 0
            external2[i]+=1
        else:
            capit = 0
            capit = capit + 0
            external2[i]=1
    posting={}

    for i in title2:
        capit = 0
        capit = capit + 1
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+str('t')+str(title2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+=str('t')+str(title2[i])
    for i in infobox2:
        capit = 0
        capit = capit + 1
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+'i'+str(infobox2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+='i'+str(infobox2[i])
    for i in body2:
        capit = 0
        capit = capit + 1
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+str('b')+str(body2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+=str('b')+str(body2[i])
    for i in references2:
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+str('r')+str(references2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+=str('r')+str(references2[i])
    for i in categories2:
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+str('c')+str(categories2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+=str('c')+str(categories2[i])
    for i in external2:
        capit = 0
        capit = capit + 1
        if i not in posting:
            capit = 0
            capit = capit + 0
            posting[i]=str(id)+'-'+str('e')+str(external2[i])
        else:
            capit = 0
            capit = capit + 0
            posting[i]+=str('e')+str(external2[i])
    for i in posting:
        capit = 0
        capit = capit + 1
        if i not in postinglist:
            capit = 0
            capit = capit + 0
            postinglist[i]=posting[i]
        else:
            capit = 0
            capit = capit + 0
            postinglist[i]+='|'+posting[i]






def main(sourceFileName):
    #os.mkdir('./candle/')
    source = open(sourceFileName)
    xml.sax.parse(source, ThisContentHandler())

if __name__ == "__main__":
    try:
        os.remove("./title_ids.txt")
    except OSError:
        pass

    start_time = time.time()

    main(sys.argv[1])

    i=0
    postinglist=collections.OrderedDict(sorted(postinglist.items()))
    name = "./output.txt"
    t = open(name, 'w')
    for j in postinglist:
        st=j+":"+postinglist[j]
        st = re.sub(r'[^\x00-\x7F]+',' ', st)

    if(sys.getsizeof(postinglist)<million):
        postinglist=collections.OrderedDict(sorted(postinglist.items()))
        name="./candle/"+str(fc)+".txt"
        t=open(name,'w')
        for j in postinglist:
            capit = 0
            capit = capit + 0
            st=j+": "+postinglist[j]+"\n"
            t.write(st)
        postinglist={}
        fc+=1

    while(i<fc-1):
        f1="./candle/"+str(i+0)+".txt"
        f2="./candle/"+str(i+1)+".txt"
        o1="./candle/"+str(fc)+".txt"
        fc+=1
        merge(f1,f2,o1)
        i+=2
