from django.db import models
from django.contrib.auth.models import User

# Create your models here.

m_cate = (('Men','Men'),('Women','Women'),('Kids','Kids'))
s_cate = (('Ring','Ring'),('Chain','Chain'),('Bracelet','Bracelet'),('Bangles','Bangles'),('Necklace','Necklace'),('Anklet','Anklet'),('Barrette','Barrette'),('Belt buckle','Belt buckle'),
('Belly chain','Belly chain'),('Bindi','Bindi'),('Bolo tie','Bolo tie'),
('Bracelet','Bracelet'),('Brooch','Brooch'),('Earrings','Earrings'),('Ear cuff','Ear cuff'),
('Fascinator','Fascinator'),('Hairpin','Hairpin'),('Hatpin','Hatpin'))

p_mate = (('Gold','Gold'),('Silver','Silver'),('Platinum','Platimnum'),('Brass','Brass'),('Bangles','Bangles'),('Diamond','Diamond'),('Pearl','Pearl'))
p_brand = (('Tanishq','Tanishq'),('TBZ','TBZ'),('Malabar','Malabar'),('Kalyan','Kalyan'),('Bhima','Bhima'))
occa = (('Birthday','Birthday'),('Marriage Anniversary','Marriage Anniversary'),('Engagement','Engagement'),('Partywear','Partywear'),('Alltime','Alltime'))

ptype= (('Single Material','Single Material'),('Double Material','Double Material'),('Mix Material','Mix Material')) 
pstatus = (('Available','Available'),('Out of Stock','Out of Stock'),('limited stock','limited stock'))
pmode = (('Trending','Trending'),('Popular','Popular'),('New Arrival','New Arrival'),('Running','Running'))

# Product 
class ProductModel(models.Model):
    name= models.CharField(max_length=300)
    main_cate = models.CharField(choices=m_cate,max_length=200)
    sub_cate = models.CharField(choices=s_cate,max_length=200)
    og_price = models.IntegerField()
    discount = models.IntegerField()
    discounted_price = models.IntegerField(null=True)
    sell_price = models.IntegerField(null=True)
    p_type = models.CharField(default = 'Single Material',choices=ptype,max_length=200)
    p_material = models.CharField(choices=p_mate,max_length=200)
    p_brand = models.CharField(choices=p_brand,max_length=200)
    p_occasion = models.CharField(choices=occa,max_length=200)
    p_status = models.CharField(default='Available',choices=pstatus,max_length=100)
    p_mode = models.CharField(choices=pmode,default='Running',max_length=100)
    p_des = models.TextField()
    photo = models.ImageField(upload_to='product/')
    created_at = models.DateField(auto_now_add=True)

    @property
    def discounted_price(self):
        return ((self.og_price)*(self.discount))/100

    @property
    def sell_price(self):
        return (self.og_price)-(self.discounted_price)

# Customer Address
class CustomerModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.EmailField()
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField() 
    state = models.CharField(max_length=200)

    objects = models.Manager()



psize = (('S','S'),('M','M'),('L','L'),('XL','Xl'))


# Cart
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(choices=psize,max_length=100,default='S')

    @property
    def product_total(self):
        return (self.quantity)*(self.product.sell_price)

step = (('Pending','Pending'),('Accepted','Accepted'),('Packing','Packing'),('Shipping','Shipping'),('Deliverd','Deliverd'))
# Orders
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    psize = models.CharField(max_length=20,default='S')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=step,max_length=200,default='Pending')    

    @property
    def product_total(self):
        return (self.quantity)*(self.product.sell_price)