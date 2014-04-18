from django.contrib import admin
from img_upload.models import Image, Album, Tag, Attending

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__unicode__","title","user", "eDate", "description"]
	list_filter = ["tags", "albums"]

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title"]

class TagAdmin(admin.ModelAdmin):
	list_display = ["tag"]

class AttendingAdmin(admin.ModelAdmin):
	list_display = ["user"]

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Attending, AttendingAdmin)
