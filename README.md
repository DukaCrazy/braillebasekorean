### - pip install braillebasekorean

# Korean

```python
from braillebasekorean import BrailleBaseKorean

bbk = BrailleBaseKorean()
print(bbk.output_braille_txt("우리는 한국 점자의 역사에 참여하게 되어 매우 기쁩니다!"))
```
Output: ⠍⠐⠕⠉⠪⠒⠀⠚⠣⠒⠈⠍⠁⠀⠨⠎⠢⠨⠣⠺⠀⠱⠁⠠⠣⠝⠀⠰⠣⠢⠱⠚⠣⠈⠝⠀⠊⠽⠎⠀⠑⠗⠍⠀⠈⠕⠠⠘⠪⠃⠉⠕⠊⠣⠖

# Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.

## Pre-registered Letters and Characters
78 >>> Jamo
        
        CHOSEONG = (
            "ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ",
            "ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
        )

        JUNGSEONG = (
            "ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ",
            "ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"
        )

        JONGSEONG = (
            "", "ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ",
            "ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ",
            "ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
        )

11172 >>> Hangul

```python
from braillebasekorean import BrailleBaseKorean

bbk = BrailleBaseKorean()
print(bbk.confidence_test("우리는 한국 점자의 역사에 참여하게 되어 매우 기쁩니다!"))
```

Output: {0: ['우', ['⠍']], 1: ['리', ['⠐', '⠕']], 2: ['는', ['⠉', '⠪', '⠒']], 3: [' ', ['⠀']], 4: ['한', ['⠚', '⠣', '⠒']], 5: ['국', ['⠈', '⠍', '⠁']], 6: [' ', ['⠀']], 7: ['점', ['⠨', '⠎', '⠢']], 8: ['자', ['⠨', '⠣']], 9: ['의', ['⠺']], 10: [' ', ['⠀']], 11: ['역', ['⠱', '⠁']], 12: ['사', ['⠠', '⠣']], 13: ['에', ['⠝']], 14: [' ', ['⠀']], 15: ['참', ['⠰', '⠣', '⠢']], 16: ['여', ['⠱']], 17: ['하', ['⠚', '⠣']], 18: ['게', ['⠈', '⠝']], 19: [' ', ['⠀']], 20: ['되', ['⠊', '⠽']], 21: ['어', ['⠎']], 22: [' ', ['⠀']], 23: ['매', ['⠑', '⠗']], 24: ['우', ['⠍']], 25: [' ', ['⠀']], 26: ['기', ['⠈', '⠕']], 27: ['쁩', ['⠠', '⠘', '⠪', '⠃']], 28: ['니', ['⠉', '⠕']], 29: ['다', ['⠊', '⠣']], 30: ['!', ['⠖']]}


### The developed algorithm demonstrates accuracy for its intended purpose. If necessary, we may require the assistance of a specialist to review and validate the underlying Jamo mapping table.