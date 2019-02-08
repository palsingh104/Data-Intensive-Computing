# Student Name: Palwinder Singh 
# Partner Name:  Gursimrat Singh
# Course: CSE 5/487
# Instructor: Bina Ramamurthy
# Lab1 Part1

#Problem 1
sales1<-c(12,14,16,29,30,45,19,20,16, 19, 34, 20)
sales2<-rpois(12,34)  # random numbers, Poisson distribution, mean at 34, 12 numbers
par(bg="cornsilk")   # par() and layout() for combining 

plot(sales1, col="blue", type="o", ylim=c(0,100), xlab="Month", ylab="Sales" ) #plot to make a graph
title(main="Sales by Month") #title

lines(sales2, type="o", pch=22, lty=2, col="red")#lines to make line on existing graph pch=22 and lty = 2 to make line dotted
grid(nx=NA, ny=NULL)  #grid 
legend("topright", inset=.05, c("Sales1","Sales2"), fill=c("blue","red"), horiz=TRUE) #to making box for each elements



#Problem 2
sales<-read.table(file = file.choose(), header=T)
sales # to verify that data has been read
barplot(as.matrix(sales), main="Sales Data", ylab= "Total",beside=T, col=rainbow(5))


#Problem 3
fn<-boxplot(sales,col=c("orange","green"))$stats

text(1.45, fn[3,2], paste("Median =", fn[3,2]), adj=0, cex=.7)
text(0.45, fn[3,1],paste("Median =", fn[3,1]), adj=0, cex=.7)
grid(nx=NA, ny=NULL)


#Problem 4
fb1<-read.csv(file.choose())
aapl1<-read.csv(file.choose())
par(bg="cornsilk")
plot(aapl1$Adj.Close, col="blue", type="o", ylim=c(140,200), xlab="Days", ylab="Price" )
lines(fb1$Adj.Close, type="o", pch=22, lty=2, col="red")
legend("topright", inset=.05, c("Apple","Facebook"), fill=c("blue","red"), horiz=TRUE)
hist(aapl1$Adj.Close, col=rainbow(8))




#Problem 5
library (help=datasets)
library(datasets)
data()
attach(mpg)
head(mpg)
summary(mpg)
#after analysis remove the data from the memory
detach(mpg)
head(uspop)
plot(uspop)



#Problem 6
library(ggmap)
library(maptools)
library(maps)
visited <- c("San Francisco","Chennai","London", "Melbourne", "Johannesburg, SA")
ll.visited <- geocode(visited)
visit.x <- ll.visited$lon
visit.y <- ll.visited$lat
map("world", fill=TRUE, col="white", bg="lightblue", ylim=c(-60, 90), mar=c(0,0,0,0))
points(visit.x,visit.y, col="red", pch=36)

#USA map
library("ggmap")
library("maptools")
library(maps)
visited <- c("San Francisco", "New York", "Buffalo", "Dallas, TX")
ll.visited <- geocode(visited)
visit.x <- ll.visited$lon
visit.y <- ll.visited$lat
map("state", fill=TRUE, col=rainbow(50), bg="lightblue", mar=c(0,0,0,0))
points(visit.x,visit.y, col="yellow", pch=36)


#Problem 7
library(lattice)
splom(mtcars[c(1,3,4,5,6)], main="MTCARS Data")
splom(mtcars[c(1,3,4,6)], main="MTCARS Data")
splom(mtcars[c(1,3,4,6)], col=rainbow(8),main="MTCARS Data")
splom(rock[c(1,2,3,4)], main="ROCK Data")



#Problem 8
ignette("grid")# launches long form documentation about the function (opens up in pdf format)
library(ggplot2)

g <- ggplot(midwest, aes(x=area, y=poptotal)) + geom_point() + geom_smooth(method="lm")  # set se=FALSE to turnoff confidence bands

# Zoom in without deleting the points outside the limits.
# As a result, the line of best fit is the same as the original plot.
g1 <- g + coord_cartesian(xlim=c(0,0.1), ylim=c(0, 1000000))  # zooms in
plot(g1)

#example ref:http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html

