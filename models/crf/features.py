def word_features(sentence, index):
    word = sentence[index]

    features = {
        "word": word,
        "is_upper": word.isupper(),
        "is_title": word.istitle(),
        "is_digit": word.isdigit(),
        "prefix_3": word[:3],
        "suffix_3": word[-3:],
    }

    if index > 0:
        prev_word = sentence[index - 1]
        features["prev_word"] = prev_word

    if index < len(sentence) - 1:
        next_word = sentence[index + 1]
        features["next_word"] = next_word

    return features
