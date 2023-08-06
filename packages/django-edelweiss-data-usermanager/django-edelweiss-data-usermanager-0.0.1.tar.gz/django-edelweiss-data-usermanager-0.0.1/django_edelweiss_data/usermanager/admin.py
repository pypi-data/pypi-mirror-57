from django.contrib import admin
from django import forms
from django.db import models

from .models import Dataset, User, Group, Published, InProgress, UserDataset, GroupDataset


class DatasetUserInline(admin.TabularInline):
    model = UserDataset


class DatasetGroupInline(admin.TabularInline):
    model = GroupDataset


class UserGroupInline(admin.TabularInline):
    model = Group.users.through


class ReadOnlyInline(admin.TabularInline):
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields


class DatasetInProgressInline(ReadOnlyInline):
    model = InProgress
    fields = ['name', 'created']


class DatasetPublishedInline(ReadOnlyInline):
    model = Published
    fields = ['version', 'name', 'created']


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = [DatasetPublishedInline, DatasetInProgressInline, DatasetUserInline, DatasetGroupInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [DatasetUserInline, UserGroupInline]
    exclude = ['datasets']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [DatasetGroupInline, UserGroupInline]
    exclude = ['datasets', 'users']

    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput},
    }
