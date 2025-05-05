from django.db import models
from django.contrib.auth import get_user_model
from skills.models import Skill

User = get_user_model()


# Create your models here.

class Swap(models.Model):
    requester = models.ForeignKey(User, related_name='sent_swaps', on_delete=models.CASCADE)
    requested_skill = models.ForeignKey(Skill, related_name='incoming_swaps', on_delete=models.CASCADE)
    offered_skill = models.ForeignKey(Skill, related_name='outgoing_swaps', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requester.username} offers {self.offered_skill.skill_name} for {self.requested_skill.skill_name}"