from django.contrib import admin
from adminpp import admin_models
from post.models import Post, PostReply


class PostAdminModel(admin_models.AdminModel):
    title = admin_models.CharField()
    content = admin_models.CharField()
    user = admin_models.CharField(source='author')

    class Meta:
        model = Post

    def get_queryset(self):
        return super(PostAdminModel, self).get_queryset()


class PostReplyAdminModel(admin_models.AdminModel):
    content = admin_models.CharField()

    class Meta:
        model = PostReply


admin_models.adminpp_register(admin.site, PostAdminModel)
admin_models.adminpp_register(admin.site, PostReplyAdminModel)
