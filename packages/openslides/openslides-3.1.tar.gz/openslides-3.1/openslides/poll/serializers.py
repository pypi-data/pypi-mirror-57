from ..utils.rest_api import ValidationError


def default_votes_validator(data):
    """
    Use this validator in your poll serializer. It checks that the values
    for the default votes (see models.CollectDefaultVotesMixin) are greater
    than or equal to -2.
    """
    for key in data:
        if (
            key in ("votesvalid", "votesinvalid", "votescast")
            and data[key] is not None
            and data[key] < -2
        ):
            raise ValidationError(
                {"detail": "Value for {0} must not be less than -2", "args": [key]}
            )
    return data
