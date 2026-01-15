from django import forms
from .models import MediaItem

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ('titulo', 'origin', 'media_type', 'status', 'rank', 'comment')
        
        # RENAME THE LABELS
        labels = {
            'titulo': 'Título',
            'origin': 'Criador / Estudio',
            'media_type': 'Categoria',
            'rank': 'Nota (0-10)',
            'comment': 'Comentário',
        }

        # BOOTSTRAP STYLING (Class="form-control")
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., The Matrix'}),
            'origin': forms.TextInput(attrs={'class': 'form-control','placeholder': 'e.g., The Wachowskis'}),
            'media_type': forms.Select(attrs={'class': 'form-select'}), # 'form-select' looks better for dropdowns
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rank': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }