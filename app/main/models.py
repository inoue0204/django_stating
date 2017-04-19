from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import logging
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nick_name = models.CharField('ニックネーム', max_length=128, blank=True)

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pref_code = models.IntegerField('都道府県', blank=False)
    city = models.CharField('市区町村', max_length=10, blank=True)

class Book(models.Model):
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name='感想', related_name='impressions')
    comment = models.TextField('コメント', blank=True)