import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='bsdsf21a002@pucit.edu.pk'
recipient='sheraz601050@gmail.com'
mail.login('bsdsf21a002@pucit.edu.pk','m15v5l61')
header='To:'+receipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()

#Before running above script, sender's gmail account must be configured to allow 'less secure apps'. Visit following link.

#https://myaccount.google.com/lesssecureapps
