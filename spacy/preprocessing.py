def is_token_allowed(token, skip_punctuation=False, skip_one_letter_length=False):
    if skip_punctuation and skip_one_letter_length:
        if not token or not token.text.strip() or token.is_punct or len(token) == 1:
            return False
        return True
    if skip_punctuation:
        if not token or not token.text.strip() or token.is_punct:
            return False
        return True
    if skip_one_letter_length:
        if not token or not token.text.strip() or len(token) == 1:
            return False
        return True
    return token and token.text.strip()
