# CORTES AUTOMÁTICOS DE VÍDEOS

Este script em Python usa a biblioteca MoviePy para detectar e cortar partes silenciosas de um vídeo, permitindo remover trechos sem áudio ou com áudio abaixo de um limiar de volume especificado. O código também oferece a opção de adicionar uma imagem estática ao vídeo final.

## Pré-requisitos
- python 3.1x
- MoviePy
- Numpy
- Pillow

## Como Usar

### Instalando as dependências
```bash
pip install moviepy numpy pillow
```

### Executando o script
```bash
python autocut.py
```

### Funções Principais
`detect_silence(audio_clip, threshold=0.01, chunk_size=0.1)`
Esta função detecta partes silenciosas em um clipe de áudio, retornando uma lista de intervalos de tempo em que o áudio não é silencioso.

- `audio_clip`: O clipe de áudio a ser analisado.
- `threshold`: O limiar de volume abaixo do qual um trecho é considerado silencioso (padrão: 0.01).
- `chunk_size`: O tamanho em segundos de cada intervalo de análise (padrão: 0.1).

`custom_resize(clip, newsize)`
Esta função redimensiona um clipe de vídeo para o tamanho especificado sem usar o atributo 'ANTIALIAS', usando o método Lanczos de interpolação.

- `clip`: O clipe de vídeo a ser redimensionado.
- `newsize`: A nova largura e altura do clipe no formato (largura, altura).

`cut_video_on_silence(video_path, output_path, image_path='', silence_threshold=0.01, chunk_size=0.1)`
Esta função corta o vídeo para remover partes silenciosas e, opcionalmente, adiciona uma imagem estática ao vídeo final.

- `video_path`: O caminho do vídeo de entrada.
- `output_path`: O caminho do arquivo de vídeo de saída.
- `image_path`: Opcional. O caminho da imagem a ser adicionada ao vídeo final.
- `silence_threshold`: O limiar de volume abaixo do qual um trecho é considerado silencioso (padrão: 0.01).
- `chunk_size`: O tamanho em segundos de cada intervalo de análise de áudio (padrão: 0.1).

## Exemplo de Uso
O exemplo abaixo corta o vídeo 'video.mp4', remove partes silenciosas, adiciona a imagem 'image.png' e salva o resultado como 'output.mp4'.

```python
cut_video_on_silence(
    video_path='video.mp4',
    output_path='output.mp4',
    image_path='image.png',
    silence_threshold=0.01,
    chunk_size=0.1
)
```

## Contribuições
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, abra uma issue para discutir as mudanças propostas ou envie um pull request diretamente.

## Licença
Este projeto está licenciado sob a **MIT License**.
