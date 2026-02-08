def word_shape(word):
    # ye function word ki shape nikalta hai jese Google -> Xxxxx
    shape = ""
    for char in word:
        if char.isupper():
            shape += "X"
        elif char.islower():
            shape += "x"
        elif char.isdigit():
            shape += "d"
        else:
            shape += char
    return shape


def simplified_word_shape(word):
    # simplified version banata hai shape ka
    shape = word_shape(word)
    if not shape:
        return shape

    simplified = shape[0]
    for char in shape[1:]:
        if char != simplified[-1]:
            simplified += char
    return simplified


def extract_features(sentence, index):
    # ye main function hai jo sare features extract karta hai
    word = sentence[index]

    # basic features
    features = {
        "bias": 1.0,
        "word.lower()": word.lower(),
        "word.isupper()": word.isupper(),
        "word.istitle()": word.istitle(),
        "word.isdigit()": word.isdigit(),
        "word.isalpha()": word.isalpha(),
        "word.isalnum()": word.isalnum(),
        "word_shape": word_shape(word),
        "word_shape_short": simplified_word_shape(word),
    }

    # word ki length check karte hain
    features["word_length"] = len(word)
    features["word_length_bin"] = (
        "short" if len(word) < 4 else ("medium" if len(word) < 8 else "long")
    )

    # prefix nikal rahe hain different lengths ke
    for i in [1, 2, 3, 4]:
        if len(word) >= i:
            features[f"prefix_{i}"] = word[:i].lower()

    # suffix bhi same tarah se
    for i in [1, 2, 3, 4]:
        if len(word) >= i:
            features[f"suffix_{i}"] = word[-i:].lower()

    # character composition check kar rahe
    features["has_digit"] = any(char.isdigit() for char in word)
    features["has_upper"] = any(char.isupper() for char in word)
    features["has_lower"] = any(char.islower() for char in word)
    features["has_punct"] = any(not char.isalnum() for char in word)
    features["has_hyphen"] = "-" in word
    features["has_apostrophe"] = "'" in word

    # mixed case checking
    features["is_mixed_case"] = any(c.isupper() for c in word) and any(
        c.islower() for c in word
    )
    features["starts_with_upper"] = word[0].isupper() if word else False
    features["all_caps"] = word.isupper() and word.isalpha()

    # numeric pattern detect karne ke liye
    features["is_numeric"] = word.isdigit()
    features["contains_digit"] = any(c.isdigit() for c in word)
    features["is_year"] = (
        word.isdigit() and len(word) == 4 and word.startswith(("19", "20"))
    )

    # special patterns jese url wagera
    features["is_url_like"] = "www" in word.lower() or "http" in word.lower()
    features["is_email_like"] = "@" in word
    features["has_dot"] = "." in word

    # pichle word ka context
    if index > 0:
        prev_word = sentence[index - 1]
        features.update(
            {
                "-1:word.lower()": prev_word.lower(),
                "-1:word.istitle()": prev_word.istitle(),
                "-1:word.isupper()": prev_word.isupper(),
                "-1:word.isdigit()": prev_word.isdigit(),
                "-1:word_shape": word_shape(prev_word),
                "-1:suffix_2": (
                    prev_word[-2:].lower() if len(prev_word) >= 2 else prev_word.lower()
                ),
            }
        )
    else:
        features["BOS"] = True

    # agle word ka context
    if index < len(sentence) - 1:
        next_word = sentence[index + 1]
        features.update(
            {
                "+1:word.lower()": next_word.lower(),
                "+1:word.istitle()": next_word.istitle(),
                "+1:word.isupper()": next_word.isupper(),
                "+1:word.isdigit()": next_word.isdigit(),
                "+1:word_shape": word_shape(next_word),
                "+1:prefix_2": (
                    next_word[:2].lower() if len(next_word) >= 2 else next_word.lower()
                ),
            }
        )
    else:
        features["EOS"] = True

    # bigram features - do words ko combine kar k dekhte hain
    if index > 0:
        features["-1:0:words"] = f"{sentence[index-1].lower()}_{word.lower()}"
    if index < len(sentence) - 1:
        features["0:+1:words"] = f"{word.lower()}_{sentence[index+1].lower()}"

    # extended context window -2 aur +2 tak
    if index > 1:
        prev_prev_word = sentence[index - 2]
        features["-2:word.lower()"] = prev_prev_word.lower()
        features["-2:word.istitle()"] = prev_prev_word.istitle()

    if index < len(sentence) - 2:
        next_next_word = sentence[index + 2]
        features["+2:word.lower()"] = next_next_word.lower()
        features["+2:word.istitle()"] = next_next_word.istitle()

    # position features sentence mein kahan hai word
    features["position_in_sentence"] = index
    features["relative_position"] = (
        "start" if index < 3 else ("end" if index > len(sentence) - 4 else "middle")
    )

    return features
