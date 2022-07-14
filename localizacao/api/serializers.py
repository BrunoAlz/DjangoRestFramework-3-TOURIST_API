from rest_framework.serializers import ModelSerializer


from localizacao.models import Localizacao

class LocalizacaoSerializer(ModelSerializer):
    
    class Meta:    

        model = Localizacao
        fields = (
            'id', 'endereco1', 'endereco2', 
            'cidade', 'estado', 'latitude', 
            'longitude',
        )