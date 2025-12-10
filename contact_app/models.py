from django.db import models
from login.models import Registration

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=255)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
# here we target the login model id as foreign key
# foreignkey always target to Primary key of the datasets
# foreignkey target pk and id. pk is only one in table
# user = models.ForeignKey(Registration, to_field="email", on_delete=models.CASCADE)
# if i habe changed the pk to the email then it write like this.


# Session server-side hota hai → Browser me actual data nahi.
# Browser me sirf session ID stored hoti hai (cookie me).