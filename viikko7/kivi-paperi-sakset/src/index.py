from kps_moodit import hae_moodi

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\n (d) Näytösottelu"
              "\nMuilla valinnoilla lopetetaan"
              )

        peli = hae_moodi(
            input()
        )

        if peli is not None:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
