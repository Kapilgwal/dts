from django.db import models
from datetime import datetime

class BasicInfo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, max_length=100)
    dob = models.DateField(blank=True)
    role = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=100, blank=False)
    organization = models.CharField(max_length=100, blank=False)
    employeeId = models.CharField(max_length=15, blank=True, unique=True, db_index=True)
    contactNo = models.CharField(max_length=15, blank=True)

    def save(self, *args, **kwargs):
        if not self.employeeId:
            current_year = datetime.now().strftime('%Y')
            count_for_year = BasicInfo.objects.filter(employeeId__startswith=f"EMP{current_year}").count() + 1
            self.employeeId = f"EMP{current_year}{str(count_for_year).zfill(4)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.employeeId})"


class Document(models.Model):
    documentId = models.CharField(max_length=20, blank=True, unique=True)
    documentName = models.CharField(max_length=100, blank=False)
    documentReason = models.CharField(max_length=500, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, related_name='documents_created')
    assigned_to = models.ForeignKey(BasicInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents_received')
    updatedAt = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    document_file = models.FileField(upload_to='documents/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.documentId:
            current_year = datetime.now().strftime('%Y')
            count_for_year = Document.objects.filter(documentId__startswith=f"DOC{current_year}").count() + 1
            self.documentId = f"DOC{current_year}{str(count_for_year).zfill(4)}"
        super().save(*args, **kwargs)

    def __str__(self):
        sender_id = self.created_by.employeeId if self.created_by else "Unknown"
        receiver_id = self.assigned_to.employeeId if self.assigned_to else "N/A"
        return f"{self.documentName} (from {sender_id} to {receiver_id})"
