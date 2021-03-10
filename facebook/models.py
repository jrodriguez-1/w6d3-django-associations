from django.db import models
from django.core.validators import EmailValidator, URLValidator

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, validators=[EmailValidator])

    def __str__(self):
        return f"{self.name}"

class UserProfile(models.Model):
    url = models.CharField(max_length=256, validators=[URLValidator])
    profile_image = models.CharField(max_length=256, validators=[URLValidator], blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.url}"


class Expression(models.Model):
    expression = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.expression}"





class GenericExpression(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey("content_type", "object_id")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="g_expressions")
    
    expression = models.ForeignKey(Expression, on_delete=models.CASCADE, related_name="g_expressions")

    def __str__(self):
        return f"{self.user} expressed {self.expression} for {self.content}"




class Post(models.Model):
    text = models.CharField(max_length=1024)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    expressions = GenericRelation(GenericExpression)

    def __str__(self):
        return f"POST {self.text} by {self.poster}"

class Comment(models.Model):
    text = models.CharField(max_length=1024)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    expressions = GenericRelation(GenericExpression)

    def __str__(self):
        return f"COMMENT {self.text} by {self.commenter} on {self.post}"

class Reply(models.Model):
    text = models.CharField(max_length=1024)
    replier = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    expressions = GenericRelation(GenericExpression)

    def __str__(self):
        return f"REPLY: {self.text} by {self.replier} on {self.comment}"


class PostExpression(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="post_expressions")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_expressions")
    
    expression = models.ForeignKey(Expression, on_delete=models.CASCADE, related_name="post_expressions")

    def __str__(self):
        return f"{self.user} expressed {self.expression} for {self.post}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post", "user"], name="post_user_expression")
        ]