from django import forms
from django.utils.safestring import mark_safe


# creating a form
class InputForm(forms.Form):

	ad_url = forms.URLField()
	utm_source = forms.CharField(label=mark_safe('<br /><br />UTM Source'))
	utm_medium = forms.CharField(label=mark_safe('<br /><br />UTM Medium'))
	utm_campaign = forms.CharField(label=mark_safe('<br /><br />UTM Campaign'))
	utm_content = forms.CharField(label=mark_safe('<br /><br />UTM Content'))
	utm_term = forms.CharField(label=mark_safe('<br /><br />UTM Term'))
