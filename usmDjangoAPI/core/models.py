from django.db import models

# Create your models here.


# Main components ------------------------------------------------------------------------------------------------------------
class Environment(models.Model):
    environment_name = models.CharField(primary_key=True,
                                        max_length=30,)

class Package(models.Model):
    package_name = models.CharField(primary_key=True,
                                    max_length=30,)

class Node(models.Model):
    node_name = models.CharField(   primary_key=True, 
                                    max_length=30,)
    environment = models.ForeignKey(Environment,
                                    on_delete=models.CASCADE,)
    #bundles = models.ForeignKey(    )
    #packages = models.ForeignKey(   )

class Bundle(models.Model):
    bundle_name = models.CharField( primary_key=True,
                                    max_length=30,)
    is_public = models.BooleanField()
    sub_bundles = models.ManyToManyField("self",
                                        symmetrical=False,
                                        through="BundleComposeBundle",
                                        through_fields=("top_bundle_name", "sub_bundle_name")),
    packages = models.ManyToManyField(  "self",
                                        symmetrical=False,
                                        through="PackageComposeBundle",
                                        through_fields=("top_bundle_name", "package_name")),
    

# Associations between components ------------------------------------------------------------------------------------------
class BundleComposeBundle(models.Model):
    top_bundle_name = models.ForeignKey(Bundle, 
                                        on_delete=models.CASCADE)
    sub_bundle_name = models.ForeignKey(    Bundle,
                                            related_name="sub_bundle_name",
                                            on_delete=models.CASCADE,)
    class Meta:
        unique_together = ["top_bundle_name", "sub_bundle_name"]

class PackageComposeBundle(models.Model):
    bundle_name = models.ForeignKey(Bundle, 
                                    on_delete=models.CASCADE)
    package_name = models.ForeignKey(   Package,
                                        on_delete=models.CASCADE,)
    class Meta:
        unique_together = ["bundle_name", "package_name"]

class BundleComposeNode(models.Model):
    node_name = models.ForeignKey(  Node, 
                                    on_delete=models.CASCADE)
    bundle_name = models.ForeignKey(Bundle,
                                    related_name="bundles",
                                    on_delete=models.CASCADE,)
    class Meta:
        unique_together = ["node_name", "bundle_name"]

class PackageComposeNode(models.Model):
    node_name = models.ForeignKey(  Node, 
                                    on_delete=models.CASCADE)
    package_name = models.ForeignKey(Package,
                                    related_name="packages",
                                    on_delete=models.CASCADE,)
    class Meta:
        unique_together = ["node_name", "package_name"]