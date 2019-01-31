# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'


from django import forms

class TagForm(forms.Form):
    city = forms.CharField(label='tag i.e cute', max_length=100)
