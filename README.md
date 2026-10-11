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

## 1. Linguistic and Technological Foundation
<p>BrailleBaseKorean is feasible because the structure of the Korean language follows a logical system that facilitates the identification and decomposition of the jamo that make up Hangul. This structure makes it possible to develop clean algorithms that follow systematic rules for converting text into braille.</p>

## 2. Educational Impact and Accessibility
<p> The tool has the potential to serve a wide range of audiences:<br>
<br>
Korean language educators: Teachers without technical knowledge of braille can produce accessible materials from authentic Korean texts.<br>
<br>
Individuals interested in braille: People who want to learn, study, or explore the tactile reading and writing system.<br>
<br>
Blind foreign learners of Korean: Individuals who can use authentic Korean texts to create their own accessible learning materials.<br>
<br>
The goal is to simplify the process: users simply copy and paste Korean text into the tool to generate the corresponding braille output. </p>

## 3. Generation of Multiple Formats and Representations
<p>In addition to converting text, BrailleBaseKorean can generate metadata in structured formats such as XML and JSON, expanding the possibilities for data integration and reuse.<br>
<br>
Another distinguishing feature is its ability to generate both the braille representation and its mirrored version, which indicates the positions of the six dots to be embossed or punched into paper to create a tactile representation readable by blind users.<br>
<br>
This functionality bridges the gap between digital text conversion and the physical production of braille materials.</p>
