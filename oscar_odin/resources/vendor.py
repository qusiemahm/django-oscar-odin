from odin import Resource
from odin import fields

class VendorResource(Resource):
    id = fields.IntegerField()
    user_id = fields.IntegerField()
    registration_date = fields.DateTimeField()
    registration_status = fields.StringField()
    rating = fields.FloatField()
    total_ratings = fields.IntegerField()
    company_name = fields.StringField(null=True)
    brand_name = fields.StringField(null=True)
    brand_name_en = fields.StringField(null=True)
    brand_name_ar = fields.StringField(null=True)
    is_valid = fields.BooleanField()

    class Meta:
        name = "VendorResource"

    @classmethod
    def from_model_instance(cls, instance, *args, **kwargs):
        # same logic as before
        legal_info = getattr(instance, "legal_information", None)
        business_details = getattr(instance, "business_details", None)

        return cls(
            id=instance.id,
            user_id=instance.user_id,
            registration_date=instance.registration_date,
            registration_status=instance.registration_status,
            rating=instance.rating,
            total_ratings=instance.total_ratings,
            company_name=(
                legal_info.company_name if legal_info and legal_info.company_name else "Unknown"
            ),
            brand_name=(
                business_details.brand_name if business_details and business_details.brand_name else ""
            ),
            brand_name_en=(
                business_details.brand_name_en if business_details and business_details.brand_name_en else ""
            ),
            brand_name_ar=(
                business_details.brand_name_ar if business_details and business_details.brand_name_ar else ""
            ),
            is_valid=instance.is_valid,
        )
