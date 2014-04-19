from django.contrib import admin
from img_upload.models import Image, Album, Tag, Attending

# Register your models here.

## Image class has fields: 
## title eDate image tags description albums user pub_date
class ImageAdmin(admin.ModelAdmin):

	search_fields = ["title"]
	list_display = ["__unicode__","title", "user", "tags_", "album_", "eDate", "thumbnail", "is_upcoming_event", "description"]
	list_filter = ["tags", "albums"]

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title", "public"]

## Has: tag, image
class TagAdmin(admin.ModelAdmin):
	list_display = ["tag"]

## Has: user, image
class AttendingAdmin(admin.ModelAdmin):
	list_display = ["image", "user"]

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Attending, AttendingAdmin)
