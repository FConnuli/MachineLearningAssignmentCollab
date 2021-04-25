import csv

##########################################
## Created By Steven, Francis, & Giorgi ##
##########################################

## Classes ####################################################################################################################################

# this class is an Amino Acid and holds all relavent Amino Acid data. any data not included in this initialy can be added to the self.data Dictionay later
class AminoAcid:
    def __init__(self,amino_acid_name,_1_letter_code,data = {}):
        self.name = amino_acid_name
        self.m1code = _1_letter_code
        self.data = data

# this is a class that holds all the amino acid and realtive data we will use for this assignment.
# if you want to add more data, then just add it to the 'data' parameter. (see Amino Acid for more detail) 
class AminoAcids:
    def __init__(self):
        self.__aminoAcids = [
            AminoAcid("Alanine","A",{'volume': 31.0}),
            AminoAcid("Cysteine","C",{"volume": 55.0}),
            AminoAcid("Aspartic acid","D",{"volume": 54.0}),
            AminoAcid("Glutamic acid","E",{"volume": 83.0}),
            AminoAcid("Phenylalanine","F",{"volume": 132.0}),
            AminoAcid("Glycine","G",{"volume": 3.0}),
            AminoAcid("Histidine","H",{"volume": 96.0}),
            AminoAcid("Isoleucine","I",{"volume": 111.0}),
            AminoAcid("Lysine","K",{"volume": 119.0}),
            AminoAcid("Leucine","L",{"volume": 111.0}),
            AminoAcid("Methionine","M",{"volume": 105.0}),
            AminoAcid("Asparagine","N",{"volume": 56.0}),
            AminoAcid("Proline","P",{"volume": 32.0}),
            AminoAcid("Glutamine","Q",{"volume": 85.0}),
            AminoAcid("Arginine","R",{"volume": 124.0}),
            AminoAcid("Serine","S",{"volume": 32.0}),
            AminoAcid("Threonine","T",{"volume": 61.0}),
            AminoAcid("Valine","V",{"volume": 84.0}),
            AminoAcid("Tryptophan","W",{"volume": 170.0}),
            AminoAcid("Tyrosine","Y",{"volume": 136.0}),
            ]
    def getAminoAcids(self):
        return self.__aminoAcids
# This is the protein class. here you find all protein data and amino acid data found in this protien.
#  Please be sure to call 'updateData()' to make sure all your data is updated before any calculations
class Protein:
    def __init__(self,sequence, foldNum, name = "Protein",):
        self.sequence = sequence
        self.__amino_acids = []
        self.data = {}
        self.data["fold"] = "fold" + foldNum
        self.__name = name
    # this function counts the amount of the given amino_acid is contained in this protein.
    def getNumberOfAminoAcidInProtein(self,amino_acid):
        count = 0
        lastIndex = 0
        while lastIndex != -1:
        #    print("testing if "+str(amino_acid.m1code)+" in "+ self.sequence[lastIndex: len(self.sequence)-1])
            lastIndex = self.sequence.find(amino_acid.m1code,lastIndex)
            if lastIndex != -1:
                count+=1
                lastIndex+=1
        return count
    # this function returns the total amount of amino acids in this protein
    def getNumberOfAllAminoAcidsInProtein(self):
        count = 0
        for amino_acid in self.__amino_acids:
            count+=amino_acid.data["count"]
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
    # returns the name of the protein
    def getName(self):
        return self.__name
    # updates the data in the protein
    def updateData(self):
        self.getVolume()
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
        with open('volume.csv', 'w+') as f:
            fieldnames = ['fold','volume']
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writeheader()
            for protein in self.__proteins:
                #print(protein)
                number_of_amino_acids = protein.getNumberOfAllAminoAcidsInProtein()
                if(number_of_amino_acids == 0):
                    print("critical error at protein"+protein.getName())
                    number_of_amino_acids = 1
                writer.writerow({'fold': protein.data["fold"], 'volume': protein.data["volume"]/number_of_amino_acids})
                #f.write("%s,%s\n"%(key,my_dict[key]))

            
## FUNCTIONS #######################################################################################################################



#loads the given file path in read mode and returns an array of string data
def loadFile(path):
    file = open(path,"r")
    data = file.read().split(DATA_SEPERATOR);
    file.close()
    return data


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

label_data = loadFile(LABEL_FILE_PATH)
#comp_data = loadFile(COMP_FILE_PATH)
#g_data = loadFile(GDATA_FILE_PATH)
#occur_data = loadFile(OCCUR_FILE_PATH)

proteins = Proteins()
# note: it is assumed that all the data is the same length
for i in range(len(sequence_data)):
    if(len(str(sequence_data[i])) > 0):
        proteins.addProtein(Protein(sequence_data[i], label_data[i], "Protein "+str(i)))
    else:
        print("warning@"+SEQUENCE_FILE_PATH+"@"+str(i)+": cannot add empty protein string!")

    proteins.outputFeatureVector()

print("done...")
