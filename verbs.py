#!/usr/bin/env python3


from accentuation import recessive, perispomenon, properispomenon
from syllabify import is_vowel, syllabify


def make_perispomenon(w): return perispomenon(syllabify(w))[0]
def make_properispomenon(w): return properispomenon(syllabify(w))[0]


class Endings:

    def __init__(self, stem):
        self.stem = stem


class Endings1(Endings):

    def _1S(self): return recessive(self.stem + "ω")
    def _2S(self): return recessive(self.stem + "εις")
    def _3S(self): return recessive(self.stem + "ει")
    def _1P(self): return recessive(self.stem + "ο" + "μεν")
    def _2P(self): return recessive(self.stem + "ε" + "τε")
    def _3P(self): return recessive(self.stem + "ου" + "σι(ν)")


class Endings3(Endings):

    def _1S(self): return recessive(self.stem + "ον")
    def _2S(self): return recessive(self.stem + "ε" + "ς")
    def _3S(self): return recessive(self.stem + "ε")
    def _1P(self): return recessive(self.stem + "ο" + "μεν")
    def _2P(self): return recessive(self.stem + "ε" + "τε")
    def _3P(self): return recessive(self.stem + "ο" + "ν")


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

    def _1S(self): return recessive(self.stem + "ο" + "μαι")
    def _2S(self): return "{}/{}".format(
                          recessive(self.stem + "ει"), # ε + σαι
                          recessive(self.stem + "ῃ")   # ε + σαι
    )
    def _3S(self): return recessive(self.stem + "ε" + "ται")
    def _1P(self): return recessive(self.stem + "ο" + "μεθα")
    def _2P(self): return recessive(self.stem + "ε" + "σθε")
    def _3P(self): return recessive(self.stem + "ο" + "νται")


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

    def _1S(self): return recessive(self.stem + "ο" + "μην")
    def _2S(self): return recessive(self.stem + "ου") # ε + σο
    def _3S(self): return recessive(self.stem + "ε" + "το")
    def _1P(self): return recessive(self.stem + "ο" + "μεθα")
    def _2P(self): return recessive(self.stem + "ε" + "σθε")
    def _3P(self): return recessive(self.stem + "ο" + "ντο")


class Endings6(Endings):

    def _1S(self): return recessive(self.stem + "α" + "μην")
    def _2S(self): return recessive(self.stem + "ω") # α + σο
    def _3S(self): return recessive(self.stem + "α" + "το")
    def _1P(self): return recessive(self.stem + "α" + "μεθα")
    def _2P(self): return recessive(self.stem + "α" + "σθε")
    def _3P(self): return recessive(self.stem + "α" + "ντο")


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


def redup(stem):
    if is_vowel(stem[0]):
        raise NotImplemented()
    else:
        return stem[0] + "ε" + stem


class LUW(Verb1):

    stem1 = "λυ"



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
