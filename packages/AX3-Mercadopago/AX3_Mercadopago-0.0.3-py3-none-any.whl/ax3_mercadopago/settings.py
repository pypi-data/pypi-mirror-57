from django.conf import settings


CLIENT_ID = getattr(settings, 'MERCADOPAGO_CLIENT_ID', '')
CLIENT_SECRET = getattr(settings, 'MERCADOPAGO_CLIENT_SECRET', '')
PUBLIC_KEY = getattr(settings, 'MERCADOPAGO_PUBLIC_KEY', '')
ACCESS_TOKEN = getattr(settings, 'MERCADOPAGO_ACCESS_TOKEN', '')
PAYMENT_MODEL = getattr(settings, 'MERCADOPAGO_PAYMENT_MODEL', '')
PAID_USECASE = getattr(settings, 'MERCADOPAGO_PAID_USECASE', '')
REJECTED_USECASE = getattr(settings, 'MERCADOPAGO_REJECTED_USECASE', '')
REFERENCE_PREFIX = 'test_'
