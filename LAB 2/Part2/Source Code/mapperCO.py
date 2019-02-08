import csv
from mrjob.job import MRJob
#from mrjob.step import MRStep

import re
REword=re.compile(r"(\w+)")


class MRfreqwithRE(MRJob):
    def mapper(self,_,line):
        words = REword.findall(line)
        list=["a","about","all","also","and","as","at","be","because","but","by","can","come","could","day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how","I","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this","those","time","to","two","up","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","you","http","/","ucode","_","-","!",".",",","\"","?","when","then","do","did","will","0","1","3","4","5","6","7","8","9"]
        for word in words:
            if(word[0].isdigit()):
                pass
            elif(word in list):
                pass
	    elif (len(word)<3):
		pass
            else:       
                for x in words:
                    if (x == word.lower()):
                        pass
                    elif(x in list):
                        pass
		    elif(len(word)<3):
			pass    
                    else:
                        k = word.lower()+"$"+x.lower()
                        yield k,1
        
        
if __name__ == '__main__':
    MRfreqwithRE.run()
   