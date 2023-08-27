import boto3

# Configurando o cliente do serviço Polly
polly_client = boto3.client('polly', region_name='us-east-1')  # Substitua pela região desejada

# Texto a ser convertido em áudio
text = "Hello, this is an example of text converted to audio using Amazon Polly."

# Solicitando a conversão de texto para fala
response = polly_client.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')

# Salvando o áudio em um arquivo
with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())

print("Áudio gerado e salvo como 'output.mp3'")
