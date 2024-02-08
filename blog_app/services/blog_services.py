from blog_app.validators.blog_validator import BlogValidator


class BlogServices:

    @staticmethod
    def custom_create(data):
        response = BlogValidator().custom_create(data)
        response.get('serializer').save()
        return response.get('serializer').data

    @staticmethod
    def custom_update(data, blog_id):
        response = BlogValidator().custom_update(data, blog_id)
        response.get('serializer').save()
        return response.get('serializer').data

    @staticmethod
    def create_blog_comment(data):
        response = BlogValidator().create_blog_comments(data)
        response.get('serializer').save()
        return response.get('serializer').data
