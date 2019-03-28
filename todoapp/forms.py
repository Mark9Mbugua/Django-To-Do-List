from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder' : 'Enter todo e.g Prepare for interviews', 
            'aria-label': 'Todo', 'aria-describeby': 'add-btn'}
        ))
