#!/usr/bin/env python3


from accentuation import recessive, oxytone, paroxytone, perispomenon, properispomenon
from syllabify import is_vowel, syllabify


def make_oxytone(w): return oxytone(syllabify(w))[0]
def make_paroxytone(w): return paroxytone(syllabify(w))[0]
def make_perispomenon(w): return perispomenon(syllabify(w))[0]
def make_properispomenon(w): return properispomenon(syllabify(w))[0]


def phon(w):
    w = w.replace("ά+ω", "ῶ")

    w = w.replace("ά+ει", "ᾷ")

    w = w.replace("ά+ε", "ᾶ")
    w = w.replace("α+έ", "ά")
    w = w.replace("α+ε", "α")

    w = w.replace("ά+ου", "ῶ")

    w = w.replace("ά+ο", "ῶ")
    w = w.replace("α+ό", "ώ")
    w = w.replace("α+ο", "ω")

    return w


class Endings:

    def __init__(self, stem):
        self.stem = stem


class Endings1(Endings):

    def _1S(self): return phon(recessive(self.stem + "ω"))
    def _2S(self): return phon(recessive(self.stem + "εις"))
    def _3S(self): return phon(recessive(self.stem + "ει"))
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

    def _1S(self): return recessive(self.stem + "ω")
    def _2S(self): return recessive(self.stem + "ῃς")
    def _3S(self): return recessive(self.stem + "ῃ")
    def _1P(self): return recessive(self.stem + "ω" + "μεν")
    def _2P(self): return recessive(self.stem + "η" + "τε")
    def _3P(self): return recessive(self.stem + "ω" + "σι(ν)")


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
                          phon(recessive(self.stem + "ει")), # ε + σαι
                          phon(recessive(self.stem + "ῃ"))   # ε + σαι
    )
    def _3S(self): return phon(recessive(self.stem + "ε" + "ται"))
    def _1P(self): return phon(recessive(self.stem + "ο" + "μεθα"))
    def _2P(self): return phon(recessive(self.stem + "ε" + "σθε"))
    def _3P(self): return phon(recessive(self.stem + "ο" + "νται"))


class Endings2B(Endings2):

    def _2S(self): return phon(recessive(self.stem + "ει")) # ε + σαι


class Endings13(Endings):

    def _1S(self): return recessive(self.stem + "ω" + "μαι")
    def _2S(self): return recessive(self.stem + "ῃ")
    def _3S(self): return recessive(self.stem + "η" + "ται")
    def _1P(self): return recessive(self.stem + "ω" + "μεθα")
    def _2P(self): return recessive(self.stem + "η" + "σθε")
    def _3P(self): return recessive(self.stem + "ω" + "νται")


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

    def _1S(self): return recessive(self.stem + "οι" + "μι")
    def _2S(self): return make_paroxytone(self.stem + "οι" + "ς")
    def _3S(self): return make_paroxytone(self.stem + "οι" + "")
    def _1P(self): return recessive(self.stem + "οι" + "μεν")
    def _2P(self): return recessive(self.stem + "οι" + "τε")
    def _3P(self): return recessive(self.stem + "οι" + "εν")


class Endings17(Endings):

    def _1S(self): return recessive(self.stem + "αι" + "μι")
    def _2S(self): return "{}/{}".format(
                          make_paroxytone(self.stem + "αι" + "ς"),
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

    def _1S(self): return recessive(self.stem + "οι" + "μην")
    def _2S(self): return recessive(self.stem + "οι" + "ο")
    def _3S(self): return recessive(self.stem + "οι" + "το")
    def _1P(self): return recessive(self.stem + "οι" + "μεθα")
    def _2P(self): return recessive(self.stem + "οι" + "σθε")
    def _3P(self): return recessive(self.stem + "οι" + "ντο")


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

    def _2S(self): return recessive(self.stem + "ε")
    def _3S(self): return recessive(self.stem + "ε" + "τω")
    def _2P(self): return recessive(self.stem + "ε" + "τε")
    def _3P(self): return recessive(self.stem + "ο" + "ντων")


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

    def _2S(self): return recessive(self.stem + "ου")
    def _3S(self): return recessive(self.stem + "ε" + "σθω")
    def _2P(self): return recessive(self.stem + "ε" + "σθε")
    def _3P(self): return recessive(self.stem + "ε" + "σθων")


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

    def NSM(self): return recessive(self.stem + "ων")
    def NSF(self): return recessive(self.stem + "ουσα")
    def NSN(self): return recessive(self.stem + "ον")


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

    def NSM(self): return recessive(self.stem + "ο" + "μενος")
    def NSF(self): return recessive(self.stem + "ο" + "μενη")
    def NSN(self): return recessive(self.stem + "ο" + "μενον")


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

    def PAN(self): return recessive(self.stem1 + "ειν")
    def PMN(self): return recessive(self.stem1 + "εσθαι")
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
    luw = LUW()

    assert luw.PAI()._1S() == "λύω"
    assert luw.PAI()._2S() == "λύεις"
    assert luw.PAI()._3S() == "λύει"
    assert luw.PAI()._1P() == "λύομεν"
    assert luw.PAI()._2P() == "λύετε"
    assert luw.PAI()._3P() == "λύουσι(ν)"

    assert luw.PMI()._1S() == "λύομαι"
    assert luw.PMI()._2S() == "λύει/λύῃ"
    assert luw.PMI()._3S() == "λύεται"
    assert luw.PMI()._1P() == "λυόμεθα"
    assert luw.PMI()._2P() == "λύεσθε"
    assert luw.PMI()._3P() == "λύονται"

    assert luw.IAI()._1S() == "ἔλυον"
    assert luw.IAI()._2S() == "ἔλυες"
    assert luw.IAI()._3S() == "ἔλυε"
    assert luw.IAI()._1P() == "ἐλύομεν"
    assert luw.IAI()._2P() == "ἐλύετε"
    assert luw.IAI()._3P() == "ἔλυον"

    assert luw.IMI()._1S() == "ἐλυόμην"
    assert luw.IMI()._2S() == "ἐλύου"
    assert luw.IMI()._3S() == "ἐλύετο"
    assert luw.IMI()._1P() == "ἐλυόμεθα"
    assert luw.IMI()._2P() == "ἐλύεσθε"
    assert luw.IMI()._3P() == "ἐλύοντο"

    assert luw.FAI()._1S() == "λύσω"
    assert luw.FAI()._2S() == "λύσεις"
    assert luw.FAI()._3S() == "λύσει"
    assert luw.FAI()._1P() == "λύσομεν"
    assert luw.FAI()._2P() == "λύσετε"
    assert luw.FAI()._3P() == "λύσουσι(ν)"

    assert luw.FMI()._1S() == "λύσομαι"
    assert luw.FMI()._2S() == "λύσει/λύσῃ"
    assert luw.FMI()._3S() == "λύσεται"
    assert luw.FMI()._1P() == "λυσόμεθα"
    assert luw.FMI()._2P() == "λύσεσθε"
    assert luw.FMI()._3P() == "λύσονται"

    assert luw.FPI()._1S() == "λυθήσομαι"
    assert luw.FPI()._2S() == "λυθήσει/λυθήσῃ"
    assert luw.FPI()._3S() == "λυθήσεται"
    assert luw.FPI()._1P() == "λυθησόμεθα"
    assert luw.FPI()._2P() == "λυθήσεσθε"
    assert luw.FPI()._3P() == "λυθήσονται"

    assert luw.AAI()._1S() == "ἔλυσα"
    assert luw.AAI()._2S() == "ἔλυσας"
    assert luw.AAI()._3S() == "ἔλυσε"
    assert luw.AAI()._1P() == "ἐλύσαμεν"
    assert luw.AAI()._2P() == "ἐλύσατε"
    assert luw.AAI()._3P() == "ἔλυσαν"

    assert luw.AMI()._1S() == "ἐλυσάμην"
    assert luw.AMI()._2S() == "ἐλύσω"
    assert luw.AMI()._3S() == "ἐλύσατο"
    assert luw.AMI()._1P() == "ἐλυσάμεθα"
    assert luw.AMI()._2P() == "ἐλύσασθε"
    assert luw.AMI()._3P() == "ἐλύσαντο"

    assert luw.API()._1S() == "ἐλύθην"
    assert luw.API()._2S() == "ἐλύθης"
    assert luw.API()._3S() == "ἐλύθη"
    assert luw.API()._1P() == "ἐλύθημεν"
    assert luw.API()._2P() == "ἐλύθητε"
    assert luw.API()._3P() == "ἐλύθησαν"

    assert luw.XAI()._1S() == "λέλυκα"
    assert luw.XAI()._2S() == "λέλυκας"
    assert luw.XAI()._3S() == "λέλυκε"
    assert luw.XAI()._1P() == "λελύκαμεν"
    assert luw.XAI()._2P() == "λελύκατε"
    assert luw.XAI()._3P() == "λελύκασι(ν)"

    assert luw.XMI()._1S() == "λέλυμαι"
    assert luw.XMI()._2S() == "λέλυσαι"
    assert luw.XMI()._3S() == "λέλυται"
    assert luw.XMI()._1P() == "λελύμεθα"
    assert luw.XMI()._2P() == "λέλυσθε"
    assert luw.XMI()._3P() == "λέλυνται"

    assert luw.YAI()._1S() == "ἐλελύκη"
    assert luw.YAI()._2S() == "ἐλελύκης"
    assert luw.YAI()._3S() == "ἐλελύκει"
    assert luw.YAI()._1P() == "ἐλελύκεμεν"
    assert luw.YAI()._2P() == "ἐλελύκετε"
    assert luw.YAI()._3P() == "ἐλελύκεσαν"

    assert luw.YMI()._1S() == "ἐλελύμην"
    assert luw.YMI()._2S() == "ἐλέλυσο"
    assert luw.YMI()._3S() == "ἐλέλυτο"
    assert luw.YMI()._1P() == "ἐλελύμεθα"
    assert luw.YMI()._2P() == "ἐλέλυσθε"
    assert luw.YMI()._3P() == "ἐλέλυντο"

    assert luw.PAS()._1S() == "λύω"
    assert luw.PAS()._2S() == "λύῃς"
    assert luw.PAS()._3S() == "λύῃ"
    assert luw.PAS()._1P() == "λύωμεν"
    assert luw.PAS()._2P() == "λύητε"
    assert luw.PAS()._3P() == "λύωσι(ν)"

    assert luw.PMS()._1S() == "λύωμαι"
    assert luw.PMS()._2S() == "λύῃ"
    assert luw.PMS()._3S() == "λύηται"
    assert luw.PMS()._1P() == "λυώμεθα"
    assert luw.PMS()._2P() == "λύησθε"
    assert luw.PMS()._3P() == "λύωνται"

    assert luw.AAS()._1S() == "λύσω"
    assert luw.AAS()._2S() == "λύσῃς"
    assert luw.AAS()._3S() == "λύσῃ"
    assert luw.AAS()._1P() == "λύσωμεν"
    assert luw.AAS()._2P() == "λύσητε"
    assert luw.AAS()._3P() == "λύσωσι(ν)"

    assert luw.AMS()._1S() == "λύσωμαι"
    assert luw.AMS()._2S() == "λύσῃ"
    assert luw.AMS()._3S() == "λύσηται"
    assert luw.AMS()._1P() == "λυσώμεθα"
    assert luw.AMS()._2P() == "λύσησθε"
    assert luw.AMS()._3P() == "λύσωνται"

    assert luw.APS()._1S() == "λυθῶ"
    assert luw.APS()._2S() == "λυθῇς"
    assert luw.APS()._3S() == "λυθῇ"
    assert luw.APS()._1P() == "λυθῶμεν"
    assert luw.APS()._2P() == "λυθῆτε"
    assert luw.APS()._3P() == "λυθῶσι(ν)"

    assert luw.XAS()._1S() == "λελύκω"
    assert luw.XAS()._2S() == "λελύκῃς"
    assert luw.XAS()._3S() == "λελύκῃ"
    assert luw.XAS()._1P() == "λελύκωμεν"
    assert luw.XAS()._2P() == "λελύκητε"
    assert luw.XAS()._3P() == "λελύκωσι(ν)"

    assert luw.PAO()._1S() == "λύοιμι"
    assert luw.PAO()._2S() == "λύοις"
    assert luw.PAO()._3S() == "λύοι"
    assert luw.PAO()._1P() == "λύοιμεν"
    assert luw.PAO()._2P() == "λύοιτε"
    assert luw.PAO()._3P() == "λύοιεν"

    assert luw.PMO()._1S() == "λυοίμην"
    assert luw.PMO()._2S() == "λύοιο"
    assert luw.PMO()._3S() == "λύοιτο"
    assert luw.PMO()._1P() == "λυοίμεθα"
    assert luw.PMO()._2P() == "λύοισθε"
    assert luw.PMO()._3P() == "λύοιντο"

    assert luw.FAO()._1S() == "λύσοιμι"
    assert luw.FAO()._2S() == "λύσοις"
    assert luw.FAO()._3S() == "λύσοι"
    assert luw.FAO()._1P() == "λύσοιμεν"
    assert luw.FAO()._2P() == "λύσοιτε"
    assert luw.FAO()._3P() == "λύσοιεν"

    assert luw.FMO()._1S() == "λυσοίμην"
    assert luw.FMO()._2S() == "λύσοιο"
    assert luw.FMO()._3S() == "λύσοιτο"
    assert luw.FMO()._1P() == "λυσοίμεθα"
    assert luw.FMO()._2P() == "λύσοισθε"
    assert luw.FMO()._3P() == "λύσοιντο"

    assert luw.FPO()._1S() == "λυθησοίμην"
    assert luw.FPO()._2S() == "λυθήσοιο"
    assert luw.FPO()._3S() == "λυθήσοιτο"
    assert luw.FPO()._1P() == "λυθησοίμεθα"
    assert luw.FPO()._2P() == "λυθήσοισθε"
    assert luw.FPO()._3P() == "λυθήσοιντο"

    assert luw.AAO()._1S() == "λύσαιμι"
    assert luw.AAO()._2S() == "λύσαις/λύσειας"
    assert luw.AAO()._3S() == "λύσαι/λύσειε"
    assert luw.AAO()._1P() == "λύσαιμεν"
    assert luw.AAO()._2P() == "λύσαιτε"
    assert luw.AAO()._3P() == "λύσαιεν/λύσειαν"

    assert luw.AMO()._1S() == "λυσαίμην"
    assert luw.AMO()._2S() == "λύσαιο"
    assert luw.AMO()._3S() == "λύσαιτο"
    assert luw.AMO()._1P() == "λυσαίμεθα"
    assert luw.AMO()._2P() == "λύσαισθε"
    assert luw.AMO()._3P() == "λύσαιντο"

    assert luw.APO()._1S() == "λυθείην"
    assert luw.APO()._2S() == "λυθείης"
    assert luw.APO()._3S() == "λυθείη"
    assert luw.APO()._1P() == "λυθεῖμεν/λυθείημεν"
    assert luw.APO()._2P() == "λυθεῖτε/λυθείητε"
    assert luw.APO()._3P() == "λυθεῖεν/λυθείησαν"

    assert luw.XAO()._1S() == "λελύκοιμι"
    assert luw.XAO()._2S() == "λελύκοις"
    assert luw.XAO()._3S() == "λελύκοι"
    assert luw.XAO()._1P() == "λελύκοιμεν"
    assert luw.XAO()._2P() == "λελύκοιτε"
    assert luw.XAO()._3P() == "λελύκοιεν"

    assert luw.PAD()._2S() == "λῦε"
    assert luw.PAD()._3S() == "λυέτω"
    assert luw.PAD()._2P() == "λύετε"
    assert luw.PAD()._3P() == "λυόντων"

    assert luw.PMD()._2S() == "λύου"
    assert luw.PMD()._3S() == "λυέσθω"
    assert luw.PMD()._2P() == "λύεσθε"
    assert luw.PMD()._3P() == "λυέσθων"

    assert luw.AAD()._2S() == "λῦσον"
    assert luw.AAD()._3S() == "λυσάτω"
    assert luw.AAD()._2P() == "λύσατε"
    assert luw.AAD()._3P() == "λυσάντων"

    assert luw.AMD()._2S() == "λῦσαι"
    assert luw.AMD()._3S() == "λυσάσθω"
    assert luw.AMD()._2P() == "λύσασθε"
    assert luw.AMD()._3P() == "λυσάσθων"

    assert luw.APD()._2S() == "λύθητι"
    assert luw.APD()._3S() == "λυθήτω"
    assert luw.APD()._2P() == "λύθητε"
    assert luw.APD()._3P() == "λυθέντων"

    assert luw.XMD()._2S() == "λέλυσο"
    assert luw.XMD()._3S() == "λελύσθω"
    assert luw.XMD()._2P() == "λέλυσθε"
    assert luw.XMD()._3P() == "λελύσθων"

    assert luw.PAN() == "λύειν"
    assert luw.PMN() == "λύεσθαι"
    assert luw.FAN() == "λύσειν"
    assert luw.FMN() == "λύσεσθαι"
    assert luw.FPN() == "λυθήσεσθαι"
    assert luw.AAN() == "λῦσαι"
    assert luw.AMN() == "λύσασθαι"
    assert luw.APN() == "λυθῆναι"
    assert luw.XAN() == "λελυκέναι"
    assert luw.XMN() == "λελύσθαι"

    assert luw.PAP().NSM() == "λύων"
    assert luw.PAP().NSF() == "λύουσα"
    assert luw.PAP().NSN() == "λῦον"

    assert luw.PMP().NSM() == "λυόμενος"
    assert luw.PMP().NSF() == "λυομένη"
    assert luw.PMP().NSN() == "λυόμενον"

    assert luw.FAP().NSM() == "λύσων"
    assert luw.FAP().NSF() == "λύσουσα"
    assert luw.FAP().NSN() == "λῦσον"

    assert luw.FMP().NSM() == "λυσόμενος"
    assert luw.FMP().NSF() == "λυσομένη"
    assert luw.FMP().NSN() == "λυσόμενον"

    assert luw.FPP().NSM() == "λυθησόμενος"
    assert luw.FPP().NSF() == "λυθησομένη"
    assert luw.FPP().NSN() == "λυθησόμενον"

    assert luw.AAP().NSM() == "λύσας"
    assert luw.AAP().NSF() == "λύσασα"
    assert luw.AAP().NSN() == "λῦσαν"

    assert luw.AMP().NSM() == "λυσάμενος"
    assert luw.AMP().NSF() == "λυσαμένη"
    assert luw.AMP().NSN() == "λυσάμενον"

    assert luw.APP().NSM() == "λυθείς"
    assert luw.APP().NSF() == "λυθεῖσα"
    assert luw.APP().NSN() == "λυθέν"

    assert luw.XAP().NSM() == "λελυκώς"
    assert luw.XAP().NSF() == "λελυκυῖα"
    assert luw.XAP().NSN() == "λελυκός"

    assert luw.XMP().NSM() == "λελυμένος"
    assert luw.XMP().NSF() == "λελυμένη"
    assert luw.XMP().NSN() == "λελυμένον"

    timaw = TIMAW()

    assert timaw.PAI()._1S() == "τιμῶ"
    assert timaw.PAI()._2S() == "τιμᾷς"
    assert timaw.PAI()._3S() == "τιμᾷ"
    assert timaw.PAI()._1P() == "τιμῶμεν"
    assert timaw.PAI()._2P() == "τιμᾶτε"
    assert timaw.PAI()._3P() == "τιμῶσι(ν)"

    assert timaw.PMI()._1S() == "τιμῶμαι"
    assert timaw.PMI()._2S() == "τιμᾷ"
    assert timaw.PMI()._3S() == "τιμᾶται"
    assert timaw.PMI()._1P() == "τιμώμεθα"
    assert timaw.PMI()._2P() == "τιμᾶσθε"
    assert timaw.PMI()._3P() == "τιμῶνται"

    assert timaw.IAI()._1S() == "ἐτίμων"
    assert timaw.IAI()._2S() == "ἐτίμας"
    assert timaw.IAI()._3S() == "ἐτίμα"
    assert timaw.IAI()._1P() == "ἐτιμῶμεν"
    assert timaw.IAI()._2P() == "ἐτιμᾶτε"
    assert timaw.IAI()._3P() == "ἐτίμων"

    assert timaw.IMI()._1S() == "ἐτιμώμην"
    assert timaw.IMI()._2S() == "ἐτιμῶ"
    assert timaw.IMI()._3S() == "ἐτιμᾶτο"
    assert timaw.IMI()._1P() == "ἐτιμώμεθα"
    assert timaw.IMI()._2P() == "ἐτιμᾶσθε"
    assert timaw.IMI()._3P() == "ἐτιμῶντο"
