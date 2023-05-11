from django.db import models

# Create your models here.

class Component(models.Model):
    component_id = models.AutoField(
        primary_key=True,
    )
    
class AbstractComposite(Component):
    pass

class CompositeType(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=50
    )
    
class CompositeData(models.Model):
    top_component_name = models.ForeignKey( 
        AbstractComposite, 
        on_delete=models.CASCADE,
        related_name="top_component"
    )
    sub_component_name = models.ForeignKey( 
        Component,
        on_delete=models.CASCADE,
        related_name="sub_components"
    )

    composite_type = models.ForeignKey(
        CompositeType,
        on_delete=models.CASCADE,
        related_name="composite_type"
    )

    class Meta:
        unique_together = ["top_component_name", "sub_component_name"]
    pass

class Environment(AbstractComposite):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    pass

class NodeGroup(AbstractComposite):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    pass

class Node(AbstractComposite):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    pass

class GrpackBundle(AbstractComposite):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    pass

class Module(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=50,
    )
    pass

class AbstractLeaf(Component):
    module= models.OneToOneField(
        to=Module,
        on_delete=models.CASCADE,
    )
    pass

class Os(models.Model):
    name    = models.CharField(primary_key=True, max_length=50)
    version = models.CharField(max_length=50)

class PackageData(models.Model):
    package_name    = models.CharField(primary_key=True, max_length=50)
    version         = models.CharField(max_length=50)

class Grpack(AbstractLeaf):
    name = models.CharField(
        unique=True
    )
    pass

class Package(models.Model):
    package_id = models.AutoField(
        primary_key=True
    )
    os = models.OneToOneField(
        Os,
        on_delete=models.CASCADE
    )

    data = models.OneToOneField(
        PackageData,
        on_delete=models.CASCADE
    )
    related_grpack = models.ForeignKey(
        Grpack,
        on_delete=models.CASCADE,
        related_name="packages"
    )    
    pass

















"""

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

"""