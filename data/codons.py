#!/usr/bin/python
""" Ter = ["TAA", "TAG", "TGA"]
    Phe = ["TTT", "TTC"]
    Leu = ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG", "CTN"]
    Ser = ["TCT", "TCC", "TCA", "TCG", "TCN", "AGT", "AGC"]
    Tyr = ["TAT", "TAC"]
    Cys = ["TGT", "TGC"]
    Trp = ["TGG"]
    Pro = ["CCT", "CCC", "CCA", "CCG", "CCN"]
    His = ["CAT", "CAC"]
    Gln = ["CAA", "CAG"]
    Arg = ["CGT", "CGC", "CGA", "CGG", "CGN", "AGA", "AGG"]
    Ile = ["ATT", "ATC", "ATA"]
    Met = ["ATG"]
    Thr = ["ACT", "ACC", "ACA", "ACG", "ACN"]
    Asn = ["AAT", "AAC"]
    Lys = ["AAA", "AAG"]
    Val = ["GTT", "GTC", "GTA", "GTG", "GTN"]
    Ala = ["GCT", "GCC", "GCA", "GCG", "GCN"]
    Asp = ["GAT", "GAC"]
    Glu = ["GAA", "GAG"]
    Gly = ["GGT", "GGC", "GGA", "GGG", "GGN"]
    Any = ["TAN", "TTN", "TGN", "CAN", "ATN", "AAN", "GAN", "AGN", \
                   "ANA", "ANT", "ANG", "ANC", \
                   "TNA", "TNT", "TNG", "TNC", \
                   "GNA", "GNT", "GNG", "GNC", \
                   "CNA", "CNT", "CNG", "CNC", \
                   "NAA", "NAT", "NAG", "NAC", \
                   "NTA", "NTT", "NTG", "NTC", \
                   "NGA", "NGT", "NGG", "NGC", \
                   "NCA", "NCT", "NCG", "NCC", \
                   "NNA", "NNT", "NNG", "NNC", \
                   "ANN", "TNN", "GNN", "NNC", \
                   "NAN", "NTN", "NGN", "NCN", \
                   "NNN"]
    Any : "X", Ter: "*", Phe: "F",
    Leu: "L", Ser: "S", Tyr: "Y",
    Cys: "C", Trp: "W", Pro: "P",
    His: "H", Gln: "Q", Arg: "R",
    Ile: "I", Met: "M", Thr: "T",	   
    Asn: "N", Lys: "K", Val: "V",
    Ala: "A", Asp: "D", Glu: "E",
    Gly: "G" """

standard = { 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L',
             'CTA': 'L', 'CTG': 'L', 'CTN': 'L', 'TGG': 'W',
             'TAA': '*', 'TAG': '*', 'TGA': '*', 'ATG': 'M',
             'TTT': 'F', 'TTC': 'F', 'TAT': 'Y', 'TAC': 'Y',
             'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
             'TCN': 'S', 'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 
             'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CCN': 'P',
             'TGT': 'C', 'TGC': 'C', 'CAT': 'H', 'CAC': 'H',
             'CAA': 'Q', 'CAG': 'Q', 'AAT': 'N', 'AAC': 'N',
             'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
             'CGN': 'R', 'AGA': 'R', 'AGG': 'R', 'ATT': 'I', 
             'ATC': 'I', 'ATA': 'I', 'AAA': 'K', 'AAG': 'K',
             'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
             'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
             'ACN': 'T', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V',
             'GTG': 'V', 'GTN': 'V', 'GCT': 'A', 'GCC': 'A',
             'GCA': 'A', 'GCG': 'A', 'GCN': 'A', 'GGT': 'G', 
             'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'GGN': 'G',
             'TAN': 'X', 'TTN': 'X', 'TGN': 'X', 'CAN': 'X', 
             'ATN': 'X', 'AAN': 'X', 'GAN': 'X', 'AGN': 'X',
             'ANA': 'X', 'ANT': 'X', 'ANG': 'X', 'ANC': 'X', 
             'TNA': 'X', 'TNT': 'X', 'TNG': 'X', 'TNC': 'X', 
             'GNA': 'X', 'GNT': 'X', 'GNG': 'X', 'GNC': 'X', 
             'CNA': 'X', 'CNT': 'X', 'CNG': 'X', 'CNC': 'X', 
             'NAA': 'X', 'NAT': 'X', 'NAG': 'X', 'NAC': 'X', 
             'NTA': 'X', 'NTT': 'X', 'NTG': 'X', 'NTC': 'X', 
             'NGA': 'X', 'NGT': 'X', 'NGG': 'X', 'NGC': 'X', 
             'NCA': 'X', 'NCT': 'X', 'NCG': 'X', 'NCC': 'X', 
             'NNA': 'X', 'NNT': 'X', 'NNG': 'X', 'NNC': 'X', 
             'ANN': 'X', 'TNN': 'X', 'GNN': 'X', 'NNC': 'X', 
             'NAN': 'X', 'NTN': 'X', 'NGN': 'X', 'NCN': 'X', 
             'NNN': 'X'
}