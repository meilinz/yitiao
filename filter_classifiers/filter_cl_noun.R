library(plyr)
load("../classifier_data/cl_noun_clean.Rdata")
noun_list <- levels(d$noun)
result_list <- vector("list", length(noun_list))

count_classifier <- function(noun, data){
  x <- data[which(data$noun == noun),]
  #count_cl <- as.data.frame(table(droplevels((x$classifier))))
  count_cl <- count(x, 'classifier') # uncomment this if plyr is available, and change count_cl$Freq to count_cl$freq in next line
  count_cl$cl_prop <- round(count_cl$freq/length(x$noun), digits = 3)
  #colnames(count_cl)[1] <- 'classifier'
  result <<- merge(x, count_cl, by="classifier")
}

i = 1
count = 0
system.time(
  for (noun in noun_list){
    count_classifier(noun, d)
    result_list[[i]]<- result
    i = i + 1
    count = count + 1
    if(count == 200){
      cat('\n',i)
      count = 0
    }
  }
  )

result <- do.call("rbind", result_list)
cat("The result has ", length(result$noun), " observations\n")
save(result, file = "../classifier_data/cl_noun_cl_prop_added.Rdata")

#load("../classifier_data/cl_noun_cl_prop_added.Rdata")

print("finished calculating classifier proportion for each noun type!\n")
print("start filtering classifier-noun pairs...\n")

result <- result[order(result$file_name, result$sentence_token_num),] 
result <- result[c("num", "classifier", "noun", "sentence_token_num", "cl_token_num", "noun_token_num", "file_name", "freq", "cl_prop")]
colnames(result)[8] <- "cl_freq_for_noun"
colnames(result)[9] <- "cl_prop_for_noun"
head(result, 10)

result_filtered <- result[which(result$cl_freq_for_noun > 1 & result$cl_prop_for_noun >= 0.02),]
result_filtered <- result_filtered[which(result_filtered$cl_prop_for_noun < 0.98),]

result_filtered <- as.data.frame(lapply(result_filtered, function (x) if (is.factor(x)) factor(x) else x))
length(result_filtered$classifier)
length(levels(result_filtered$classifier))
length(levels(result_filtered$noun))

noun_list <- levels(result_filtered$noun)
exclude_noun_list <- vector(mode="character", length=length(noun_list))

count_classifier <- function(noun, data){
  x <- data[which(data$noun == noun),]
  count_cl <- count(x, 'classifier') # use this if plyr is available, and change count_cl$Freq to count_cl$freq
  #count_cl <- as.data.frame(table(droplevels((x$classifier))))
  count_cl$cl_prop <- round(count_cl$freq/length(x$noun), digits = 3)
  #colnames(count_cl)[1] <- 'classifier'
  if (length(count_cl$classifier) < 2 | !"个" %in% count_cl$classifier) {#filter out nouns without "ge" and nouns with fewer than 2 cls
    exclude_noun <<- noun
    exclude_noun
  }
}

i = 1
count = 0
system.time(
  for (noun in noun_list){
    count_classifier(noun, result_filtered)
    try(exclude_noun_list[[i]]<- exclude_noun)
    i = i + 1
    count = count + 1
    if(count == 200){
      cat('\n',i)
      count = 0
    }
  }
)

exclude_noun_list <- exclude_noun_list[exclude_noun_list != ""]

result_filtered <- result_filtered[which(!result_filtered$noun %in% exclude_noun_list),]
result_filtered <- as.data.frame(lapply(result_filtered, function (x) if (is.factor(x)) factor(x) else x))
cat("The filtered result has ", length(result_filtered$noun), " observations\n")
cat("The filtered result has ", length(levels(result_filtered$noun)), " unique nouns\n")

save(result_filtered, file = "../classifier_data/cl_noun_cl_prop_filtered.Rdata")
write.csv(result_filtered, file = "../classifier_data/cl_noun_cl_prop_filtered.csv", row.names = FALSE)

