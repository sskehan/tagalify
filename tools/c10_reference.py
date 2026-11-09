from dsl import *

REFERENCE = {
    "title": "Cheat sheet",
    "intro": "Every rule from Lessons 1 to 8 on one page. Tap any coloured word to hear it.",
    "sections": [
        {"id": "order", "title": "How a sentence is built", "blocks": [
            PAT("Predicate first (everyday)",
                [("Pattern", [("Malaki", "pred"), ("ang", "marker"), ("bahay", "noun")])],
                note="The big thing comes first. The house is big."),
            PAT("Subject first (with ay)",
                [("Pattern", [("Ang", "marker"), ("bahay", "noun"), ("ay", "ay"), ("malaki", "pred")])],
                note="Ay appears only when the subject comes first."),
            P("To flip: move the predicate to the front, delete ay, keep the marker with the subject."),
        ]},
        {"id": "markers", "title": "Markers", "blocks": [
            TABLE(["Job", "Name", "Common noun", "More than one"],
                  [["Subject", "[[si|marker]]", "[[ang|marker]]", "[[sina|marker]] / [[ang mga|marker]]"],
                   ["Owner (of)", "[[ni|marker]]", "[[ng|marker]]", "[[nina|marker]] / [[ng mga|marker]]"],
                   ["Place (at, to, in)", "[[kay|marker]]", "[[sa|marker]]", "[[kina|marker]] / [[sa mga|marker]]"]],
                  note="Names use si / ni / kay. Common nouns use ang / ng / sa."),
        ]},
        {"id": "pronouns", "title": "Pronouns", "blocks": [
            TABLE(["English", "Subject (after the predicate)", "Owner, after the noun", "Owner, before the noun", "Basic form"],
                  [["I, me, my", "[[ako|pron]]", "[[ko|poss]]", "[[aking|poss]]", "[[akin|poss]]"],
                   ["you (one)", "[[ikaw|pron]] / [[ka|pron]]", "[[mo|poss]]", "[[iyong|poss]]", "[[iyo|poss]]"],
                   ["he, she", "[[siya|pron]]", "[[niya|poss]]", "[[kaniyang|poss]]", "[[kaniya|poss]]"],
                   ["we (not you)", "[[kami|pron]]", "[[namin|poss]]", "[[aming|poss]]", "[[amin|poss]]"],
                   ["we (with you)", "[[tayo|pron]]", "[[natin|poss]]", "[[ating|poss]]", "[[atin|poss]]"],
                   ["you (plural, polite)", "[[kayo|pron]]", "[[ninyo|poss]]", "[[inyong|poss]]", "[[inyo|poss]]"],
                   ["they", "[[sila|pron]]", "[[nila|poss]]", "[[kanilang|poss]]", "[[kanila|poss]]"]]),
            TABLE(["Near me", "Near you", "Far from both"],
                  [["[[ito|pron]] (this)", "[[iyan|pron]] (that)", "[[iyon|pron]] (that over there)"],
                   ["[[nito|poss]] (of this)", "[[niyan|poss]] (of that)", "[[niyon|poss]] (of that over there)"]],
                  title="This and that"),
        ]},
        {"id": "linkers", "title": "Linkers", "blocks": [
            TABLE(["The first word ends in…", "Linker", "Example"],
                  [["a vowel", "[[-ng|link]]", "[[malaking bahay|noun]]"],
                   ["n", "[[-g|link]]", "[[mayamang lalaki|noun]]"],
                   ["any other consonant", "[[na|link]]", "[[mabait na bata|noun]]"]]),
            BOX("remember", "Remember", items=[
                "The first word decides the linker, in either order.",
                "With several adjectives, only the last takes the linker.",
                "Repeat an adjective with na for emphasis: malinaw na malinaw."]),
        ]},
        {"id": "possession", "title": "Possession", "blocks": [
            PAT("Thing first, owner second",
                [("Pattern", [("ang", "marker"), ("bahay", "noun"), ("ni", "marker"), ("Ana", "noun")])]),
            BOX("rule", "Rules", items=[
                "Plural: ang aking mga anak (possessive before mga).",
                "Mix one before-form and one after-form: ang aking ina ... bahay ko."]),
        ]},
        {"id": "polite", "title": "Politeness", "blocks": [
            TABLE(["Word", "Use"],
                  [["[[po|part]]", "polite, for elders and strangers (any sentence)"],
                   ["[[ho|part]]", "polite, a little softer (after a word ending in a vowel it can sound smoother)"],
                   ["[[opo|part]]", "polite yes"],
                   ["[[oho|part]]", "polite yes, a little softer"]]),
        ]},
        {"id": "sounds", "title": "Sounds and stress", "blocks": [
            TABLE(["Sign", "Meaning"],
                  [["CAPITALS in Say it", "stressed syllable, said louder and a little longer"],
                   ["ʔ", "glottal stop: a tiny catch of the throat at the end"],
                   ["ng", "one sound, like the end of \"sing\""],
                   ["r", "a quick tap of the tongue, like the middle of \"butter\""]]),
        ]},
    ],
}
