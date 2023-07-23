from django import forms
item=item=(('1','OIL'),('2','Grocerey'),('3','Cosmetics'))
class market(forms.Form):
    Name=forms.CharField(max_length=20)
    Item=forms.ChoiceField(choices=item)
    Quantity=forms.IntegerField()
    Rate=forms.IntegerField()
