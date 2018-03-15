from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

class Lot(models.Model):
    LOTS_PER_PAGE = 6
    STATUS_OPEN = 'open'
    STATUS_END = 'end'
    STATUS_CANCEL = 'cancel'
    STATUS_CHOICES = (
        (STATUS_OPEN, 'Открыт'),
        (STATUS_END, 'Завершен'),
        (STATUS_CANCEL, 'Отменен')
    )

    name = models.CharField(max_length=300)
    description = models.TextField()
    # image = models.FileField(upload_to='uploads/')
    date_from = models.DateTimeField(default=timezone.now())
    date_to = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_OPEN)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def get_all(self, page = 1):
        # Returns all available lots by page number
        all_lots = Lot.objects.filter(
            date_from__lte=timezone.now(),
            date_to__gte = timezone.now(),
            status=self.STATUS_OPEN
        )
        paginator = Paginator(all_lots, self.LOTS_PER_PAGE)

        return paginator.get_page(page)

    def get_detail(self, pk):

        return get_object_or_404(Lot, pk=pk)

    def get_end_time(self):
        # Count last time
        end_time = self.date_to - timezone.now()

        return "%s д, %.2dч: %.2dм: %.2dс" %\
               (end_time.days,end_time.seconds//3600,(end_time.seconds//60)%60, end_time.seconds%60)

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    sum = models.IntegerField()