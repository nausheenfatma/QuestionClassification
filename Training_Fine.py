#readfile is the Loctraining.txt from which indices has to be fetched
#readline1 is the fullfeature
#readfile2 is the fullfeaturefile from which data has to be copied
#writefile is the file in which extracted dat has to be saved	
from readproperties import read_property

def extract(readline,readfile1,writefile1):
	fineindexedfile=open(readline,"r")
        fullfeaturefile=open(readfile1,"r")
        write_file=open(writefile1,"w")
        linesfromfeaturefile=fullfeaturefile.readlines()
        for line in fineindexedfile:
		print line
		indexno=line.split()[0]
		print indexno
                #  linesfrom=fullfeaturefie.readlines()
                lineread=linesfromfeaturefile[int(indexno)-1]
		print lineread
                write_file.write(lineread)
        fineindexedfile.close()
        fullfeaturefile.close()
        write_file.close()
        #write_ner_file.close()

#################LOC class################
#f1="LOC_training.txt"
Full_train_features_POS_file=read_property('POS_features_train_coarse_path')
#Fine_write_file="LOC_training_POS.txt"
#extract(f1,Full_train_features_file,Fine_write_file)

Full_train_features_NER_file=read_property('NER_features_train_coarse_path')
#Fine_write_file="LOC_training_NER.txt"
#extract(f1,Full_train_features_file,Fine_write_file)

Full_train_features_WORD_file=read_property('word_features_train_coarse_path')
#Fine_write_file="LOC_training_word.txt"
#extract(f1,Full_train_features_file,Fine_write_file)

Full_train_features_CHUNK_file=read_property('Chunk_features_train_path')
#Fine_write_file="LOC_training_Chunk.txt"
#extract(f1,Full_train_features_file,Fine_write_file)


classes=['LOC','ENTY','ABBR','DESC','HUM','NUM']

for classlabel in classes:
    print classlabel
    f1=read_property('FineInputFiles')+classlabel+"_training.txt"
    Fine_write_file=read_property('FineOutputfilesPath')+classlabel+'_training_POS.txt'
    extract(f1,Full_train_features_POS_file,Fine_write_file)
    Fine_write_file=read_property('FineOutputfilesPath')+classlabel+'_training_NER.txt' 
    extract(f1,Full_train_features_NER_file,Fine_write_file)   
    Fine_write_file=read_property('FineOutputfilesPath')+classlabel+'_training_word.txt'  
    extract(f1,Full_train_features_WORD_file,Fine_write_file)  
    Fine_write_file=read_property('FineOutputfilesPath')+classlabel+'_training_Chunk.txt'
    extract(f1,Full_train_features_CHUNK_file,Fine_write_file)





	
