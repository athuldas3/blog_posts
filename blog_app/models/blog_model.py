# Blog Posts with fields for title, content, publication date, and author.
from django.db import models
from blog_app.models.base.abstract_base_model import AbstractBase
from blog_app.models.user_model import User


# abstract class brings in the default fields set to the model, example id:uuid, created_date etc.
class Blog(AbstractBase):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="blog_author")
    title = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    # already has a created_date field overing the abstract class so can be used as the published date

    class Meta:
        db_table = "blog"
        verbose_name_plural = "blogs"
        ordering = ('created_date', )


# comments
class Comment(AbstractBase):
    blog = models.ForeignKey(
        Blog, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="blog_comment")
    comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "comment"
        verbose_name_plural = "comments"
        ordering = ('created_date',)


class TagsCategories(AbstractBase):
    TAG_CHOICES = [
        ('t', 'tags'),
        ('c', 'categories'),
    ]
    type = models.CharField(max_length=1, choices=TAG_CHOICES)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tags_categories"
        verbose_name_plural = "tags_categories"
        ordering = ('created_date',)


# Tags or Categories for Blog
class BlogTags(AbstractBase):

    blog = models.ForeignKey(
        Blog, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="tags_blog")
    tags = models.ForeignKey(
        TagsCategories, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="blog_tags_categories")

    class Meta:
        db_table = "blog_tags"
        verbose_name_plural = "blog_tags"
        ordering = ('created_date',)
