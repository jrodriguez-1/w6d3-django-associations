from facebook.models import User, Post, Comment, Reply, Expression, PostExpression, GenericExpression

# delete all data
User.objects.all().delete()
Post.objects.all().delete()
Comment.objects.all().delete()
Reply.objects.all().delete()
Expression.objects.all().delete()
PostExpression.objects.all().delete()
GenericExpression.objects.all().delete()

# create users
u1 = User(name="Joe Biden", email="joe@whitehouse.gov")
u1.save()

u2 = User(name="Jill Biden", email="jill@whitehouse.gov")
u2.save()

# create posts
p1 = Post(poster=u1, text="We sent Major and Champ back home :(")
p1.save()

p2 = Post(poster=u1, text="Stimulus Care Package got passed!")
p2.save()

# create comments
c1 = Comment(commenter=u2, text="Major bit one of our security staff", post=p1)
c1.save()

c2 = Comment(commenter=u2, text="Sad to see the dogs leave", post=p1)
c2.save()

def qprint(title, qset):
    print("==", title, "==")
    for q in qset:
        print(q)

qprint(p1.text, p1.comments.all())

# expressions
x1 = Expression(expression="LIKE")
x1.save()

x2 = Expression(expression="SAD")
x2.save()

x3 = Expression(expression="FUNNY")
x3.save()

# post-expressions
px1 = PostExpression(post=p1, user=u2, expression=x2)
px1.save()

qprint("post1 expressions", p1.post_expressions.all())

# generic-expressions (can be used with posts, comments, and replies!)
gx1 = GenericExpression(content=p1, user=u2, expression=x2)
gx1.save()

qprint("post1 generic expressions", p1.expressions.all())

gx2 = GenericExpression(content=c1, user=u1, expression=x1)
gx2.save()

qprint("comment1 generic expressions", c1.expressions.all())
