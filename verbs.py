from accentuation import recessive, make_oxytone, make_paroxytone, make_proparoxytone, make_perispomenon, make_properispomenon
from syllabify import is_vowel
from characters import strip_length


def phon(w):

    w = w.replace("ἕ", "hέ")
    w = w.replace("ἑ", "hε")
    w = w.replace("εἷ", "hεῖ")

    w = w.replace("α#σο", "ω")

    w = w.replace("έ#σο", "οῦ")
    w = w.replace("ε#σο", "ου")

    w = w.replace("ό#σο", "οῦ")
    w = w.replace("ο#σο", "ου")

    w = w.replace("ά+ι#σο", "ά+ιο")
    w = w.replace("αι#σο", "αιο")

    w = w.replace("έ+ι#σο", "έ+ιο")

    w = w.replace("εῖ#σο", "εῖο")

    w = w.replace("ό+ι#σο", "ό+ιο")
    w = w.replace("οι#σο", "οιο")

    w = w.replace("ά+ε#σαι", "ᾷ") # @@@
    w = w.replace("ό+ε#σαι", "οῖ") # @@@
    w = w.replace("ᾶ#σαι", "ᾷ")
    w = w.replace("α#σαι", "ᾳ")
    w = w.replace("η#σαι", "ῃ")

    w = w.replace("ά+ω", "ῶ")
    w = w.replace("α+ώ", "ώ")
    w = w.replace("α+ω", "ω")

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

    w = w.replace("α+ό+ε", "ῶ")
    w = w.replace("α+ο+ε", "ω")

    w = w.replace("ᾶ+ο", "ῶ")
    w = w.replace("ά+ο", "ῶ")
    w = w.replace("α+ό", "ώ")
    w = w.replace("α+ο", "ω")

    w = w.replace("ά+ι", "αῖ")
    w = w.replace("α+ί", "αί")

    w = w.replace("ᾶ+ι", "ᾷ")

    w = w.replace("έ+ω", "ῶ")
    w = w.replace("ε+ώ", "ώ")
    w = w.replace("ε+ω", "ω")

    w = w.replace("έ+ῃ", "ῇ")

    w = w.replace("έ+η", "ῆ")

    w = w.replace("έ+ε+ι", "εῖ")
    w = w.replace("έ+ει", "εῖ")

    w = w.replace("έ+ε", "εῖ")
    w = w.replace("ε+έ", "εί")
    w = w.replace("ε+ε", "ει")

    w = w.replace("έ+οι", "οῖ")
    w = w.replace("ε+οί", "οί")

    w = w.replace("ε+ο+ε", "ου")

    w = w.replace("έ+ου", "οῦ")

    w = w.replace("έ+ο", "οῦ")
    w = w.replace("ε+ό", "ού")
    w = w.replace("ε+ο", "ου")

    w = w.replace("έ+α", "ᾶ")

    w = w.replace("ό+ω", "ῶ")
    w = w.replace("ο+ώ", "ώ")
    w = w.replace("ο+ω", "ω")

    w = w.replace("ό+η+ι", "οῖ")
    w = w.replace("ό+ῃ", "οῖ")

    w = w.replace("ό+η", "ῶ")

    w = w.replace("ό+ε+ι", "οῖ")
    w = w.replace("ό+ει", "οῦ")

    w = w.replace("ο+ό+ε", "οῦ")
    w = w.replace("ο+ο+ε", "ου")

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

    w = w.replace("ῆ+ι", "ῇ")
    w = w.replace("η+ῖ", "ῇ")
    w = w.replace("η+ι", "ῃ")

    w = w.replace("η+ε", "η") # @@@

    w = w.replace("ῡ+ε", "ῡ") # @@@

    w = w.replace("ύ+ε", "ῦ")
    w = w.replace("υ+έ", "ύ")
    w = w.replace("υ+ε", "υ")

    w = w.replace("ῶ+ι", "ῷ")
    w = w.replace("ω+ι", "ῳ")

    w = w.replace("έ+ι", "εῖ")
    w = w.replace("ε+ί", "εί")
    w = w.replace("ε+ι", "ει")

    w = w.replace("ά~α", "ᾶ")
    w = w.replace("έ~α", "έα")
    w = w.replace("ό~α", "όα")
    w = w.replace("ύ~α", "ύα")

    w = w.replace("hεί", "εἵ")
    w = w.replace("hεῖ", "εἷ")
    w = w.replace("hει", "εἱ")
    w = w.replace("hέ", "ἕ")
    w = w.replace("hε", "ἑ")
    w = w.replace("hῆ", "ἧ")
    w = w.replace("hῇ", "ᾗ")
    w = w.replace("hῶ", "ὧ")
    w = w.replace("hώ", "ὥ")
    w = w.replace("hοῦ", "οὗ")

    return w


def replace_final(w, a, b):
    if w[-len(a):] == a:
        return w[:-len(a)] + b
    else:
        return w


def phon2(w):

    w = replace_final(w, "α", "η")
    w = replace_final(w, "ε", "η")
    w = replace_final(w, "εἱ", "ἡ")
    w = replace_final(w, "ο", "ω")
    w = replace_final(w, "υ", "ῡ")

    return w


def nothing(self, stem):
    return stem


def lengthen(self, stem):
    return phon2(stem)


def alt(self, endings1, endings2, attr):
    return "{}/{}".format(
        getattr(endings1(self.stem), attr)(),
        getattr(endings2(self.stem), attr)(),
    )


def oxytone(self, stem):
    return make_oxytone(stem)


def paroxytone(self, stem):
    return make_paroxytone(stem)


def proparoxytone(self, stem):
    return make_proparoxytone(stem)


def perispomenon(self, stem):
    return make_perispomenon(stem)


def properispomenon(self, stem):
    return make_properispomenon(stem)


class Endings:

    conn_1S = ""
    conn_2S = ""
    conn_3S = ""
    conn_1P = ""
    conn_2P = ""
    conn_3P = ""

    prep_stem_1S = nothing
    prep_stem_2S = nothing
    prep_stem_3S = nothing
    prep_stem_1P = nothing
    prep_stem_2P = nothing
    prep_stem_3P = nothing

    accentuation_1S = lambda self, stem: recessive(stem)
    accentuation_2S = lambda self, stem: recessive(stem)
    accentuation_3S = lambda self, stem: recessive(stem)
    accentuation_1P = lambda self, stem: recessive(stem)
    accentuation_2P = lambda self, stem: recessive(stem)
    accentuation_3P = lambda self, stem: recessive(stem)

    def __init__(self, stem):
        self.stem = stem

    def _1S(self): return phon(self.accentuation_1S(self.prep_stem_1S(self.stem) + self.conn_1S + self.ending_1S))
    def _2S(self): return phon(self.accentuation_2S(self.prep_stem_2S(self.stem) + self.conn_2S + self.ending_2S))
    def _3S(self): return phon(self.accentuation_3S(self.prep_stem_3S(self.stem) + self.conn_3S + self.ending_3S))

    def _1P(self): return phon(self.accentuation_1P(self.prep_stem_1P(self.stem) + self.conn_1P + self.ending_1P))
    def _2P(self): return phon(self.accentuation_2P(self.prep_stem_2P(self.stem) + self.conn_2P + self.ending_2P))
    def _3P(self): return phon(self.accentuation_3P(self.prep_stem_3P(self.stem) + self.conn_3P + self.ending_3P))


class PrimaryActive(Endings):

    ending_1S = "+ω"
    ending_2S = "+ις"
    ending_3S = "+ι"

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "σι(ν)"


class SecondaryActive(Endings):

    ending_1S = "ν"
    ending_2S = "ς"
    ending_3S = ""

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "ν"


class SecondaryActive2(SecondaryActive):

    ending_3P = "σαν"


class ImperativeActive(Endings):

    ending_2S = ""
    ending_3S = "τω"
    ending_2P = "τε"
    ending_3P = "ντων"


class PrimaryMiddle(Endings):

    ending_1S = "μαι"
    ending_2S = "#σαι"
    ending_3S = "ται"

    ending_1P = "μεθα"
    ending_2P = "σθε"
    ending_3P = "νται"


class PrimaryMiddle2(PrimaryMiddle):

    ending_2S = "σαι"


class SecondaryMiddle(Endings):

    ending_1S = "μην"
    ending_2S = "#σο"
    ending_3S = "το"

    ending_1P = "μεθα"
    ending_2P = "σθε"
    ending_3P = "ντο"


class SecondaryMiddle2(SecondaryMiddle):

    ending_2S = "σο"


class ImperativeMiddle(Endings):

    ending_2S = "#σο"
    ending_3S = "σθω"
    ending_2P = "σθε"
    ending_3P = "σθων"


class ImperativeMiddle2(ImperativeMiddle):

    ending_2S = "σο"


class Endings1(PrimaryActive):

    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_1P = "+ο"
    conn_2P = "+ε"
    conn_3P =  "+ου"


class Endings1mi(PrimaryActive):

    prep_stem_1S = lengthen
    prep_stem_2S = lengthen
    prep_stem_3S = lengthen

    conn_3P = "~α"

    ending_1S = "μι"
    ending_2S = "ς"
    ending_3S = "σι(ν)"


class Endings1miB(Endings1mi):

    conn_3P = "+α"


class Endings3(SecondaryActive):

    conn_1S = "+ο"
    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_1P = "+ο"
    conn_2P = "+ε"
    conn_3P = "+ο"


class Endings7(SecondaryActive2):

    pass


class Endings7B(SecondaryActive2):

    prep_stem_1S = lengthen
    prep_stem_2S = lengthen
    prep_stem_3S = lengthen
    prep_stem_1P = lengthen
    prep_stem_2P = lengthen
    prep_stem_3P = lengthen


class Endings3mi(SecondaryActive2):

    conn_1S = "+ο"
    conn_2S = "+ε"
    conn_3S = "+ε"


class Endings3miB(SecondaryActive2):

    prep_stem_1S = lengthen

    conn_2S = "+ε"
    conn_3S = "+ε"


class Endings3miB2(SecondaryActive2):

    conn_1S = "+ε"
    conn_2S = "+ε"
    conn_3S = "+ε"


class Endings3miC(Endings3mi):

    def _1S(self): return alt(self, Endings3miB2, Endings3miB, "_1S")


class Endings3miD(SecondaryActive2):

    prep_stem_1S = lengthen
    prep_stem_2S = lengthen
    prep_stem_3S = lengthen


class Endings5(SecondaryActive):

    conn_1P = "α"
    conn_2P = "α"
    conn_3P = "α"

    ending_1S = "α"
    ending_2S = "ας"
    ending_3S = "ε"


class Endings5B(SecondaryActive2):

    prep_stem_1S = lengthen
    prep_stem_2S = lengthen
    prep_stem_3S = lengthen

    conn_1S = "κ"
    conn_2S = "κ"
    conn_3S = "κ"

    ending_1S = "α"
    ending_2S = "ας"
    ending_3S = "ε"


class Endings8(Endings5):

    ending_3P = "σι(ν)"


class Endings12(PrimaryActive):

    conn_2S = "+η"
    conn_3S = "+η"
    conn_1P = "+ω"
    conn_2P = "+η"
    conn_3P = "+ω"


class Endings12mi(Endings12):

    prep_stem_2S = lengthen
    prep_stem_3S = lengthen
    prep_stem_2P = lengthen


class Endings14(Endings12):

    accentuation_1S = perispomenon
    accentuation_2S = perispomenon
    accentuation_3S = perispomenon
    accentuation_1P = properispomenon
    accentuation_2P = properispomenon
    accentuation_3P = properispomenon


class Endings10(SecondaryActive2):

    conn_1P = "ε"
    conn_2P = "ε"
    conn_3P = "ε"

    ending_1S = "η"
    ending_2S = "ης"
    ending_3S = "ει"


class Endings9(PrimaryMiddle2):

    pass


class Endings2B(PrimaryMiddle):

    conn_1S = "+ο"
    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_1P = "+ο"
    conn_2P = "+ε"
    conn_3P = "+ο"

    ending_2S = "#σαι"


class Endings2(Endings2B):

    def _2S(self): return "{}/{}".format(
                          phon(recessive(self.stem + "+ε+ι")), # ε + σαι
                          phon(recessive(self.stem + "+ῃ"))   # ε + σαι
    )


class Endings13(PrimaryMiddle):

    conn_1S = "+ω"
    conn_2S = "+η"
    conn_3S = "+η"
    conn_1P = "+ω"
    conn_2P = "+η"
    conn_3P = "+ω"

    ending_2S = "#σαι"


class Endings13mi(Endings13):

    prep_stem_2S = lengthen
    prep_stem_3S = lengthen
    prep_stem_2P = lengthen


class Endings11(SecondaryMiddle2):

    pass


class Endings4(SecondaryMiddle):

    conn_1S = "+ο"
    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_1P = "+ο"
    conn_2P = "+ε"
    conn_3P = "+ο"


class Endings6(SecondaryMiddle):

    conn_1S = "α"
    conn_2S = "α"
    conn_3S = "α"
    conn_1P = "α"
    conn_2P = "α"
    conn_3P = "α"


class Endings6B(SecondaryMiddle):

    pass


class Endings15(Endings):

    conn_1S = "+οι"
    conn_2S = "+οι"
    conn_3S = "+οι"
    conn_1P = "+οι"
    conn_2P = "+οι"
    conn_3P = "+οι"

    ending_1S = "μι"
    ending_2S = "ς"
    ending_3S = ""
    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "εν"

    accentuation_3S = paroxytone


class Endings15C(Endings15):

    conn_1S = "+οιη"
    conn_2S = "+οιη"
    conn_3S = "+οιη"
    conn_1P = "+οιη"
    conn_2P = "+οιη"
    conn_3P = "+οιη"

    ending_1S = "ν"
    ending_3P = "σαν"


class Endings15B(Endings15):

    def _1S(self): return alt(self, Endings15C, Endings15, "_1S")
    def _2S(self): return alt(self, Endings15C, Endings15, "_2S")
    def _3S(self): return alt(self, Endings15C, Endings15, "_3S")
    def _1P(self): return alt(self, Endings15, Endings15C, "_1P")
    def _2P(self): return alt(self, Endings15, Endings15C, "_2P")
    def _3P(self): return alt(self, Endings15, Endings15C, "_3P")


class Endings15miA(SecondaryActive):

    conn_1P = "+ι"
    conn_2P = "+ι"
    conn_3P = "+ι"

    ending_3P = "εν"


class Endings15miB(SecondaryActive):

    conn_1P = "ιη"
    conn_2P = "ιη"
    conn_3P = "ιη"

    ending_3P = "σαν"


class Endings15mi(SecondaryActive):

    conn_1S = "ιη"
    conn_2S = "ιη"
    conn_3S = "ιη"

    def _1P(self): return alt(self, Endings15miA, Endings15miB, "_1P")
    def _2P(self): return alt(self, Endings15miA, Endings15miB, "_2P")
    def _3P(self): return alt(self, Endings15miA, Endings15miB, "_3P")


class Endings17A(Endings):

    conn_2S = "+αι"
    conn_3S = "+αι"
    conn_3P = "+αι"

    ending_2S = "ς"
    ending_3S = ""
    ending_3P = "εν"

    accentuation_3S = paroxytone


class Endings17B(Endings):

    conn_2S = "+ει"
    conn_3S = "+ει"
    conn_3P = "+ει"

    ending_2S = "ας"
    ending_3S = "ε"
    ending_3P = "αν"


class Endings17(Endings):

    conn_1S = "+αι"
    conn_2S = "+αι"
    conn_3S = "+αι"
    conn_1P = "+αι"
    conn_2P = "+αι"
    conn_3P = "+αι"

    ending_1S = "μι"
    def _2S(self): return alt(self, Endings17A, Endings17B, "_2S")
    def _3S(self): return alt(self, Endings17A, Endings17B, "_3S")
    ending_1P = "μεν"
    ending_2P = "τε"
    def _3P(self): return alt(self, Endings17A, Endings17B, "_3P")


class Endings16(SecondaryMiddle):

    conn_1S = "+οι"
    conn_2S = "+οι"
    conn_3S = "+οι"
    conn_1P = "+οι"
    conn_2P = "+οι"
    conn_3P = "+οι"


class Endings16mi(SecondaryMiddle):

    conn_1S = "+ι"
    conn_2S = "+ι"
    conn_3S = "+ι"
    conn_1P = "+ι"
    conn_2P = "+ι"
    conn_3P = "+ι"


class Endings18(SecondaryMiddle):

    conn_1S = "αι"
    conn_2S = "αι"
    conn_3S = "αι"
    conn_1P = "αι"
    conn_2P = "αι"
    conn_3P = "αι"


class Endings19A(SecondaryActive):

    conn_1P = "ει"
    conn_2P = "ει"
    conn_3P = "ει"

    ending_3P = "εν"

    accentuation_1P = properispomenon
    accentuation_2P = properispomenon
    accentuation_3P = properispomenon


class Endings19B(SecondaryActive):

    conn_1P = "ειη"
    conn_2P = "ειη"
    conn_3P = "ειη"

    ending_1P = "μεν"
    ending_2P = "τε"
    ending_3P = "σαν"


class Endings19(SecondaryActive):

    conn_1S = "ειη"
    conn_2S = "ειη"
    conn_3S = "ειη"

    def _1P(self): return alt(self, Endings19A, Endings19B, "_1P")
    def _2P(self): return alt(self, Endings19A, Endings19B, "_2P")
    def _3P(self): return alt(self, Endings19A, Endings19B, "_3P")


class Endings20mi(ImperativeActive):

    ending_2S = "+ε"


class Endings20miB(Endings20mi):

    prep_stem_2S = lengthen


class Endings20miC(ImperativeActive):

    ending_2S = "ς"


class Endings20miD(ImperativeActive):

    prep_stem_2S = lengthen
    prep_stem_3S = lengthen
    prep_stem_2P = lengthen

    ending_2S = "+θι"


class Endings20(ImperativeActive):

    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_2P = "+ε"
    conn_3P = "+ο"


class Endings22(ImperativeActive):

    conn_3S = "α"
    conn_2P = "α"
    conn_3P = "α"

    ending_2S = "ον"


class Endings24(ImperativeActive):

    conn_2S = "+η"
    conn_3S = "+η"
    conn_2P = "+η"
    conn_3P = "+ε"

    ending_2S = "τι"


class Endings21(ImperativeMiddle):

    conn_2S = "+ε"
    conn_3S = "+ε"
    conn_2P = "+ε"
    conn_3P = "+ε"


class Endings23(ImperativeMiddle):

    conn_2S = "α"
    conn_3S = "α"
    conn_2P = "α"
    conn_3P = "α"

    ending_2S = "ι"


class Endings25(ImperativeMiddle2):

    pass


class Endings25B(ImperativeMiddle):

    pass


class ParticipleEndings:

    conn_NSM = ""
    conn_GSM = ""
    conn_NSF = ""
    conn_GSF = ""
    conn_NSN = ""
    conn_GSN = ""

    prep_stem_NSM = nothing
    prep_stem_GSM = nothing
    prep_stem_NSF = nothing
    prep_stem_GSF = nothing
    prep_stem_NSN = nothing
    prep_stem_GSN = nothing

    accentuation_NSM = nothing
    accentuation_GSM = nothing
    accentuation_NSF = nothing
    accentuation_GSF = nothing
    accentuation_NSN = nothing
    accentuation_GSN = nothing

    def __init__(self, stem):
        self.stem = stem

    def NSM(self): return self.accentuation_NSM(phon(self.prep_stem_NSM(self.stem) + self.conn_NSM + self.ending_NSM))
    def GSM(self): return self.accentuation_GSM(phon(self.prep_stem_GSM(self.stem) + self.conn_GSM + self.ending_GSM))
    def NSF(self): return self.accentuation_NSF(phon(self.prep_stem_NSF(self.stem) + self.conn_NSF + self.ending_NSF))
    def GSF(self): return self.accentuation_GSF(phon(self.prep_stem_GSF(self.stem) + self.conn_GSF + self.ending_GSF))
    def NSN(self): return self.accentuation_NSN(phon(self.prep_stem_NSN(self.stem) + self.conn_NSN + self.ending_NSN))
    def GSN(self): return self.accentuation_GSN(phon(self.prep_stem_GSN(self.stem) + self.conn_GSN + self.ending_GSN))


class ActiveParticiple(ParticipleEndings):

    ending_NSM = "+ων"
    ending_GSM = "ντος"
    ending_NSF = "+εσα"
    ending_GSF = "+εσης"
    ending_NSN = "ν"
    ending_GSN = "ντος"


class ActiveParticiple2(ActiveParticiple):

    ending_NSM = "+ες"


class PerfectActiveParticiple(ParticipleEndings):

    ending_NSM = "+ως"
    ending_GSM = "+οτος"
    ending_NSF = "+υια"
    ending_GSF = "+υιας"
    ending_NSN = "+ος"
    ending_GSN = "+οτος"

    accentuation_NSM = oxytone
    accentuation_GSM = paroxytone
    accentuation_NSF = properispomenon
    accentuation_GSF = properispomenon
    accentuation_NSN = oxytone
    accentuation_GSN = paroxytone


class MiddleParticiple(ParticipleEndings):

    ending_NSM = "μενος"
    ending_NSF = "μενη"
    ending_NSN = "μενον"


class Endings26(ActiveParticiple):

    conn_GSM = "+ο"
    conn_NSF = "+ο"
    conn_GSF = "+ο"
    conn_NSN = "+ο"
    conn_GSN = "+ο"

    accentuation_NSM = paroxytone
    accentuation_GSM = proparoxytone
    accentuation_NSF = proparoxytone
    accentuation_GSF = proparoxytone
    accentuation_NSN = properispomenon
    accentuation_GSN = proparoxytone


class Endings26Contract(Endings26):

    accentuation_NSM = perispomenon
    accentuation_GSM = properispomenon
    accentuation_NSF = properispomenon
    accentuation_GSF = properispomenon
    accentuation_NSN = perispomenon
    accentuation_GSN = properispomenon


class Endings26mi(ActiveParticiple2):

    accentuation_NSM = oxytone
    accentuation_GSM = paroxytone
    accentuation_NSF = properispomenon
    accentuation_GSF = paroxytone
    accentuation_NSN = oxytone
    accentuation_GSN = paroxytone


class Endings28(ActiveParticiple2):

    conn_NSM = "+α"
    conn_GSM = "+α"
    conn_NSF = "+α"
    conn_GSF = "+α"
    conn_NSN = "+α"
    conn_GSN = "+α"

    accentuation_NSM = paroxytone
    accentuation_GSM = proparoxytone
    accentuation_NSF = proparoxytone
    accentuation_GSF = proparoxytone
    accentuation_NSN = properispomenon
    accentuation_GSN = proparoxytone


class Endings30(ActiveParticiple2):

    conn_NSM = "+ε"
    conn_NSF = "+ε"
    conn_NSN = "+ε"

    accentuation_NSM = oxytone
    accentuation_NSF = properispomenon
    accentuation_NSN = oxytone


class Endings32(MiddleParticiple):

    accentuation_NSM = paroxytone
    accentuation_NSF = paroxytone
    accentuation_NSN = paroxytone


class Endings27mi(MiddleParticiple):

    accentuation_NSM = proparoxytone
    accentuation_NSF = paroxytone
    accentuation_NSN = proparoxytone


class Endings27(MiddleParticiple):

    conn_NSM = "+ο"
    conn_NSF = "+ο"
    conn_NSN = "+ο"

    accentuation_NSM = proparoxytone
    accentuation_NSF = paroxytone
    accentuation_NSN = proparoxytone


class Endings29(MiddleParticiple):

    conn_NSM = "+α"
    conn_NSF = "+α"
    conn_NSN = "+α"

    accentuation_NSM = proparoxytone
    accentuation_NSF = paroxytone
    accentuation_NSN = proparoxytone


class Endings31(PerfectActiveParticiple):

    pass


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
    def PAP(self): return Endings26Contract(self.stem1)


class Verb1B(Verb1C):

    def PMI(self): return Endings2B(self.stem1)
    def PAP(self): return Endings26Contract(self.stem1)


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
    def AMI(self): return Endings11(aug(self.stem2))


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
        elif stem[0] == "ἑ":
            return "εἱ" + stem[1:]
        else:
            raise NotImplementedError(stem)
    else:
        return "ἐ" + stem


def redup(stem):
    if is_vowel(stem[0]):
        raise NotImplementedError(stem)
    else:
        return stem[0] + "ε" + stem


def calculate_form(entry, parse):
    c = entry
    for step in parse.split("."):
        if step[0] in "123":
            step = "_" + step
        c = getattr(c(), step)

    return strip_length(c().replace("+", "")), (c.__self__.__class__.__name__, c.__qualname__)
