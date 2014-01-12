#!/usr/bin/env python3


from accentuation import recessive, oxytone, paroxytone, perispomenon, properispomenon
from syllabify import is_vowel, syllabify


def make_oxytone(w): return oxytone(syllabify(w))[0]
def make_paroxytone(w): return paroxytone(syllabify(w))[0]
def make_perispomenon(w): return perispomenon(syllabify(w))[0]
def make_properispomenon(w): return properispomenon(syllabify(w))[0]


def phon(w):
    w = w.replace("ά+ω", "ῶ")
    w = w.replace("α+ώ", "ώ")

    w = w.replace("ά+ῃ", "ᾷ")

    w = w.replace("ά+η", "ᾶ")

    w = w.replace("ά+ε+ι", "ᾷ")
    w = w.replace("ά+ει", "ᾶ")

    w = w.replace("ά+ε", "ᾶ")
    w = w.replace("α+έ", "ά")
    w = w.replace("α+ε", "α")

    w = w.replace("ά+οι", "ῷ")
    w = w.replace("α+οί", "ῴ")
    w = w.replace("α+οι", "ῳ")
    w = w.replace("ά+ου", "ῶ")

    w = w.replace("ᾶ+ο", "ῶ")
    w = w.replace("ά+ο", "ῶ")
    w = w.replace("α+ό", "ώ")
    w = w.replace("α+ο", "ω")

    w = w.replace("ε+ι", "ει")

    return w


class Endings:

    def __init__(self, stem):
        self.stem = stem


class Endings1(Endings):

    def _1S(self): return phon(recessive(self.stem + "ω"))
    def _2S(self): return phon(recessive(self.stem + "ε+ις"))
    def _3S(self): return phon(recessive(self.stem + "ε+ι"))
    def _1P(self): return phon(recessive(self.stem + "ο" + "μεν"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "τε"))
    def _3P(self): return phon(recessive(self.stem + "ου" + "σι(ν)"))


class Endings3(Endings):

    def _1S(self): return phon(recessive(self.stem + "ον"))
    def _2S(self): return phon(recessive(self.stem + "ε" + "ς"))
    def _3S(self): return phon(recessive(self.stem + "ε"))
    def _1P(self): return phon(recessive(self.stem + "ο" + "μεν"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "τε"))
    def _3P(self): return phon(recessive(self.stem + "ο" + "ν"))


class Endings5(Endings):

    def _1S(self): return recessive(self.stem + "α")
    def _2S(self): return recessive(self.stem + "α" + "ς")
    def _3S(self): return recessive(self.stem + "ε")
    def _1P(self): return recessive(self.stem + "α" + "μεν")
    def _2P(self): return recessive(self.stem + "α" + "τε")
    def _3P(self): return recessive(self.stem + "α" + "ν")


class Endings8(Endings5):

    def _3P(self): return recessive(self.stem + "α" + "σι(ν)")


class Endings12(Endings):

    def _1S(self): return phon(recessive(self.stem + "ω"))
    def _2S(self): return phon(recessive(self.stem + "ῃς"))
    def _3S(self): return phon(recessive(self.stem + "ῃ"))
    def _1P(self): return phon(recessive(self.stem + "ω" + "μεν"))
    def _2P(self): return phon(recessive(self.stem + "η" + "τε"))
    def _3P(self): return phon(recessive(self.stem + "ω" + "σι(ν)"))


class Endings14(Endings):

    def _1S(self): return make_perispomenon(self.stem + "ω")
    def _2S(self): return make_perispomenon(self.stem + "ῃς")
    def _3S(self): return make_perispomenon(self.stem + "ῃ")
    def _1P(self): return make_properispomenon(self.stem + "ω" + "μεν")
    def _2P(self): return make_properispomenon(self.stem + "η" + "τε")
    def _3P(self): return make_properispomenon(self.stem + "ω" + "σι(ν)")


class Endings7(Endings):

    def _1S(self): return recessive(self.stem + "ν")
    def _2S(self): return recessive(self.stem + "ς")
    def _3S(self): return recessive(self.stem + "")
    def _1P(self): return recessive(self.stem + "μεν")
    def _2P(self): return recessive(self.stem + "τε")
    def _3P(self): return recessive(self.stem + "σαν")


class Endings10(Endings):

    def _1S(self): return recessive(self.stem + "η")
    def _2S(self): return recessive(self.stem + "ης")
    def _3S(self): return recessive(self.stem + "ει")
    def _1P(self): return recessive(self.stem + "ε" + "μεν")
    def _2P(self): return recessive(self.stem + "ε" + "τε")
    def _3P(self): return recessive(self.stem + "ε" + "σαν")


class Endings9(Endings):

    def _1S(self): return recessive(self.stem + "μαι")
    def _2S(self): return recessive(self.stem + "σαι")
    def _3S(self): return recessive(self.stem + "ται")
    def _1P(self): return recessive(self.stem + "μεθα")
    def _2P(self): return recessive(self.stem + "σθε")
    def _3P(self): return recessive(self.stem + "νται")


class Endings2(Endings):

    def _1S(self): return phon(recessive(self.stem + "ο" + "μαι"))
    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "ε+ι")), # ε + σαι
                          phon(recessive(self.stem + "ῃ"))   # ε + σαι
    )
    def _3S(self): return phon(recessive(self.stem + "ε" + "ται"))
    def _1P(self): return phon(recessive(self.stem + "ο" + "μεθα"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "ο" + "νται"))


class Endings2B(Endings2):

    def _2S(self): return phon(recessive(self.stem + "ε+ι")) # ε + σαι


class Endings13(Endings):

    def _1S(self): return phon(recessive(self.stem + "ω" + "μαι"))
    def _2S(self): return phon(recessive(self.stem + "ῃ"))
    def _3S(self): return phon(recessive(self.stem + "η" + "ται"))
    def _1P(self): return phon(recessive(self.stem + "ω" + "μεθα"))
    def _2P(self): return phon(recessive(self.stem + "η" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "ω" + "νται"))


class Endings11(Endings):

    def _1S(self): return recessive(self.stem + "μην")
    def _2S(self): return recessive(self.stem + "σο")
    def _3S(self): return recessive(self.stem + "το")
    def _1P(self): return recessive(self.stem + "μεθα")
    def _2P(self): return recessive(self.stem + "σθε")
    def _3P(self): return recessive(self.stem + "ντο")


class Endings4(Endings):

    def _1S(self): return phon(recessive(self.stem + "ο" + "μην"))
    def _2S(self): return phon(recessive(self.stem + "ου")) # ε + σο
    def _3S(self): return phon(recessive(self.stem + "ε" + "το"))
    def _1P(self): return phon(recessive(self.stem + "ο" + "μεθα"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "ο" + "ντο"))


class Endings6(Endings):

    def _1S(self): return recessive(self.stem + "α" + "μην")
    def _2S(self): return recessive(self.stem + "ω") # α + σο
    def _3S(self): return recessive(self.stem + "α" + "το")
    def _1P(self): return recessive(self.stem + "α" + "μεθα")
    def _2P(self): return recessive(self.stem + "α" + "σθε")
    def _3P(self): return recessive(self.stem + "α" + "ντο")


class Endings15(Endings):

    def _1S(self): return phon(recessive(self.stem + "οι" + "μι"))
    def _2S(self): return recessive(self.stem + "οι" + "ς")
    def _3S(self): return make_paroxytone(self.stem + "οι" + "")
    def _1P(self): return recessive(self.stem + "οι" + "μεν")
    def _2P(self): return recessive(self.stem + "οι" + "τε")
    def _3P(self): return recessive(self.stem + "οι" + "εν")


class Endings15B(Endings15):

    def _1S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "ην")),
                          phon(recessive(self.stem + "οι" + "μι")),
    )
    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "ης")),
                          phon(recessive(self.stem + "οι" + "ς")),
    )
    def _3S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "η")),
                          phon(make_paroxytone(self.stem + "οι" + "")),
    )
    def _1P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "μεν")),
                          phon(recessive(self.stem + "οι" + "ημεν")),
    )
    def _2P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "τε")),
                          phon(recessive(self.stem + "οι" + "ητε")),
    )
    def _3P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "οι" + "εν")),
                          phon(recessive(self.stem + "οι" + "ησαν")),
    )


class Endings17(Endings):

    def _1S(self): return recessive(self.stem + "αι" + "μι")
    def _2S(self): return "{}/{}".format(
                          recessive(self.stem + "αι" + "ς"),
                          recessive(self.stem + "ει" + "ας"),
    )
    def _3S(self): return "{}/{}".format(
                          make_paroxytone(self.stem + "αι" + ""),
                          recessive(self.stem + "ει" + "ε"),
    )
    def _1P(self): return recessive(self.stem + "αι" + "μεν")
    def _2P(self): return recessive(self.stem + "αι" + "τε")
    def _3P(self): return "{}/{}".format(
                          recessive(self.stem + "αι" + "εν"),
                          recessive(self.stem + "ει" + "αν"),
    )


class Endings16(Endings):

    def _1S(self): return phon(recessive(self.stem + "οι" + "μην"))
    def _2S(self): return phon(recessive(self.stem + "οι" + "ο"))
    def _3S(self): return phon(recessive(self.stem + "οι" + "το"))
    def _1P(self): return phon(recessive(self.stem + "οι" + "μεθα"))
    def _2P(self): return phon(recessive(self.stem + "οι" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "οι" + "ντο"))


class Endings18(Endings):

    def _1S(self): return recessive(self.stem + "αι" + "μην")
    def _2S(self): return recessive(self.stem + "αι" + "ο")
    def _3S(self): return recessive(self.stem + "αι" + "το")
    def _1P(self): return recessive(self.stem + "αι" + "μεθα")
    def _2P(self): return recessive(self.stem + "αι" + "σθε")
    def _3P(self): return recessive(self.stem + "αι" + "ντο")


class Endings19(Endings):

    def _1S(self): return recessive(self.stem + "ειη" + "ν")
    def _2S(self): return recessive(self.stem + "ειη" + "ς")
    def _3S(self): return recessive(self.stem + "ειη" + "")
    def _1P(self): return "{}/{}".format(
                          make_properispomenon(self.stem + "ει" + "μεν"),
                          recessive(self.stem + "ειη" + "μεν"),
    )
    def _2P(self): return "{}/{}".format(
                          make_properispomenon(self.stem + "ει" + "τε"),
                          recessive(self.stem + "ειη" + "τε"),
    )
    def _3P(self): return "{}/{}".format(
                          make_properispomenon(self.stem + "ει" + "εν"),
                          recessive(self.stem + "ειη" + "σαν"),
    )


class Endings20(Endings):

    def _2S(self): return phon(recessive(self.stem + "ε"))
    def _3S(self): return phon(recessive(self.stem + "ε" + "τω"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "τε"))
    def _3P(self): return phon(recessive(self.stem + "ο" + "ντων"))


class Endings22(Endings):

    def _2S(self): return recessive(self.stem + "ον")
    def _3S(self): return recessive(self.stem + "α" + "τω")
    def _2P(self): return recessive(self.stem + "α" + "τε")
    def _3P(self): return recessive(self.stem + "α" + "ντων")


class Endings24(Endings):

    def _2S(self): return recessive(self.stem + "η" + "τι")
    def _3S(self): return recessive(self.stem + "η" + "τω")
    def _2P(self): return recessive(self.stem + "η" + "τε")
    def _3P(self): return recessive(self.stem + "ε" + "ντων")


class Endings21(Endings):

    def _2S(self): return phon(recessive(self.stem + "ου"))
    def _3S(self): return phon(recessive(self.stem + "ε" + "σθω"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "ε" + "σθων"))


class Endings23(Endings):

    def _2S(self): return recessive(self.stem + "αι")
    def _3S(self): return recessive(self.stem + "α" + "σθω")
    def _2P(self): return recessive(self.stem + "α" + "σθε")
    def _3P(self): return recessive(self.stem + "α" + "σθων")


class Endings25(Endings):

    def _2S(self): return recessive(self.stem + "σο")
    def _3S(self): return recessive(self.stem + "σθω")
    def _2P(self): return recessive(self.stem + "σθε")
    def _3P(self): return recessive(self.stem + "σθων")


class Endings26(Endings):

    def NSM(self): return phon(recessive(self.stem + "ων"))
    def NSF(self): return phon(recessive(self.stem + "ουσα"))
    def NSN(self): return phon(make_properispomenon(self.stem + "ον"))


class Endings28(Endings):

    def NSM(self): return make_paroxytone(self.stem + "ας")
    def NSF(self): return recessive(self.stem + "ασα")
    def NSN(self): return recessive(self.stem + "αν")


class Endings30(Endings):

    def NSM(self): return make_oxytone(self.stem + "εις")
    def NSF(self): return make_properispomenon(self.stem + "εισα")
    def NSN(self): return make_oxytone(self.stem + "εν")


class Endings32(Endings):

    def NSM(self): return make_paroxytone(self.stem + "μενος")
    def NSF(self): return recessive(self.stem + "μενη")
    def NSN(self): return make_paroxytone(self.stem + "μενον")


class Endings27(Endings):

    def NSM(self): return phon(recessive(self.stem + "ο" + "μενος"))
    def NSF(self): return phon(recessive(self.stem + "ο" + "μενη"))
    def NSN(self): return phon(recessive(self.stem + "ο" + "μενον"))


class Endings29(Endings):

    def NSM(self): return recessive(self.stem + "α" + "μενος")
    def NSF(self): return recessive(self.stem + "α" + "μενη")
    def NSN(self): return recessive(self.stem + "α" + "μενον")


class Endings31(Endings):

    def NSM(self): return make_oxytone(self.stem + "ως")
    def NSF(self): return make_properispomenon(self.stem + "υια")
    def NSN(self): return make_oxytone(self.stem + "ος")


class Verb1:

    def PAI(self): return Endings1(self.stem1)
    def PMI(self): return Endings2(self.stem1)
    def IAI(self): return Endings3("ἐ" + self.stem1)
    def IMI(self): return Endings4("ἐ" + self.stem1)
    def FAI(self): return Endings1(self.stem1 + "σ")
    def FMI(self): return Endings2(self.stem1 + "σ")
    def FPI(self): return Endings2(self.stem1 + "θη" + "σ")
    def AAI(self): return Endings5("ἐ" + self.stem1 + "σ")
    def AMI(self): return Endings6("ἐ" + self.stem1 + "σ")
    def API(self): return Endings7("ἐ" + self.stem1 + "θη")
    def XAI(self): return Endings8(redup(self.stem1) + "κ")
    def XMI(self): return Endings9(redup(self.stem1))
    def YAI(self): return Endings10("ἐ" + redup(self.stem1) + "κ")
    def YMI(self): return Endings11("ἐ" + redup(self.stem1))

    def PAS(self): return Endings12(self.stem1)
    def PMS(self): return Endings13(self.stem1)
    def AAS(self): return Endings12(self.stem1 + "σ")
    def AMS(self): return Endings13(self.stem1 + "σ")
    def APS(self): return Endings14(self.stem1 + "θ")
    def XAS(self): return Endings12(redup(self.stem1) + "κ")

    def PAO(self): return Endings15(self.stem1)
    def PMO(self): return Endings16(self.stem1)
    def FAO(self): return Endings15(self.stem1 + "σ")
    def FMO(self): return Endings16(self.stem1 + "σ")
    def FPO(self): return Endings16(self.stem1 + "θη" + "σ")
    def AAO(self): return Endings17(self.stem1 + "σ")
    def AMO(self): return Endings18(self.stem1 + "σ")
    def APO(self): return Endings19(self.stem1 + "θ")
    def XAO(self): return Endings15(redup(self.stem1) + "κ")

    def PAD(self): return Endings20(self.stem1)
    def PMD(self): return Endings21(self.stem1)
    def AAD(self): return Endings22(self.stem1 + "σ")
    def AMD(self): return Endings23(self.stem1 + "σ")
    def APD(self): return Endings24(self.stem1 + "θ")
    def XMD(self): return Endings25(redup(self.stem1))

    def PAN(self): return phon(recessive(self.stem1 + "ειν"))
    def PMN(self): return phon(recessive(self.stem1 + "εσθαι"))
    def FAN(self): return recessive(self.stem1 + "σ" + "ειν")
    def FMN(self): return recessive(self.stem1 + "σ" + "ε" + "σθαι")
    def FPN(self): return recessive(self.stem1 + "θη" + "σ" + "ε" + "σθαι")
    def AAN(self): return recessive(self.stem1 + "σαι")
    def AMN(self): return recessive(self.stem1 + "σ" + "α" + "σθαι")
    def APN(self): return make_properispomenon(self.stem1 + "θη" + "ναι")
    def XAN(self): return make_paroxytone(redup(self.stem1) + "κ" + "ε" + "ναι")
    def XMN(self): return make_paroxytone(redup(self.stem1) + "σθαι")

    def PAP(self): return Endings26(self.stem1)
    def PMP(self): return Endings27(self.stem1)
    def FAP(self): return Endings26(self.stem1 + "σ")
    def FMP(self): return Endings27(self.stem1 + "σ")
    def FPP(self): return Endings27(self.stem1 + "θησ")
    def AAP(self): return Endings28(self.stem1 + "σ")
    def AMP(self): return Endings29(self.stem1 + "σ")
    def APP(self): return Endings30(self.stem1 + "θ")
    def XAP(self): return Endings31(redup(self.stem1) + "κ")
    def XMP(self): return Endings32(redup(self.stem1))


class Verb1B(Verb1):

    def PMI(self): return Endings2B(self.stem1)
    def PAO(self): return Endings15B(self.stem1)


def redup(stem):
    if is_vowel(stem[0]):
        raise NotImplemented()
    else:
        return stem[0] + "ε" + stem


class LUW(Verb1):

    stem1 = "λυ"


class TIMAW(Verb1B):

    stem1 = "τιμα+"


if __name__ == "__main__":

    VERBS = {
        "λύω": LUW(),
        "τιμῶ": TIMAW(),
    }

    passed = 0
    fails = []
    with open("test.txt") as f:
        for line in f:
            record = line.strip().split("#")[0]
            if not record:
                continue
            lemma, parse, form = record.split()
            c = VERBS[lemma]
            for step in parse.split("."):
                if step[0] in "123":
                    step = "_" + step
                c = getattr(c, step)()
            if c == form:
                passed += 1
            else:
                fails.append("{} != {}".format(record, c))

    print("{} passed".format(passed))
    if fails:
        print("{} failed".format(len(fails)))
        print(fails[0])
