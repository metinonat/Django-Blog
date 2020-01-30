from django import forms
from article.models import Article, Comment
from backend.settings import MIN_ARTICLE_LENGTH, MIN_COMMENT_LENGTH

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['owner', 'image']

    def clean_header(self):
        header = self.cleaned_data.get('header')
        if Article.objects.filter(header=header).exists():
            raise forms.ValidationError('There is another post with the same header. Please choose an unique header.')
        if header == '':
            raise forms.ValidationError('Header cannot be empty.')
        return header

    def clean_content(self):
        if len(self.cleaned_data.get('content')) < MIN_ARTICLE_LENGTH:
            raise forms.ValidationError(f'Content must be at lest {MIN_ARTICLE_LENGTH} words long')
        return self.cleaned_data.get('content')

class ArticleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['owner', 'image']
    
    def clean_header(self):
        header = self.cleaned_data.get('header')
        if Article.objects.filter(header=header).exists():
            raise forms.ValidationError('There is another post with the same header. Please choose an unique header.')
        if header == '':
            raise forms.ValidationError('Header cannot be empty.')
        return header

    def clean_content(self):
        if len(self.cleaned_data.get('content')) < MIN_ARTICLE_LENGTH:
            raise forms.ValidationError(f'Content must be at lest {MIN_ARTICLE_LENGTH} words long')
        return self.cleaned_data.get('content')

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['owner','article']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < MIN_COMMENT_LENGTH:
            raise forms.ValidationError(f'Your Comment must be at least {MIN_COMMENT_LENGTH} characters long.')
        return content