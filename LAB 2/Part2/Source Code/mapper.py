

from mrjob.job import MRJob
import re
REword=re.compile(r"[\w]+")
x=["is","are","was","a","your","sex","href","https","text","data","class","had","dateline","feedback","author","said","dateline","articlebody","error","has","page","advertisement","_blank","html","byline","para","count","has","about","body","nytimes","www","com","were","story","span","itemprop","content","body","all","also","and","as","at","be","because","but","by","can","come","could","day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how","I","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this","those","time","to","two","up","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","you","http","/","ucode","_","-","!",".",",","\"","?","when","then","do","did","will","0","1","3","4","5","6","7","8","9"]
class MRfreqwithRE(MRJob):
     
    def mapper(self,_,line):
        words = REword.findall(line)
        for word in words:
            word=word.lower()
            if word in x:
		pass
            elif(len(word)<3):
		pass
	    else:
                yield word,1


if __name__ == '__main__':
    MRfreqwithRE.run()