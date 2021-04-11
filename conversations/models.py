from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampledModel):
    """ Corversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "Number of message"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of message"


class Message(core_models.TimeStampledModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user} says "{self.message}"'
