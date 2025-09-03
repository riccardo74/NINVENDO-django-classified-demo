#!/usr/bin/env python
"""
Script di debug per verificare lo stato degli acquisti dell'utente tommaso
Eseguire con: python manage.py shell -c "exec(open('debug_purchase_status.py').read())"
"""

from django.contrib.auth.models import User
from payments.models import PaymentTransaction, PurchaseRequest, SellerProfile

print("=" * 60)
print("DEBUG STATO ACQUISTI TOMMASO")
print("=" * 60)

# Trova l'utente tommaso
try:
    tommaso = User.objects.get(username='tommaso')
    print(f"✓ Utente trovato: {tommaso.username} (ID: {tommaso.id})")
except User.DoesNotExist:
    print("✗ Utente 'tommaso' non trovato")
    
    # Mostra tutti gli utenti disponibili
    print("\nUtenti disponibili:")
    for user in User.objects.all():
        print(f"  - {user.username}")
    exit()

print("\n" + "-" * 40)
print("1. TRANSAZIONI DI PAGAMENTO")
print("-" * 40)

transactions = PaymentTransaction.objects.filter(buyer=tommaso)
print(f"Transazioni totali: {transactions.count()}")

for i, t in enumerate(transactions, 1):
    print(f"\nTransazione {i}:")
    print(f"  UUID: {t.uuid}")
    print(f"  Status: {t.status}")
    print(f"  Articolo: {t.item.title}")
    print(f"  Venditore: {t.seller.username}")
    print(f"  Importo totale: €{t.total_amount_euros}")
    print(f"  Creata: {t.created_at}")
    print(f"  Completata: {t.completed_at}")
    print(f"  Stripe Session ID: {t.stripe_checkout_session_id}")
    print(f"  Stripe Payment Intent: {t.stripe_payment_intent_id}")

print("\n" + "-" * 40)
print("2. RICHIESTE DI ACQUISTO")
print("-" * 40)

requests = PurchaseRequest.objects.filter(buyer=tommaso)
print(f"Richieste totali: {requests.count()}")

for i, r in enumerate(requests, 1):
    print(f"\nRichiesta {i}:")
    print(f"  UUID: {r.uuid}")
    print(f"  Status: {r.status}")
    print(f"  Articolo: {r.item.title}")
    print(f"  Venditore: {r.seller.username}")
    print(f"  Creata: {r.created_at}")
    print(f"  Scade: {r.expires_at}")
    print(f"  È scaduta: {r.is_expired()}")
    
    # Transazione collegata
    if r.payment_transaction:
        print(f"  Transazione collegata: {r.payment_transaction.uuid}")
        print(f"  Status transazione: {r.payment_transaction.status}")
    else:
        print(f"  Transazione collegata: NESSUNA")

print("\n" + "-" * 40)
print("3. STATISTICHE CALCOLATE")
print("-" * 40)

# Simula il calcolo nelle view
completed_transactions = transactions.filter(status='succeeded')
active_requests = requests.filter(status__in=['pending', 'approved'])

print(f"Transazioni completate (succeeded): {completed_transactions.count()}")
print(f"Totale speso: €{sum(t.total_amount_euros for t in completed_transactions)}")
print(f"Richieste attive (pending/approved): {active_requests.count()}")
print(f"  - Pendenti: {active_requests.filter(status='pending').count()}")
print(f"  - Approvate: {active_requests.filter(status='approved').count()}")

print("\n" + "-" * 40)
print("4. CHECK SPECIFICI")
print("-" * 40)

# Verifica articoli disattivati
purchased_items = [t.item for t in completed_transactions]
if purchased_items:
    print("Articoli acquistati e loro stato:")
    for item in purchased_items:
        print(f"  - {item.title}: {'ATTIVO' if item.is_active else 'DISATTIVATO'}")

# Verifica collegamenti request <-> transaction
print(f"\nVerifica collegamenti:")
for r in requests:
    if r.payment_transaction:
        trans = r.payment_transaction
        print(f"  Request {r.uuid.hex[:8]} → Transaction {trans.uuid.hex[:8]} ({trans.status})")
    else:
        print(f"  Request {r.uuid.hex[:8]} → NESSUNA TRANSAZIONE")

print("\n" + "-" * 40)
print("5. VERIFICA STATUS CONSTANTS")
print("-" * 40)

# Verifica le costanti del modello
print("PurchaseRequest STATUS constants:")
print(f"  STATUS_PENDING: {getattr(PurchaseRequest, 'STATUS_PENDING', 'MANCANTE')}")
print(f"  STATUS_APPROVED: {getattr(PurchaseRequest, 'STATUS_APPROVED', 'MANCANTE')}")
print(f"  STATUS_COMPLETED: {getattr(PurchaseRequest, 'STATUS_COMPLETED', 'MANCANTE')}")

print("\nPaymentTransaction STATUS constants:")
print(f"  STATUS_SUCCEEDED: {getattr(PaymentTransaction, 'STATUS_SUCCEEDED', 'MANCANTE')}")
print(f"  STATUS_PROCESSING: {getattr(PaymentTransaction, 'STATUS_PROCESSING', 'MANCANTE')}")

print("\n" + "=" * 60)
print("DEBUG COMPLETATO")
print("=" * 60)