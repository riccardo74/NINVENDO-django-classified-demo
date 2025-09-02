from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row, Column, Div, Field
from crispy_forms.bootstrap import InlineRadios

from django_classified.models import Item
from .models import TradeProposal, TradeFeedback, UserTradeProfile, TradeMessage

User = get_user_model()


# ------------------------------------------------------------
# Profilo Utente Esteso (usando UserTradeProfile invece di UserProfile)
# ------------------------------------------------------------
class UserProfileForm(forms.ModelForm):
    """Form per modificare le informazioni del profilo utente esteso"""
    
    class Meta:
        model = UserTradeProfile
        fields = ['phone_number', 'show_phone_in_trades', 'location', 'bio']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+39 123 456 7890',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'es. Milano, Roma, Napoli...',
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Racconta qualcosa di te...',
                'class': 'form-control'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Labels personalizzate
        self.fields['phone_number'].label = 'Numero di Telefono'
        self.fields['show_phone_in_trades'].label = 'Mostra negli scambi accettati'
        self.fields['location'].label = 'Città/Zona'
        self.fields['bio'].label = 'Biografia'
        
        # Crispy layout se disponibile
        try:
            self.helper = FormHelper()
            self.helper.form_method = "post"
            self.helper.layout = Layout(
                HTML('<h4>📞 Informazioni di Contatto</h4>'),
                Field('phone_number', placeholder='+39 123 456 7890'),
                Field('show_phone_in_trades'),
                HTML('<small class="form-text text-muted">Il tuo numero sarà visibile solo negli scambi accettati</small>'),
                HTML('<hr>'),
                HTML('<h4>📍 Localizzazione</h4>'),
                Field('location'),
                HTML('<hr>'),
                HTML('<h4>👤 Biografia</h4>'),
                Field('bio'),
                HTML('<hr>'),
                Div(
                    Submit('save', '💾 Salva Profilo', css_class='btn btn-primary btn-block'),
                    css_class='text-center'
                )
            )
        except ImportError:
            # Se crispy_forms non è disponibile, usa un form semplice
            pass


# ------------------------------------------------------------
# Messaggistica interna per gli scambi
# ------------------------------------------------------------
class TradeMessageForm(forms.ModelForm):
    """
    Form per inviare un messaggio interno in un Trade con supporto immagini.
    Firma: TradeMessageForm(trade, sender, data=None, files=None, **kwargs)
    """
    class Meta:
        model = TradeMessage
        fields = ["message", "image"]
        widgets = {
            "message": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Scrivi un messaggio per organizzare lo scambio...",
                "class": "form-control"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control-file",
                "accept": "image/*"
            })
        }

    def __init__(self, trade, sender, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trade = trade
        self.sender = sender
        
        # Labels personalizzate
        self.fields['message'].label = 'Messaggio'
        self.fields['message'].required = False  # Non obbligatorio se c'è un'immagine
        self.fields['image'].label = 'Allega Immagine'
        
        # Help text
        self.fields['image'].help_text = 'Formati supportati: JPG, PNG, GIF (max 5MB)'

        # Crispy layout con supporto immagini
        try:
            self.helper = FormHelper()
            self.helper.form_method = "post"
            self.helper.form_enctype = "multipart/form-data"  # Importante per i file
            self.helper.layout = Layout(
                Field("message", placeholder="Scrivi un messaggio..."),
                HTML('<div class="form-group">'),
                HTML('<label for="id_image">📷 Allega Immagine (opzionale)</label>'),
                Field("image"),
                HTML('<small class="form-text text-muted">Formati: JPG, PNG, GIF - Max 5MB</small>'),
                HTML('</div>'),
                HTML('<hr>'),
                Submit("send", "📨 Invia Messaggio", css_class="btn btn-info btn-block")
            )
        except ImportError:
            pass
    
    def clean(self):
        """Validazione personalizzata: deve esserci messaggio O immagine"""
        cleaned_data = super().clean()
        message = cleaned_data.get('message', '').strip()
        image = cleaned_data.get('image')
        
        if not message and not image:
            raise ValidationError(
                "È necessario scrivere un messaggio o allegare un'immagine."
            )
        
        return cleaned_data
    
    def clean_image(self):
        """Validazione dell'immagine"""
        image = self.cleaned_data.get('image')
        
        if image:
            # Controllo dimensione file (5MB max)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("L'immagine è troppo grande. Dimensione massima: 5MB")
            
            # Controllo tipo file
            if not image.content_type.startswith('image/'):
                raise ValidationError("Il file deve essere un'immagine (JPG, PNG, GIF)")
            
            # Lista formati supportati
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp']
            if image.content_type not in allowed_types:
                raise ValidationError("Formato non supportato. Usa JPG, PNG, GIF o WebP")
        
        return image

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.trade = self.trade
        obj.sender = self.sender
        # Destinatario = l'altro partecipante allo scambio
        obj.recipient = self.trade.to_user if self.sender == self.trade.from_user else self.trade.from_user
        
        if commit:
            obj.save()
        return obj
    
    
# ------------------------------------------------------------
# Creazione proposta di scambio
# ------------------------------------------------------------
class TradeProposalForm(forms.ModelForm):
    """Form per creare una proposta di scambio"""

    class Meta:
        model = TradeProposal
        fields = ["offer_item", "message"]
        widgets = {
            "message": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Scrivi un messaggio opzionale per la tua proposta...",
                "class": "form-control"
            }),
        }

    def __init__(self, user, target_item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.target_item = target_item

        # Solo annunci attivi dell'utente corrente, escluso quello target
        self.fields["offer_item"].queryset = Item.objects.filter(
            user=user,
            is_active=True
        ).exclude(pk=target_item.pk)

        self.fields["offer_item"].empty_label = "Seleziona il tuo annuncio da offrire..."

        # Avviso se l'utente non ha annunci attivi
        if not self.fields["offer_item"].queryset.exists():
            self.fields["offer_item"].help_text = """
            <div class="alert alert-warning">
                Non hai annunci attivi da offrire.
                <a href="/item/new/" class="alert-link">Pubblica un annuncio</a> prima di proporre scambi.
            </div>
            """

        # Crispy layout
        try:
            self.helper = FormHelper()
            self.helper.form_method = "post"
            self.helper.layout = Layout(
                HTML(f"""
                    <div class="card mb-3">
                        <div class="card-header bg-info text-white">
                            <h5><i class="fas fa-exchange-alt"></i> Proponi Scambio</h5>
                        </div>
                        <div class="card-body">
                            <p><strong>Annuncio richiesto:</strong> {self.target_item.title}</p>
                            <p class="text-muted">Proprietario: {self.target_item.user.username}</p>
                        </div>
                    </div>
                """),
                Field("offer_item", css_class="form-control form-control-lg"),
                Field("message"),
                HTML("<hr>"),
                Div(
                    Submit("submit", "📤 Invia Proposta", css_class="btn btn-success btn-lg btn-block"),
                    HTML('<a href="{{ want_item.get_absolute_url }}" class="btn btn-secondary btn-block">❌ Annulla</a>'),
                    css_class="text-center"
                )
            )
        except ImportError:
            pass

    def clean_offer_item(self):
        offer_item = self.cleaned_data.get("offer_item")
        if not offer_item:
            raise ValidationError("Devi selezionare un annuncio da offrire.")

        if offer_item.user != self.user:
            raise ValidationError("Puoi offrire solo i tuoi annunci.")

        if offer_item == self.target_item:
            raise ValidationError("Non puoi offrire lo stesso annuncio che stai richiedendo.")

        # Evita proposte duplicate pendenti
        existing = TradeProposal.objects.filter(
            from_user=self.user,
            to_user=self.target_item.user,
            offer_item=offer_item,
            want_item=self.target_item,
            state=TradeProposal.STATE_SENT
        ).exists()
        if existing:
            raise ValidationError("Hai già una proposta pendente per questo scambio.")

        return offer_item


# ------------------------------------------------------------
# Risposta alla proposta (accetta / rifiuta / controproposta)
# ------------------------------------------------------------
class TradeResponseForm(forms.Form):
    """Form per rispondere a una proposta (accetta/rifiuta con messaggio)"""

    ACTION_ACCEPT = "accept"
    ACTION_DECLINE = "decline"
    ACTION_COUNTER = "counter"

    ACTION_CHOICES = [
        (ACTION_ACCEPT, "✅ Accetta"),
        (ACTION_DECLINE, "❌ Rifiuta"),
        (ACTION_COUNTER, "🔄 Fai Controproposta"),
    ]

    action = forms.ChoiceField(
        choices=ACTION_CHOICES,
        widget=forms.RadioSelect,
        label="Come vuoi rispondere?"
    )

    response_message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Messaggio opzionale..."}),
        required=False,
        label="Messaggio di risposta"
    )

    # Solo per controposte
    counter_offer_item = forms.ModelChoiceField(
        queryset=Item.objects.none(),
        required=False,
        empty_label="Seleziona un altro tuo annuncio...",
        label="Il tuo annuncio alternativo"
    )

    def __init__(self, user, trade_proposal, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.trade_proposal = trade_proposal

        # Solo annunci dell'utente destinatario (diversi da quello già proposto)
        self.fields["counter_offer_item"].queryset = Item.objects.filter(
            user=user,
            is_active=True
        ).exclude(pk=trade_proposal.want_item.pk)

        # Crispy layout
        try:
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML(f"""
                    <div class="card">
                        <div class="card-header">
                            <h5>Risposta a: {self.trade_proposal.from_user.username}</h5>
                        </div>
                        <div class="card-body">
                            <p><strong>Offre:</strong> {self.trade_proposal.offer_item.title}</p>
                            <p><strong>Vuole:</strong> {self.trade_proposal.want_item.title}</p>
                            <p><strong>Messaggio originale:</strong><br>
                               <em>{self.trade_proposal.message or 'Nessun messaggio'}</em></p>
                        </div>
                    </div>
                    <hr>
                """),
                InlineRadios("action"),
                Field("response_message"),
                Div(
                    Field("counter_offer_item"),
                    css_id="counter-offer-section",
                    style="display: none;"
                ),
                HTML("""
                    <script>
                        document.addEventListener('DOMContentLoaded', function() {
                            const actionRadios = document.querySelectorAll('input[name="action"]');
                            const counterSection = document.getElementById('counter-offer-section');
                            actionRadios.forEach(radio => {
                                radio.addEventListener('change', function() {
                                    counterSection.style.display = (this.value === 'counter') ? 'block' : 'none';
                                });
                            });
                        });
                    </script>
                """),
                Submit("submit", "Invia Risposta", css_class="btn btn-primary btn-lg btn-block")
            )
        except ImportError:
            pass

    def clean(self):
        cleaned_data = super().clean()
        action = cleaned_data.get("action")
        counter_item = cleaned_data.get("counter_offer_item")

        if action == self.ACTION_COUNTER and not counter_item:
            raise ValidationError("Devi selezionare un annuncio per la controproposta.")
        return cleaned_data


# ------------------------------------------------------------
# Feedback post-scambio
# ------------------------------------------------------------
class TradeFeedbackForm(forms.ModelForm):
    """
    Form per lasciare feedback dopo uno scambio completato.
    Pre-assegna trade/rater/ratee sull'istanza per evitare errori di validazione.
    """

    class Meta:
        model = TradeFeedback
        fields = ["rating", "comment"]
        widgets = {
            "comment": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Condividi la tua esperienza con questo scambio..."
            })
        }

    def __init__(self, trade_proposal, rater, *args, **kwargs):
        """
        Firma: TradeFeedbackForm(trade_proposal, rater, data=None, files=None, **kwargs)
        """
        super().__init__(*args, **kwargs)

        # Pre-assegna campi chiave sull'istanza usata dal ModelForm
        self.instance.trade = trade_proposal
        self.instance.rater = rater
        self.instance.ratee = trade_proposal.to_user if rater == trade_proposal.from_user else trade_proposal.from_user

        # Sostituisce il campo rating con un TypedChoiceField (1..5) + InlineRadios
        self.fields["rating"] = forms.TypedChoiceField(
            coerce=int,
            choices=[(i, f"{i} ⭐") for i in range(1, 6)],
            widget=InlineRadios(),
            label="Valutazione"
        )

        # Crispy layout
        try:
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML(f"""
                    <div class="card mb-3">
                        <div class="card-header">
                            <h5>Valuta il tuo scambio con {self.instance.ratee.username}</h5>
                        </div>
                        <div class="card-body">
                            <p><strong>Scambio:</strong> {trade_proposal.offer_item.title} ↔ {trade_proposal.want_item.title}</p>
                            <p class="text-muted">Puoi lasciare un giudizio da 1 a 5 stelle.</p>
                        </div>
                    </div>
                """),
                InlineRadios("rating"),
                Field("comment"),
                Submit("submit", "⭐ Invia Valutazione", css_class="btn btn-warning btn-lg btn-block")
            )
        except ImportError:
            pass


# ------------------------------------------------------------
# Ricerca scambi compatibili
# ------------------------------------------------------------
class TradeSearchForm(forms.Form):
    """Form per cercare scambi compatibili"""

    category = forms.ModelChoiceField(
        queryset=None,   # popolata dinamicamente
        required=False,
        empty_label="Tutte le categorie"
    )

    area = forms.ModelChoiceField(
        queryset=None,   # popolata dinamicamente
        required=False,
        empty_label="Tutte le aree"
    )

    keywords = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Cerca per parole chiave...",
            "class": "form-control"
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Popola dinamicamente da django-classified
        try:
            from django_classified.models import Group
            self.fields["category"].queryset = Group.objects.filter(
                item__isnull=False
            ).distinct()
        except Exception:
            pass

        try:
            from django_classified.models import Area
            self.fields["area"].queryset = Area.objects.filter(
                item__isnull=False
            ).distinct()
        except Exception:
            pass

        # Crispy layout
        try:
            self.helper = FormHelper()
            self.helper.form_method = "get"
            self.helper.layout = Layout(
                Row(
                    Column("category", css_class="col-md-4"),
                    Column("area", css_class="col-md-4"),
                    Column("keywords", css_class="col-md-4"),
                ),
                Submit("search", "🔍 Cerca Scambi", css_class="btn btn-outline-primary btn-block")
            )
        except ImportError:
            pass


# ------------------------------------------------------------
# Form di utilità per moderazione/admin
# ------------------------------------------------------------
class TradeReportForm(forms.Form):
    """Form per segnalare problemi con uno scambio"""
    
    REASON_CHOICES = [
        ('spam', 'Spam o contenuto inappropriato'),
        ('fake', 'Annuncio falso o ingannevole'),
        ('offline', 'Utente non risponde'),
        ('rude', 'Comportamento scorretto'),
        ('other', 'Altro'),
    ]
    
    reason = forms.ChoiceField(
        choices=REASON_CHOICES,
        widget=forms.RadioSelect,
        label="Motivo della segnalazione"
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False,
        label="Descrizione dettagliata"
    )
    
    def __init__(self, trade, reporter, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trade = trade
        self.reporter = reporter
        
        try:
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML(f'<h5>Segnala Scambio #{trade.pk}</h5>'),
                InlineRadios('reason'),
                Field('description'),
                Submit('submit', '🚨 Invia Segnalazione', css_class='btn btn-danger')
            )
        except ImportError:
            pass