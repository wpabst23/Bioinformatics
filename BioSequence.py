## William Pabst
## Eastern Connecticut State University
## Intro to Bioinformatics
## Homework 1
##
##The following is a method that takes in a gene sequence (a series of A's, T's, G's, and C's), and outputs the
##complement and reverse complement sequences for the input. Invalid Characters are replaced with "-" in the 2 latter sequences).

class genesequence():
    seq = input("Enter a gene sequence starting at 5': ").upper() #Takes in a gene sequence, and converts all characters to uppoercase

    #This block creates variables for our sequences, and prepares them to be manipulated
    seq = list(seq)
    compseq = "3'- "
    compseq = list(compseq)
    revcompseq = "5'- "
    revcompseq = list(revcompseq)

    i = 0
    while i < len(seq): #This loop goes through the sequence to construct the complement
        if seq[i].upper() == 'A':
            compseq.append('T')

        if seq[i].upper() == 'T':
            compseq.append('A')

        if seq[i].upper() == 'C':
            compseq.append('G')

        if seq[i].upper() == 'G':
            compseq.append('C')
        if seq[i].upper() != 'A' and seq[i].upper() != 'T' and seq[i].upper() != 'C' and seq[i].upper() != 'G':
            compseq.append('-')
        i = i + 1
    compseq.append(" -5'")

    i = len(seq) + 3
    while i > 3: #This loop goes through the complement to construct the reverse complement
        if compseq[i].upper() == 'A':
            revcompseq.append('T')
        if compseq[i].upper() == 'T':
            revcompseq.append('A')
        if compseq[i].upper() == 'C':
            revcompseq.append('G')
        if compseq[i].upper() == 'G':
            revcompseq.append('C')
        if compseq[i] == '-':
            revcompseq.append('-')
        i = i - 1
    revcompseq.append(" -3'")

    #Output
    seq = ''.join(seq)
    print("The sequence you entered was: " + "5'- " + seq + " -3'")
    compseq = ''.join(compseq)
    print("The complement of that sequence is: " + compseq)
    revcompseq = ''.join(revcompseq)
    print("The reverse complement of that sequence is: " + revcompseq)



def main():
    genesequence()

if __name__ == "__main__": main()