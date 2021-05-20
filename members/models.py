from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator

# Create your models here.


class Memberarea(models.Model):
    area_id = models.IntegerField(primary_key=True, default=1999, editable=False)
    area_name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not Memberarea.objects.count():
            self.area_id = 2000
        else:
            self.area_id = Memberarea.objects.last().area_id + 1
        super(Memberarea, self).save(*args, **kwargs)

    def __str__(self):
        return self.area_name


class Memberprofile(models.Model):
    member_no = models.IntegerField(primary_key=True, default=0, editable=False)
    member_name = models.CharField(max_length=500)
    phone_regex = RegexValidator(regex="(^([+]{1}[8]{2}|0088)?(01){1}[3-9]{1}\d{8})$")
    member_phone_number = models.CharField(
        validators=[phone_regex], max_length=14, blank=True
    )
    member_nid = models.PositiveBigIntegerField(max_length=17)

    member_image = models.ImageField(
        default="member_icon.png", upload_to="members-profile-pictures"
    )
    member_mother_name = models.CharField(max_length=500)
    member_father_name = models.CharField(max_length=500)
    member_spouse_name = models.CharField(max_length=500)
    nominee = models.CharField(max_length=500)
    present_address = models.CharField(max_length=500)
    present_city = models.CharField(max_length=50, null=True, blank=True)
    present_village = models.CharField(max_length=50, null=True, blank=True)
    present_union = models.CharField(max_length=50, null=True, blank=True)
    present_word = models.CharField(max_length=50, null=True, blank=True)
    present_thana = models.CharField(max_length=50, null=True, blank=True)
    present_district = models.CharField(max_length=50, null=True, blank=True)
    permanent_address = models.CharField(max_length=500)
    permanent_city = models.CharField(max_length=50, null=True, blank=True)
    permanent_village = models.CharField(max_length=50, null=True, blank=True)
    permanent_union = models.CharField(max_length=50, null=True, blank=True)
    permanent_word = models.CharField(max_length=50, null=True, blank=True)
    permanent_thana = models.CharField(max_length=50, null=True, blank=True)
    permanent_district = models.CharField(max_length=50, null=True, blank=True)
    member_area = models.ForeignKey(Memberarea, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not Memberprofile.objects.count():
            self.member_no = 1000
        else:
            self.member_no = Memberprofile.objects.last().member_no + 1
        super(Memberprofile, self).save(*args, **kwargs)

    def __str__(self):
        return self.member_name