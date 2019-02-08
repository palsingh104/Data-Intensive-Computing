random <- read.csv("Combineddata.csv")
st<-as.data.frame(random$place_full_name)
new1 <- as.character(random$place_full_name)
#Choping State Abs
new<-sapply(strsplit(new1,", "),"[",2)
new2<-as.data.frame(new)
one <-as.data.frame(summary(new2,55,split(TRUE)))


two<-as.character(one$Freq)
new6<-sapply(strsplit(two,": "),"[",2)
new6
new8<-sapply(strsplit(two,": "),"]",1)
new8
write.csv(two,"format.csv")
