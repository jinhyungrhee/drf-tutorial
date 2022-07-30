from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Serializer는 Form과 유사 (장고의 클래스를 JSON으로 JSON을 장고의 클래스로 변경)
'''
class SnippetSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(required=False, allow_blank=True, max_length=100)
  code = serializers.CharField(style={'base_template': 'textarea.html'})
  linenos = serializers.BooleanField(required=False)
  language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
  style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

  # validated_data로 'Snippet' 인스턴스를 생성하고 리턴함
  def create(self, validated_data):
    return Snippet.objects.create(**validated_data)

  # validated_data로 기존에 존재하는 Snippet 인스턴스르 갱신하고 리턴함
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.linenos = validated_data.get('linenos', instance.linenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance
'''

# SnippetSerializer를 ModelSerializer를 사용하여 리팩토링
class SnippetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Snippet
    fields = ['id', 'title', 'code', 'linenos', 'language', 'style']