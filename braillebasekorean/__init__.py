from braillebase import *
from koreanwritingsystem import KoreanWritingSystem

class BrailleBaseKorean(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        
        self.setting_braille_rules_uppercase("⠠", "⠠") #2026/06/08

        CHOSEONG = [
        ["lㄱ", ["⠈"], 2], 
        ["lㄲ", ["⠠","⠈"], 2], 
        ["lㄴ", ["⠉"], 2], 
        ["lㄷ", ["⠊"], 2], 
        ["lㄸ", ["⠠","⠊"], 2], 
        ["lㄹ", ["⠐"], 2], 
        ["lㅁ", ["⠑"], 2], 
        ["lㅂ", ["⠘"], 2],  
        ["lㅃ", ["⠠","⠘"], 2], 
        ["lㅅ", ["⠠"], 2], 
        ["lㅆ", ["⠠","⠠"], 2], 
        #["lㅇ", [""], 2], 
        ["lㅈ", ["⠨"], 2], 
        ["lㅉ", ["⠠","⠨"], 2], 
        ["lㅊ", ["⠰"], 2], 
        ["lㅋ", ["⠋"], 2], 
        ["lㅌ", ["⠓"], 2], 
        ["lㅍ", ["⠙"], 2], 
        ["lㅎ", ["⠚"], 2]] #2026/08/24

        JUNGSEONG = [
        ["vㅏ", ["⠣"], 2], 
        ["vㅐ", ["⠗"], 2], 
        ["vㅑ", ["⠜"], 2], 
        ["vㅒ", ["⠜", "⠗"], 2], 
        ["vㅓ", ["⠎"], 2], 
        ["vㅔ", ["⠝"], 2], 
        ["vㅕ", ["⠱"], 2], 
        ["vㅖ", ["⠌"], 2], 
        ["vㅗ", ["⠥"], 2], 
        ["vㅘ", ["⠧"], 2], 
        ["vㅙ", ["⠧","⠗"], 2], 
        ["vㅚ", ["⠽"], 2], 
        ["vㅛ", ["⠬"], 2], 
        ["vㅜ", ["⠍"], 2], 
        ["vㅝ", ["⠏"], 2], 
        ["vㅞ", ["⠏","⠗"], 2], 
        ["vㅟ", ["⠍","⠗"], 2], 
        ["vㅠ", ["⠩"], 2], 
        ["vㅡ", ["⠪"], 2], 
        ["vㅢ", ["⠺"], 2], 
        ["vㅣ", ["⠕"], 2]] #2026/08/24

        JONGSEONG = [
        #["", [""], 2],
        ["tㄱ", ["⠁"], 2], 
        ["tㄲ", ["⠁","⠁"], 2], 
        ["tㄳ", ["⠁","⠄"], 2],
        ["tㄴ", ["⠒"], 2], 
        ["tㄵ", ["⠒","⠅"], 2],
        ["tㄶ", ["⠒","⠴"], 2],
        ["tㄷ", ["⠔"], 2], 
        ["tㄹ", ["⠂"], 2], 
        ["tㄺ", ["⠂","⠁"], 2],
        ["tㄻ", ["⠂","⠢"], 2],
        ["tㄼ", ["⠂","⠃"], 2],
        ["tㄽ", ["⠂","⠄"], 2],
        ["tㄾ", ["⠂","⠦"], 2],
        ["tㄿ", ["⠂","⠲"], 2],
        ["tㅀ", ["⠂","⠴"], 2],
        ["tㅁ", ["⠢"], 2], 
        ["tㅂ", ["⠃"], 2],  
        ["tㅄ", ["⠃","⠄"], 2],
        ["tㅅ", ["⠄"], 2], 
        ["tㅆ", ["⠄","⠄"], 2], 
        ["tㅇ", ["⠶"], 2], 
        ["tㅈ", ["⠅"], 2], 
        ["tㅊ", ["⠆"], 2], 
        ["tㅋ", ["⠖"], 2], 
        ["tㅌ", ["⠦"], 2], 
        ["tㅍ", ["⠲"], 2], 
        ["tㅎ", ["⠴"], 2]] #2026/08/27

        self.append_multiple_braille_letters(CHOSEONG)
        self.append_multiple_braille_letters(JUNGSEONG)
        self.append_multiple_braille_letters(JONGSEONG)

        for codepoint in range(0xAC00, 0xD7A3 + 1):
            register_list = []

            hangul = chr(codepoint)
            hangul_list = KoreanWritingSystem.decompose_hangul_to_jamo(hangul, True)

            # CHOSEONG
            jamo_l = hangul_list[0]
            if jamo_l != "lㅇ":
                braille_l = self.output_braille_txt(jamo_l)
                if braille_l:
                    register_list.extend(braille_l)

            # JUNGSEONG
            jamo_v = hangul_list[1]
            braille_v = self.output_braille_txt(jamo_v)
            if braille_v:
                register_list.extend(braille_v)

            # JONGSEONG
            if len(hangul_list) == 3:
                jamo_t = hangul_list[2]
                braille_t = self.output_braille_txt(jamo_t)
                if braille_t:
                    register_list.extend(braille_t)

            self.append_braille_letter(hangul, register_list, 2)
    