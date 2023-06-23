from django.contrib import admin

from apps.users.models import User, Role, Group, Lesson


admin.site.register(User)
admin.site.register(Role)
admin.site.register(Group)
admin.site.register(Lesson)
