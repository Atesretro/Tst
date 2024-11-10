def get_love_message(user_username: str, target_username: str, love_percentage: int) -> str:
    """Return a love message based on the love percentage."""
    if 0 <= love_percentage <= 10:
        return f"@{user_username} and @{target_username} There’s a small spark between you two, your love percentage is... %{love_percentage}."
    elif 11 <= love_percentage <= 21:
        return f"@{user_username} and @{target_username} There’s a slight attraction between you two, your love percentage is... %{love_percentage}."
    elif 22 <= love_percentage <= 33:
        return f"@{user_username} and @{target_username} There’s a small amount of chemistry between you, your love percentage is... %{love_percentage}."
    elif 34 <= love_percentage <= 45:
        return f"@{user_username} and @{target_username} There’s a positive attraction between you, your love percentage is… %{love_percentage}."
    elif 46 <= love_percentage <= 67:
        return f"@{user_username} and @{target_username} There’s a strong attraction between you, your love percentage is… %{love_percentage}."
    elif 68 <= love_percentage <= 79:
        return f"@{user_username} and @{target_username} There is a very high compatibility between you, your love percentage is… %{love_percentage}."
    elif 80 <= love_percentage <= 91:
        return f"@{user_username} and @{target_username} There is a perfect connection between you, your love percentage is… %{love_percentage}."
    else:  # 92-100
        return f"@{user_username} and @{target_username} There is a flawless compatibility between you, your love percentage is… %{love_percentage}!"


def get_friendship_message(user_username: str, target_username: str, friendship_score: int) -> str:
    """Return a friendship message based on the friendship score."""
    if 0 <= friendship_score <= 10:
        return f"@{user_username} and @{target_username} There is a very low level of friendship between you, your friendship score is… %{friendship_score}."
    elif 11 <= friendship_score <= 30:
        return f"@{user_username} and @{target_username} There is a low level of friendship between you, your friendship score is… %{friendship_score}."
    elif 31 <= friendship_score <= 50:
        return f"@{user_username} and @{target_username} There is an average level of friendship between you, your friendship score is… %{friendship_score}."
    elif 51 <= friendship_score <= 70:
        return f"@{user_username} and @{target_username} There is a good level of friendship between you, your friendship score is… %{friendship_score}."
    elif 71 <= friendship_score <= 90:
        return f"@{user_username} and @{target_username} There is a high level of friendship between you, your friendship score is… %{friendship_score}."
    else:  # 91-100
        return f"@{user_username} and @{target_username} There is a perfect friendship between you, your friendship score is… %{friendship_score}!"



def get_hate_message(user_username: str, target_username: str, hate_percentage: int) -> str:
    """Return a hate message based on the hate percentage."""
    if 0 <= hate_percentage <= 10:
        return f"@{user_username} and @{target_username} There is a very low level of hatred between you, your hatred score is… %{hate_percentage}."
    elif 11 <= hate_percentage <= 30:
        return f"@{user_username} and @{target_username} There is a low level of hatred between you, your hatred score is… %{hate_percentage}."
    elif 31 <= hate_percentage <= 50:
        return f"@{user_username} and @{target_username} There is an average level of hatred between you, your hatred score is… %{hate_percentage}."
    elif 51 <= hate_percentage <= 70:
        return f"@{user_username} and @{target_username} There is a high level of hatred between you, your hatred score is… %{hate_percentage}."
    elif 71 <= hate_percentage <= 90:
        return f"@{user_username} and @{target_username} There is a very high level of hatred between you, your hatred score is… %{hate_percentage}."
    else:  # 91-100
        return f"@{user_username} and @{target_username} There is an intense level of hatred between you, your hatred score is… %{hate_percentage}!"


def get_trust_message(user_username: str, target_username: str, trust_level: int) -> str:
    """Return a trust message based on the trust level."""
    if 0 <= trust_level <= 20:
        return f"@{user_username} and @{target_username} There is a very low level of trust between you, your trust percentage is… %{trust_level}."
    elif 21 <= trust_level <= 40:
        return f"@{user_username} and @{target_username} There is a low level of trust between you, your trust percentage is… %{trust_level}."
    elif 41 <= trust_level <= 60:
        return f"@{user_username} and @{target_username} There is an average level of trust between you, your trust percentage is… %{trust_level}."
    elif 61 <= trust_level <= 80:
        return f"@{user_username} and @{target_username} There is a high level of trust between you, your trust percentage is… %{trust_level}."
    else:  # 81-100
        return f"@{user_username} and @{target_username} There is a very high level of trust between you, your trust percentage is… %{trust_level}!"