from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=2048)
    length = models.IntegerField()

    def __str__(self):
        return f"id:{self.pk}, name:{self.name}"


class User(models.Model):
    name = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson, through='WatchStatus',
                                     through_fields=('user', 'lesson'), related_name='users')

    def __str__(self):
        return f"id:{self.pk}, name:{self.name}"


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='product_owner')
    name = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson, related_name='products')
    users = models.ManyToManyField(User, through="Access", through_fields=('product', 'user'), related_name='products')

    def __str__(self):
        return f"id:{self.pk}, name:{self.name}, owner:({self.owner}), lessons:({self.lessons}), users:({self.users})"


class Access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'user',)

    def __str__(self):
        return f"Access to Product '{self.product.name}' " \
               f"is {'blocked' if self.blocked else 'granted'} for user {self.user.name}"


class WatchStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.IntegerField()
    watched = models.IntegerField(default=0)
    last_watch_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('lesson', 'user',)

    def __str__(self):
        return f"So far user '{self.user.name}' has watched '{self.lesson.name}' for {self.watch_time} sec. Lesson is" \
               f"marked as '{'watched' if self.watched else 'not watched'}'. Last watch at {self.last_watch_date} "




