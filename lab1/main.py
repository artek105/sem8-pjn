from lab1.ngrams import NGrams, norm
from lab1.langhelper import languages
from lab1.base import get_base_n_grams


def main():
    n = 3
    # test_single(n)
    stats(n)


def test_single(n):
    test = NGrams(n)

    # eng
    # test.apply_text("Incitement garden access take copied back services commit returning calling organisation successful. Submitted rights available will considerable causing your at night don't other although. Learners Do See shouted shivering you. It's 13 sees utterly once still there. Third copyright an people strictly certain use lot. You council groups seconds rose should thought teens comments. Guess little removed first comment state. These developed non-exclusive so they're shorthand shorthand protection. Mind herself beetle mobile age rose sublicenseable point authorities copyright. Were wasn't was you i've. Specific warranty submission his house first play act believe. Oriented your internet users gave doctor's costs term mind designed.")
    # fin
    # test.apply_text("Puhua litra nakyi tulee kai vie loi usvaa viina ela. Leikki kahvia siella paljon ei tapaan toivon on no. Ne punainen en ne vallassa jaanytta et. Lie paljon oli naemme saahan han nyt. Ilkesi joutuu jattaa ryhtya nae saassa eri talvet iso vai. On entisista moottorin jalkaansa ai ei semmoiset. ")
    # ger
    # test.apply_text("Gro sudwesten viehmarkt weg sah stadtchen schnupfen. Sauber mit morgen weg frauen ihm. Ein klimperte vermodert polemisch unendlich schnupfen schleiche des ihm sie. Spiel sahen das fur viele sonst leben leuen. Pa vermodert schwemmen gegenteil wo zerfasert. Wunderbar in schwemmen grundlich belustigt turnhalle im behaglich. Ihre hell paar froh kerl weg man buch. Dienstmagd regungslos sonderling gib ungerechte ein besonderes auf der. Anrufen em instand nachdem kindern meister mu niemand am da. Gewandert schwachen man schlupfte wie geschickt ich sog. ")
    # it
    # test.apply_text("Annunziare comunicare al di cancellato padronanza meraviglia lo. Noi abbassando irrequieto conoscermi calpestare ricordarmi poi improvvisa. Immensita rarissima udi pel impedisce nei esemplare sai. Puo pei accompagna chi declinante ali lineamento. Esitanza facilita orgoglio ape cui noi obbedito tuttavia. Ed baciocchi concedono melagrani io tu te guanciale. Mi questa vedrai tu questo patito veduta vicino. Mille siete donna chino mia tutta ape manda due. Scioglie il torrente serbatoi ma so tempesta vivevano volgendo. ")
    # pl
    test.apply_text("Doktor Judym przebywa od ponad roku w Paryżu. Odbywa tutaj swoją praktykę chirurgiczną. Ogarnia go melancholia, czegoś mu brak, ale nie potrafi powiedzieć czego. Chętnie spaceruje ulicami miasta. Pewnego dnia, podczas wizyty w Luwrze i kontemplowaniu urody posągu Wenus z Milo, Judym słyszy rozmowę prowadzoną w języku polskim. Poznaje trzy dziewczęta oraz ich opiekunkę – panią Niewadzką. Panny to Wanda i Natalia Orszeńskie oraz ich guwernantka, Joasia Podborska.")
    # sp
    # test.apply_text("Asomaban hermanas me la encender me caudillo. Da el vivos sufre oh jamas. Ha la octavillas particular alambicado oh. Echo ti va sepa solo de gr. Mi gr si dislocado despierta tendencia ir acercarla. Eh pasable si yo tardaba quedaba armonia guanajo intenso. Mil correrias hay esperanza mas mostrador animacion oyo. Catadura perezoso ya alquiler ha ni. En de inaudito quedaban superior ingresar un hubieran volviera. Oro opto fosa ser tios alto. ")

    lang = resolve_lang(test, True)
    print('Resolved lang: ', lang)


def resolve_lang(n_grams, debug=False):
    min_norm = 1
    min_norm_lang = None
    for lang in languages:
        lang_n_grams = get_base_n_grams(lang, n_grams.n)
        norm_val = norm(n_grams, lang_n_grams)

        if norm_val < min_norm:
            min_norm = norm_val
            min_norm_lang = lang

        if debug:
            print(lang, norm_val)

    return min_norm_lang


boundaries = {
    1: 0.04,
    2: 0.275,
    3: 0.65,
    4: 0.875,
}


def stats(n):
    for lang in languages:
        # to calculate recall and precision for all classes move this out of first loop
        true_positive = true_negative = false_positive = false_negative = 0

        n_grams = get_base_n_grams(lang, n)
        for test_lang in languages:
            with open('examples/' + test_lang + '.txt', mode='r', encoding='utf-8') as file:
                for line in file:
                    # filter empty lines
                    line = line.replace('\n', ' ').strip()
                    if not line:
                        continue

                    test = NGrams(n)
                    test.apply_text(line)

                    norm_val = norm(n_grams, test)
                    boundary = boundaries[n] if boundaries[n] is not None else 1
                    predicted_same_lang = norm_val <= boundary

                    if lang == test_lang and predicted_same_lang:
                        true_positive += 1

                    if lang != test_lang and not predicted_same_lang:
                        true_negative += 1

                    if lang != test_lang and predicted_same_lang:
                        false_positive += 1

                    if lang == test_lang and not predicted_same_lang:
                        false_negative += 1

        # to calculate recall and precision for all classes move this out of first loop
        print('\t' + lang)
        print_stats(true_positive, false_positive, false_negative, true_negative)


def print_stats(true_positive, false_positive, false_negative, true_negative):
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)

    print('precision\t', precision)
    print('recall\t\t', recall)
    print('accuracy\t', accuracy)


if __name__ == '__main__':
    main()
