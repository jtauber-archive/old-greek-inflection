#!/usr/bin/env python3


import sys

from accentuation import recessive, make_oxytone, make_paroxytone, make_perispomenon, make_properispomenon
from syllabify import is_vowel
from characters import strip_length


def phon(w):

    w = w.replace("α#σο", "ω")

    w = w.replace("έ#σο", "οῦ")
    w = w.replace("ε#σο", "ου")

    w = w.replace("ό#σο", "οῦ")
    w = w.replace("ο#σο", "ου")

    w = w.replace("ά+ι#σο", "ά+ιο")
    w = w.replace("αι#σο", "αιο")

    w = w.replace("έ+ι#σο", "έ+ιο")

    w = w.replace("ό+ι#σο", "ό+ιο")
    w = w.replace("οι#σο", "οιο")

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

    w = w.replace("ά+ι", "αῖ")
    w = w.replace("α+ί", "αί")

    w = w.replace("έ+ω", "ῶ")
    w = w.replace("ε+ώ", "ώ")

    w = w.replace("έ+ῃ", "ῇ")

    w = w.replace("έ+η", "ῆ")

    w = w.replace("έ+ε+ι", "εῖ")
    w = w.replace("έ+ει", "εῖ")

    w = w.replace("έ+ε", "εῖ")
    w = w.replace("ε+έ", "εί")
    w = w.replace("ε+ε", "ει")

    w = w.replace("έ+οι", "οῖ")
    w = w.replace("ε+οί", "οί")

    w = w.replace("έ+ου", "οῦ")

    w = w.replace("έ+ο", "οῦ")
    w = w.replace("ε+ό", "ού")
    w = w.replace("ε+ο", "ου")

    w = w.replace("έ+α", "ᾶ")

    w = w.replace("ό+ω", "ῶ")
    w = w.replace("ο+ώ", "ώ")

    w = w.replace("ό+ῃ", "οῖ")

    w = w.replace("ό+η", "ῶ")

    w = w.replace("ό+ε+ι", "οῖ")
    w = w.replace("ό+ει", "οῦ")

    w = w.replace("ό+ε", "οῦ")
    w = w.replace("ο+έ", "ού")
    w = w.replace("ο+ε", "ου")

    w = w.replace("ό+ου", "οῦ")

    w = w.replace("ό+οι", "οῖ")
    w = w.replace("ο+οί", "οί")

    w = w.replace("ό+ο", "οῦ")
    w = w.replace("ο+ό", "ού")
    w = w.replace("ο+ο", "ου")

    w = w.replace("ό+ι", "οῖ")
    w = w.replace("ο+ί", "οί")

    w = w.replace("ώ+η", "ῶ")
    w = w.replace("ώ+ῃ", "ῷ") # @@@

    w = w.replace("ή+η", "ῆ")
    w = w.replace("ή+ῃ", "ῇ")

    w = w.replace("η+ε", "η") # @@@

    w = w.replace("ῡ+ε", "ῡ") # @@@

    w = w.replace("ύ+ε", "ῦ")
    w = w.replace("υ+έ", "ύ")

    w = w.replace("ω+ι", "ῳ")

    w = w.replace("έ+ι", "εῖ")
    w = w.replace("ε+ί", "εί")
    w = w.replace("ε+ι", "ει")

    w = w.replace("ά~α", "ᾶ")
    w = w.replace("έ~α", "έα")
    w = w.replace("ό~α", "όα")
    w = w.replace("ύ~α", "ύα")

    return w


def replace_final(w, a, b):
    if w[-1] == a:
        return w[:-1] + b
    else:
        return w


def phon2(w):

    w = replace_final(w, "α", "η")
    w = replace_final(w, "ε", "η")
    w = replace_final(w, "ο", "ω")
    w = replace_final(w, "υ", "ῡ")

    return w


class Endings:

    sg_conn = ["", "", ""]
    pl_conn = ["", "", ""]

    def __init__(self, stem):
        self.stem = stem

    def _1S(self): return phon(recessive(self.stem + self.sg_conn[0] + self.ending_1S))
    def _2S(self): return phon(recessive(self.stem + self.sg_conn[1] + self.ending_2S))
    def _3S(self): return phon(recessive(self.stem + self.sg_conn[2] + self.ending_3S))

    def _1P(self): return phon(recessive(self.stem + self.pl_conn[0] + self.ending_1P))
    def _2P(self): return phon(recessive(self.stem + self.pl_conn[1] + self.ending_2P))
    def _3P(self): return phon(recessive(self.stem + self.pl_conn[2] + self.ending_3P))


class SingularBase1(Endings):

    ending_1S = "ν"
    ending_2S = "ς"
    ending_3S = ""


class SingularBase2(Endings):

    ending_1S = "μην"
    ending_2S = "#σο"
    ending_3S = "το"


class SingularBase2B(Endings):

    ending_1S = "μην"
    ending_2S = "σο"
    ending_3S = "το"


class PluralBase1(Endings):

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "σαν"


class PluralBase2(Endings):

    ending_1P = "μεθα"
    ending_2P = "σθε"
    ending_3P = "ντο"


class PluralBase3(Endings):

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "σι(ν)"


class PluralBase4(Endings):

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "ν"


class PluralBase5(Endings):

    ending_1P = "μεθα"
    ending_2P = "σθε"
    ending_3P = "νται"


class MDBase1(Endings):

    ending_3S = "σθω"
    ending_2P = "σθε"
    ending_3P = "σθων"


class ADBase1(Endings):

    ending_3S = "τω"
    ending_2P = "τε"
    ending_3P = "ντων"


class Endings1(PluralBase3):

    pl_conn = ["+ο", "+ε", "+ου"]

    ending_1S = "+ω"
    ending_2S = "+ε+ις"
    ending_3S = "+ε+ι"


class Endings1mi(PluralBase3):

    pl_conn = ["", "", "~α"]

    def _1S(self): return phon(recessive(phon2(self.stem) + "μι"))
    def _2S(self): return phon(recessive(phon2(self.stem) + "ς"))
    def _3S(self): return phon(recessive(phon2(self.stem) + "σι(ν)"))


class Endings1miB(Endings1mi):

    pl_conn = ["", "", "+α"]


class Endings3(PluralBase4, SingularBase1):

    sg_conn = ["+ο", "+ε", "+ε"]
    pl_conn = ["+ο", "+ε", "+ο"]


class Endings7(PluralBase1, SingularBase1):

    pass


class Endings7B(Endings):

    def _1S(self): return phon(recessive(phon2(self.stem) + "ν"))
    def _2S(self): return phon(recessive(phon2(self.stem) + "ς"))
    def _3S(self): return phon(recessive(phon2(self.stem) + ""))
    def _1P(self): return phon(recessive(phon2(self.stem) + "μεν"))
    def _2P(self): return phon(recessive(phon2(self.stem) + "τε"))
    def _3P(self): return phon(recessive(phon2(self.stem) + "σαν"))


class Endings3mi(PluralBase1, SingularBase1):

    sg_conn = ["+ο", "+ε", "+ε"]


class Endings3miB(Endings3mi):

    def _1S(self): return phon(recessive(phon2(self.stem) + "ν"))


class Endings3miC(Endings3mi):

    def _1S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+εν")),
                          phon(recessive(phon2(self.stem) + "ν")))

class Endings3miD(Endings3miB):

    def _2S(self): return phon(recessive(phon2(self.stem) + "ς"))
    def _3S(self): return phon(recessive(phon2(self.stem) + ""))


class Endings5(PluralBase4):

    pl_conn = ["α", "α", "α"]

    ending_1S = "α"
    ending_2S = "ας"
    ending_3S = "ε"


class Endings5B(PluralBase1):

    def _1S(self): return phon(recessive(phon2(self.stem) + "κ" + "α"))
    def _2S(self): return phon(recessive(phon2(self.stem) + "κ" + "α" + "ς"))
    def _3S(self): return phon(recessive(phon2(self.stem) + "κ" + "ε"))


class Endings8(Endings5):

    ending_3P = "σι(ν)"


class Endings12(PluralBase3):

    pl_conn = ["+ω", "+η", "+ω"]

    ending_1S = "+ω"
    ending_2S = "+ῃς"
    ending_3S = "+ῃ"


class Endings12mi(Endings12):

    def _2S(self): return phon(recessive(phon2(self.stem) + "+ῃς"))
    def _3S(self): return phon(recessive(phon2(self.stem) + "+ῃ"))
    def _2P(self): return phon(recessive(phon2(self.stem) + "+η" + "τε"))


class Endings14(Endings):

    def _1S(self): return phon(make_perispomenon(self.stem + "ω"))
    def _2S(self): return phon(make_perispomenon(self.stem + "ῃς"))
    def _3S(self): return phon(make_perispomenon(self.stem + "ῃ"))
    def _1P(self): return phon(make_properispomenon(self.stem + "ω" + "μεν"))
    def _2P(self): return phon(make_properispomenon(self.stem + "η" + "τε"))
    def _3P(self): return phon(make_properispomenon(self.stem + "ω" + "σι(ν)"))


class Endings10(PluralBase1):

    pl_conn = ["ε", "ε", "ε"]

    ending_1S = "η"
    ending_2S = "ης"
    ending_3S = "ει"


class Endings9(PluralBase5):

    ending_1S = "μαι"
    ending_2S = "σαι"
    ending_3S = "ται"


class Endings2B(PluralBase5):

    sg_conn = ["+ο", "+ε", "+ε"]
    pl_conn = ["+ο", "+ε", "+ο"]

    ending_1S = "μαι"
    ending_2S = "+ι" # ε + σαι
    ending_3S = "ται"


class Endings2(Endings2B):

    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+ε+ι")), # ε + σαι
                          phon(recessive(self.stem + "+ῃ"))   # ε + σαι
    )


class Endings13(PluralBase5):

    sg_conn = ["+ω", "+ῃ", "+η"]
    pl_conn = ["+ω", "+η", "+ω"]

    ending_1S = "μαι"
    ending_3S = "ται"

    def _2S(self): return phon(recessive(self.stem + "+ῃ"))


class Endings13mi(Endings13):

    def _2S(self): return phon(recessive(phon2(self.stem) + "+ῃ"))
    def _3S(self): return phon(recessive(phon2(self.stem) + "+η" + "ται"))
    def _2P(self): return phon(recessive(phon2(self.stem) + "+η" + "σθε"))


class Endings11(PluralBase2, SingularBase2B):

    pass


class Endings4(PluralBase2, SingularBase2):

    sg_conn = ["+ο", "+ε", "+ε"]
    pl_conn = ["+ο", "+ε", "+ο"]


class Endings6(PluralBase2, SingularBase2):

    sg_conn = ["α", "α", "α"]
    pl_conn = ["α", "α", "α"]


class Endings6B(PluralBase2, SingularBase2):

    pass


class Endings15(Endings):

    sg_conn = ["οι", "οι", "οι"]
    pl_conn = ["οι", "οι", "οι"]

    ending_1S = "μι"
    ending_2S = "ς"
    def _3S(self): return phon(make_paroxytone(self.stem + "οι" + ""))
    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "εν"


class Endings15B(Endings15):

    def _1S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "ην")),
                          phon(recessive(self.stem + "+οι" + "μι")),
    )
    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "ης")),
                          phon(recessive(self.stem + "+οι" + "ς")),
    )
    def _3S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "η")),
                          phon(make_paroxytone(self.stem + "+οι" + "")),
    )
    def _1P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "μεν")),
                          phon(recessive(self.stem + "+οι" + "ημεν")),
    )
    def _2P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "τε")),
                          phon(recessive(self.stem + "+οι" + "ητε")),
    )
    def _3P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+οι" + "εν")),
                          phon(recessive(self.stem + "+οι" + "ησαν")),
    )


class Endings15mi(SingularBase1):

    sg_conn = ["ιη", "ιη", "ιη"]

    def _1P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+ι" + "μεν")),
                          phon(recessive(self.stem + "ι" + "ημεν")),
    )
    def _2P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+ι" + "τε")),
                          phon(recessive(self.stem + "ι" + "ητε")),
    )
    def _3P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+ι" + "εν")),
                          phon(recessive(self.stem + "ι" + "ησαν")),
    )


class Endings17(Endings):

    sg_conn = ["αι", "αι", "αι"]
    pl_conn = ["αι", "αι", "αι"]

    ending_1S = "μι"
    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "αι" + "ς")),
                          phon(recessive(self.stem + "ει" + "ας")),
    )
    def _3S(self): return "{}/{}".format(
                          phon(make_paroxytone(self.stem + "αι" + "")),
                          phon(recessive(self.stem + "ει" + "ε")),
    )
    ending_1P = "μεν"
    ending_2P = "τε"
    def _3P(self): return "{}/{}".format(
                          phon(recessive(self.stem + "αι" + "εν")),
                          phon(recessive(self.stem + "ει" + "αν")),
    )


class Endings16(PluralBase2, SingularBase2):

    sg_conn = ["+οι", "+οι", "+οι"]
    pl_conn = ["+οι", "+οι", "+οι"]


class Endings16mi(PluralBase2, SingularBase2):

    sg_conn = ["+ι", "+ι", "+ι"]
    pl_conn = ["+ι", "+ι", "+ι"]


class Endings18(PluralBase2, SingularBase2):

    sg_conn = ["αι", "αι", "αι"]
    pl_conn = ["αι", "αι", "αι"]


class Endings19(SingularBase1):

    sg_conn = ["ειη", "ειη", "ειη"]

    def _1P(self): return "{}/{}".format(
                          phon(make_properispomenon(self.stem + "ει" + "μεν")),
                          phon(recessive(self.stem + "ειη" + "μεν")),
    )
    def _2P(self): return "{}/{}".format(
                          phon(make_properispomenon(self.stem + "ει" + "τε")),
                          phon(recessive(self.stem + "ειη" + "τε")),
    )
    def _3P(self): return "{}/{}".format(
                          phon(make_properispomenon(self.stem + "ει" + "εν")),
                          phon(recessive(self.stem + "ειη" + "σαν")),
    )


class Endings20mi(ADBase1):

    ending_2S = "+ε"


class Endings20miB(ADBase1):

    def _2S(self): return phon(recessive(phon2(self.stem) + "+ε"))


class Endings20miC(ADBase1):

    ending_2S = "ς"


class Endings20miD(ADBase1):

    def _2S(self): return phon(recessive(phon2(self.stem) + "+θι"))
    def _3S(self): return phon(recessive(phon2(self.stem) + self.ending_3S))
    def _2P(self): return phon(recessive(phon2(self.stem) + self.ending_2P))


class Endings20(ADBase1):

    sg_conn = [None, "", "+ε"]
    pl_conn = [None, "+ε", "+ο"]

    ending_2S = "+ε"


class Endings22(ADBase1):

    sg_conn = [None, "", "α"]
    pl_conn = [None, "α", "α"]

    ending_2S = "ον"


class Endings24(ADBase1):

    sg_conn = [None, "η", "η"]
    pl_conn = [None, "η", "ε"]

    ending_2S = "τι"


class Endings21(MDBase1):

    sg_conn = [None, "+ε", "+ε"]
    pl_conn = [None, "+ε", "+ε"]

    ending_2S = "#σο"


class Endings23(MDBase1):

    sg_conn = [None, "α", "α"]
    pl_conn = [None, "α", "α"]

    def _2S(self): return phon(recessive(self.stem + "αι"))


class Endings25(MDBase1):

    ending_2S = "σο"


class Endings25B(MDBase1):

    ending_2S = "#σο"


class Endings26(Endings):

    def NSM(self): return phon(recessive(self.stem + "+ων"))
    def NSF(self): return phon(recessive(self.stem + "+ουσα"))
    def NSN(self): return phon(make_properispomenon(self.stem + "+ον"))


class Endings26mi(Endings):

    def NSM(self): return phon(make_oxytone(self.stem + "+ες"))
    def NSF(self): return phon(recessive(self.stem + "+εσα"))
    def NSN(self): return phon(make_oxytone(self.stem + "ν"))


class Endings28(Endings):

    def NSM(self): return phon(make_paroxytone(self.stem + "ας"))
    def NSF(self): return phon(recessive(self.stem + "ασα"))
    def NSN(self): return phon(recessive(self.stem + "αν"))


class Endings30(Endings):

    def NSM(self): return phon(make_oxytone(self.stem + "εις"))
    def NSF(self): return phon(make_properispomenon(self.stem + "εισα"))
    def NSN(self): return phon(make_oxytone(self.stem + "εν"))


class Endings32(Endings):

    def NSM(self): return phon(make_paroxytone(self.stem + "μενος"))
    def NSF(self): return phon(recessive(self.stem + "μενη"))
    def NSN(self): return phon(make_paroxytone(self.stem + "μενον"))


class ParticipleBase1(Endings):

    pl_conn = ""

    def NSM(self): return phon(recessive(self.stem + self.pl_conn + "μενος"))
    def NSF(self): return phon(recessive(self.stem + self.pl_conn + "μενη"))
    def NSN(self): return phon(recessive(self.stem + self.pl_conn + "μενον"))


class Endings27mi(ParticipleBase1):

    pass


class Endings27(ParticipleBase1):

    pl_conn = "+ο"


class Endings29(ParticipleBase1):

    pl_conn = "α"


class Endings31(Endings):

    def NSM(self): return phon(make_oxytone(self.stem + "ως"))
    def NSF(self): return phon(make_properispomenon(self.stem + "υια"))
    def NSN(self): return phon(make_oxytone(self.stem + "ος"))


class Verb1:

    def PAI(self): return Endings1(self.stem1)
    def PMI(self): return Endings2(self.stem1)
    def IAI(self): return Endings3(aug(self.stem1))
    def IMI(self): return Endings4(aug(self.stem1))
    def FAI(self): return Endings1(self.stem1 + "σ")
    def FMI(self): return Endings2(self.stem1 + "σ")
    def FPI(self): return Endings2(self.stem1 + "θη" + "σ")
    def AAI(self): return Endings5(aug(self.stem1 + "σ"))
    def AMI(self): return Endings6(aug(self.stem1 + "σ"))
    def API(self): return Endings7(aug(self.stem1 + "θη"))
    def XAI(self): return Endings8(redup(self.stem1) + "κ")
    def XMI(self): return Endings9(redup(self.stem1))
    def YAI(self): return Endings10(aug(redup(self.stem1) + "κ"))
    def YMI(self): return Endings11(aug(redup(self.stem1)))

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

    def PAN(self): return phon(recessive(self.stem1 + "+ειν"))
    def PMN(self): return phon(recessive(self.stem1 + "+εσθαι"))
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


class Verb1C(Verb1):

    def PAO(self): return Endings15B(self.stem1)


class Verb1B(Verb1C):

    def PMI(self): return Endings2B(self.stem1)


class Verb2(Verb1):

    def PAI(self): return Endings1mi(self.stem1)
    def PMI(self): return Endings9(self.stem1)
    def IAI(self): return Endings3mi(aug(self.stem1))
    def IMI(self): return Endings11(aug(self.stem1))
    def AAI(self): return Endings5B(aug(self.stem2))
    def AMI(self): return Endings6B(aug(self.stem2))

    def PAS(self): return Endings12mi(self.stem1)
    def PMS(self): return Endings13mi(self.stem1)

    def PAO(self): return Endings15mi(self.stem1)
    def PMO(self): return Endings16mi(self.stem1)

    def PAD(self): return Endings20mi(self.stem1)
    def PMD(self): return Endings25(self.stem1)

    def PAN(self): return make_paroxytone(self.stem1 + "ναι")
    def PMN(self): return recessive(self.stem1 + "σθαι")

    def PAP(self): return Endings26mi(self.stem1)
    def PMP(self): return Endings27mi(self.stem1)

    def AAS(self): return Endings12mi(self.stem2)
    def AMS(self): return Endings13mi(self.stem2)

    def AAO(self): return Endings15mi(self.stem2)
    def AMO(self): return Endings16mi(self.stem2)

    def AAD(self): return Endings20miC(self.stem2)
    def AMD(self): return Endings25B(self.stem2)

    def AAN(self): return phon(recessive(self.stem2 + "+εναι"))
    def AMN(self): return recessive(self.stem2 + "σθαι")

    def AAP(self): return Endings26mi(self.stem2)
    def AMP(self): return Endings27mi(self.stem2)


class Verb2B(Verb2):

    def IAI(self): return Endings3miB(aug(self.stem1))


class Verb2C(Verb2B):

    def PAI(self): return Endings1miB(self.stem1)
    def IAI(self): return Endings3miC(self.stem1)


class Verb2D(Verb2):

    def IAI(self): return Endings3miD(self.stem1)
    def AAI(self): return Endings7B(aug(self.stem2))
    def PAD(self): return Endings20miB(self.stem1)
    def AAD(self): return Endings20miD(self.stem2)
    def AAN(self): return phon(recessive(phon2(self.stem2) + "+ναι"))


class Verb2E(Verb2):

    def IAI(self): return Endings3miD(aug(self.stem1))
    def PAS(self): return Endings12(self.stem1)
    def PAO(self): return Endings15(self.stem1)
    def PMO(self): return Endings16(self.stem1)
    def PAD(self): return Endings20miB(self.stem1)


def aug(stem):
    if is_vowel(stem[0]):
        if stem[0] == "ἱ":
            return stem
        else:
            raise NotImplementedError(stem)
    else:
        return "ἐ" + stem


def redup(stem):
    if is_vowel(stem[0]):
        raise NotImplementedError(stem)
    else:
        return stem[0] + "ε" + stem


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


class hISTHMI(Verb2D):

    stem1 = "ἱστα"
    stem2 = "στα"


class DEIKNUMI(Verb2E):

    stem1 = "δεικνυ"


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
}


def calculate_form(lemma, parse):
    c = VERBS[lemma]
    for step in parse.split("."):
        if step[0] in "123":
            step = "_" + step
        c = getattr(c(), step)

    return strip_length(c().replace("+", "")), (c.__self__.__class__.__name__, c.__qualname__)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        lemma_filter = sys.argv[1]
    else:
        lemma_filter = None

    passed = 0
    fails = []
    with open("test.txt") as f:
        for line in f:
            record = line.strip().split("#")[0]
            if not record:
                continue
            lemma, parse, form = record.split()
            if lemma_filter and lemma_filter != lemma:
                continue

            prediction, rule = calculate_form(lemma, parse)

            if prediction == form:
                passed += 1
            else:
                fails.append("{} != {} {}".format(record, prediction, rule))

    print("{} passed".format(passed))
    if fails:
        print("{} failed".format(len(fails)))
        print(fails[0])
