library(tidyverse)

read.blast = function(folder, use_list = F){
  column_names = c("qseqid", "sseqid", "pident", "length", "mismatch", "gapopen",
                   "qstart", "qend", "sstart", "send", "evalue", "bitscore")
  
  if(use_list){
    out = list()
    files = list.files(folder)
    for (file in files){
      all.samples = column_names
      
      data = read.csv(file = str_c(folder, '/', file), sep = '\t',
                      header = F)
      all.samples = rbind(all.samples, data)
      
      colnames(all.samples) = all.samples[1,]
      all.samples = all.samples[-1,]
      all.samples[,3:12] = sapply(all.samples[,3:12], as.numeric)
      
      out[[str_replace(file, '.csv', '')]] = all.samples                    
    }
  } else {
    files = list.files(folder)
    all.samples = matrix(column_names, ncol = length(column_names))
    for (file in files){
      data = read.csv(file = str_c(folder, '/', file), sep = '\t',
                      header = F)
      all.samples = rbind(all.samples, data)
    }
    colnames(all.samples) = all.samples[1,]
    all.samples = all.samples[-1,]
    all.samples[,3:12] = sapply(all.samples[,3:12], as.numeric)
    out = all.samples
  }
  return(out)
}

