from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div, Field
from crispy_forms.layout import Layout


from .models import Categoria, SubCategoria, Marca


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(
                '',
                # Field('type_note',  wrapper_class='col-md-12'),
                Div('descripcion', css_class='col-md-12'),
                Div('estado', css_class='col-md-2'),

            ),
        )


class EditarCategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EditarCategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(
                '',
                # Field('type_note',  wrapper_class='col-md-12'),
                Div('descripcion', css_class='col-md-12'),
                Div('estado', css_class='col-md-2'),

            ),
        )


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SubCategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(
                '',
                # Field('type_note',  wrapper_class='col-md-12'),
                Div('categoria', css_class='col-md-12'),
                Div('descripcion', css_class='col-md-12'),
                Div('estado', css_class='col-md-2'),

            ),
        )
        self.fields['categoria'].empty_label = "Seleccione la Categoria"


class EditarSubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EditarSubCategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(
                '',
                # Field('type_note',  wrapper_class='col-md-12'),
                Div('categoria', css_class='col-md-12'),
                Div('descripcion', css_class='col-md-12'),
                Div('estado', css_class='col-md-2'),

            ),
        )
        self.fields['categoria'].empty_label = "Seleccione la Categoria"


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(MarcaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(
                '',
                # Field('type_note',  wrapper_class='col-md-12'),
                Div('descripcion', css_class='col-md-12'),
                Div('estado', css_class='col-md-2'),

            ),
        )


class EditarMarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']

    def __init__(self, *args, **kwargs):
        super(EditarMarcaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
           Div(

                # Field('type_note',  wrapper_class='col-md-12'),
                Field('descripcion', css_class='col-md-10'),
                Field('estado', css_class='col-md-2'),

            ),
        )
