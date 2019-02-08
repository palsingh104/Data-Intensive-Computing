library(maps)
library(ggplot2)
library(dplyr)
library("ggmap")
library("maptools")


us <- map_data("state")
flu=read.csv(file.choose())

gg <- ggplot()+ geom_map(data=us, map=us,aes(x=us$long, y=us$lat, map_id=region), color="#000000", size=0.05) + ggtitle("                  A Weekly Influenza Surveillance Report Prepared by the Influenza Division
Influenza-Like Illness (ILI) Activity Level Indicator Determined by Data Reported to ILINet(week 4)")
gg <- gg + geom_map(data=flu, map=us,
                    aes(fill=flu$ACTIVITY.LEVEL, map_id=statename),#lowercase to avoid vector error
                    color="#000000", size=0.15)

gg = gg + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank(), axis.title.x=element_blank(),
                axis.text.x=element_blank(),
                axis.ticks.x=element_blank(),axis.title.y=element_blank(),
                axis.text.y=element_blank(),
                axis.ticks.y=element_blank(),legend.position="bottom")

gg<-gg+scale_fill_manual(values = c("green3","yellow1","red3","chartreuse3","chartreuse2","chartreuse1","chartreuse","tan1","orangered1"))

gg+coord_map()
