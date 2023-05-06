from django import forms

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topic_name=forms.CharField()
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()
    
    
    
    
        