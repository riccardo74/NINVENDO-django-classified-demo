from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row, Column, Div, Field

from django_classified.models import Item
from .models import PurchaseRequest, SellerProfile


class PurchaseRequestForm(forms.ModelForm):
    """Form per richiedere l'acquisto di un annuncio"""
    
    class Meta:
        model = PurchaseRequest
        fields = ['message', 'delivery_method', 'shipping_address']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Scrivi un messaggio opzionale al venditore...',
                'class': 'form-control'
            }),
            'delivery_method': forms.Select(attrs={'class': 'form-control'}),
            'shipping_address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Inserisci il tuo indirizzo completo per la spedizione...',
                'class': 'form-control'
            }),
        }
    
    def __init__(self, item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item = item
        
        # Labels personalizzate
        self.fields['message'].label = 'Messaggio al Venditore'
        self.fields['delivery_method'].label = 'Metodo di Consegna Preferito'
        self.fields['shipping_address'].label = 'Indirizzo di Spedizione'
        
        # Il campo indirizzo è opzionale ma richiesto se scegli spedizione
        self.fields['shipping_address'].required = False
        
        # Help text
        self.fields['message'].help_text = 'Presenta te stesso e specifica eventuali domande sull\'articolo'
        self.fields['delivery_method'].help_text = 'Come preferisci ricevere l\'articolo?'
        self.fields['shipping_address'].help_text = 'Necessario solo se scegli "Spedizione" o "Entrambi"'
        
        # Crispy Forms layout
        try:
            self.helper = FormHelper()
            self.helper.form_method = "post"
            self.helper.layout = Layout(
                HTML(f'''
                    <div class="card mb-3">
                        <div class="card-header bg-primary text-white">
                            <h5>🛒 Richiesta di Acquisto</h5>
                        </div>
                        <div class="card-body">
                            <p><strong>Articolo:</strong> {self.item.title}</p>
                            <p><strong>Venditore:</strong> {self.item.user.username}</p>
                            <p><strong>Prezzo:</strong> {self.item.price}€</p>
                        </div>
                    </div>
                '''),
                
                Field('message'),
                HTML('<hr>'),
                
                HTML('<h6>🚚 Modalità di Consegna</h6>'),
                Field('delivery_method', css_class='form-control mb-3'),
                
                Field('shipping_address', css_class='address-field'),
                
                HTML('''
                    <div class="alert alert-info">
                        <h6>ℹ️ Come Funziona</h6>
                        <ol>
                            <li>Invia la richiesta al venditore</li>
                            <li>Il venditore approva la richiesta</li>
                            <li>Procedi al pagamento sicuro con Stripe</li>
                            <li>Ricevi l'articolo secondo l'accordo</li>
                        </ol>
                    </div>
                '''),
                
                HTML('<hr>'),
                Div(
                    Submit('submit', '📤 Invia Richiesta di Acquisto', css_class='btn btn-primary btn-lg btn-block'),
                    css_class='text-center'
                )
            )
        except ImportError:
            pass
    
    def clean(self):
        cleaned_data = super().clean()
        delivery_method = cleaned_data.get('delivery_method')
        shipping_address = cleaned_data.get('shipping_address', '').strip()
        
        # Se ha scelto spedizione, l'indirizzo è obbligatorio
        if delivery_method in ['shipping', 'both'] and not shipping_address:
            raise ValidationError({
                'shipping_address': 'L\'indirizzo di spedizione è richiesto per il metodo di consegna selezionato.'
            })
        
        return cleaned_data


class SellerOnboardingForm(forms.ModelForm):
    """Form per configurazione venditore"""
    
    class Meta:
        model = SellerProfile
        fields = ['accepts_payments', 'auto_accept_payments']
        widgets = {
            'accepts_payments': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto_accept_payments': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['accepts_payments'].label = 'Accetta pagamenti online'
        self.fields['auto_accept_payments'].label = 'Approva automaticamente le richieste di acquisto'
        
        self.fields['accepts_payments'].help_text = 'Permetti agli utenti di acquistare i tuoi annunci con pagamenti online'
        self.fields['auto_accept_payments'].help_text = 'Le richieste saranno approvate automaticamente (sconsigliato per articoli di valore elevato)'
        
        # Crispy Forms layout
        try:
            self.helper = FormHelper()
            self.helper.form_method = "post"
            self.helper.layout = Layout(
                HTML('<h4>💰 Configurazione Vendite</h4>'),
                
                Div(
                    Field('accepts_payments'),
                    HTML('<small class="form-text text-muted">Permetti agli utenti di acquistare i tuoi annunci online</small>'),
                    css_class='form-check mb-3'
                ),
                
                Div(
                    Field('auto_accept_payments'),
                    HTML('<small class="form-text text-muted">Approva automaticamente le richieste (sconsigliato per articoli costosi)</small>'),
                    css_class='form-check mb-3'
                ),
                
                HTML('''
                    <div class="alert alert-warning">
                        <h6>⚠️ Commissioni</h6>
                        <p>Su ogni vendita vengono applicate:</p>
                        <ul>
                            <li><strong>3% di commissione piattaforma</strong></li>
                            <li><strong>1.4% + €0.25 di commissione Stripe</strong></li>
                        </ul>
                        <p class="mb-0">Le commissioni sono automaticamente detratte dal pagamento dell'acquirente.</p>
                    </div>
                '''),
                
                HTML('<hr>'),
                Submit('save', '💾 Salva Configurazione', css_class='btn btn-success btn-block')
            )
        except ImportError:
            pass


class PaymentFilterForm(forms.Form):
    """Form per filtrare cronologia pagamenti"""
    
    STATUS_CHOICES = [
        ('', 'Tutti gli stati'),
        ('pending', 'In Attesa'),
        ('processing', 'In Elaborazione'),  
        ('succeeded', 'Completato'),
        ('failed', 'Fallito'),
        ('cancelled', 'Annullato'),
        ('refunded', 'Rimborsato'),
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date', 
            'class': 'form-control'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['status'].label = 'Stato'
        self.fields['date_from'].label = 'Dal'
        self.fields['date_to'].label = 'Al'
        
        # Crispy Forms layout
        try:
            self.helper = FormHelper()
            self.helper.form_method = "get"
            self.helper.layout = Layout(
                Row(
                    Column('status', css_class='col-md-4'),
                    Column('date_from', css_class='col-md-4'),
                    Column('date_to', css_class='col-md-4'),
                ),
                HTML('<hr>'),
                Div(
                    Submit('filter', '🔍 Filtra', css_class='btn btn-info'),
                    HTML('<a href="?" class="btn btn-secondary ml-2">🔄 Reset</a>'),
                    css_class='text-center'
                )
            )
        except ImportError:
            pass