#Merging two files (reviews and listings)

reviews=read.csv("reviews_new.csv")
listings=read.csv("listings_new.csv")
x=merge(reviews,listings,by.x=c("id"),by.y=c("id"))
write.csv(x, file = "MyData.csv", row.names=FALSE)