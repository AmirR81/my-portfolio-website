from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('body',)



class SearchForm(forms.Form):
    search = forms.CharField()
