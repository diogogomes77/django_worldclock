from django.contrib import admin

from app.models import ChosenCountry, Profile, Country


class ChosenCountryInline(admin.TabularInline):
    model = ChosenCountry
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    inlines = [ChosenCountryInline, ]


admin.site.register(Profile, ProfileAdmin)


class ProfileInline(admin.TabularInline):
    model = Country.profiles.through
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]


admin.site.register(Country, CountryAdmin)


#class ChosenCountryAdmin(admin.ModelAdmin):

admin.site.register(ChosenCountry)