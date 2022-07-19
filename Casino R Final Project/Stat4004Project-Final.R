#Stats 4004 - Jessie Grable & Marhawe Asmerom
#1 - made roulette function that follows martingale betting system 
roulette = function()
{
  winnings = c()   #intitalize variables
  betsize = 1
  current_winnings = 0
  number_of_bets = 0
  amount_of_bets = 1
  pocketmoney = 100 
  while (current_winnings < 10 & betsize <= 100 + current_winnings) {   # if lost is less than 10 or winnings more than 110 
    red = rbinom(1,1,18/37)
    number_of_bets = number_of_bets + 1 
    if(red == 1)   #red roulette
    {
      winnings = c(winnings,1)
      current_winnings = current_winnings + betsize
      betsize = 1
      pocketmoney = c(pocketmoney,100 + current_winnings)
    }else{
      winnings = c(winnings,0)
      current_winnings = current_winnings - betsize
      betsize = 2 * betsize
      pocketmoney = c(pocketmoney,100 + current_winnings)
    }
    amount_of_bets = c(amount_of_bets,betsize)
  }
    if(current_winnings >= 10 ) { #determine win-lose record 
      final_output = 1
      final_balance = 100 + current_winnings
    }else{
      final_output = 0 
      final_balance = 100 + current_winnings
    }
  return(list(number_of_bets = number_of_bets,   #returns outputs 
              amount_of_bets = amount_of_bets,
              winloserecord = winnings , 
              pocketmoney = pocketmoney,
              finalwinnings = final_output,
              finalbalance = final_balance))


  
}




#2
  number_of_rep = 100000
  s1 = "The confidence interval is" 
  s3 = "to"
  s2 = "Maximum amount lost is"
  
  
  nbets_won = rep(NA ,number_of_rep)   #create variables 
  final = rep(NA,number_of_rep)
  playtime = rep(NA,number_of_rep)
  balance = rep(NA,number_of_rep)
  
  for(i in 1:number_of_rep) {   #runs 100000 simulations of the roulette games 
    gamei = roulette()
      nbets_won[i] = sum(gamei$winloserecord)
      final[i] = gamei$finalwinnings
      playtime[i]=gamei$number_of_bets
      balance[i]=gamei$finalbalance
  }

#a - find the average amount of games won
mu1 = mean(nbets_won) 
var1 = var(nbets_won)
CI1 = c(mu1 - 1.96*sqrt(var1/number_of_rep) , mu1 + 1.96*sqrt(var1/number_of_rep)) 
print(paste(s1,CI1,s3))
#b - find the average proportion of games won 
phat = mean(final)
var2 = phat * (1 - phat) 
CI2 = c(phat - 1.96*sqrt(var2/number_of_rep) , phat + 1.96*sqrt(var2/number_of_rep)) 
print(paste(s1,CI2,s3))
#c -  expected playtime 
mu2 = mean(playtime)
var3 = var(playtime) 
CI3 = c(mu2 - 1.96*sqrt(var3/number_of_rep) , mu2 + 1.96*sqrt(var3/number_of_rep)) 
print(paste(s1,CI3,s3))
#d most money you can lose
maximumlose = min(balance - 100)
print(paste(s2,maximumlose))



#3 - plot the first 1,000 projections for bet index 
simulations = 1000
numberbets = rep(NA,simulations)
pmoney = vector('list',simulations)
finaloutput = rep(NA,simulations)

for(r in 1:simulations) {
  gamet = roulette()
  numberbets[r]=gamet$number_of_bets
  pmoney[[r]]=gamet$pocketmoney
  finaloutput[r]=gamet$winloserecord
}

plot(1:numberbets[1], pmoney[[1]], color=ifelse(finaloutput[1]==1, 'blue', 'red'))   #plot the number of bets compared to pocket money


for (i in 2: simulations){
  lines(1:numberbets[i], pmoney[[i]], color=ifelse(finaloutput[i]==1, 'blue', 'red'))
}




