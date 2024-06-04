from enzona_api.enzona_business_payment import enzona_business_payment

ebp = enzona_business_payment(CONSUMER_KEY, CONSUMER_SECRET)

merchant_uuid = "her put your merchant_uuid" #your merchant_uuid

SHIPPING = 10.0
DISCOUNT = 2.0
TIP = 5.0
MERCHANT_OP_ID = 950201146651 #your market identifier
INVOICE_NUMBER = 1004 #invoice number
TERMINAL_ID = 12121 #terminal identifier (POS, Cash Register, etc.)
URL_RETURN = "http://www.example.com/return_payment"
URL_CANCEL = "http://www.example.com/cancel_payment"

product1 = Product(name="producto1", description="description1", quantity=1, price=403.5, tax=20.18)
product2 = Product(name="producto2", description="description2", quantity=2, price=300.0, tax=15.0)
lst_products = [product1.get_product(), product2.get_product()]

pay = Payments(
    merchant_uuid=merchant_uuid,
    description_payment= "Description pay",
    currency="CUP",
    shipping=SHIPPING,
    discount=DISCOUNT,
    tip=TIP,
    lst_products=lst_products,
    merchant_op_id=MERCHANT_OP_ID,
    invoice_number=INVOICE_NUMBER,
    return_url=URL_RETURN,
    cancel_url=URL_CANCEL,
    terminal_id=TERMINAL_ID
)

response = ebp.create_payments(payment=pay.get_payment())
transaction_uuid = response.transaction_uuid()
link_confirm = response.link_confirm()