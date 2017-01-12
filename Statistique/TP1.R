install.packages("rmarkdown")
data("iris")
kt = runif(100, min = 0 , max = 100)
Y = cumsum(kt)
moy = Y /(1:100) 
plot(moy,type="l",xlab="k",ylab="Moyenne empirique",ylim=c(0,100))
abline(50,0, col="red") # 50 correspond à la valeur limite predite par la loi des grands nombres (0 +100)/2
kt = runif(100, min = 0 , max = 100)
Y = cumsum(kt)
moy = Y /(1:100)
lines(moy,type="l",col="blue")

