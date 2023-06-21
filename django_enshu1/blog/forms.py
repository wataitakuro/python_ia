class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)
    name= forms.CharField(label='記事名' , required=False)

class Meta:
    model = Comment
    field = ('name ', 'text', 'target') #targetフィールドを含めない
