import csv


fileReader = open("../../output/analysis/vary_nT_results.csv", "r", encoding="utf8")
csvReader  = csv.reader(fileReader)

f = open("../../output/analysis/vary_nT_results_latex.txt","w") #opens file with name of "test.txt"
acHeader = next(csvReader)

#Print header
f.write("\\begin{tabular}{rrcccccc} \n")
f.write("\\hline \\hline \\\\[-0.9em] \n")
f.write("%s & " %acHeader[0])
f.write("%s & " %acHeader[1])
#for item in acHeader[2:-1]:
#    f.write("%s & " %item)
#f.write("%s \\\\ \\hline \\hline \\\\[-0.9em] \n" %acHeader[-1])

estimators =acHeader[2::2]
for item in estimators[:-1]:
    f.write("%s & " %item)
f.write("%s \\\\ \\hline \\hline \\\\[-0.9em] \n" %estimators[-1])


#Print main table
for acRow in csvReader:
    f.write("%s & " %acRow[0])
    f.write("%s & " %acRow[1])
    for i in range(2, len(acRow)-2, 2):
        f.write("%s / %s &" % (acRow[i],acRow[i+1]) )
    f.write("%s / %s \\\\ \n" % (acRow[len(acRow)-2],acRow[len(acRow)-1]) )

f.write("\\end{tabular}")

fileReader.close()
f.close()
