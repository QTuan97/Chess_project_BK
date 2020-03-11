from django.contrib import admin
from .models import Questions,Choices
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choices
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']



admin.site.register(Questions, QuestionAdmin)

admin.site.register(Choices)

