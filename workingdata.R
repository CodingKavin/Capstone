setwd("C:/Users/kavin/OneDrive")

rawdata2014 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2014_report_english.csv", header = TRUE)
rawdata2015 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2015_report_english.csv", header = TRUE)
rawdata2016 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2016_report_english.csv", header = TRUE)
rawdata2017 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2017_energy_consumption.csv", header = TRUE)
rawdata2018 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2018_final_data_set.csv", header = TRUE)
rawdata2019 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2019_final_data_set.csv", header = TRUE)

install.packages("dplyr")
library("dplyr")

length(unique(rawdata2014$Operation))

datadf <- data.frame(unique(rawdata2014$Operation))

colSums(rawdata2014 != 0)

colnames(datadf) <- c("Operation")

namelist <- c("Sector", "City", "GHG.Emissions.KG.2014", "Energy.Intensity.GJ_m2.2014", "GHG.Emissions.KG.2015", "Energy.Intensity.GJ_m2.2015", "GHG.Emissions.KG.2016", "Energy.Intensity.GJ_m2.2016", "GHG.Emissions.KG.2017", "Energy.Intensity.GJ_m2.2017", "GHG.Emissions.KG.2018", "Energy.Intensity.GJ_m2.2018", "GHG.Emissions.KG.2019", "Energy.Intensity.GJ_m2.2019")

for (i in namelist){
  datadf[,i] <- NA
}

for (i in 1:nrow(datadf)){
  for (j in 1:nrow(rawdata2014)){
    if (datadf$Operation[i] == rawdata2014$operation[j]){
      datadf$City[i] <- rawdata2014$City[j]
      datadf$Sector[i] <- rawdata2014$Sector[j]
      datadf$GHG.Emissions.KG.2014[i] <- rawdata2014$GHG.Emissions.KG[j]
      datadf$Energy.Intensity.GJ_m2.2014[i] <- rawdata2014$Energy.Intensity.GJ_m2[j]
    }
  }
}
