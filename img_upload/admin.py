from django.contrib import admin
from img_upload.models import Image, Album, Tag, Attending, Event

# Register your models here.

## Image class has fields: 
## title eDate image tags description albums user pub_date
class EventAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__unicode__","title", "image", "user", "attending_", "tags_", "eDate", "is_upcoming_event", "description"]
	list_filter = ["tags", "user"]

class ImageAdmin(admin.ModelAdmin):
	search_fields = ["albums"]
	list_display = ["__unicode__","album_"]
	list_filter = ["image", "albums"]

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title", "public"]

## Has: tag, image
class TagAdmin(admin.ModelAdmin):
	list_display = ["tag"]

## Has: user, image
class AttendingAdmin(admin.ModelAdmin):
	list_display = ["user"]

admin.site.register(Event, EventAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Attending, AttendingAdmin)
