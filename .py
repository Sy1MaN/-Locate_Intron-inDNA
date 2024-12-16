def locate_intron(a,b):
    intron1 = []
    checker = 0
    num = -1
    dict1={
        "UUU": "PHE", "UUC":"PHE", "UUA":"LEU","UUG":"LEU","UCU":"SER",
         "UCC":"SER", "UCA":"SER","UCG":"SER","UAU":"TYR","UAC":"TYR",
         "UAA":"stop","UAG":"stop","UGU":"CYS","UGC":"CYS","UGA":"stop",
         "UGG":"TRP",
         "CUU":"LEU","CUC":"LEU","CUA":"LEU","CUG":"LEU","CCU":"PRO",
         "CCC":"PRO","CCA":"PRO","CCG":"PRO","CAU":"HIS","CAC":"HIS",
         "CAA":"GLN","CAG":"GLN","CGU":"ARG","CGC":"ARG","CGA":"ARG",
         "CGG":"ARG",
         "AUU":"ILE","AUC":"ILE","AUA":"ILE","AUG":"MET","ACU":"THR",
         "ACC":"THR","ACA":"THR","ACG":"THR","AAU":"ASN","AAC":"ASN",
         "AAA":"LYS","AAG":"LYS","AGU":"SER","AGC":"SER","AGA":"ARG",
         "AGG":"ARG",
         "GUU":"VAL","GUC":"VAL","GUA":"VAL","GUG":"VAL","GCU":"ALA",
         "GCC":"ALA","GCA":"ALA","GCG":"ALA","GAU":"ASP","GAC":"ASP",
         "GAA":"GLU","GAG":"GLU","GGU":"GLY","GGC":"GLY","GGA":"GLY",
         "GGG":"GLY"
         }
    mrna = []       
    for i in a:
        if i == "A":
            mrna.append("U")
        elif i == "T":
            mrna.append("A")
        elif i == "G":
            mrna.append("C")
        elif i == "C":
            mrna.append("G")
    end = []
    for i in range(0,len(mrna)-2,3):
        codon=mrna[i]+mrna[i+1]+mrna[i+2]
        end.append(dict1[codon])
        num+=1
        if end[num]!=b[num]:
            end.remove(end[-1])
            checker=i
            intron1.append(checker)
            break
    for i in range(checker,len(mrna)):
        codon=mrna[i]+mrna[i+1]+mrna[i+2]
        if codon in dict1 and dict1[codon] == b[num]  and dict1[mrna[i+3]+mrna[i+4]+mrna[i+5]]== b[num+1] and dict1[mrna[i+6]+mrna[i+7]+mrna[i+8]]== b[num+2]:
            checker = i
            intron1.append(checker-1)
            break
        else:
            continue
    for i in range(checker,len(mrna)-2,3):
        codon=mrna[i]+mrna[i+1]+mrna[i+2]
        end.append(dict1[codon])
        num+=1
        if end[num-1]!=b[num-1]:
            end.remove(end[-1])
            end.remove(end[-1])
            checker=i-3
            intron1.append(checker)
            break
        else:
            continue
    for i in range(checker,len(mrna)-2):
        codon=mrna[i]+mrna[i+1]+mrna[i+2]
        if codon in dict1 and dict1[codon] == b[num]  and dict1[mrna[i+3]+mrna[i+4]+mrna[i+5]]== b[num+1] and dict1[mrna[i+6]+mrna[i+7]+mrna[i+8]]== b[num+2]:
            checker = i-6
            intron1.append(checker-1)
            break
        else:
            continue
    for i in range(checker,len(mrna),3):
        codon=mrna[i]+mrna[i+1]+mrna[i+2]
        end.append(dict1[codon])
        num+=1
        if end[num-3]!=b[num-3]:
            end.remove(end[-1])
            end.remove(end[-1])
            checker=i-3
            intron1.append(checker)
            break
        else:
            continue 
    intron1_place = []
    intron2_place = []
    for i in range(4):
        if i<2:
            intron1_place.append(intron1[i])
        else:
            intron2_place.append(intron1[i])
    return [intron1_place,intron2_place]

print(locate_intron(["T","C","T","G","C","A","G","C","A","G","A","G","G","G","G","C","C", 
"G","T","C","G","G","C","A","G","A","A","G","G","A","G","G","G","C", 
"T","C","G","G","G","C","A","G","G","C","T","C","T","G","C","G","A", 
"C","T","C","G","T","A","G","G","C","A","C","C","A","G","G","C","G", 
"T","G","A","G","A","C","C","T","G","T","A","G","C","C","C","C","C", 
"G","A","T","C","A","C","C","A","T","G","T","A","C","A","G","C","T", 
"T","C","A","T","G","G","G","T","G","G","T","G","G","C","C","T","G", 
"T","T","C","T","G","T","G","C","C","T","G","G","G","T","G","G","G", 
"G","A","C","C","A","T","C","C","T","C","C","T","G","G","T","G","G", 
"T","G","G","C","C","A","T","G","G","C","A","A","C","A","G","A","C", 
"G","G","G","G","C","C","A","A","G","G","A","C","A","C","C","T","G", 
"T","A","T","T","C","C","A","G","A","T","G","G","A","G","A","A","C", 
"T","C","T","G","C","G","G","C","T","C","A","A","A","G","A","G","G", 
"G","A","A","A","G","G","G","A","G","C","A","A","C","C","C","A","A", 
"G","G","T","C","A","C","T","C","A","G","C","G","G","A","G","G","C", 
"T","G","A","C","T","C","C","T","G","G","T","C","C","T","A","G","G", 
"C","T","G","G","A","A","G","G","A","G","G","A","A","G","A","A","T", 
"A","G","G","G","C","C","C","A","T","G","G","G","A","G","G","G","A", 
"G","C","T","G","A","G","A","A","G","A","C","T"],["ARG","ARG","ARG","LEU","PRO","GLY","SER","ARG","LEU","PRO","PRO", 
"GLU","PRO","VAL","ARG","ASP","ALA","GLU","LEU","VAL","VAL","HIS", 
"VAL","GLU","VAL","PRO","THR","THR","GLY","GLN","ASP","THR","ASP", 
"PRO","PRO","LEU","VAL","GLY","GLY","PRO","PRO","PRO","VAL","PRO", 
"LEU","SER","PRO","PRO","THR","GLU","ASP","GLN","ASP","PRO","THR", 
"PHE","LEU","LEU","LEU","ILE","PRO","GLY","THR","LEU","PRO","ARG", 
"LEU","PHE","stop"]))
