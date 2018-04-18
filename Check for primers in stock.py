
# 7 lines of data
filename = "ENdata.csv"
file = open(filename,"r")
data = []
count = 0
for line in file:
    data.append(line[0:-2].upper())
#print(data)
    #Gathered a list (data) of different available primers
    
test_seq= "TAATACAGAGATGATGTATCCAGCAGATGGTGGTCTGAGGGGATACACTCATATGGCACTGAAAGTTGATGGTGGTGGCCATCTGTCTTGCTCTTTCGTAACAACTTACAGGTCAAAAAAGACCGTCGGGAACATCAAGATGCCCGGTATCCATGCCGTTGATCACCGCCTGGAAAGGTTAGAGGAAAGTGACAATGAAATGTTCGTAGTACAACGCGAACACGCAGTTGCCAAGTTCGCCGGGCTTGGTGGTGGGATGGACGAGCTGTACAAGTAAgtttaaacatagcctcgactgtgccttctagttgccagccatctgttgtttgcccctcccccgtgccttccttgaccctggaaggtgccactcccactgtcctttcctaataaaatgaggaaattgcatcgcattgtctgagtaggtgtcattctattctggggggtggggtggggcaggacagcaagggggaggattgggaagacaatagcaggca".upper()
#test_seq is the part that I should change.
#this is the sequence we are looking for primers in.
primer = []

def recursive(x,y,sequence,genome,store):
    if sequence[x] == genome[y]:
        try:
            recursive((x+1),(y+1),sequence,genome,store)
        except:
            store.append(sequence)
#recursive function basically goes through each part of 
# the string sequentially checking to see if the
# next nucleotide matches the sequence.
# purpose of the except line is to catch when you are
            #at the end of the sequnce.

for sequence in data:
    for num in range(0,(len(test_seq)-len(sequence))-1):
        recursive(0,num,sequence,test_seq,primer)
print(primer)
#probably should have been a function,
#iterates through each sequnce in the data set,
# iterates over a number of lengths which should be
#between the length of the primer on the sequnce.