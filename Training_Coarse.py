import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tag.stanford import NERTagger
from scipy.sparse import hstack
from sklearn.svm import LinearSVC
from practnlptools.tools import Annotator
from readproperties import read_property

##removing special characters from sentence##
def preprocess(raw_sentence):
    sentence= re.sub(r'[$|.|!|"|(|)|,|;|`|\']',r'',raw_sentence)
    return sentence

##making the file format ready to use##
def file_preprocess(filename):
	corpus=[]
	classes=[]
	f=open(filename,'r')
	fi=open(read_property('word_features_train_coarse_path'),"w")
	lines=f.readlines()
	for line in lines:
		line=line.rstrip('\n')
		line=preprocess(line)
		#print "The line is  ",line
		sentence=""
		words=line.split()
		for i in range(0,len(words)):
			if not(i==0):
				sentence=sentence+(words[i])+" "
		fi.write(sentence+"\n")
		corpus.append(sentence)
	f.close()
	fi.close()
	return corpus,classes


##Compute POS##
def compute_POS_Tags(corpus):
      #POS=[]
      fi=open(read_property('POS_features_train_coarse_path'),"w")
      for sentence in corpus:
            text = nltk.word_tokenize(sentence)
            pos_seq=nltk.pos_tag(text)
            #print pos_seq
            pos_tags=""
            for pos in pos_seq:
                  pos_tags=pos_tags+pos[1]+" "
	    fi.write(pos_tags+"\n")
            #print pos_tags
            #POS.append(pos_tags)
      #print "The bag of words of POS is ",POS
      fi.close()
      #return POS
      
      
##Compute NER##     
def compute_NER(corpus):
      #NER=[]
      fi=open(read_property('NER_features_train_coarse_path'),"w")
      st = NERTagger(read_property('StanfordNerClassifier'),read_property('StanfordNerJarPath'))
      for sentence in corpus:
            ner=st.tag(sentence.split())
            #print ner
            #pos_seq=nltk.pos_tag(text)
            #print pos_seq
            ner_tag=""
            for n in ner:
                  #print n[1]
                  ner_tag=ner_tag+n[1]+" "
            #print pos_tags
	    fi.write(ner_tag+"\n")
            #NER.append(ner_tag)
      #print "The bag of words of NER is ",NER
      fi.close()
      #return NER



##Compute Chunks##     
def compute_Chunks(corpus):
      #Chunk_Tags=[]
      fi=open(read_property('Chunk_features_train_path'),"w")
      annotator=Annotator()
      for sentence in corpus:
	    chunks=annotator.getAnnotations(sentence)['chunk']
            chunk=""
            for elem in chunks:
                  chunk=chunk+elem[1]+" "
            #print chunk
	    fi.write(chunk+"\n")
            #Chunk_Tags.append(chunk)
      #print "The bag of words for Chunks is ",Chunk_Tags
      fi.close()
      #return Chunk_Tags


 
     


filename_train=read_property('trainingfilepath')
corpus,train_class=file_preprocess(filename_train)

compute_POS_Tags(corpus)
compute_NER(corpus)
compute_Chunks(corpus)

