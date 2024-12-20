from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:\n"
          f"Mehuvarasto: {mehua}\n"
          f"Olutvarasto: {olutta}\n")

    print("Olut getterit:\n"
          f"saldo = {olutta.saldo}\n"
          f"tilavuus = {olutta.tilavuus}\n"
          f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n")

    print("Mehu setterit:\n"
          "Lisätään 50.7\n"
          f"Mehuvarasto: {mehua}\n"
          "Otetaan 3.14\n"
          f"Mehuvarasto: {mehua}\n")

    print("Virhetilanteita:\n"
          "Varasto(-100.0);\n"
          f"{Varasto(-100.0)}\n"
          "Varasto(100.0, -50.7)\n"
          f"{Varasto(100.0, -50.7)}\n")

    print(f"Olutvarasto: {olutta}\n"
          "olutta.lisaa_varastoon(1000.0)\n"
          f"Olutvarasto: {olutta}\n")

    print(f"Mehuvarasto: {mehua}\n"
          "mehua.lisaa_varastoon(-666.0)\n"
          f"Mehuvarasto: {mehua}\n")

    print(f"Olutvarasto: {olutta}\n"
          "olutta.ota_varastosta(1000.0)\n"
          f"saatiin {olutta.ota_varastosta(1000.0)}\n"
          f"Olutvarasto: {olutta}\n")

    print(f"Mehuvarasto: {mehua}\n"
          "mehua.otaVarastosta(-32.9)\n"
          f"saatiin {mehua.ota_varastosta(-32.9)}\n"
          f"Mehuvarasto: {mehua}\n")


if __name__ == "__main__":
    main()
