from verbs import (
    Verb1, Verb1B, Verb1C,
    Verb2, Verb2B, Verb2C, Verb2D, Verb2E,
)


class LUW(Verb1):

    stem1 = "λυ+"


class TIMAW(Verb1B):

    stem1 = "τιμα"


class POIEW(Verb1C):

    stem1 = "ποιε"


class DHLOW(Verb1B):

    stem1 = "δηλο"


class DIDWMI(Verb2):

    stem1 = "διδο"
    stem2 = "δο"


class TIQHMI(Verb2B):

    stem1 = "τιθε"
    stem2 = "θε"


class hIHMI(Verb2C):

    stem1 = "ἱε"
    stem2 = "ἑ"


class hISTHMI(Verb2D):

    stem1 = "ἱστα"
    stem2 = "στα"


class DEIKNUMI(Verb2E):

    stem1 = "δεικνυ"


class GIGNWSKW(Verb2D):

    stem2 = "γνο"


VERBS = {
    "λύω": LUW,
    "τιμῶ": TIMAW,
    "ποιῶ": POIEW,
    "δηλῶ": DHLOW,
    "δίδωμι": DIDWMI,
    "τίθημι": TIQHMI,
    "ἵημι": hIHMI,
    "ἵστημι": hISTHMI,
    "δείκνυμι": DEIKNUMI,
    "γιγνώσκω": GIGNWSKW,
}
