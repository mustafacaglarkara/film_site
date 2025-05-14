from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost, BlogCategory


class BlogPostTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content",
    )


translator.register(BlogPost, BlogPostTranslationOptions)


class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(BlogCategory, BlogCategoryTranslationOptions)
