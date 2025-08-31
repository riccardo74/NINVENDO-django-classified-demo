from django.shortcuts import render

from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib import messages

from .models import TradeProposal
try:
    # modello Annunci del pacchetto classified
    from django_classified.models import Item
except Exception:
    Item = None  # fallback per sviluppo

# Inbox (ricevuti)
class InboxTradesView(LoginRequiredMixin, ListView):
    template_name = "trade/list.html"
    context_object_name = "trades"

    def get_queryset(self):
        return TradeProposal.objects.filter(to_user=self.request.user).order_by("-created_at")

# Inviati
class SentTradesView(LoginRequiredMixin, ListView):
    template_name = "trade/list.html"
    context_object_name = "trades"

    def get_queryset(self):
        return TradeProposal.objects.filter(from_user=self.request.user).order_by("-created_at")

# Proponi scambio
class ProposeTradeView(LoginRequiredMixin, View):
    def get(self, request, item_id):
        want_item = get_object_or_404(Item, pk=item_id)
        if want_item.user == request.user:
            return HttpResponseForbidden("Non puoi proporre scambi a te stesso.")
        return render(request, "trade/propose.html", {"want_item": want_item})

    def post(self, request, item_id):
        want_item = get_object_or_404(Item, pk=item_id)
        if want_item.user == request.user:
            return HttpResponseForbidden("Non puoi proporre scambi a te stesso.")
        # versione minima: crea una finta proposta per test
        # (sostituisci con il form reale appena pronto)
        offer_item_id = request.POST.get("offer_item_id")
        offer_item = get_object_or_404(Item, pk=offer_item_id, user=request.user)
        TradeProposal.objects.create(
            from_user=request.user,
            to_user=want_item.user,
            offer_item=offer_item,
            want_item=want_item,
            message=request.POST.get("message", "")
        )
        messages.success(request, "Proposta inviata.")
        return redirect("trade:sent")

# Azioni di stato (stub, POST-only)
class AcceptTradeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tp = get_object_or_404(TradeProposal, pk=pk, to_user=request.user)
        tp.accept(); tp.save()
        messages.success(request, "Proposta accettata.")
        return redirect("trade:inbox")

class DeclineTradeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tp = get_object_or_404(TradeProposal, pk=pk, to_user=request.user)
        tp.decline(); tp.save()
        messages.info(request, "Proposta rifiutata.")
        return redirect("trade:inbox")

class CancelTradeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tp = get_object_or_404(TradeProposal, pk=pk)
        if tp.from_user != request.user and tp.to_user != request.user:
            return HttpResponseForbidden()
        tp.cancel(); tp.save()
        messages.warning(request, "Proposta annullata.")
        return redirect("trade:sent")

class CompleteTradeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tp = get_object_or_404(TradeProposal, pk=pk)
        if tp.from_user != request.user and tp.to_user != request.user:
            return HttpResponseForbidden()
        tp.complete(); tp.save()
        messages.success(request, "Scambio completato.")
        return redirect("trade:inbox")
