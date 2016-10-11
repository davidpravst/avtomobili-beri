# -*- coding: utf-8 -*-

class Avto():
    znamka = ""
    model = ""
    barva = ""

    def nastavi_znamko(self, znamka):
        self.znamka = znamka

    def nastavi_model(self, model):
        self.model = model

    def nastavi_barvo(self, barva):
        self.barva = barva

    def izpisi_vse(self):
        print self.znamka + "; " + self.model + "; " + self.barva

avto = Avto()
podpicje_count = 0
beseda = ""
avtomobili_list = []

with open("avtomobili.txt", "r") as avtomobili_file:
    vrstica = avtomobili_file.readlines()
    for x in vrstica:
        for crka in x:
            if crka == ";":
                podpicje_count = podpicje_count + 1
                if podpicje_count == 1:
                    avto.nastavi_znamko(beseda)
                    beseda = ""
                else:
                    avto.nastavi_model(beseda)
                    beseda = ""
                    podpicje_count = 0
            elif crka == "\n":
                avto.nastavi_barvo(beseda)
                beseda = ""
            elif crka == " ":
                pass
            else:
                beseda = beseda + crka
        avtomobili_list.append(avto)
        avto = Avto() #tole resetira spremenljivko, da pravilno doda objekt v seznam, drugače je štala

for x in avtomobili_list:
    x.izpisi_vse()
