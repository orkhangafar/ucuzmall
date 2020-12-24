from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from posts.models import Post

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category','price', 'phone', 'image', )

    def __init__(self, *args, **kwargs):
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = "mt-10"
        self.fields['title'].label = "Kitab adı"
        self.fields['content'].label = "Ətraflı məlumat"
        self.fields['category'].label = "Kateqoriya seç"
        self.fields['price'].label = "Qiymət"
        self.fields['phone'].label = "Əlaqə nömrəsi"
        self.fields['image'].label = "Şəkil seç"


        self.helper.layout = Layout(
            #Field("requiredField", css_class="single-input", placeholder="Başlıq"),
            Field("title", css_class="single-input", placeholder="Başlıq"),
            Field("category", css_class="single-input"),
            Field("price", css_class="single-input"),
            Field("phone", css_class="single-input"),
            #Field("tag", css_class="single-input", data_role="tagsinput"),
            Field("content", css_class="single-input", placeholder="Mətn yazın"),
            Field("image", css_class="single-input", placeholder="Şəkil Seç"),
        )

        self.helper.add_input(Submit('submit', 'Qeyd Et', css_class="site-btn submit-order-btn, mt-10"))