import re
import urllib.parse


def build_keyboard(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


# https://stackoverflow.com/a/49146722/330558
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def get_share_url(title, text):
    title = urllib.parse.quote(title)
    text = urllib.parse.quote(text)
    return 'https://telegram.me/share/url?url={title}&text={text}'.format(title=title, text=text)
