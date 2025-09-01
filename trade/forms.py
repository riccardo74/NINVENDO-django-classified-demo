# trade/forms.py - Versione minimale per risolvere l'import error
from django import forms
from django.core.exceptions import ValidationError

# Per ora importiamo solo quello che serve
try:
    from django_classified.models import Item
except ImportError:
    Item = None

from .models import TradeProposal, TradeFeedback


class TradeProposalForm(forms.ModelForm):
    """Form base per creare una proposta di scambio"""
    
    class Meta:
        model = TradeProposal
        fields = ['offer_item', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Scrivi un messaggio opzionale...',
                'class': 'form-control'
            }),
        }
    
    def __init__(self, user, target_item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.target_item = target_item
        
        # Solo annunci attivi dell'utente corrente
        if Item:
            self.fields['offer_item'].queryset = Item.objects.filter(
                user=user,
                is_active=True
            ).exclude(pk=target_item.pk)
        
        self.fields['offer_item'].empty_label = "Seleziona il tuo annuncio..."
    
    def clean_offer_item(self):
        offer_item = self.cleaned_data.get('offer_item')
        if not offer_item:
            raise ValidationError("Devi selezionare un annuncio da offrire.")
        return offer_item


# Form placeholder per evitare errori di import
class TradeResponseForm(forms.Form):
    """Placeholder - da implementare"""
    action = forms.CharField(widget=forms.HiddenInput(), initial='accept')


class TradeFeedbackForm(forms.ModelForm):
    """Form per feedback"""
    
    class Meta:
        model = TradeFeedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} ⭐") for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3})
        }