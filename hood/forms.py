from django.forms import ModelForm

from accounts.models import Profile
from .models import Posts,Business

class AddPostForm(ModelForm):
    
    class Meta:
        model = Posts
        fields = '__all__'
        exclude = ('posted_on','owner','location','tags')
        
class AddBusinessForm(ModelForm):
    
    class Meta:
        model = Business
        fields = '__all__'
        exclude = ('owner','location')
        
class UpdateProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)