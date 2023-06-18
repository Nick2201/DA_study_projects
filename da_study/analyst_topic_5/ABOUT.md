# DATA

## DataFrames
BASE:         retail

retail_df_C  : canceled
retail_df    : approved

## 
HAVE:
    PERiods: 01.12.2010 по 12.09.2011:
IDENT:    
    InvoiceNo – номер транзакции
    StockCode – код товара
    Description – описание товара
ORDER:
    Quantity – количество единиц товара
    InvoiceDate – дата транзакции 
    UnitPrice – цена за единицу товара
CUSTOMER:
    CustomerID – id клиента
    Country – страна, где проживает клиент
## COLUMNS
COLUMNS: ['invoiceno', 'stockcode', 'description', 'quantity', 'invoicedate','unitprice', 'customerid', 'country']