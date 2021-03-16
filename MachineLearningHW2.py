import csv
## Classes ####################################################################################################################################

# this class is an Amino Acid and holds all relavent Amino Acid data. any data not included in this initialy can be added to the self.data Dictionay later
class AminoAcid:
    def __init__(self,amino_acid_name,_3_letter_code,_1_letter_code,codons,data = {}):
        self.name = amino_acid_name
        self.m3code = _3_letter_code
        self.m1code = _1_letter_code
        self.__codons = codons
        self.data = data
    # returns an string array of condons
    def getCondons(self):
        return self.__codons.split(',')
    # returns the codons as a string with comma seperators
    def getCondonsString(self):
        return self.__codons
    # overriden string str() method
    def __str__(self):
        a = self.name
        for key,value in self.data.items():
            a += "\n\t\t"+str(key)+": "+str(value)
        return a
# this is a class that holds all the amino acid and realtive data we will use for this assignment.
# if you want to add more data, then just add it to the 'data' parameter. (see Amino Acid for more detail) 
class AminoAcids:
    def __init__(self):
        self.__aminoAcids = [
            AminoAcid("Alanine","Ala","A","GCA,GCC,GCG,GCT",{'volume': 31.0}),
            AminoAcid("Cysteine","Cys","C","TGC,TGT",{"volume": 55.0}),
            AminoAcid("Aspartic acid","Asp","D","GAC,GAT",{"volume": 54.0}),
            AminoAcid("Glutamic acid","Glu","E","GAA,GAG",{"volume": 83.0}),
            AminoAcid("Phenylalanine","Phe","F","TTC,TTT",{"volume": 132.0}),
            AminoAcid("Glycine","Gly","G","GGA,GGC,GGG,GGT",{"volume": 3.0}),
            AminoAcid("Histidine","His","H","CAC,CAT",{"volume": 96.0}),
            AminoAcid("Isoleucine","Ile","I","ATA,ATC,ATT",{"volume": 111.0}),
            AminoAcid("Lysine","Lys","K","AAA,AAG",{"volume": 119.0}),
            AminoAcid("Leucine","Leu","L","CTA,CTC,CTG,CTT,TTA,TTG",{"volume": 111.0}),
            AminoAcid("Methionine","Met","M","ATG",{"volume": 105.0}),
            AminoAcid("Asparagine","Asn","N","AAC,AAT",{"volume": 56.0}),
            AminoAcid("Proline","Pro","P","CCA,CCC,CCG,CCT",{"volume": 32.0}),
            AminoAcid("Glutamine","Glu","Q","CAA,CAG",{"volume": 85.0}),
            AminoAcid("Arginine","Arg","R","AGA,AGG,CGA,CGC,CGG,CGT",{"volume": 124.0}),
            AminoAcid("Serine","Set","S","AGC,AGT,TCA,TCC,TCG,TCT",{"volume": 32.0}),
            AminoAcid("Threonine","Thr","T","ACA,ACC,ACG,ACT",{"volume": 61.0}),
            AminoAcid("Valine","Val","V","GTA,GTC,GTG,GTT",{"volume": 84.0}),
            AminoAcid("Tryptophan","Trp","W","TGG",{"volume": 170.0}),
            AminoAcid("Tyrosine","Tyr","Y","TAC,TAT",{"volume": 136.0}),
            ]
    def getAminoAcids(self):
        return self.__aminoAcids
# This is the protein class. here you find all protein data and amino acid data found in this protien.
#  Please be sure to call 'updateData()' to make sure all your data is updated before any calculations
class Protein:
    def __init__(self,sequence,name = "Protein"):
        self.sequence = sequence
        self.__amino_acids = []
        self.data = {}
        self.__name = name
    # this function counts the amount of the given amino_acid is contained in this protein.
    def getNumberOfAminoAcidInProtein(self,amino_acid):
        sequences = chunkstring(self.sequence,3)
        count = 0
        lastIndex = -3
        for codon in amino_acid.getCondons():
            while lastIndex != -1:
                lastIndex = self.sequence.find(codon,lastIndex+3)
                count+=1
        return count
    # this function tests if the given amino_acid is contained in this protein.
    # if it is, then it is added to the protein's 'self.__amino_acid' array
    def testAndAddAminoAcid(self,amino_acid):
        amino_acid_count = self.getNumberOfAminoAcidInProtein(amino_acid)
        if(amino_acid_count > 0):
            self.__addAminoAcid(amino_acid,amino_acid_count)
    def __addAminoAcid(self,amino_acid, amount):
    # this adds the amino_acid to the proteins 'self.__amino_acid' array.
        amino_acid.data["count"] = amount
        self.__amino_acids.append(amino_acid)
    # this gets the volume data from all the amino acids in the 'self.__amino_acid' array and calculates the protein's volume based on that.
    def getVolume(self):
        volume = 0
        for amino_acid in self.__amino_acids:
            volume += amino_acid.data["volume"]*amino_acid.data["count"]
        self.data["volume"] = volume
        return volume
    # updates the data in the protein
    def updateData(self):
        self.getVolume()
    # unfinished!
    def formatForCSV(self):
        updateData()
        return self.__name+","+self.data["volume"]+","+self.sequence
    # overriden str()
    def __str__(self):
        s = self.__name+"\nProtein Data:"
        for key,value in self.data.items():
            s+= "\n\t "+str(key)+": "+str(value)
        s+="\nAmino Acid Data:"
        for a in self.__amino_acids:
            s += "\n\t"+str(a)
        return s
# this holds an array of protiens and related functions
class Proteins:
    def __init__(self):
        self.__proteins = []
        self.AminoAcids = AminoAcids()
    def addProtein(self,protein):
        for amino_acid in self.AminoAcids.getAminoAcids():
            protein.testAndAddAminoAcid(amino_acid)
        protein.updateData()
        self.__proteins.append(protein)
    def getProteins(self):
        return self.__proteins
    def outputFeatureVector(self):
        with open('test.csv', 'w') as f:
            fieldnames = ['volume']
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writeheader()
            for protein in self.__proteins:
                #print(protein)
                writer.writerow({'volume': protein.data["volume"]})
                #f.write("%s,%s\n"%(key,my_dict[key]))
            

            
## FUNCTIONS #######################################################################################################################

# normalizes the given value to a number between 0-1
#   (number) value:         value to be normalized
#   (number) min_value:     smallest possible value
#   (number) max_value:     largest posible value
def normalize(value,min_value,max_value):
    return (value - min_value)/(max_value - min_value)

# breaks the given string into chunks by length
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

#loads the given file path in read mode and returns an array of string data
def loadFile(path):
    file = open(path,"r")
    data = file.read().split(DATA_SEPERATOR);
    file.close()
    return data

#converts Dictionary contents into a csv file
def convertDictonaryToCSV(my_dict):
    with open('test.csv', 'w') as f:
        #fieldnames = ['volume']
        #writer = csv.DictWriter(csvfile, fieldname = fieldnames)
        #writer.writeheader
        for key in my_dict.keys():
            #writer.writerow({'volume': my_dict[key].})
            f.write("%s,%s\n"%(key,my_dict[key]))

## CONSTANTS

SEQUENCE_FILE_PATH = "Sequence.txt"
LABEL_FILE_PATH = "Label.txt"
COMP_FILE_PATH = "comp.csv"
GDATA_FILE_PATH = "g_data.csv"
OCCUR_FILE_PATH = "occur.csv"
DATA_SEPERATOR = '\n'
AMINO_ACIDS = AminoAcids()


## MAIN ##################################################################################################################################

# load all the data
sequence_data = loadFile(SEQUENCE_FILE_PATH)

#label_data = loadFile(LABEL_FILE_PATH)
#comp_data = loadFile(COMP_FILE_PATH)
#g_data = loadFile(GDATA_FILE_PATH)
#occur_data = loadFile(OCCUR_FILE_PATH)

proteins = Proteins()
# note: it is assumed that all the data is the same length
for i in range(len(sequence_data)):
    proteins.addProtein(Protein(sequence_data[i],"Protein "+str(i)))

## not needed any more ##
##########################################################################################################
#    combined_data.append(AminoData(label_data[i],sequence_data[i],comp_data[i],g_data[i],occur_data[i]))
#    proteins.append(Protein(sequence_data[i],"Protein "+str(i)))
#    for j in range(len(AMINO_ACIDS.getAminoAcids())):
#        proteins[i].testAndAddAminoAcid(AMINO_ACIDS.getAminoAcids()[j])
#    proteins[i].updateData()
##########################################################################################################

# print out results
for protein in proteins.getProteins():
    print(str(protein))

proteins.outputFeatureVector()

print("done...")
