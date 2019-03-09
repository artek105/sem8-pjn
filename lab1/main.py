from lab1.ngrams import NGrams, norm
from lab1.langhelper import languages
from lab1.base import get_base_n_grams


def main():
    n = 3
    test = NGrams(n)

    # eng
    # test.fit_by_text("Incitement garden access take copied back services commit returning calling organisation successful. Submitted rights available will considerable causing your at night don't other although. Learners Do See shouted shivering you. It's 13 sees utterly once still there. Third copyright an people strictly certain use lot. You council groups seconds rose should thought teens comments. Guess little removed first comment state. These developed non-exclusive so they're shorthand shorthand protection. Mind herself beetle mobile age rose sublicenseable point authorities copyright. Were wasn't was you i've. Specific warranty submission his house first play act believe. Oriented your internet users gave doctor's costs term mind designed.")
    # fin
    # test.fit_by_text("Puhua litra nakyi tulee kai vie loi usvaa viina ela. Leikki kahvia siella paljon ei tapaan toivon on no. Ne punainen en ne vallassa jaanytta et. Lie paljon oli naemme saahan han nyt. Ilkesi joutuu jattaa ryhtya nae saassa eri talvet iso vai. On entisista moottorin jalkaansa ai ei semmoiset. ")
    # ger
    # test.fit_by_text("Gro sudwesten viehmarkt weg sah stadtchen schnupfen. Sauber mit morgen weg frauen ihm. Ein klimperte vermodert polemisch unendlich schnupfen schleiche des ihm sie. Spiel sahen das fur viele sonst leben leuen. Pa vermodert schwemmen gegenteil wo zerfasert. Wunderbar in schwemmen grundlich belustigt turnhalle im behaglich. Ihre hell paar froh kerl weg man buch. Dienstmagd regungslos sonderling gib ungerechte ein besonderes auf der. Anrufen em instand nachdem kindern meister mu niemand am da. Gewandert schwachen man schlupfte wie geschickt ich sog. ")
    # it
    # test.fit_by_text("Annunziare comunicare al di cancellato padronanza meraviglia lo. Noi abbassando irrequieto conoscermi calpestare ricordarmi poi improvvisa. Immensita rarissima udi pel impedisce nei esemplare sai. Puo pei accompagna chi declinante ali lineamento. Esitanza facilita orgoglio ape cui noi obbedito tuttavia. Ed baciocchi concedono melagrani io tu te guanciale. Mi questa vedrai tu questo patito veduta vicino. Mille siete donna chino mia tutta ape manda due. Scioglie il torrente serbatoi ma so tempesta vivevano volgendo. ")
    # pl
    test.fit_by_text("Doktor Judym przebywa od ponad roku w Paryżu. Odbywa tutaj swoją praktykę chirurgiczną. Ogarnia go melancholia, czegoś mu brak, ale nie potrafi powiedzieć czego. Chętnie spaceruje ulicami miasta. Pewnego dnia, podczas wizyty w Luwrze i kontemplowaniu urody posągu Wenus z Milo, Judym słyszy rozmowę prowadzoną w języku polskim. Poznaje trzy dziewczęta oraz ich opiekunkę – panią Niewadzką. Panny to Wanda i Natalia Orszeńskie oraz ich guwernantka, Joasia Podborska.")
    # sp
    # test.fit_by_text("Ganado correo operas cuerpo sirvio la manera lo es. En lacrimoso pelagatos insomnios ha ti expresion el. Que rapidisimo caballeros escopetazo exclamaron don son forasteros amabilidad los. Dias gr hago lema baja toco moza eh en. Dos corrian iba declaro sentido nos exigian pre ceguera. Cogio rio sus hay angel senas sabra feo arena. Explico pistola cuantos fuertes mal muy pequeno andando. Esposo evitar crespo es ya esposa al cuerda. ")

    for lang in languages:
        n_grams = get_base_n_grams(lang, n)
        print(lang, norm(n_grams, test))


if __name__ == '__main__':
    main()
