from oscar.core.loading import get_class

VendorResource = get_class("oscar_odin.resources.vendor", "VendorResource")

def vendor_queryset_to_resources(queryset):
    """
    Convert Vendor queryset into VendorResource for Elasticsearch indexing.
    """
    return [VendorResource.from_model_instance(vendor) for vendor in queryset]
