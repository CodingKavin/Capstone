rawdata2014 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2014_report_english.csv", header = TRUE)
rawdata2015 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2015_report_english.csv", header = TRUE)
rawdata2016 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/bps_2016_report_english.csv", header = TRUE)
rawdata2017 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2017_energy_consumption.csv", header = TRUE)
rawdata2018 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2018_final_data_set.csv", header = TRUE)
rawdata2019 <- read.csv("Desktop/Data Science Projects/Emissions Data Ontario/CSV/2019_final_data_set.csv", header = TRUE)



###2014

sum2014 <- as.data.frame(table(rawdata2014$Sector))

rawdata2014$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2014$Energy.Intensity.GJ_m2)
rawdata2014$GHG.Emissions.KG <- as.numeric(rawdata2014$GHG.Emissions.KG)

ECsumM2014 <- 0
ECsumPS2014 <- 0
ECsumPH2014 <- 0
ECsumSB2014 <- 0

GHGsumM2014 <- 0
GHGsumPS2014 <- 0
GHGsumPH2014 <- 0
GHGsumSB2014 <- 0

for (i in 1:nrow(rawdata2014)){
    if (rawdata2014$Sector[i] == 'Municipal'){
      ECsumM2014 <-  sum(c(ECsumM2014, rawdata2014$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
      GHGsumM2014 <-  sum(c(GHGsumM2014, rawdata2014$GHG.Emissions.KG[i]), na.rm = TRUE)}
    if (rawdata2014$Sector[i] == 'Post-Secondary Educational Institution'){
      ECsumPS2014 <-  sum(c(ECsumPS2014, rawdata2014$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
      GHGsumPS2014 <- sum(c(GHGsumPS2014, rawdata2014$GHG.Emissions.KG[i]), na.rm = TRUE)}
    if (rawdata2014$Sector[i] == 'Public Hospital'){
      ECsumPH2014 <- sum(c(ECsumPH2014, rawdata2014$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
      GHGsumPH2014 <- sum(c(GHGsumPH2014, rawdata2014$GHG.Emissions.KG[i]), na.rm = TRUE)}
    if (rawdata2014$Sector[i] == 'School Board'){
      ECsumSB2014 <- sum(c(ECsumSB2014, rawdata2014$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
      GHGsumSB2014 <- sum(c(GHGsumSB2014, rawdata2014$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2014) = c("Sector", "GHG Emissions")

sum2014$`GHG Emissions` <- c(GHGsumM2014, GHGsumPS2014, GHGsumPH2014, GHGsumSB2014)
sum2014$'Energy Intensity' <- c(ECsumM2014, ECsumPS2014, ECsumPH2014, ECsumSB2014)

pie(sum2014$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2014")
barplot(sum2014$`Energy Intensity`, main="Energy intensity by sector in 2014", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

### 2015

sum2015 <- as.data.frame(table(rawdata2015$Sector))

rawdata2015$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2015$Energy.Intensity.GJ_m2)
rawdata2015$GHG.Emissions.KG <- as.numeric(rawdata2015$GHG.Emissions.KG)

ECsumM2015 <- 0
ECsumPS2015 <- 0
ECsumPH2015 <- 0
ECsumSB2015 <- 0

GHGsumM2015 <- 0
GHGsumPS2015 <- 0
GHGsumPH2015 <- 0
GHGsumSB2015 <- 0

for (i in 1:nrow(rawdata2015)){
  if (rawdata2015$Sector[i] == 'Municipal'){
    ECsumM2015 <-  sum(c(ECsumM2015, rawdata2015$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumM2015 <-  sum(c(GHGsumM2015, rawdata2015$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2015$Sector[i] == 'Post-Secondary Educational Institution'){
    ECsumPS2015 <-  sum(c(ECsumPS2015, rawdata2015$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPS2015 <- sum(c(GHGsumPS2015, rawdata2015$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2015$Sector[i] == 'Public Hospital'){
    ECsumPH2015 <- sum(c(ECsumPH2015, rawdata2015$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPH2015 <- sum(c(GHGsumPH2015, rawdata2015$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2015$Sector[i] == 'School Board'){
    ECsumSB2015 <- sum(c(ECsumSB2015, rawdata2015$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumSB2015 <- sum(c(GHGsumSB2015, rawdata2015$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2015) = c("Sector", "GHG Emissions")

sum2015$`GHG Emissions` <- c(GHGsumM2015, GHGsumPS2015, GHGsumPH2015, GHGsumSB2015)
sum2015$'Energy Intensity' <- c(ECsumM2015, ECsumPS2015, ECsumPH2015, ECsumSB2015)

pie(sum2015$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2015")
barplot(sum2015$`Energy Intensity`, main="Energy intensity by sector in 2015", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

###2016

sum2016 <- as.data.frame(table(rawdata2016$Sector))

rawdata2016$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2016$Energy.Intensity.GJ_m2)
rawdata2016$GHG.Emissions.KG <- as.numeric(rawdata2016$GHG.Emissions.KG)

ECsumM2016 <- 0
ECsumPS2016 <- 0
ECsumPH2016 <- 0
ECsumSB2016 <- 0

GHGsumM2016 <- 0
GHGsumPS2016 <- 0
GHGsumPH2016 <- 0
GHGsumSB2016 <- 0

for (i in 1:nrow(rawdata2016)){
  if (rawdata2016$Sector[i] == 'Municipal'){
    ECsumM2016 <-  sum(c(ECsumM2016, rawdata2016$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumM2016 <-  sum(c(GHGsumM2016, rawdata2016$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2016$Sector[i] == 'Post-Secondary Educational Institution'){
    ECsumPS2016 <-  sum(c(ECsumPS2016, rawdata2016$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPS2016 <- sum(c(GHGsumPS2016, rawdata2016$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2016$Sector[i] == 'Public Hospital'){
    ECsumPH2016 <- sum(c(ECsumPH2016, rawdata2016$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPH2016 <- sum(c(GHGsumPH2016, rawdata2016$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2016$Sector[i] == 'School Board'){
    ECsumSB2016 <- sum(c(ECsumSB2016, rawdata2016$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumSB2016 <- sum(c(GHGsumSB2016, rawdata2016$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2016) = c("Sector", "GHG Emissions")

sum2016$`GHG Emissions` <- c(GHGsumM2016, GHGsumPS2016, GHGsumPH2016, GHGsumSB2016)
sum2016$'Energy Intensity' <- c(ECsumM2016, ECsumPS2016, ECsumPH2016, ECsumSB2016)

pie(sum2016$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2016")
barplot(sum2016$`Energy Intensity`, main="Energy intensity by sector in 2016", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

###2017

sum2017 <- as.data.frame(table(rawdata2017$Sector))

rawdata2017$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2017$Energy.Intensity.GJ_m2)
rawdata2017$GHG.Emissions.KG <- as.numeric(rawdata2017$GHG.Emissions.KG)

ECsumM2017 <- 0
ECsumPS2017 <- 0
ECsumPH2017 <- 0
ECsumSB2017 <- 0

GHGsumM2017 <- 0
GHGsumPS2017 <- 0
GHGsumPH2017 <- 0
GHGsumSB2017 <- 0

for (i in 1:nrow(rawdata2017)){
  if (rawdata2017$Sector[i] == 'Municipal'){
    ECsumM2017 <-  sum(c(ECsumM2017, rawdata2017$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumM2017 <-  sum(c(GHGsumM2017, rawdata2017$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2017$Sector[i] == 'Post-Secondary Educational Institution'){
    ECsumPS2017 <-  sum(c(ECsumPS2017, rawdata2017$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPS2017 <- sum(c(GHGsumPS2017, rawdata2017$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2017$Sector[i] == 'Public Hospital'){
    ECsumPH2017 <- sum(c(ECsumPH2017, rawdata2017$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPH2017 <- sum(c(GHGsumPH2017, rawdata2017$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2017$Sector[i] == 'School Board'){
    ECsumSB2017 <- sum(c(ECsumSB2017, rawdata2017$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumSB2017 <- sum(c(GHGsumSB2017, rawdata2017$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2017) = c("Sector", "GHG Emissions")

sum2017$`GHG Emissions` <- c(GHGsumM2017, GHGsumPS2017, GHGsumPH2017, GHGsumSB2017)
sum2017$'Energy Intensity' <- c(ECsumM2017, ECsumPS2017, ECsumPH2017, ECsumSB2017)

pie(sum2017$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2017")
barplot(sum2017$`Energy Intensity`, main="Energy intensity by sector in 2017", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

###2018

sum2018 <- as.data.frame(table(rawdata2018$Sector))

rawdata2018$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2018$Energy.Intensity.GJ_m2)
rawdata2018$GHG.Emissions.KG <- as.numeric(rawdata2018$GHG.Emissions.KG)

ECsumM2018 <- 0
ECsumPS2018 <- 0
ECsumPH2018 <- 0
ECsumSB2018 <- 0

GHGsumM2018 <- 0
GHGsumPS2018 <- 0
GHGsumPH2018 <- 0
GHGsumSB2018 <- 0

for (i in 1:nrow(rawdata2018)){
  if (rawdata2018$Sector[i] == 'Municipal'){
    ECsumM2018 <-  sum(c(ECsumM2018, rawdata2018$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumM2018 <-  sum(c(GHGsumM2018, rawdata2018$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2018$Sector[i] == 'Post-Secondary Educational Institution'){
    ECsumPS2018 <-  sum(c(ECsumPS2018, rawdata2018$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPS2018 <- sum(c(GHGsumPS2018, rawdata2018$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2018$Sector[i] == 'Public Hospital'){
    ECsumPH2018 <- sum(c(ECsumPH2018, rawdata2018$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPH2018 <- sum(c(GHGsumPH2018, rawdata2018$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2018$Sector[i] == 'School Board'){
    ECsumSB2018 <- sum(c(ECsumSB2018, rawdata2018$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumSB2018 <- sum(c(GHGsumSB2018, rawdata2018$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2018) = c("Sector", "GHG Emissions")

sum2018$`GHG Emissions` <- c(GHGsumM2018, GHGsumPS2018, GHGsumPH2018, GHGsumSB2018)
sum2018$'Energy Intensity' <- c(ECsumM2018, ECsumPS2018, ECsumPH2018, ECsumSB2018)

pie(sum2018$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2018")
barplot(sum2018$`Energy Intensity`, main="Energy intensity by sector in 2018", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

###2019

sum2019 <- as.data.frame(table(rawdata2019$Sector))

rawdata2019$Energy.Intensity.GJ_m2 <- as.numeric(rawdata2019$Energy.Intensity.GJ_m2)
rawdata2019$GHG.Emissions.KG <- as.numeric(rawdata2019$GHG.Emissions.KG)

ECsumM2019 <- 0
ECsumPS2019 <- 0
ECsumPH2019 <- 0
ECsumSB2019 <- 0

GHGsumM2019 <- 0
GHGsumPS2019 <- 0
GHGsumPH2019 <- 0
GHGsumSB2019 <- 0

for (i in 1:nrow(rawdata2019)){
  if (rawdata2019$Sector[i] == 'Municipal'){
    ECsumM2019 <-  sum(c(ECsumM2019, rawdata2019$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumM2019 <-  sum(c(GHGsumM2019, rawdata2019$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2019$Sector[i] == 'Post-Secondary Educational Institution'){
    ECsumPS2019 <-  sum(c(ECsumPS2019, rawdata2019$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPS2019 <- sum(c(GHGsumPS2019, rawdata2019$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2019$Sector[i] == 'Public Hospital'){
    ECsumPH2019 <- sum(c(ECsumPH2019, rawdata2019$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumPH2019 <- sum(c(GHGsumPH2019, rawdata2019$GHG.Emissions.KG[i]), na.rm = TRUE)}
  if (rawdata2019$Sector[i] == 'School Board'){
    ECsumSB2019 <- sum(c(ECsumSB2019, rawdata2019$Energy.Intensity.GJ_m2[i]), na.rm = TRUE)
    GHGsumSB2019 <- sum(c(GHGsumSB2019, rawdata2019$GHG.Emissions.KG[i]), na.rm = TRUE)}
}

colnames(sum2019) = c("Sector", "GHG Emissions")

sum2019$`GHG Emissions` <- c(GHGsumM2019, GHGsumPS2019, GHGsumPH2019, GHGsumSB2019)
sum2019$'Energy Intensity' <- c(ECsumM2019, ECsumPS2019, ECsumPH2019, ECsumSB2019)

pie(sum2019$`GHG Emissions`, labels = c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'), main = "GHG Emissions by sector in 2019")
barplot(sum2019$`Energy Intensity`, main="Energy intensity by sector in 2019", names.arg=c('Municipal', 'Post Secondary', 'Public Hospitals', 'School Board'))

summary(rawdata2014$GHG.Emissions.KG)
summary(rawdata2015$GHG.Emissions.KG)
summary(rawdata2016$GHG.Emissions.KG)
summary(rawdata2017$GHG.Emissions.KG)
summary(rawdata2018$GHG.Emissions.KG)
summary(rawdata2019$GHG.Emissions.KG)

summary(rawdata2014$Energy.Intensity.GJ_m2)
summary(rawdata2015$Energy.Intensity.GJ_m2)
summary(rawdata2016$Energy.Intensity.GJ_m2)
summary(rawdata2017$Energy.Intensity.GJ_m2)
summary(rawdata2018$Energy.Intensity.GJ_m2)
summary(rawdata2019$Energy.Intensity.GJ_m2)


