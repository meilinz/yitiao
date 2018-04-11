library(plyr)
getwd()
data <- read.csv("../classifier_data/classifier_noun_pairs_sogoucs2008.csv", header = FALSE)
print("finish reading data")
colnames(data)[1] <- "num"
colnames(data)[2] <- "classifier"
colnames(data)[3] <- "noun"
colnames(data)[4] <- "sentence_token_num"
colnames(data)[5] <- "cl_token_num"
colnames(data)[6] <- "noun_token_num"
colnames(data)[7] <- "file_name"

top_cl <- head(names(sort(table(data$classifier), decreasing = TRUE)), 300)
lowerbound <- data[data$classifier==top_cl[300],]
cat("The unfiltered lowerbound classifier has ", length(lowerbound$classifier), "observations\n")

cl_freq_table <- count(data, 'classifier')
top_cl_table <- subset(cl_freq_table, freq>=length(lowerbound$classifier))
top_cl_table <- top_cl_table[ order(top_cl_table$freq, decreasing = TRUE), ]

x = (sum(top_cl_table$freq)/length(data$classifier))*100
cat("The top 300 classifiers cover ", x, "% of the data\n")

ma2015 <- scan("../classifier_data/ma2015_classifier_list.txt",what="",sep="\n")

z <- top_cl_table$classifier %in% ma2015
length(top_cl_table$classifier[z]) #91

d <- subset(data, data$classifier %in% top_cl)
d <- subset(d, d$classifier %in% ma2015)
#exclude_cl <- c("点", "样", "种", "类","层","等","级","截","节","码","章","股")
exclude_cl <- c("点", "样", "种", "类","层","等","级","截","节","码","章","股","份","滴","番","页","列","团","局","段","片","重","阵","顿","场")
d <- subset(d, !(d$classifier %in% exclude_cl))
length(unique(d$classifier))# 79 classifiers left
cat("Now we have ", length(unique(d$classifier)), "unique classifies left\n")

noun_freq_table <- count(d, 'noun')
noun_freq_table <- noun_freq_table[ order(noun_freq_table$freq, decreasing = FALSE), ]#78916 nouns
exclude_noun <- subset(noun_freq_table, freq<3)$noun
d <- subset(d, !(d$noun %in% exclude_noun))
exclude_noun_nonchn <- grep("[Ａ-Ｚａ-ｚ０-９｀～！＠＃＄＾＆＊（）＝｜｛｝＇：；＇，﹐﹔…·····《》〔→↓×㎡φπ—［］．＂’＜＞／？～！＠＃＆＊％―－、“”Ⅲ]", noun_freq_table$noun, value = TRUE, perl = TRUE)
d <- subset(d, !(d$noun %in% exclude_noun_nonchn))
exclude_noun_numwords <-
  c("一","二","三","四","五","六","七","八","九","十","百","千","万","十万","百万","千万","亿","一百","二百","两百","三百","四百",
    "五百","六百","七百","八百","九百","一千","二千","两千","三千","四千","五千","六千","七千","八千","九千",
    "一万","二万","两万","三万","四万","五万","六万","七万","八万","九万")
d <- subset(d, !(d$noun %in% exclude_noun_numwords))

d <- as.data.frame(lapply(d, function (x) if (is.factor(x)) factor(x) else x))
cat("The dataset has ", length(d$noun), " observations\n")
cat("The dataset has ", length(levels(d$noun)), "unique noun types\n")

save(d, file = "../classifier_data/cl_noun_clean.Rdata")
