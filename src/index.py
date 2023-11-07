from varasto import Varasto

def mehuvaraston_tila(mehua):
    print(f"Mehuvarasto: {mehua}")

def olutvaraston_tila(olutta):
    print(f"Olutvarasto: {olutta}")

def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setteri(mehua):
    print("Mehu setterit:")
    lisaa_mehua(50.7, mehua)
    otetaan_mehua(3.14, mehua)

def lisaa_mehua(maara, mehua):
    print(f"Lisätään {maara}")
    mehua.lisaa_varastoon(maara)
    mehuvaraston_tila(mehua)

def otetaan_mehua(maara, mehua):
    mehuvaraston_tila(mehua)
    print(f"mehua.otaVarastosta({maara})")
    saatiin = mehua.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    mehuvaraston_tila(mehua)

def lisaa_olutta(maara, olutta):
    olutvaraston_tila(olutta)
    print(f"olutta.lisaa_varastoon({maara})")
    olutta.lisaa_varastoon(maara)
    olutvaraston_tila(olutta)

def otetaan_olutta(maara, olutta):
    print(f"olutta.ota_varastosta({maara})")
    saatiin = olutta.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    olutvaraston_tila(olutta)

def virhetilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    mehuvaraston_tila(mehua)
    olutvaraston_tila(olutta)

    olut_getterit(olutta)
    mehu_setteri(mehua)

    virhetilanteita()

    lisaa_olutta(1000.0, olutta)

    mehuvaraston_tila(mehua)
    lisaa_mehua(-666.0, mehua)

    olutvaraston_tila(olutta)
    otetaan_olutta(1000.0, olutta)

    otetaan_mehua(-32.9, mehua)

if __name__ == "__main__":
    main()
