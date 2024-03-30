from django import forms
from .models import Comment

class PlaceCommentView(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control','style':'width:100px'}))
    
    class Meta: 
        model = Comment
        fields = ('comment_text', 'stars_given')
        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'form-control','style':'height:100px'})
        }
