from django.test import TestCase
from . models import Comment, Business, Post,Neighbourhood, Profile
from django.contrib.auth.models import User


# Create your tests here.

# Profile model test  
      
class ProfileTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.image= Profile(profile_pict = 'img.jpg', bio ='image', email = "fi@gmail.com",phone_number = '07854222')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     

        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)   
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(profile_pict = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(profile_pict = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)         

    # Testing  update method of Profile model    
    def test_update(self):
        self.image.save_profile()
        image = Profile.objects.filter(profile_pict = 'img.jpg').first()
        update = Profile.objects.filter(id = image.id).update(profile_pict = 'cake.jpg')
        updated = Profile.objects.filter(profile_pict = 'cake.jpg').first()
        self.assertNotEqual(image.profile_pict, updated.profile_pict)      

# Post model test  
class PostTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.post= Post(description = 'nice', categories ='business')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post)) 

class NeighbourhoodTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.kimisagara= Neighbourhood(name = 'kigali', police ='112', police_address = "kimisagara",health_center = 'kamuhoza', health_center_address = '113')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kimisagara,Neighbourhood))  
       
        # Testing Save Method of Neighbourhood model
    def test_save_method(self):
        self.kimisagara.save_neigborhood()
        neighbors = Neighbourhood.objects.all()
        self.assertTrue(len(neighbors) > 0)          
        
    # Testing  update method of Neighbourhood model    
    def test_update(self):
        self.kimisagara.save_neigborhood()
        kimisagara = Neighbourhood.objects.filter(name = 'kigali', police ='112', police_address = "kimisagara",health_center = 'kamuhoza', health_center_address = '113').first()
        update = Neighbourhood.objects.filter(id = kimisagara.id).update(name = 'nyarugenge')
        updated = Neighbourhood.objects.filter(name = 'nyarugenge').first()
        self.assertNotEqual(kimisagara.name, updated.name)                
        
    # Testing  delete method of Neighbourhood model     
    def test_delete(self):
        self.kimisagara= Neighbourhood(name = 'kigali', police ='112', police_address = "kimisagara",health_center = 'kamuhoza', health_center_address = '113')
        self.kimisagara.save_neigborhood()
        kimisagara = Neighbourhood.objects.filter(name = 'kigali').first()
        delete = Neighbourhood.objects.filter(id = kimisagara.id).delete()
        kimisagara = Neighbourhood.objects.all()
        self.assertTrue(len(kimisagara) == 0)           
        
    # Test Create
    def test_create_neighborhood(self):
        self.kimisagara.save_neigborhood()
        self.assertTrue(len(Neighbourhood.objects.all()) > 0)        
        
    # # Test Find
    # def test_find_neighborhood(self):
    #     self.kimisagara.save_neigborhood()
    #     self.searched_hood = Neighbourhood.find_neighborhood(1)
    #     self.assertTrue(self.searched_hood == self.hood)   
         
    # # Test Update Occupants
    # def test_update_occupants(self):
    #     self.kimisagara.save_neigborhood()
    #     self.kimisagara = Neighbourhood.objects.get(id=1)
    #     self.kimisagara.update_occupants()
    #     self.updated_hood = Neighbourhood.objects.get(id=1)
    #     self.assertTrue(self.updated_hood.occupants > 1)  
          
# Business model test          
class BusinessTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.resto= Business(bsn_name = 'restorant', bsn_email = "fi@gmail.com")
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.resto,Business))             
        
    # Test Create
    def test_create_business(self):
        self.resto.save_business()
        self.assertTrue(len(Business.objects.all()) > 0)         
        
