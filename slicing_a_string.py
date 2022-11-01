
AWS_arn="arn:aws:iam::123456789012:user/development/product_1234/"
account_number= (AWS_arn[13:25])
print(account_number)