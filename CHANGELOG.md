
## 2026/11/14 - Version 0.3.0
- Renamed translate_text_to_braille() to convert_text_to_braille_data().
- Consolidated Braille conversion outputs into a single method supporting ten return types (0–9).
- Centralized index generation to avoid repeated conversions.
- Standardized data retrieval for all output types, including full data and mirrored Braille.
- Preserved the default behavior: unrecognized types return the standard Braille character list (type 0).
- Reduced the number of methods dependent on the conversion method from 18 to 13.

## 2026/9/6 - Version 0.2.9 Sumary
- Update to the logic that processes uppercase and lowercase characters.
