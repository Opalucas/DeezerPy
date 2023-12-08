# Script para baixar playlists do deezer com python!
Este script utiliza a biblioteca [PyDeezer](https://github.com/acgonzales/pydeezer) para realizar o download de playlists do deezer. Todos os créditos sobre a biblioteca vão para o autor [acgonzales](https://github.com/acgonzales)

## Instalação
Instale a biblioteca PyDeezer:
```bash
pip  install  py-deezer
```

## Copie o código do arquivo main.py
Na variável ``download_dir`` especifique o caminho que deseja salvar os arquivos.

Para a variável ``arl``, você deve fazer login no [Deezer](https://www.deezer.com/br/), abrir o DevTools do navegador e procurar por cookies, onde terá um cookie de mesmo nome com uma informação criptografadas, basta copiar essa informação e colocar como valor da variável ``arl``.

Na variável ``playlist_id`` você deve colocar o ID da playlist que você deseja baixar. O link das playlist do deezer trazem essa informação no final: 
#### Exemplo ``https://www.deezer.com/br/playlist/999999999``

Após as correções acima, basta executar o script e os arquivos serão baixados no diretório especificados.


## 
Para maiores informações sobre a biblioteca citada, consulte a documentação da mesma.

### Contato: 
<div>  
      <a href="https://www.linkedin.com/in/lucas-floripes/" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>