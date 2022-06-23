# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 1 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK ALGORITMANYA

import os.path
import time

def sama(a,b):
    for i in range(len(b)):
        if a[0] == b[i][0] and a[1] == b[i][1]:
            return True
    return False

class ScoringScheme:
    MATCH = 1
    MISMATCH = -1
    GAP = -2

class Solver:
    def __init__(self):
        self.matrix = []
        self.DNA1 = ""
        self.DNA2 = ""
        self.runtime = 0
        self.route = []
        self.DNA1Sol = ""
        self.DNA2Sol = ""
        self.sol = ""
        self.points = []
        self.points2 = []

    def createMatrix(self):
        for i in range(len(self.DNA2) + 2):
            self.matrix.append([])
            for j in range(len(self.DNA1) + 2):
                self.matrix[i].append(0)

        # BASIS (MENGISI BARIS PERTAMA DAN KOLOM PERTAMA DENGAN GAP)
        self.matrix[0][0] = " "
        self.matrix[0][1] = " "
        self.matrix[1][0] = " "
        for i in range(len(self.DNA2)):
            self.matrix[i+2][0] = self.DNA2[i]
            self.matrix[i+2][1] = (ScoringScheme.GAP)*(i+1)
        for j in range(len(self.DNA1)):
            self.matrix[0][j+2] = self.DNA1[j]
            self.matrix[1][j+2] = (ScoringScheme.GAP)*(j+1)

        # REKURENS (DENGAN PENDEKATAN DYNAMIC PROGRAMMING)
        for i in range(2, len(self.DNA2)+2):
            for j in range(2, len(self.DNA1)+2):
                if self.DNA2[i-2] == self.DNA1[j-2]:
                    self.matrix[i][j] = max(self.matrix[i-1][j-1] + ScoringScheme.MATCH, self.matrix[i-1][j] + ScoringScheme.GAP, self.matrix[i][j-1] + ScoringScheme.GAP)
                else:
                    self.matrix[i][j] = max(self.matrix[i-1][j-1] + ScoringScheme.MISMATCH, self.matrix[i-1][j] + ScoringScheme.GAP, self.matrix[i][j-1] + ScoringScheme.GAP)

    def traceback(self):
        baris = len(self.DNA2) + 1
        kolom = len(self.DNA1) + 1

        self.points.append([baris,kolom])
        # Traceback dari paling bawah kanan matrix hingga ke atas kiri
        while not (baris == 1 and kolom == 1):
            if baris == 1:
                self.route.append("L")
                self.DNA1Sol = self.DNA1[kolom-2] + self.DNA1Sol
                self.DNA2Sol = "-" + self.DNA2Sol
                kolom -= 1
                self.points.append([baris,kolom])
            elif kolom == 1 : 
                self.route.append("U")
                self.DNA1Sol = "-" + self.DNA1Sol
                self.DNA2Sol = self.DNA2[baris-2] + self.DNA2Sol
                baris -= 1
                self.points.append([baris,kolom])
            else :
                if self.DNA2[baris-2] == self.DNA1[kolom-2]:
                    self.route.append("M")
                    self.DNA1Sol = self.DNA1[kolom-2] + self.DNA1Sol
                    self.DNA2Sol = self.DNA2[baris-2] + self.DNA2Sol
                    baris -= 1
                    kolom -= 1
                    self.points.append([baris,kolom])
                else :
                    if (self.matrix[baris-1][kolom-1] >= self.matrix[baris][kolom-1]) and (self.matrix[baris-1][kolom-1] >= self.matrix[baris-1][kolom]):
                        self.route.append("D")
                        baris -= 1
                        kolom -= 1
                        self.DNA2Sol = "-" + self.DNA2Sol
                        self.DNA1Sol = "-" + self.DNA1Sol
                        self.points2.append([baris,kolom])
                    elif (self.matrix[baris-1][kolom-1] <= self.matrix[baris][kolom-1]) and (self.matrix[baris][kolom-1] >= self.matrix[baris-1][kolom]):
                        self.route.append("L")
                        self.DNA1Sol = self.DNA1[kolom-2] + self.DNA1Sol
                        self.DNA2Sol = "-" + self.DNA2Sol
                        kolom -= 1
                        self.points.append([baris,kolom])
                    else :
                        self.route.append("U")
                        self.DNA1Sol = "-" + self.DNA1Sol
                        self.DNA2Sol = self.DNA2[baris-2] + self.DNA2Sol
                        baris -= 1
                        self.points.append([baris,kolom])

        # Menyusun solusi keselarasan optimal
        for i in range (len(self.DNA1Sol)) :
            if self.DNA1Sol[i] != "-" and self.DNA2Sol[i] != "-":
                if self.DNA1Sol[i] == self.DNA2Sol[i]:
                    self.sol += self.DNA1Sol[i]
                else:
                    self.sol += "(" + "" + self.DNA1Sol[i] + "|" + self.DNA2Sol[i] + ")"

        #print(self.route, "\n", self.DNA1Sol, "\n", self.DNA2Sol)

    def reset(self):
        self.sol = ""
        self.DNA1Sol = ""
        self.DNA2Sol = ""
        self.matrix.clear()
        self.route.clear()
        self.points.clear()
        self.points2.clear()

    def needlemanWunsch(self):
        t = time.time()
        self.reset()
        self.createMatrix()
        self.traceback()
        self.runtime = (time.time() - t)*1000 # DALAM MILISEKON

    def displayMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=" ")
            print()
        print("Route", self.route)

    def setDNA(self,path1,path2) :
        if os.path.isfile(path1) and os.path.isfile(path2) :
            with open(path1, "r") as f :
                self.DNA1 = f.read()
            with open(path2, "r") as f :
                self.DNA2 = f.read()


